from django.db import models


# Create your models here.


class BusinessType(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Сфера бизнеса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип бизнеса"
        verbose_name_plural = "Типы бизнеса"


class BusinessCategory(models.Model):

    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название')
    type_id = models.ForeignKey('BusinessType', on_delete=models.PROTECT, verbose_name='Тип бизнеса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория бизнеса"
        verbose_name_plural = "Категории бизнеса"


class Question(models.Model):

    question = models.CharField(max_length=256, null=True, blank=True, verbose_name='Вопрос')
    category_id = models.ForeignKey('BusinessCategory', on_delete=models.PROTECT, verbose_name='Категория бизнеса')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):

    answer = models.CharField(max_length=256, null=True, blank=True, verbose_name='Варианты ответов')
    question_id = models.ForeignKey("Question", on_delete=models.PROTECT, verbose_name='Вопрос')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
