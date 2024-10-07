from django.db import models
from shared import models as shared_models
# Create your models here.

class Plant(shared_models.TimeStamp):
    name = models.CharField(max_length=64)

class Line(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="line")
    department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="line")


class Station(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="station")
    department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="station")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="station")

class EquipmentType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)    

class Equipment(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.SET_NULL,null=True)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="equipment")
    department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="equipment")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="equipment")
    station = models.ForeignKey(Station,on_delete=models.SET_NULL,null=True,related_name="equipment")
    qr = models.ImageField(upload_to='QR/',null=True,blank=True)
    location = models.CharField(max_length=64)

class CheckList(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    equipment = models.ForeignKey(Equipment,on_delete=models.SET_NULL,null=True)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="checklist")
    department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="checklist")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="checklist")
    station = models.ForeignKey(Station,on_delete=models.SET_NULL,null=True,related_name="checklist")
    image = models.ImageField(upload_to='checklist/',null=True,blank=True)

class ScheduleType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)


class Schedule(shared_models.TimeStamp):
    user = models.ForeignKey('account.User',on_delete=models.SET_NULL,null=True,related_name="schedule")
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.SET_NULL,null=True)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="schedule")
    department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="schedule")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="schedule")
    station = models.ForeignKey(Station,on_delete=models.SET_NULL,null=True,related_name="schedule")
    schedule_type = models.ForeignKey(ScheduleType,on_delete=models.SET_NULL,null=True,related_name="schedule")
    schedule_date = models.DateTimeField()


class Observation(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to = 'observation/',null=True,blank=True)
