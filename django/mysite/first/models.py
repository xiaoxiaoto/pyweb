from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid

# Create your models here.

@python_2_unicode_compatible
class Person(models.Model):
    id=models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
