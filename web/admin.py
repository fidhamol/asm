from django.contrib import admin
from . models import Service,Update,Project,Category,Contact,Career,Testimonial

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("admin_photo","title",)
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("admin_photo","title",)
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("admin_photo","title",)
    search_fields = ("title",)
    list_filter = ("title",)      


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)  


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)  


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("fullname",)
    search_fields = ("fullname",)
    list_filter = ("fullname",)     


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)                   