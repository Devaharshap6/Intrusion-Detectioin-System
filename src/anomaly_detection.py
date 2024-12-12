from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.data = []

    def update_data(self, packet):
        self.data.append(packet["length"])
        if len(self.data) > 100:  # Keep the dataset manageable
            self.data.pop(0)

    def train(self):
        if len(self.data) > 10:
            self.model.fit(np.array(self.data).reshape(-1, 1))

    def detect(self, packet):
        if len(self.data) > 10:
            prediction = self.model.predict([[packet["length"]]])
            if prediction == -1:
                return f"Anomaly detected in traffic: {packet}"
        return None
