from equipment import models as equipment_models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from equipment import query as equipment_query
@receiver(post_save, sender=equipment_models.Equipment)
def update_schedule_status(sender, instance, **kwargs):
    if instance.status  == "COMPLETED":
        instance.schedule_set.update(status="COMPLETED")


@receiver(post_save, sender=equipment_models.Observation)
def update_schedule_fullfillment_date(sender, instance, **kwargs):
    if instance.schedule:
        instance.schedule.fullfillment_date = timezone.now() 
        instance.schedule.save()


@receiver(post_save, sender=equipment_models.Audit)
def create_observation(sender, instance, **kwargs):
    if not instance.is_ok:
        observation = equipment_models.Observation.objects.filter(audit = instance).first()
        if not observation:
            equipment_models.Observation.objects.get_or_create(
                audit = instance,
                schedule=instance.schedule,
                checkpoint=instance.checkpoint,
                owner=instance.auditor
            )

@receiver(post_save, sender=equipment_models.Audit)
def update_equipment_status(sender, instance, **kwargs):
    print(f"update_equipment_status trigger.................")
    audits =  equipment_query.AuditQuery().get_audits_by_equipment_id(instance.equipment.id)
    print(f"Audit found : {audits}")
    approve_statuses = [audit.approve_status for audit in audits]
    request_statuses = [audit.request_status for audit in audits]
    print(f"approve_statuses : {approve_statuses}")
    print(f"request_statuses : {request_statuses}")
    if all(status == 'APPROVED' for status in approve_statuses):
        instance.equipment.status = 'COMPLETED'
    elif all(status == 'REJECTED' for status in approve_statuses):
        instance.equipment.status = 'REJECTED'
    elif any(status == 'CLOSED' for status in request_statuses):
        instance.equipment.status = 'PARTIAL COMPLETED'
    instance.equipment.save()




# TODO:
#  schedule status depends on equipment status
#  equipment sttus depends on audit status
#  audits status depends on observation status

# TODO: step 1
# once schedule created it's status would be Pending
# once equipment is created it's status would be Pending
# once audit is created it's status would be Open
# once observers is created it's status would be Open
