from django.contrib import admin
from trainee.models import Trainee
# Register your models here.
@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'track', 'branch', 'course')
    list_filter = ('track', 'branch', 'course')
    search_fields = ('first_name', 'last_name', 'email')