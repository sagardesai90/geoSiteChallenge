from django.contrib import admin

# Register your models here.
from .models import RequestsMade, PersonalRequests
admin.site.site_header = "Geosite Backend Challenge"
admin.site.site_title = "Processor Info"
admin.site.index_title = "Processor Info"
class RequestsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

admin.site.register(RequestsMade, RequestsAdmin)
admin.site.register(PersonalRequests)