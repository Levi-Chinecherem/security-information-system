from django.contrib import admin
from .models import SecurityIncident, SecurityGroup

class SecurityIncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'location')
    list_filter = ('timestamp', 'location')
    search_fields = ('title', 'description')
    date_hierarchy = 'timestamp'

# Create an admin class for SecurityGroup
class SecurityGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(SecurityIncident, SecurityIncidentAdmin)
admin.site.register(SecurityGroup, SecurityGroupAdmin)

admin.site.site_header = "Security Information System Admin"
admin.site.site_title = "Security Information System"
admin.site.site_url = "/home/"