"""tdd_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from xword_data import views

urlpatterns = [
    path('', views.xword_drill, name='xword-drill'),
    path('/<clue_id>/', views.xword_drill, name='xword-drill-clue'),
    path('answer/<clue_id>/', views.xword_answer, name='xword-answer')
]
