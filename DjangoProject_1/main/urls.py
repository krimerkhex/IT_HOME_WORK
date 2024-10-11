from django.urls import path
from .views import main_page, second_page, third_page,about

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
    path('second/', second_page, name='second_page'),
    path('third/', third_page, name='third_page'),

]
