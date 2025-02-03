import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from account import models as account_models
from account import utils as account_utils
from equipment import models as equipment_models


class Command(BaseCommand):
    help = "Load dummy data into the database"

    def handle(self, *args, **kwargs):
        self.create_dummy_user_type()
        self.create_dummy_plant()
        self.create_dummy_line()
        self.create_dummy_station()
        self.create_dummy_equipment_type()
        self.create_dummy_equipment()
        self.create_dummy_audit_parameter()
        self.create_dummy_checkpoint()
        self.create_dummy_observation()
        self.dump_dummy_users_into_database()
        self.stdout.write(self.style.SUCCESS("Dummy data loaded successfully!"))

    def load_json_data(self, filename):
        """Helper method to load JSON data from a file."""
        file_path = os.path.join("shared/dummy", filename)
        with open(file_path, "r") as file:
            return json.load(file)

    def create_dummy_user_type(self):
        data = self.load_json_data("user_types.json")
        for item in data:
            Group.objects.get_or_create(name=item.get("name"))

    def create_dummy_plant(self):
        data = self.load_json_data("plants.json")
        for item in data:
            equipment_models.Plant.objects.get_or_create(id=item.get("id"), name=item.get("name"))

    def create_dummy_line(self):
        data = self.load_json_data("lines.json")
        for item in data:
            try:
                equipment_models.Line.objects.get_or_create(
                    id=item.get("id"), name=item.get("name"), plant_id=item.get("plant_id")
                )
            except Exception:
                continue

    def create_dummy_station(self):
        data = self.load_json_data("stations.json")
        for item in data:
            try:
                equipment_models.Station.objects.get_or_create(
                    id=item.get("id"), name=item.get("name"), plant_id=item.get("plant_id"), line_id=item.get("line_id")
                )
            except Exception:
                continue

    def create_dummy_equipment_type(self):
        data = self.load_json_data("equipment_types.json")
        for item in data:
            try:
                equipment_models.EquipmentType.objects.get_or_create(id=item.get("id"), name=item.get("name"))
            except Exception:
                continue

    def create_dummy_equipment(self):
        data = self.load_json_data("equipments.json")
        for item in data:
            try:
                equipment_models.Equipment.objects.get_or_create(
                    id=item.get("id"),
                    name=item.get("name"),
                    equipment_type_id=item.get("equipment_type_id"),
                    plant_id=item.get("plant_id"),
                    line_id=item.get("line_id"),
                    station_id=item.get("station_id"),
                )
            except Exception:
                continue

    def create_dummy_audit_parameter(self):
        data = self.load_json_data("audit_parameters.json")
        for item in data:
            try:
                equipment_models.MasterAuditParameter.objects.get_or_create(id=item.get("id"), name=item.get("name"))
            except Exception:
                continue

    def create_dummy_checkpoint(self):
        data = self.load_json_data("checkpoints.json")
        for item in data:
            try:
                equipment_models.Checkpoint.objects.get_or_create(
                    id=item.get("id"),
                    equipment_id=item.get("equipment_id"),
                    audit_parameter_id=item.get("audit_parameter_id"),
                )
            except Exception:
                continue

    def create_dummy_observation(self):
        data = self.load_json_data("observations.json")
        for item in data:
            try:
                equipment_models.Observation.objects.get_or_create(
                    id=item.get("id"), name=item.get("name"), checkpoint_id=item.get("checkpoint_id")
                )
            except Exception:
                continue

    def dump_dummy_users_into_database(self):
        data = self.load_json_data("users.json")
        for item in data:
            try:
                user, created = account_models.User.objects.get_or_create(
                    name=item.get("name"),
                    password=account_utils.PasswordManager.hash_password(item.get("password")),
                    department_id=item.get("department"),
                    plant_id=item.get("plant"),
                    email=item.get("email"),
                    phone=item.get("phone"),
                )
                user.groups.set(item.get("user_type", []))
                user.save()
            except Exception:
                continue
