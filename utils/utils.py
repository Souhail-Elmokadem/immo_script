import re

class Utils:
    def get_numeric_value(text):
        if not text:
            return 0  # or None
        numbers = re.sub(r"[^\d]", "", text)
        return int(numbers) if numbers else 0
 

    def safe_division(numerator, denominator):
        try:
            num = Utils.get_numeric_value(numerator)
            den = Utils.get_numeric_value(denominator)
            return num / den if den else None
        except Exception:
            return None
