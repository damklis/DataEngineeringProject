from rest_framework import routers
from django.contrib import admin
from rest_framework.authtoken.models import Token

from news.models import News
from news.urls import urlpatterns
from users.models import UserModel

class NewsAdminSite(admin.AdminSite):
    
    def get_urls(self):
        urls = super(NewsAdminSite, self).get_urls()
        custom_urls = [*urlpatterns]
        return custom_urls + urls

admin_site = NewsAdminSite()

admin_site.register(UserModel)
admin_site.register(Token)
admin_site.register(News)
