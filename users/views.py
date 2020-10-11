"""
Views actions for the User app implemented here
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# have to disable pylint warning as this is the only implementation
# pylint: disable=too-many-ancestors
class SignUpView(generic.CreateView):
    """
    The Signup view of the users and actions related to that
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
