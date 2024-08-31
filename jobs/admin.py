from django.contrib import admin
from .models import JobPosition, Organization

class JobPositionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(company__user=request.user)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.company.user == request.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.company = Organization.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Organization)

