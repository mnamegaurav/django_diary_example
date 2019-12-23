from django.db import models

# Create your models here.
class Notes(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'Notes {self.time}'

    class Meta:
        verbose_name_plural = 'Notes'