from django.urls import path
from user.api.views import *


app_name: str = "api"

urlpatterns: list[path] = [
    path('', AuthenticatedUserInfoView.as_view(), name="authenticated_user_info_view")
]

