from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.title),
    path('news/', views.news, name='news'),
    path('home/', views.title, name='home'),

    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    # path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"), филиалы
]