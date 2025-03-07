from equipment import models as equipment_models

class EquipmentService:
    @staticmethod
    def verify_equipment_location(equipment_id,latitude: str, longitude: str) -> bool:
        location = f"({latitude},{longitude})"
        return equipment_models.Equipment.objects.filter(location_coordinates=str(location),id=equipment_id).exists()