from django.contrib import admin

# Register your models here.

from testapp.models import VoterModel

class VoterAdmin(admin.ModelAdmin):
    list_display = ['sno','name','fatname','epic','phone','addr']

admin.site.register(VoterModel,VoterAdmin)