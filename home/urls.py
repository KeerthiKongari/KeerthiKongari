from django.contrib import admin
from django.urls import path, include
from home import views

#django admin header customizations
admin.site.site_header = "Developer Keerthi"
admin.site.site_title = "welcome to keethi's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]