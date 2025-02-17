# farm_monitoring/
# --- config.py ---
import os

# LLM Configuration
os.environ["OPENAI_API_KEY"] = "lm-studio"  # Required but ignored
os.environ["OPENAI_API_BASE"] = "http://localhost:1234/v1"  # Force local model

# Initial Farm Data Configuration
INITIAL_FARM_DATA = {
    "plant1": {
        "temperature": 28,
        "humidity": 55,
        "wind_speed": 3,
        "solar_radiation": 600,
        "rainfall": 0,
        "soil_moisture": 25,
        "soil_status": "Moderate",
        "canopy_temperature": 30,
        "plant": "Lettuce",
        "plant_size": "Small",
        "water_tank": {
            "remaining": 2.0,
            "capacity": 5.0
        }
    },
    "plant2": {
        "temperature": 26,
        "humidity": 60,
        "wind_speed": 2,
        "solar_radiation": 550,
        "rainfall": 0,
        "soil_moisture": 30,
        "soil_status": "Good",
        "canopy_temperature": 28,
        "plant": "Tomato",
        "plant_size": "Medium",
        "water_tank": {
            "remaining": 3.0,
            "capacity": 5.0
        }
    }
}