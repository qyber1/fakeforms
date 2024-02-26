from django.db import models
from quiz.models import BusinessCategory, BusinessType


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email пользователя')
    email_verify = models.BooleanField(default=False, verbose_name='Подтвержденнный Email')
    cat = models.ForeignKey(BusinessCategory, related_name='cat', verbose_name='Категория бизнеса',
                            on_delete=models.PROTECT, null=True, blank=True)
    bis_type = models.ForeignKey(BusinessType, related_name='type', verbose_name='Ниша', on_delete=models.PROTECT,
                                 null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers", verbose_name="Пользователь",
                             null=True, blank=True)
    question = models.CharField(max_length=256, verbose_name="Вопрос")
    answer = models.CharField(max_length=256, verbose_name='Ответ')

    def __str__(self):
        return f"{self.user.email} - {self.question}"

    class Meta:
        verbose_name = "Результат пользователя"
        verbose_name_plural = "Результаты пользователей"
