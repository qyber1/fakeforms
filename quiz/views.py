from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from .forms import BusinessTypeForm, BusinessCategoryForm, QuizForm
from auth_user.models import User
from .models import Question
from .tasks import send_info_about_user
import logging
from .utils import save_user_result
# Create your views here.

logger = logging.getLogger(__name__)


class BusinessTypeView(FormView):
    template_name = 'quiz/type.html'
    form_class = BusinessTypeForm
    success_url = reverse_lazy('category')

    def form_valid(self, form) -> HttpResponseRedirect:
        logger.info('BusinessTypeView: форма валидна')
        type_ = form.cleaned_data["title"]
        self.request.session["type"] = type_.pk
        user = User.objects.get(email=self.request.session["user_email"])
        user.bis_type = type_
        user.save()
        return super().form_valid(form)


class BusinessCategoryView(View):
    template_name = 'quiz/category.html'
    success_url = reverse_lazy('questions')

    def get(self, request, *args, **kwargs) -> HttpResponse:
        logger.info('BusinessCategoryView: GET запрос')
        type_id = request.session.get("type")
        form = BusinessCategoryForm(type_id=type_id)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect | HttpResponse:
        logger.info('BusinessCategoryView: POST запрос')
        type_id = request.session.get("type")
        form = BusinessCategoryForm(request.POST, type_id=type_id)

        if form.is_valid():
            logger.info('BusinessCategoryView: форма валидна')
            category = form.cleaned_data["title"]
            request.session["category"] = category.pk
            user = User.objects.get(email=request.session["user_email"])
            user.cat = category
            user.save()
            return HttpResponseRedirect(self.success_url)
        else:
            logger.info('BusinessCategoryView: форма не валидна')
            return render(request, self.template_name, {'form': form})


class QuestionAnswerView(View):
    template_name = 'quiz/questions.html'
    success_url = reverse_lazy('success')

    def get(self, request, *args, **kwargs) -> HttpResponse:
        logging.info('QuestionAnswerView: GET запрос')
        category = request.session.get("category")
        questions = list(Question.objects.filter(category_id=category))
        form = QuizForm(questions=questions)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect | HttpResponse:
        logging.info('QuestionAnswerView: POST запрос')
        category = request.session.get("category")
        questions = list(Question.objects.filter(category_id=category))
        form = QuizForm(request.POST, questions=questions, category=request.session.get("category"))
        if form.is_valid():
            user = User.objects.get(email=request.session["user_email"])
            questions = Question.objects.filter(category_id=request.session.get("category"))
            save_user_result(user, questions, form.cleaned_data)
            logging.info(f'QuestionAnswerView: Форма валидна! Данные по пользователю {user.email} сохранены')
            send_info_about_user.delay(request.session["user_email"])
            return HttpResponseRedirect(self.success_url)
        else:
            logging.info('QuestionAnswerView: форма невалидна ')
            return render(request, self.template_name, {'form': form})


class SuccessView(View):
    template_name = 'quiz/ok.html'

    def get(self, request):
        logging.info('SuccessView: GET запрос')
        return render(request, self.template_name)

