from django.db import models
from shared import models as shared_models

# Create your models here.

class Plant(shared_models.TimeStamp):
    name = models.CharField(max_length=64)

    def __str__(self):
       return self.name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Plant.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class Line(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE,related_name="line")

    def __str__(self):
       return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Line.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class Station(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE,related_name="station")
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name="station")

    def __str__(self):
       return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Station.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)

   
class EquipmentType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)    

    def __str__(self):
       return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = EquipmentType.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class Equipment(shared_models.TimeStamp):
    name = models.CharField(max_length=64)
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE,related_name="equipment")
    # department = models.ForeignKey('account.Department',on_delete=models.CASCADE,related_name="equipment")
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name="equipment")
    station = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="equipment")
    qr = models.ImageField(upload_to='QR/',null=True,blank=True)
    sheet = models.CharField(max_length=64)

    def __str__(self):
       return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Equipment.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class ScheduleType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = ScheduleType.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class Schedule(shared_models.TimeStamp):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE,related_name="schedule")
    equipment_type = models.ForeignKey(EquipmentType,on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE,related_name="schedule")
    department = models.ForeignKey('account.Department',on_delete=models.CASCADE,related_name="schedule")
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name="schedule")
    station = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="schedule")
    schedule_type = models.ForeignKey(ScheduleType,on_delete=models.CASCADE,related_name="schedule")
    schedule_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Schedule.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class MasterAuditParameter(shared_models.TimeStamp):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = MasterAuditParameter.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)


class Checkpoint(shared_models.TimeStamp):
    equipment = models.ForeignKey(Equipment,related_name='checkpoints',on_delete=models.CASCADE)
    audit_parameter = models.ForeignKey(MasterAuditParameter,related_name='checkpoints',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.equipment.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Checkpoint.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)

# TODO: ORC
class Observation(shared_models.TimeStamp):
    REQUEST_STATUS_COICE = (
    ('pending', 'Pending'),
    ('ongoing', 'Ongoing'),
    ('complete', 'Complete'),
    )
    APPROVED_STATUS_COICE = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    name = models.CharField(max_length=64)
    checkpoint = models.ForeignKey(Checkpoint,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'observation/',null=True,blank=True)
    attempt = models.PositiveBigIntegerField(null=True, blank=True)
    category = models.CharField(max_length=64,null=True,blank=True)
    corrective_remark = models.CharField(max_length=64,null=True,blank=True)
    owner = models.ForeignKey("account.User",related_name="observations",on_delete=models.SET_NULL,null=True)
    department = models.ForeignKey("account.Department",related_name="observations",on_delete=models.SET_NULL,null=True)
    plant = models.ForeignKey(Plant,related_name="observations",on_delete=models.SET_NULL,null=True)
    remark = models.CharField(max_length=64,null=True,blank=True)
    request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_COICE, default='pending')
    approve_status = models.CharField(max_length=64,choices=APPROVED_STATUS_COICE,default='pending')
    target_date = models.DateField()


    def save(self, *args, **kwargs):
        if self.pk is None:
            obj = Observation.objects.filter().last()
            if obj:
                self.id = obj.id + 1
        super().save(*args, **kwargs)
