from django.db import models

# Create your models here.

"""
    This model is rendered on homepage as links to can hover in to view description
"""
# service tabs
class Service(models.Model):
    # title
    name = models.CharField(max_length=200)
    # short description on home page
    description = models.TextField()
    # first head on page open
    main_head = models.TextField(null=True, blank=True)
    # inner title under main head on page open
    inner_title = models.TextField()
    # background picture of main page
    background = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

"""
    Header inside, displayed as patagraphs
"""
class ServiceHeader(models.Model):
    # heade of content
    name = models.CharField(max_length=200)
    # service header belings to
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    # picture to show beside header
    picture = models.ImageField(upload_to='serviceHeader')
    # content. All content are rendered with space in between them
    content = models.TextField()
    content_2 = models.TextField(blank=True, null= True)
    content_3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} for {self.service.name}'

"""
    An inner link to the payment page
"""
class InnerLink(models.Model):
    # name 
    name = models.CharField(max_length=200)
    # inner note on expand
    inner_note = models.TextField()
    # service it belongs to
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} for {self.service.name}'
    
class Company(models.Model):
    name = models.CharField(max_length=225)
    logo = models.ImageField(upload_to='company/')
    address = models.TextField()

    def __str__(self):
        return f'Company details: {self.name}'