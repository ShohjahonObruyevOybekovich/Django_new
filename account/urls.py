from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    # ... other URL patterns ...
    path('/account/<int:id>', views.account_site, name='account_site'),
    # ... other URL patterns ...
]