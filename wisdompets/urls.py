from django.conf.urls import url
from django.contrib import admin

from adoption import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^adoption/(\d+)/', views.pet_detail, name='pet_detail'),
]
