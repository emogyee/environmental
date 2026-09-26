from django.contrib import admin
from .models import ConsultationRequest ,TeamMember,About

# Register your models here.
@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','created_at')
    list_filter = ('created_at',)
    
    
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name','email','designation','created_at','is_active','order')
    list_editable = ('order','is_active')
    search_fields = ('name','designation')
    list_filter = ('created_at','is_active')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    
    
