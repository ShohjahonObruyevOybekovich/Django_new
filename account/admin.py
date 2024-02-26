from django.contrib import admin


from .models import CustomUser
from .views import account_site

admin.site.register(CustomUser)
# admin.site.register(account_site)