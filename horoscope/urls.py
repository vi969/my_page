from django.urls import path
from . import views
urlpatterns = [
    path('<int:num_zodiac>', views.get_ifo_sign_zodiac_by_num),
    path('<str:sign_zodiac>', views.get_ifo_sign_zodiac, name='zodiac'),
]
