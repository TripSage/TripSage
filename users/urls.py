from django.urls import path
from .views import SignUpView

"""
The URL paths related to User actions
"""


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
