"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework_swagger.views import get_swagger_view

from news.admin import admin_site


swagger_docs_view = get_swagger_view(title='News API DOCS')

urlpatterns = [
    path('admin/', admin_site.urls),
    path('api/v1/', swagger_docs_view),
    path('api/v1/news/', include('search.urls')),
    path('api/v1/user/', include('users.urls')),
]
