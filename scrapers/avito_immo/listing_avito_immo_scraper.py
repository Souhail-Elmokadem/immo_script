import requests
import json
from bs4 import BeautifulSoup

def get_listing_info(url):
    # Fetch HTML content using requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("❌ Failed to retrieve the page. Status code:", response.status_code)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Find script containing JSON data
    script_tag = soup.find("script", id="__NEXT_DATA__")
    
    if not script_tag:
        print("❌ JSON data not found in script tag.")
        return None
    
    # Parse JSON content
    json_data = json.loads(script_tag.string)

    try:
        # Navigate through JSON structure
        project = json_data['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['project_details']

        # Extract unit details dynamically
        units = project.get("project_units", {})

        surface_area = "N/A"
        bedrooms = "N/A"
        bathrooms = "N/A"

        for unit_key, unit_list in units.items():
            if unit_list:  # Ensure unit list is not empty
                for unit in unit_list:
                    if "total_area" in unit and unit["total_area"]:  # Get first valid value
                        surface_area = unit["total_area"]
                    if "bedrooms" in unit and unit["bedrooms"] is not None:
                        bedrooms = unit["bedrooms"]
                    if "bathrooms" in unit and unit["bathrooms"] is not None:
                        bathrooms = unit["bathrooms"]
                    break  # Take the first unit available

        # Extract build status dynamically
        build_status = project.get("build_status", "N/A")

        # Extract longitude and latitude
        longitude = project.get("longitude", "N/A")
        latitude = project.get("latitude", "N/A")

        project_info = {
            "Project Name": project.get("name", "N/A"),
            "Build Status": build_status,  # Fixed issue where it was always 'not_started'
            "Price": project.get("price", "N/A"),
            "Location": f"{project.get('city', 'N/A')}, {project.get('district', 'N/A')}",
            "Surface Area": surface_area,
            "Bedrooms": bedrooms,
            "Bathrooms": bathrooms,
            "Completion Date": project.get("completion_date", "N/A"),
            "Developer": project.get("builder_name", "N/A"),
            "Contact Phone": project.get("contact", [{}])[0].get("phone", "N/A"),
            "Address": project.get("address", "N/A"),
            "Longitude": longitude,
            "Latitude": latitude,
            "Description": project.get("description", "N/A"),
        }

        return project_info

    except Exception as e:
        print("❌ Error extracting data:", e)
        return None
