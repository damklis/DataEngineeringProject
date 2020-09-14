from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from rest_framework.authtoken.models import Token

from news.models import News
from news.views import AdminNewsViewSet
from users.models import UserModel

router = routers.DefaultRouter()
router.register(r"news", AdminNewsViewSet)


class MyAdminSite(admin.AdminSite):
    
    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        custom_urls = [
            path(r"api/", include(router.urls))
        ]
        return custom_urls + urls

admin_site = MyAdminSite()

admin_site.register(UserModel)
admin_site.register(Token)
admin_site.register(News)
