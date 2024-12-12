from flask import Flask, render_template, jsonify
from threading import Thread
from src.ids import IntrusionDetectionSystem
from src.packet_sniffer import capture_packets

app = Flask(__name__)
ids = IntrusionDetectionSystem()

@app.route("/")
def index():
    """Render the main dashboard."""
    return render_template("index.html")

@app.route("/alerts")
def alerts():
    """API endpoint to fetch alerts."""
    return jsonify(ids.get_alerts())

def run_sniffer():
    """Run the packet sniffer in a separate thread."""
    for packet in capture_packets():
        ids.process_packet(packet)

if __name__ == "__main__":
    # Start the packet sniffer in a background thread
    sniffer_thread = Thread(target=run_sniffer, daemon=True)
    sniffer_thread.start()

    # Run the Flask app
    app.run(debug=True)
