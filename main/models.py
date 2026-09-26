from django.db import models

# Create your models here.
class ConsultationRequest(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__ (self):
        return self.full_name
    
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0,help_text='Order in which the team members appear on the site')


    
    class Meta:
        ordering=['order','name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return  self.name      
    
    
class About(models.Model):
    vision = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)