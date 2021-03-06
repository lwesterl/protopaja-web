from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts/', views.charts, name='charts'),
    path('send-json/', views.send_json, name='send-json'),
    path('api/data/', views.get_data, name='api-data'),

    path('api/device/<int:device_id>/', views.api_device, name='api_device'),

    path('data_table/', views.data_table, name='data_table'),
    path('update_data_table/', views.update_data_table, name='update_data_table'),
    path('devices/all_devices/', views.all_devices, name='all_devices'),
    path('devices/modify_devices/', views.modify_devices, name='modify_devices'),
    path('new_device_content/', views.new_device_content, name='new_device_content'),
    path('update_info/', views.update_info, name='update_info'),
    path('send_string/', views.send_string, name='send_string'),
    path('update_select/', views.update_select, name='update_select'),
    path('devices_refresh/', views.devices_refresh, name='devices_refresh'),
    path('add_emails/', views.add_emails, name='add_emails'),
    path('add_email/', views.add_email, name='add_email'),
    path('warnings/', views.warnings, name='warnings'),
    path('update_warnings/', views.update_warnings, name='update_warnings'),
    path('remove_alarms/', views.remove_alarms, name='remove_alarms'),
    path('remove_emails/', views.remove_emails, name='remove_emails'),
    path('remove_email/', views.remove_email, name='remove_email'),
    path('show_alarm/', views.show_alarm, name='show_alarm'),
    path('change_alarm_settings/', views.change_alarm_settings, name='change_alarm_settings'),
    path('update_settings/', views.update_settings, name='update_settings'),
    path('change_temp_settings/', views.change_temp_settings, name='change_temp_settings'),
    path('temp_settings/', views.temp_settings, name='temp_settings'),
    path('change_humd_settings/', views.change_humd_settings, name='change_humd_settings'),
    path('humd_settings/', views.humd_settings, name='humd_settings'),
    path('change_light_settings/', views.change_light_settings, name='change_light_settings'),
    path('light_settings/', views.light_settings, name='light_settings'),
    path('alarm_csv/', views.alarm_csv, name='alarm_csv')
]
