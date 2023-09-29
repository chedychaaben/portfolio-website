from django.contrib import admin

from .models import Preview, Quote, Skill, Project,ProjectTech , ProjectImage, ContactForm
# Register your models here.
admin.site.register(Preview)
admin.site.register(Quote)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProjectTech)
admin.site.register(ProjectImage)
admin.site.register(ContactForm)