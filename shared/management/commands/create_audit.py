from django.core.management.base import BaseCommand
from equipment import models as equipment_models
from django.utils import timezone

class Command(BaseCommand):
    help = "Create a Audit"

    def handle(self, *args, **kwargs):
        self.create_audit()
        self.stdout.write(self.style.SUCCESS(f"Audit created successfully!"))

    def create_audit(self, *args, **kwargs):
        count = 0
        schedule_tasks = equipment_models.Schedule.objects.filter(schedule_date__lte = timezone.now())
        for schedule in schedule_tasks:
            count += 1
            if count % 2 == 0:
                equipment_models.Audit.objects.create(
                    equipment = schedule.equipment,
                    schedule = schedule,
                    auditor = schedule.user,
                    checkpoint=schedule.equipment.checkpoints.filter().first(),
                    is_ok=True
                )
            else:
                equipment_models.Audit.objects.create(
                    remark="Need to verify again about it",
                    equipment = schedule.equipment,
                    schedule = schedule,
                    auditor = schedule.user,
                    checkpoint=schedule.equipment.checkpoints.filter().first(),
                    is_ok=False
                )