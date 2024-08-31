from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import JobPositionList

urtpatterns = [
    path('all_jobs', JobPositionList.as_view()),
]