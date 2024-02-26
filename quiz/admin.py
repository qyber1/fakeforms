from django.contrib import admin
from .models import BusinessCategory, BusinessType, Question, Answer


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'type_id']
    list_filter = ['type_id']
    search_fields = ['title']


@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'category_id']
    list_filter = ['category_id']
    search_fields = ['question']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question_category', 'answer']
    list_filter = ["question_id__category_id"]

    def question_category(self, obj):
        return obj.question_id.category_id

    question_category.short_description = 'Категория бизнеса'