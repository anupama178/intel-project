import psutil
import time
from pymongo import MongoClient
import subprocess
import threading
client = MongoClient('localhost', 27017)
db = client.telemetry_database 
collection = db.cpu_telemetry  

def capture_telemetry():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        timestamp = time.time()

        telemetry_data = {
            'timestamp': timestamp,
            'cpu_percent': cpu_percent,
        }

        collection.insert_one(telemetry_data)

        time.sleep(1) 

def start_stress_test():
    subprocess.run(['docker', 'run', '--rm', 'stress-ng', '--cpu', '4', '--cpu-load', '100'])

if __name__ == '__main__':
    stress_thread = threading.Thread(target=start_stress_test)
    stress_thread.start()

    capture_telemetry()
