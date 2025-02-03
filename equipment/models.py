from django.db import models
from shared import models as shared_models
# Create your models here.

class Plant(shared_models.TimeStamp):
    name = models.CharField(max_length=64)

    def __str__(self):
       return self.name

class Line(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="line")

    def __str__(self):
       return self.name

class Station(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="station")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="station")

    def __str__(self):
       return self.name
   
class EquipmentType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)    


    def __str__(self):
       return self.name
class Equipment(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.SET_NULL,null=True)
    plant = models.ForeignKey(Plant,on_delete=models.SET_NULL,null=True,related_name="equipment")
    # department = models.ForeignKey('account.Department',on_delete=models.SET_NULL,null=True,related_name="equipment")
    line = models.ForeignKey(Line,on_delete=models.SET_NULL,null=True,related_name="equipment")
    station = models.ForeignKey(Station,on_delete=models.SET_NULL,null=True,related_name="equipment")
    qr = models.ImageField(upload_to='QR/',null=True,blank=True)
    sheet = models.CharField(max_length=64,null=True,blank=True)

    def __str__(self):
       return self.name

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



class MasterAuditParameter(shared_models.TimeStamp):
    name = models.CharField(max_length=64)



    def __str__(self):
        return self.name
    
class Checkpoint(shared_models.TimeStamp):
    equipment = models.ForeignKey(Equipment,related_name='checkpoints',on_delete=models.CASCADE)
    audit_parameter = models.ForeignKey(MasterAuditParameter,related_name='checkpoints',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.equipment

class Observation(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    checkpoint = models.ForeignKey(Checkpoint,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to = 'observation/',null=True,blank=True)

    def __str__(self):
        return self.name