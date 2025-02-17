# --- agents.py ---
from crewai import Agent

# Agent Definitions
sensor_agent = Agent(
    role="Sensor Agent",
    goal="Collects and reports environmental and soil data.",
    backstory="This agent reads sensor data and provides it to the Decision Agent in a structured format.",
    verbose=True
)

decision_agent = Agent(
    role="Decision Agent",
    goal="Analyze sensor data and determine irrigation needs.",
    backstory="Uses AI to analyze sensor readings and decide whether to irrigate.",
    verbose=True
)

actuator_agent = Agent(
    role="Actuator Agent",
    goal="Execute irrigation actions based on the Decision Agent's instructions.",
    backstory="Controls the irrigation system based on received decisions.",
    verbose=True
)