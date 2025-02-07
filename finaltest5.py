import subprocess
class SensorReading:
    def __init__(self,sensor_id,timestamp,value):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
    
    def display(self):
        print(f"[{self.timestamp}] Sensor {self.sensor_id}: {self.value}")
    
sen1 = SensorReading("TEMP-01","2025-02-06 16:45:00",25.6)
sen1.display()

class SensorLog(SensorReading):
    def __init__(self,sensor_id,timestamp,value,readings):
        super().__init__(sensor_id,timestamp,value)
        self.readings = readings

    def add_reading(self,sensor_reading):
        self.readings.append(sensor_reading)

    def show_all(self):
        for i in self.readings:
            i.display()
    
    def save_to_file(self,filename):
        try:
            with open(filename,"w") as f:
                for i in self.readings:
                    f.write(f"[{i.timestamp}] Sensor {i.sensor_id}: {i.value}\n")

        except Exception as e:
            print(e)

    def save_with_subprocess(self,filename):
        try:
            with open(filename,"w") as f:
                for i in self.readings:
                    s = subprocess.Popen(["tee"],stdin=subprocess.PIPE,stdout=f,text=True)
                    s.communicate(f"[{i.timestamp}] Sensor {i.sensor_id}: {i.value}\n")

        except Exception as e:
            print(e)        


sen2 = SensorReading("PRESSURE-01","2025-02-06 16:45:00",1.2)
log = SensorLog("","",0,[])
log.add_reading(sen1)
log.add_reading(sen2)
log.show_all()
log.save_with_subprocess("sensor_log.txt")