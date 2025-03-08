from equipment import models as equipment_models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
@receiver(post_save, sender=equipment_models.Observation)
def update_schedule_status(sender, instance, **kwargs):

    if instance.schedule:
        instance.schedule.status = "completed"
        instance.schedule.save()

@receiver(post_save, sender=equipment_models.Observation)
def update_schedule_fullfillment_date(sender, instance, **kwargs):

    if instance.schedule:
        instance.schedule.fullfillment_date = timezone.now() 
        instance.schedule.save()


@receiver(post_save, sender=equipment_models.Audit)
def create_observation(sender, instance, **kwargs):
    if not instance.is_ok:
        equipment_models.Observation.objects.create(
            audit = instance,
            schedule=instance.schedule,
            checkpoint=instance.checkpoint,
            owner=instance.auditor
        )

        