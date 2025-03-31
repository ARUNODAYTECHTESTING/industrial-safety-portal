import base64
import logging
from django.core.files.base import ContentFile

# Configure logging
logger = logging.getLogger(__name__)
def decode_base64_image(base64_string, filename_prefix="audit"):
    """
    Decodes a base64-encoded image and returns a ContentFile.
    """
    logger.debug(f"Attempting to decode image with prefix {filename_prefix}")
    
    if not base64_string:
        logger.error("Base64 string is empty or None")
        return None
        
    try:
        if not base64_string.startswith("data:image"):
            logger.error(f"Invalid Base64 image format: {base64_string[:30]}...")
            return None

        # Split the metadata and actual base64 data
        format, imgstr = base64_string.split(";base64,")
        ext = format.split("/")[-1]  # Extract file extension (e.g., png, jpg, jpeg)
        
        logger.debug(f"Image format: {format}, extension: {ext}")
        
        # Decode the base64 string
        decoded_image = base64.b64decode(imgstr)

        if len(decoded_image) == 0:
            logger.warning("Decoded image is empty")
            return None

        # Log image details
        logger.info(f"Successfully decoded image of size {len(decoded_image)} bytes with extension {ext}")

        # Create a ContentFile with a unique name
        filename = f"{filename_prefix}.{ext}"
        logger.debug(f"Creating ContentFile with name: {filename}")
        return ContentFile(decoded_image, name=filename)
    
    except Exception as e:
        logger.exception(f"Error decoding base64 image: {e}")
        return None