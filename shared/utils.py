import math

class CoordinateRangeCalculator:
    def __init__(self, latitude, longitude, range_meters):
        self.latitude = latitude
        self.longitude = longitude
        self.range_meters = range_meters
    @staticmethod
    def extract_coordinates(coord_string):
        # Remove parentheses and split by comma
        lat, lon = coord_string.strip("()").split(",")
        # Convert to float and return
        return float(lat), float(lon)

    def calculate_latitude_change(self):
        # 1 degree latitude = 111,000 meters
        return self.range_meters / 111000


    def calculate_longitude_change(self):
        # 1 degree longitude varies by latitude
        meters_per_degree = 111000 * abs(math.cos(math.radians(self.latitude)))
        return self.range_meters / meters_per_degree

    def get_coordinate_range(self):
        lat_change = self.calculate_latitude_change()
        lon_change = self.calculate_longitude_change()

        min_latitude = self.latitude - lat_change
        max_latitude = self.latitude + lat_change
        min_longitude = self.longitude - lon_change
        max_longitude = self.longitude + lon_change

        return {
            'min_latitude': min_latitude,
            'max_latitude': max_latitude,
            'min_longitude': min_longitude,
            'max_longitude': max_longitude
        }

    def is_within_range(self, user_latitude, user_longitude):
        coord_range = self.get_coordinate_range()
        return (
            coord_range['min_latitude'] <= float(user_latitude) <= coord_range['max_latitude'] and
            coord_range['min_longitude'] <= float(user_longitude) <= coord_range['max_longitude']
        )


# Example usage
# calc = CoordinateRangeCalculator(10.41, 10.41)
# print("Coordinate Range:", calc.get_coordinate_range())

# # Check if a point is within the range
# user_latitude = 7.715
# user_longitude = 13.105
# print("Is within range:", calc.is_within_range(user_latitude, user_longitude))