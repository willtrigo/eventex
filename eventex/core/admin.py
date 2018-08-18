"""Set admin of the core."""
from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInline(admin.TabularInline):
    """Set contact in line."""

    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    """Set model admin of the speaker."""

    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        """Create a hyperlink from the speaker's website."""
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        """Show the image of the speaker."""
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj):
        """Show the speaker's email."""
        return obj.contact_set.emails().first()
        # ------ more easy way to do this.
        # return obj.contact_set(manager='emails').first()
        # return Contact.emails.filter(speaker=obj).first() # filter more malleable
        # ------ hard way to do this.
        # return Contact.objects.filter(kind=Contact.EMAIL, speaker=obj).first() # filter fixed

    email.short_description = 'e-mail'

    def phone(self, obj):
        """Show the speaker's phone."""
        return obj.contact_set.phones().first()
        # ------ more easy way to do this.
        # return obj.contact_set(manager='phones').first()
        # return Contact.phones.filter(speaker=obj).first() # filter more malleable
        # ------ hard way to do this.
        # return Contact.objects.filter(kind=Contact.PHONE, speaker=obj).first() # filter fixed

    phone.short_description = 'telefone'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
admin.site.register(Course)
