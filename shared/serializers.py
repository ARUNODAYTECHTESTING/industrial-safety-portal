from rest_framework import serializers
from typing import Tuple, Any, Dict, Union,List
from django.db.models import QuerySet,Model

class SerializerValidator:
    def __init__(self, serializer_class: serializers.Serializer):
        self.serializer_class = serializer_class

    def validate(self, payload: dict) -> Tuple[int, Union[Dict[str, Any], dict]]:
        """Validate the input data using the serializer."""
        serializer = self.serializer_class(data=payload)
        if not serializer.is_valid():
            return 400,serializer
        
        return 200, serializer

    def serialize_queryset(self, queryset: QuerySet) -> Tuple[int, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """Serialize the queryset to JSON."""
        try:
            serialized_data = self.serializer_class(queryset, many=True).data
            return 200, serialized_data
        except Exception as e:
            return 400, {'error': str(e)}
    
   
    def serialize_object(self, obj: Model) -> Tuple[int, Union[Dict[str, Any], dict]]:
        
        """Serialize the model object to JSON."""
        try:
            serialized_data = self.serializer_class(obj).data
            return 200, serialized_data
        except Exception as e:
            return 400, {'error': str(e)}
    