import requests
import config

def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

def get_total_records():
    """Ask the API how many records exist right now."""
    headers = get_headers()
    check_url = f"https://api.data.gov.in/resource/{config.RESOURCE_ID}?api-key={config.API_KEY}&format=json&limit=1"
    try:
        response = requests.get(check_url, headers=headers, timeout=30)
        return response.json()["total"]
    except requests.exceptions.RequestException as e:
        print("Failed to check total records:", e)
        return None

def fetch_all_records():
    """Fetch the full set of current AQI records."""
    total = get_total_records()
    if total is None:
        return None

    headers = get_headers()
    url = f"https://api.data.gov.in/resource/{config.RESOURCE_ID}?api-key={config.API_KEY}&format=json&limit={total}"

    try:
        response = requests.get(url, headers=headers, timeout=60)
        data = response.json()
        print(f"Total available: {data['total']}, Count returned: {data['count']}")
        return data["records"]
    except requests.exceptions.RequestException as e:
        print("Failed to fetch AQI data:", e)
        return None