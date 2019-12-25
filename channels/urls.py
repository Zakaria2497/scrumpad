from django.urls import path
from . import views

app_name = 'channels'

urlpatterns = [
    path('create/', views.channelcreate, name='create'),
    path('manage/', views.ChannelManage.as_view(), name='manage'),
    path('manage/<id>',views.IndividualChannelManage.as_view(),name='manage_channel'),
    path('manage/<int:id>/basic',views.channelmanage,name='manage_basic'),
    path('manage/<int:id>/participants',views.channelmanageparticipants,name='manage_participants'),
    path('manage/toggle/<int:membership>/<int:option>',views.toggle,name='toggle')
]