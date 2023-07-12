from django.urls import path
from .views import SnackListView,SnackDetailsView,HomeView

urlpatterns = [

    path('',HomeView.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks'),
    path('snacks/<pk>/',SnackDetailsView.as_view(), name='snack_detail')
]