from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_blog, name="show_me_blog"),

]