from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_index,name='landing_index'),
    path('learn_bike/',views.learn_bike,name='learn_bike'),
    path('learn_car/',views.learn_car,name='learn_car'),
    path('learn_excavator/',views.learn_excavator,name='learn_excavator'),
    path('about_us/',views.about_us,name='about_us')
]
