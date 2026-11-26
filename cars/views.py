from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_safe

from .forms import CarForm
from .models import Car


@require_safe
def home(request):
    inventory = Car.objects.all()
    summary = inventory.aggregate(
        total=Count("pk"),
        available=Count("pk", filter=Q(is_available=True)),
        electric=Count("pk", filter=Q(fuel_type=Car.Fuel.ELECTRIC)),
    )
    status = request.GET.get("status")
    query = request.GET.get("q", "").strip()
    cars = inventory if status == "all" else inventory.filter(is_available=True)
    if query:
        cars = cars.filter(Q(name__icontains=query) | Q(brand__icontains=query) | Q(fuel_type__icontains=query))
    return render(request, "home.html", {
        "cars": cars.order_by("-pk"),
        "summary": summary,
        "status": "all" if status == "all" else "available",
        "query": query,
    })


@require_http_methods(["GET", "POST"])
def add_car(request):
    form = CarForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        car = form.save()
        messages.success(request, f"{car.brand} {car.name} was added to inventory.")
        if not car.is_available:
            return redirect(reverse("home", query={"status": "all"}))
        return redirect("home")
    return render(request, "add_car.html", {"form": form})
