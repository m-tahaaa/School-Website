from django.contrib import admin

from .models import AdmissionApplication, Event, GalleryPhoto, Notice

admin.site.site_header = "Lakhipur Middle School"
admin.site.site_title = "Lakhipur School Admin"
admin.site.index_title = "School operations"


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date_posted", "is_pinned")
    list_filter = ("category", "is_pinned", "date_posted")
    search_fields = ("title", "content")
    list_display_links = ("title",)
    ordering = ("-is_pinned", "-date_posted")
    date_hierarchy = "date_posted"


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "child_name",
        "class_sought",
        "parent_name",
        "phone_number",
        "submission_date",
        "status",
    )
    list_filter = ("status", "class_sought", "gender", "submission_date")
    search_fields = (
        "child_name",
        "parent_name",
        "phone_number",
        "email",
    )
    list_display_links = ("child_name",)
    readonly_fields = ("submission_date",)
    ordering = ("status", "-submission_date")
    date_hierarchy = "submission_date"
    list_per_page = 25


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date_added")
    list_filter = ("category", "date_added")
    search_fields = ("title",)
    list_display_links = ("title",)
    readonly_fields = ("date_added",)
    ordering = ("-date_added",)
    date_hierarchy = "date_added"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "venue")
    list_filter = ("event_date", "venue")
    search_fields = ("title", "description", "venue")
    list_display_links = ("title",)
    ordering = ("event_date", "title")
    date_hierarchy = "event_date"
