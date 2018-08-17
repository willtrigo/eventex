"""Set admin of the core."""
from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk


class ContactInline(admin.TabularInline):
    """Set contact in line."""

    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    """Set model admin of the speaker."""

    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        """Create a hyperlink from the speaker's website."""
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        """Show the image of the speaker."""
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'foto'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
