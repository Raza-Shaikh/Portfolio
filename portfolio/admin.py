from django.contrib import admin
from django.utils.html import format_html
from .models import Skill, Project, Experience, Education, Contact


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'created_at']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    ordering = ['category', '-proficiency', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'completed_date', 'created_at']
    list_filter = ['featured', 'completed_date', 'technologies']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    ordering = ['-featured', '-completed_date']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Project Details', {
            'fields': ('technologies', 'github_url', 'live_url', 'completed_date')
        }),
        ('Display Options', {
            'fields': ('featured',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('technologies')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['start_date', 'end_date']
    search_fields = ['company', 'position', 'description']
    ordering = ['-start_date']

    def is_current(self, obj):
        return obj.is_current
    is_current.boolean = True
    is_current.short_description = 'Current Position'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'gpa']
    list_filter = ['start_date', 'end_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-start_date']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f'{queryset.count()} messages marked as read.')
    mark_as_read.short_description = 'Mark selected messages as read'

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, f'{queryset.count()} messages marked as unread.')
    mark_as_unread.short_description = 'Mark selected messages as unread'

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


# Customize admin site header and title
admin.site.site_header = 'Portfolio Administration'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Welcome to Portfolio Administration'
