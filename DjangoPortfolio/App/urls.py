from django.urls import path
from .views import home,contact_post,error_view
from django.conf.urls import handler404, handler500
urlpatterns = [
    path("", home,name='home'),
    path('contact_post/', contact_post, name='contact_post'),
    path('error/', error_view, name='error_view'),
]
handler404 = 'App.views.error_404_view'
handler500 = 'App.views.error_500_view'