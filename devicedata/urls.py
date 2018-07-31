from django.urls import path

from .views import index, charts, send_json, get_data

urlpatterns = [
    path('', index, name='index'),
    path('charts/', charts, name='charts'),
    path('send-json/', send_json, name='send-json'),
    path('api/data/', get_data, name='api-data'),
]