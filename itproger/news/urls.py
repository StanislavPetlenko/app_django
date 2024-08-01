from django.urls import path
from .views import home_news, create_new

urlpatterns = [
    path('', home_news, name="home_news"),
    path('create', create_new, name='create')
    # path('about', about, name="about"),
    # path('contacts', contacts, name="contacts"),
]