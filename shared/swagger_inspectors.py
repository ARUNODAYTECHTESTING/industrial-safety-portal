from drf_yasg.inspectors import SwaggerAutoSchema

class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation):
        # Get the tags defined by the user in the operation
        tags = super().get_tags(operation)
        
        return tags