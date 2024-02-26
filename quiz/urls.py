from django.urls import path
from .views import BusinessTypeView, BusinessCategoryView, QuestionAnswerView, SuccessView

urlpatterns = [
    path("", BusinessTypeView.as_view(), name='quiz'),
    path("category/", BusinessCategoryView.as_view(), name='category'),
    path('questions/', QuestionAnswerView.as_view(), name='questions'),
    path('questions/success/', SuccessView.as_view(), name='success')
]
