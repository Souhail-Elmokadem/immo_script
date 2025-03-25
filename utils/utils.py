import re
import requests
class Utils:
    @staticmethod
    def get_numeric_value(text):
        if isinstance(text, (int, float)):
            return text
        if not text:
            return 0
        numbers = re.sub(r"[^\d]", "", text)
        return int(numbers) if numbers else 0
 

    def safe_division(numerator, denominator):
        try:
            num = Utils.get_numeric_value(numerator)
            den = Utils.get_numeric_value(denominator)
            return num / den if den else None
        except Exception:
            return None
    def geocode_address(address):
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
        except Exception as e:
            print(f"❌ Geocoding failed: {e}")
        return None, None