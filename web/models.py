from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


STATUS_CHOICHES = [
    ("", "Services "),
    ("Architectural Design", "Architectural Design"),
    ("Interior Design and Fit-out Works", "Interior Design and Fit-out Works"),
    ("3D Visualization and Graphics", "3D Visualization and Graphics"),
    ("Gypsum/Plaster Board/Plastering", "Gypsum/Plaster Board/Plastering"),
    ("Masonry, Tiling", "Masonry, Tiling"),
    ("Joinery/Carpentry", "Joinery/Carpentry"),
    ("Glazing Works", "Glazing Works"), 
]

class Contact(models.Model):
    services = models.CharField(
        max_length=50, choices=STATUS_CHOICHES, null=True, blank=True
    )    
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    message=models.TextField()

    def __str__(self):
        return self.name   


class Service(models.Model):

    ICON_CHOICES = (
        ('icon flaticon-houses', 'icon flaticon houses'),
        ('icon flaticon-living-room', 'icon flaticon living room'),
    )
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)

    bgimage = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    paragraph = models.TextField()
    paragraphread = models.TextField()
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.bgimage.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


    def __str__(self):
        return self.title
    

class Update(models.Model):
    image = models.ImageField(upload_to='photos')
    admin=models.CharField( max_length=50)
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=100)
    # paragraph = models.TextField()
    # paragraphread = models.TextField()
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


    def __str__(self):
        return self.title    
    

class Category(models.Model):  
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name     


class Project(models.Model):
    image = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , blank=True ,null=True)

    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


    def __str__(self):
        return self.title   


class Career(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    number = models.CharField(max_length=254)
    coverletter = models.TextField()
    cv = models.FileField(upload_to="career/cv/")

    def __str__(self):
        return self.fullname       


class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos')
    jobrole=models.CharField(max_length=254)
    paragraph = models.TextField()

    def __str__(self):
        return self.name               