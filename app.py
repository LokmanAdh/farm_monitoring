# --- app.py ---
import threading
from flask import Flask, render_template, jsonify
from tasks import farm_data, update_sensor_data, process_farm

app = Flask(__name__)

@app.route('/data')
def data():
    return jsonify(farm_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Start background threads
    threading.Thread(target=update_sensor_data, daemon=True).start()
    threading.Thread(target=process_farm, daemon=True).start()
    
    # Run Flask app
    app.run(debug=True, use_reloader=False)