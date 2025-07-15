from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('resume/download/', views.download_resume, name='download_resume'),

]
