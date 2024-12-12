from src.packet_sniffer import capture_packets
from src.signature_detection import load_signatures, check_signatures
from src.anomaly_detection import AnomalyDetector

class IntrusionDetectionSystem:
    def __init__(self):
        self.signatures = load_signatures()
        self.anomaly_detector = AnomalyDetector()
        self.alerts = []

    def process_packet(self, packet):
        self.anomaly_detector.update_data(packet)
        self.anomaly_detector.train()

        signature_alert = check_signatures(packet, self.signatures)
        anomaly_alert = self.anomaly_detector.detect(packet)

        for alert in [signature_alert, anomaly_alert]:
            if alert:
                self.alerts.append({"packet": packet, "alert": alert})
                return alert
        return None

    def get_alerts(self):
        return self.alerts
