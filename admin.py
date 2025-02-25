from django.contrib import admin
from .models import Profile, Education, Experience, Skill, SocialMediaLinks, FooterData, ContactMessage

# Register your models
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(SocialMediaLinks)  # Now it exists
admin.site.register(FooterData)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'submitted_at')