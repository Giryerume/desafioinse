from django.contrib import admin
from .models import Inse
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Inse)
class ViewAdmin(ImportExportModelAdmin):
    pass