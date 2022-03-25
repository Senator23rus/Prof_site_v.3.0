from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.title),
    path('create/', views.create, name='create'),
    path('news/', views.news, name='news'),
    path('news/<int:page>/', views.news, name='news_paged'),
    path('home/', views.title, name='home'),
    path('documents/', views.documents, name='documents'),

    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('filials/', views.filials, name="filials"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)