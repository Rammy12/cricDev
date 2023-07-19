from django.contrib import admin
from django.urls import path
from cric import views

urlpatterns = [
    path('predict_t20_men/',views.predict_t20score,name='predict_t20score'),
    path('predict_ipl/',views.predict_iplscore,name='predict_iplscore'),
    path('predict_odismen/',views.predict_odiscore,name='predict_odiscore'),
    path('odis/',views.get_odis_detail,name='get_odis_detail'),
    path('ipl/',views.get_ipl_detail,name='get_ipl_detail'),
    path('t20/',views.get_t20_detail,name='get_t20_detail'),
    path('save_t20/',views.save_t20_detail,name='save_t20_detail'),
    path('save_odis/',views.save_odis_detail,name='save_odis_detail'),
    path('save_ipl/',views.save_ipl_detail,name='save_ipl_detail'),
]