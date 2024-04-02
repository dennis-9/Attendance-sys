from django.db import models

# Create your models here.

class Record(models.Model):
    # Automatically set to the current date/time when the record is created.
    creation_date = models.DateTimeField(auto_now_add=True)
     
    first_name = models.CharField(max_length=100)
    
    last_name = models.CharField(max_length=100)
    
    POSITION_CHOICES = [
        ('intern', 'Intern'),
        ('worker', 'Worker'),
    ]

    position = models.CharField(max_length=100, choices=POSITION_CHOICES)  # The position of the employee (either "intern" or "worker")

    
    email = models.EmailField(max_length=255)  # A string representing an e-mail address
    
    phone = models.CharField(max_length=100)   # A string representing a phone number, which may include "-" as a separator
    
    address = models.CharField(max_length=100) # A string representing a physical address.
    
    city = models.CharField(max_length=100)   # The name of the city or locality
    
    country = models.CharField(max_length=125) # The name of the country (in English).
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    
    