from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()

# We use __str__() to make our model instances display something meaningful — usually the title, name, or identifier.
# If you don’t define __str__(), Django uses the default Python object representation, like:
# <Blog: Blog object (1)>
# Which isn’t helpful for debugging or admin display.
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
