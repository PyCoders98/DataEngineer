from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Users)
admin.site.register(Member)
admin.site.register(Categori)
admin.site.register(Packs)
admin.site.register(SiteMember)
admin.site.register(Owner)


# class applicant(admin.ModelAdmin):
#     list_display = ["name", "gender", "contact", "email", "apply_date"]


# admin.site.register(Applicant, applicant)

# class contactus(admin.ModelAdmin):
#     list_display=['name','email','comment']
# admin.site.register(ContactUs,contactus)
