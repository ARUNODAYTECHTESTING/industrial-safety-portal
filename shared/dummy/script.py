from account import models
from account import utils as account_utils
from equipment import models as equipment_models
import json
from django.contrib.auth.models import Group
def dump_dummy_users_into_databases():

    json_file_path = 'dummy/users.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            try:
                user = models.User.objects.get_or_create(
                    name=item.get('name'),
                    password=account_utils.PasswordManager.hash_password(item.get('password')),
                    department_id=item.get('department'),
                    plant_id=item.get('plant'),
                    email=item.get('email'),
                    phone=item.get('phone')
                )
                user.groups.set(item.get('user_type'))
                user.save()
            except Exception as e:
                continue
    
def create_dummy_plant():

    json_file_path = 'dummy/plants.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
        equipment_models.Plant.objects.get_or_create(id=item.get("id"),name=item.get('name'),)

def create_dummy_user_type():
    json_file_path = 'dummy/user_types.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
        Group.objects.get_or_create(name=item.get('name'),)

def create_dummy_line():
    json_file_path = 'dummy/lines.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
        equipment_models.Line.objects.get_or_create(id=item.get("id"),name=item.get('name'),plant_id=item.get('plant_id'))
       except Exception as e:
            continue

def create_dummy_station():
    json_file_path = 'dummy/stations.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
        equipment_models.Station.objects.get_or_create(id=item.get("id"),name=item.get('name'),plant_id=item.get('plant_id'),line_id=item.get('line_id'))
       except Exception as e:
            continue

def create_dummy_equipment_type():
    json_file_path = 'dummy/equipment_types.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
        equipment_models.EquipmentType.objects.get_or_create(id=item.get("id"),name=item.get('name'))
       except Exception as e:
            continue

def create_dummy_equipment():
    json_file_path = 'dummy/equipments.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
            equipment_models.Equipment.objects.get_or_create(
                                id=item.get("id"),
                                name=item.get('name'),
                                equipment_type_id=item.get('equipment_type_id'),
                                plant_id=item.get('plant_id'),
                                line_id=item.get('line_id'),
                                station_id=item.get('station_id')
                                )
       except Exception as e:
            continue

def create_dummy_audit_parameter():
    json_file_path = 'dummy/audit_parameters.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
            equipment_models.Equipment.objects.get_or_create(
                                id=item.get("id"),
                                name=item.get('name'),
                                equipment_type_id=item.get('equipment_type_id'),
                                plant_id=item.get('plant_id'),
                                line_id=item.get('line_id'),
                                station_id=item.get('station_id')
                                )
       except Exception as e:
            continue
    
def create_dummy_checpoint():
    json_file_path = 'dummy/checkpoints.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
            equipment_models.Checkpoint.objects.get_or_create(
                            id=item.get("id"),
                            equipment_id=item.get('equipment_id'),
                            audit_parameter_id=item.get('audit_parameter_id')
            )
       except Exception as e:
            continue

def create_dummy_observation():
    json_file_path = 'dummy/observations.json'

    with open(json_file_path, 'r') as file:
        data = json.load(file)  
    for item in data:
       try:
            equipment_models.Observation.objects.get_or_create(
                            id=item.get("id"),
                            name= item.get("name"),
                            checkpoint_id=item.get('checkpoint'),
            )
       except Exception as e:
            continue
       
create_dummy_user_type()
create_dummy_plant()
create_dummy_line()
create_dummy_station()
create_dummy_equipment_type()
create_dummy_equipment()
create_dummy_checpoint()
create_dummy_observation()
dump_dummy_users_into_databases()