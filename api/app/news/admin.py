from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from news.models import News
from news.views import AdminNewsList, AdminNewsDetail


class MyAdminSite(AdminSite):
    
    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        custom_urls = [
            url(r"news/", self.admin_view(AdminNewsList.as_view())),
            url(r"news/<title>", self.admin_view(AdminNewsDetail.as_view()))
        ]
        return custom_urls + urls

admin_site = MyAdminSite()

admin_site.register(User)
admin_site.register(Token)
