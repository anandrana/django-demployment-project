from django.urls import path
from basic_app import views

#TEMPLATE TAGGING

app_name = 'basic_app'
urlpatterns = [
    path('',views.relative,name='relative'),
    path('',views.other,name='other'),
    path('',views.about,name='about'),

]
