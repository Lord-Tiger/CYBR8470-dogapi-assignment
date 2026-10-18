"""
URL configuration for dogserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from dogapi.views import DogViewSet, BreedViewSet

dog_list = DogViewSet.as_view({'get': 'list', 'post': 'create'})
dog_detail = DogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
breed_list = BreedViewSet.as_view({'get': 'list', 'post': 'create'})
breed_detail = BreedViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dogs/', dog_list, name='dog-list'),
    path('api/dogs/<int:pk>/', dog_detail, name='dog-detail'),
    path('api/breeds/', breed_list, name='breed-list'),
    path('api/breeds/<int:pk>/', breed_detail, name='breed-detail'),
]
