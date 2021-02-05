from django.db import models
from django.utils import timezone
# Create your models here.
class writeBlog(models.Model):
    name = models.CharField(max_length=50, null=True)
    title = models.TextField()
    blog = models.TextField()
    date = models.DateField(default = timezone.now)
    
    class Meta:
        db_table = "blog"
    
    def __str__(self):
        return self.title

    
