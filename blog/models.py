from contextlib import nullcontext
from django.db import models


class Post(models.Model):
    # title = models.FieldType()
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=160, null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_pic = models.ImageField(
        upload_to="cover/", 
        null=True,
        help_text="อัปโหลดรูปภาพหน้าปก"
    )

    def __str__(self):
        return self.title


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.CharField(max_length=80)
    email = models.EmailField()
    detail = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    


    