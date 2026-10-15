from django.shortcuts import render


from django.shortcuts import render
from .forms import TravelPreferenceForm
from .models import TravelPackage
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
@login_required
def home(request):

    form = TravelPreferenceForm(
        request.GET or None
    )

    packages = None
    selected_priority = None
    selected_travel_type = None

    if form.is_valid():

        selected_travel_type = form.cleaned_data["travel_type"]
        selected_priority = form.cleaned_data["priority"]

        packages = TravelPackage.objects.filter(
            travel_type=selected_travel_type
        ).order_by(
            "-" + selected_priority,
            "price"
        )

    return render(
        request,
        "recommendations/home.html",
        {
            "form": form,
            "packages": packages,
            "selected_priority": selected_priority,
            "selected_travel_type": selected_travel_type,
        }
    )
def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(
        request,
        "recommendations/register.html",
        {"form": form}
    )
