from django.db import models


class WorkerModel(models.Model) : 
    status = models.CharField(max_length=100 , default='off' , null=True , blank=True)
    pid = models.SmallIntegerField(default=0)
    chat_id = models.IntegerField(default=0)
    license_date= models.DateField()
    fruitpass = models.CharField(max_length=200 , unique=True)
    second =models.IntegerField(default=0)
    

