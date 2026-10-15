
from django import forms

class TravelPreferenceForm(forms.Form):

    TRAVEL_CHOICES = [
        ("Solo", "Solo"),
        ("Friends", "Friends"),
        ("Family", "Family"),
    ]

    PRIORITY_CHOICES = [
        ("food_score", "Food"),
        ("nature_score", "Nature"),
        ("adventure_score", "Adventure"),
        ("heritage_score", "Heritage"),
        ("budget_score", "Budget"),
        ("comfort_score", "Comfort"),
    ]

    travel_type = forms.ChoiceField(
        choices=TRAVEL_CHOICES,
        label="Who are you travelling with?"
    )

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        label="What is your highest priority?"
    )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]