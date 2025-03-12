from django.contrib import admin
from userauth.models import Home  # ✅ Import from 'userauth.models'

admin.site.register(Home)
