from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["name", "brand", "year", "price", "fuel_type", "description", "is_available"]
        labels = {"name": "Model name", "price": "Asking price (USD)", "is_available": "Available for sale"}
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Corolla"}),
            "brand": forms.TextInput(attrs={"placeholder": "e.g. Toyota"}),
            "year": forms.NumberInput(attrs={"placeholder": "2025"}),
            "price": forms.NumberInput(attrs={"placeholder": "25000.00"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe the car’s condition and notable features."}),
        }
