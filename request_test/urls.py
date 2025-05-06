from django.urls import path
from .views import request_info_view, file_upload_view

app_name = 'request_test'

urlpatterns = [
    path('request-info/', request_info_view, name="request_info"),
    path('upload/', file_upload_view, name='upload_file')

]