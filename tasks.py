import random
import time
from crewai import Task, Crew
from config import INITIAL_FARM_DATA
from agents import sensor_agent, decision_agent, actuator_agent

farm_data = INITIAL_FARM_DATA.copy()

def format_sensor_data(sensor_data):
    """Formats sensor data into a structured report."""
    return (
        f"Temperature: {sensor_data['temperature']}°C\n"
        f"Humidity: {sensor_data['humidity']}%\n"
        f"Wind Speed: {sensor_data['wind_speed']} km/h\n"
        f"Solar Radiation: {sensor_data['solar_radiation']} W/m²\n"
        f"Rainfall: {sensor_data['rainfall']} mm\n"
        f"Soil Moisture: {sensor_data['soil_moisture']}% ({sensor_data['soil_status']})\n"
        f"Canopy Temperature: {sensor_data['canopy_temperature']}°C\n"
        f"Plant: {sensor_data['plant']} (Size: {sensor_data['plant_size']})\n"
        f"Water Tank: {sensor_data['water_tank']['remaining']}L remaining / {sensor_data['water_tank']['capacity']}L capacity\n"
    )

def process_plant(plant_id, sensor_data):
    """Process a single plant's data through the agent workflow."""
    formatted_data = format_sensor_data(sensor_data)

    sensor_task = Task(
        description=f"Collect sensor data and present it in the following format:\n\n{formatted_data}",
        expected_output="A structured sensor data report in the exact format provided above.",
        agent=sensor_agent
    )

    decision_task = Task(
        description=(
            "Analyze the given sensor data and decide if irrigation is required. "
            "Respond strictly in one of the following formats:\n"
            "1. 'You need [liters] liters of water for your [Plant] plant.' (Replace [liters] with the required volume.)\n"
            "2. 'Plant doesn't need water.'\n"
            "3. 'Not enough water in water tank.'"
        ),
        expected_output=(
            "A message in one of the formats:\n"
            "1. 'You need [liters] liters of water for your [Plant] plant.'\n"
            "2. 'Plant doesn't need water.'\n"
            "3. 'Not enough water in water tank.'"
        ),
        agent=decision_agent
    )

    actuator_task = Task(
        description="Execute the irrigation decision received from the Decision Agent.",
        expected_output="A confirmation that the irrigation system was activated or remained off.",
        agent=actuator_agent
    )

    crew = Crew(
        agents=[sensor_agent, decision_agent, actuator_agent],
        tasks=[sensor_task, decision_task, actuator_task],
        verbose=True
    )

    print(f"\n[PROCESSING] Starting workflow for {plant_id} ...")
    crew.kickoff()
    print(f"[PROCESSING] Finished workflow for {plant_id}.\n")

def update_sensor_data():
    """Background function to simulate sensor data updates."""
    while True:
        for plant_id, data in farm_data.items():
            data['temperature'] = round(data['temperature'] + random.uniform(-0.5, 0.5), 1)
            data['humidity'] = round(max(0, min(100, data['humidity'] + random.uniform(-1, 1))), 1)
            data['wind_speed'] = round(max(0, data['wind_speed'] + random.uniform(-0.5, 0.5)), 1)
            data['solar_radiation'] = round(max(0, data['solar_radiation'] + random.uniform(-10, 10)), 1)
            data['rainfall'] = round(random.choice([0, 0, 0, 1, 2]), 1)
            data['soil_moisture'] = round(max(0, min(100, data['soil_moisture'] + random.uniform(-1, 1))), 1)
        time.sleep(5)

def process_farm():
    """Background function to continuously process farm data."""
    while True:
        for plant_id, data in farm_data.items():
            process_plant(plant_id, data)
        time.sleep(5)