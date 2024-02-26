import logging

from django import forms
from django.db.models import QuerySet

from .models import BusinessType, BusinessCategory, Answer, Question


class BusinessTypeForm(forms.ModelForm):
    title = forms.ModelChoiceField(
        widget=forms.RadioSelect(attrs={}),
        queryset=BusinessType.objects.all(),
        to_field_name='title',
        label=''
    )

    class Meta:
        model = BusinessType
        fields = ('title',)


class BusinessCategoryForm(forms.ModelForm):
    title = forms.ModelChoiceField(
        widget=forms.RadioSelect(),
        queryset=BusinessCategory.objects.all(),
        to_field_name='title',
    )

    class Meta:
        model = BusinessCategory
        fields = ('title',)

    def __init__(self, *args, type_id=None, **kwargs):
        super(BusinessCategoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].queryset = self.get_filtered_queryset(type_id)

    def get_filtered_queryset(self, type_id) -> QuerySet:
        queryset = BusinessCategory.objects.all()
        if type_id is not None:
            queryset = queryset.filter(type_id=type_id)
        return queryset


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.category = kwargs.pop('category', None)
        questions = kwargs.pop('questions', [])
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = Answer.objects.filter(question_id=question.id)
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[(choice.id, choice.answer) for choice in choices],
                widget=forms.RadioSelect(),
                required=False,
                label=question.question
            )
            self.fields[f'other_{question.id}'] = forms.CharField(required=False, widget=forms.TextInput(),
                                                                  label='Другое')

    def clean(self) -> dict:
        cleaned_data = super().clean()

        for question in Question.objects.filter(category_id=self.category):
            logging.info(f'ID - {question.id}')
            choice = f'question_{question.id}'
            other = f"other_{question.id}"
            if cleaned_data.get(choice) or cleaned_data.get(other):
                is_data = cleaned_data.pop(f"other_{question.id}", None)
                if is_data:
                    cleaned_data[choice] = is_data
                    continue
            else:
                self.add_error(other, 'Выберите один из вариантов ответа или добавьте свой')
        return cleaned_data
