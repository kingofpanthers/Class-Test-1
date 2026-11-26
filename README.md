# Motorline

Motorline is a local Django car dealership app. The homepage lists available vehicles by default. Use the availability tabs and search box to browse inventory, or use **Add car** to create a listing. Django Admin lets you edit vehicles and change their availability.
## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_cars
python manage.py runserver
```

Open http://127.0.0.1:8000/. Load the sample fixture only when setting up a fresh database, since its three records use fixed IDs.

To use Django Admin, run `python manage.py createsuperuser` in a separate terminal and sign in at http://127.0.0.1:8000/admin/.

## How it works

The project URL configuration sends inventory requests to `cars/urls.py`, which selects a view. The homepage view uses Django's ORM to query the `Car` table in SQLite. The view passes those records to a template that renders their details, prices, availability, and fuel types. The browser submits the add-car form by POST with a CSRF token. Django validates the submission with `CarForm` and displays field errors when validation fails. After a valid submission, `form.save()` writes the record to SQLite and the view redirects to the inventory page. The fuel-type migration fills in Petrol for records created before the field was added.
