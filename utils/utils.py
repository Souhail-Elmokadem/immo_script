import re

class Utils:
    def get_numeric_value(text):
        """Extracts the full numeric value from a string (handles spaces)."""
        numbers = re.sub(r"[^\d]", "", text)  # Removes all non-numeric characters
        return int(numbers) if numbers else None  # Converts to integer if found    