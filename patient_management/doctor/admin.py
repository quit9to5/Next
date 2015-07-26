from django.contrib import admin

# Register your models here.
from .models import doctor
class login_doctor(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    class Meta:
        model = doctor

admin.site.register(doctor, login_doctor)
