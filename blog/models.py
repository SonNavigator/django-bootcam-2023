from django.db import models


class Post(models.Model):
    # title = models.FieldType()
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    
    

    