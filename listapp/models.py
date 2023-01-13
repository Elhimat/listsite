from django.db import models

class List(models.model):
listname=models.charField(max_length=255)
cuser=models.ForeignKey(User,on_delete=models.CASCADE)
cdate=models.DateTimeField(default=timezone.now)