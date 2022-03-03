from django.urls import path
from .views import view_calc_distance

app_name = 'measurements'

urlpatterns = [
    path('', view_calc_distance, name = 'view_calc_distance')
]