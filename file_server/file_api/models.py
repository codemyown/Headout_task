from django.db import models

class File(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name
