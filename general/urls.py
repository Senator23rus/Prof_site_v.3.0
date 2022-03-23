from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.title),
    path('create/', views.create, name='create'),
    path('news/', views.news, name='news'),
    path('home/', views.title, name='home'),
    path('documents/', views.documents, name='documents'),

    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('filials/', TemplateView.as_view(template_name="filials.html"), name="filials"),
]