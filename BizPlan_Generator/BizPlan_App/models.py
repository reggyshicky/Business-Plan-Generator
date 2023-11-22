from django.db import models

# Create your models here.
class BusinessPlan(models.Model):
    industry_choices = [
        ('Technology', 'Technology'),
        ('Health and Wellness', 'Health and Wellness'),
        ('Food and Beverage', 'Food and Beverage'),
        ('Retail', 'Retail'),
        ('Other', 'Other'),
    ]

    industry = models.CharField(max_length=50, choices=industry_choices)
    target_market = models.TextField()
    unique_selling_proposition = models.TextField()
    specific_requirements = models.TextField()
    goals_and_objectives = models.TextField()
    additional_information = models.TextField(blank=True, null=True)



# Responses from our contacts section
class ContactResponse(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    remarks = models.TextField()
