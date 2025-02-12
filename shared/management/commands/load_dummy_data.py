import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from account import models as account_models
from account import utils as account_utils
from equipment import models as equipment_models
from django.utils.dateparse import parse_date
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Load dummy data into the database"

    def handle(self, *args, **kwargs):
        self.setup_permissions()

        self.create_dummy_departments()
        # self.create_dummy_user_type()
        self.create_dummy_plant()
        self.create_dummy_line()
        self.create_dummy_station()
        self.create_dummy_equipment_type()
        self.create_dummy_equipment()
        self.create_dummy_audit_parameter()
        self.create_dummy_checkpoint()
        self.create_dummy_observation()
        self.dump_dummy_users_into_database()
        self.create_dummy_shedule_type()
        self.create_dummy_shedule()
        self.stdout.write(self.style.SUCCESS("Dummy data loaded successfully!"))


    def setup_permissions(self):
        """Set up permissions for different user groups"""
        permission_mapping = {
            'Super Admin': {
                account_models.Department: ['add', 'change', 'delete', 'view'],
                equipment_models.Line: ['add', 'change', 'delete', 'view'],
                equipment_models.Station: ['add', 'change', 'delete', 'view'],
                equipment_models.Equipment: ['add', 'change', 'delete', 'view'],
                equipment_models.EquipmentType: ['add', 'change', 'delete', 'view'],
                equipment_models.MasterAuditParameter: ['add', 'change', 'delete', 'view'],
                account_models.User: ['add', 'change', 'delete', 'view'],  # Added User permissions
            },
            'Portal Admin': {
                equipment_models.Plant: ['add', 'change', 'delete', 'view'],
                account_models.Department: ['add', 'change', 'delete', 'view'],
                equipment_models.Line: ['add', 'change', 'delete', 'view'],
                equipment_models.Station: ['add', 'change', 'delete', 'view'],
                equipment_models.Equipment: ['add', 'change', 'delete', 'view'],
                equipment_models.EquipmentType: ['add', 'change', 'delete', 'view'],
                equipment_models.MasterAuditParameter: ['add', 'change', 'delete', 'view'],
                account_models.User: ['add', 'change', 'delete', 'view'],  # Added User permissions
            },
            'Admin': {
                equipment_models.Equipment: ['add', 'change', 'delete', 'view'],
                equipment_models.Checkpoint: ['add', 'change', 'delete', 'view'],
                equipment_models.MasterAuditParameter: ['add', 'change', 'delete', 'view'],
                account_models.User: ['add', 'change', 'delete', 'view'],  # Added User permissions
            },
            'Auditor': {
                equipment_models.Plant: ['view'],
                account_models.Department: ['view'],
                equipment_models.Line: ['view'],
                equipment_models.Station: ['view'],
                equipment_models.Equipment: ['view'],
                equipment_models.EquipmentType: ['view'],
                equipment_models.Checkpoint: ['view'],
                equipment_models.MasterAuditParameter: ['view'],
                equipment_models.Observation: ['add', 'change', 'delete', 'view'],
            }
        }

        for group_name, model_permissions in permission_mapping.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Created group: {group_name}')
            
            # Clear existing permissions for clean setup
            group.permissions.clear()
            
            # Assign new permissions
            for model, permissions in model_permissions.items():
                content_type = ContentType.objects.get_for_model(model)
                for permission in permissions:
                    codename = f'{permission}_{model._meta.model_name}'
                    try:
                        perm = Permission.objects.get(
                            codename=codename,
                            content_type=content_type
                        )
                        group.permissions.add(perm)
                        self.stdout.write(
                            f'Added {permission} permission for {model.__name__} to {group_name}'
                        )
                    except Permission.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(
                                f'Permission {codename} does not exist for {model.__name__}'
                            )
                        )

        self.stdout.write(self.style.SUCCESS('Successfully set up all permissions'))

    def load_json_data(self, filename):
        """Helper method to load JSON data from a file."""
        file_path = os.path.join("shared/dummy", filename)
        with open(file_path, "r") as file:
            return json.load(file)
        
    def create_dummy_departments(self):
        data = self.load_json_data("departments.json")
        for item in data:
            account_models.Department.objects.get_or_create(id=item["id"],name=item.get("name"))


    # def create_dummy_user_type(self):
    #     data = self.load_json_data("user_types.json")
    #     for item in data:
    #         Group.objects.get_or_create(name=item.get("name"))

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
                equipment_models.Observation.objects.create(
                    name=item.get("name"),
                    checkpoint_id=item.get("checkpoint"),  # Changed from checkpoint_id
                    image=item.get("image"),  
                    attempt=item.get("attempt"),
                    category=item.get("category", ""), 
                    corrective_remark=item.get("corrective_remark", ""),
                    owner_id=item.get("owner"),  
                    department_id=item.get("department"),  
                    plant_id=item.get("plant"),  
                    remark=item.get("remark", ""),  
                    request_status=item.get("request_status"),  
                    approve_status=item.get("approve_status"), 
                )
            except Exception as e:
                print(f"Error creating observation: {e}")
                continue
    def dump_dummy_users_into_database(self):
        data = self.load_json_data("users.json")
        for item in data:
            try:
                user, created = account_models.User.objects.get_or_create(
                    name=item.get("name"),
                    password=account_utils.PasswordManager.hash_password('123456'),
                    department_id=item.get("department"),
                    plant_id=item.get("plant"),
                    email=item.get("email"),
                    phone=item.get("phone"),
                    token_id=item.get("token"),
                )
                user.groups.set(item.get("user_type", []))
                user.save()
            except Exception:
                continue
    def create_dummy_shedule_type(self):
        data = self.load_json_data("shedule_types.json")
        for item in data:
            equipment_models.ScheduleType.objects.get_or_create(id=item["id"],name=item.get("name"))
    
    def create_dummy_shedule(self):
        data = self.load_json_data("shedules.json")
        print("scheduel ---------------------------------------------------------")
        for item in data:
           
            equipment_models.Schedule.objects.get_or_create(
                user_id=item["user"],
                equipment_id=item["equipment"],
                plant_id=item["plant"],
                department_id=item["department"],
                line_id=item["line"],
                station_id=item["station"],
                schedule_type_id=item["schedule_type"],
                assigned_by_id = item["assigned_by"]
            )
    