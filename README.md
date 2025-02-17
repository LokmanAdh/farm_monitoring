# Farm Monitoring System

An intelligent farm monitoring system that uses AI agents to automate irrigation decisions based on real-time sensor data. The system employs three specialized agents (Sensor, Decision, and Actuator) to collect data, make decisions, and control irrigation systems.

## Features

- 🌱 Real-time monitoring of multiple plants/crops
- 🤖 AI-powered decision making for irrigation
- 📊 Web-based dashboard for sensor data visualization
- 🔄 Automated sensor data collection and processing
- 💧 Smart water management system
- 🌡️ Environmental metrics tracking (temperature, humidity, wind speed, etc.)

## Technology Stack

- **Backend**: Python, Flask
- **AI/ML**: LangChain, CrewAI
- **Frontend**: HTML, JavaScript
- **LLM Integration**: Local LM Studio setup

## Prerequisites

- Python 3.8+
- LM Studio running locally
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/farm-monitoring.git
cd farm-monitoring
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask crewai langchain-openai
```

4. Set up LM Studio:
- Download and install LM Studio
- Start the local server on port 1234
- Ensure the model "deepseek-r1-distill-qwen-7b" is loaded

## Project Structure

```
farm_monitoring/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── agents.py             # AI agent definitions
├── data_processor.py     # Core data processing logic
└── templates/
    └── index.html        # Web dashboard template
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. The dashboard will automatically update every 5 seconds with:
- Current sensor readings
- Plant status
- Water tank levels
- Environmental conditions

## Customization

### Adding New Plants

Edit `config.py` to add new plants to the `INITIAL_FARM_DATA` dictionary:

```python
"plant3": {
    "temperature": 25,
    "humidity": 58,
    "wind_speed": 2.5,
    "solar_radiation": 580,
    "rainfall": 0,
    "soil_moisture": 28,
    "soil_status": "Good",
    "canopy_temperature": 27,
    "plant": "Cucumber",
    "plant_size": "Medium",
    "water_tank": {
        "remaining": 4.0,
        "capacity": 5.0
    }
}
```

### Modifying Agent Behavior

Adjust agent parameters in `agents.py` to customize their behavior and decision-making processes.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- CrewAI for the agent framework
- LangChain for LLM integration
- Flask team for the web framework
- LM Studio for local LLM hosting

## Support

For support, please open an issue in the GitHub repository or contact the maintainers at:
- Email: your.email@example.com
- Twitter: [@yourusername](https://twitter.com/yourusername)

## Roadmap

- [ ] Add support for more crop types
- [ ] Implement weather API integration
- [ ] Add historical data visualization
- [ ] Develop mobile application
- [ ] Add alert system for critical conditions
- [ ] Implement machine learning for improved decision making

---
Made with ❤️ by [Your Name](https://github.com/LokmanAdh)
