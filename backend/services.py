import random


sensorData= {
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'vibration': round(random.uniform(0.0, 1.0), 2)
    }


def get_sensor_data():
    # Simulate sensor data retrieval
    return sensorData

def get_job_data():
    return{
        "name":"Helmet",
        "status":"Running",
        "progress": round(random.uniform(30.0,50.0),2),
        "layers":round  (random.uniform(2,5)),
    }