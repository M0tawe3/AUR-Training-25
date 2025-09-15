#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import RelativeHumidity
from sensor_msgs.msg import Temperature
from sensor_msgs.msg import FluidPressure

class monitor(Node):
    def __init__(self):
        super().__init__("monitor")

        self.sub_humidity = self.create_subscription(RelativeHumidity, "humidity", self.humidity_callback, 10)
        self.sub_temp = self.create_subscription(Temperature, "temp", self.temp_callback, 10)
        self.sub_pressurer = self.create_subscription(FluidPressure, "pressure", self.pressure_callback, 10)

        self.timer = self.create_timer(1.0, self.log_all)

        self.latest_temp = None
        self.latest_humidity = None
        self.latest_pressure = None

        self.log_file = open("weather_report.txt", "a")
        self.add_on_shutdown(self.cleanup)


    def humidity_callback(self, msg: RelativeHumidity):
        self.latest_humidity = msg.relative_humidity

    def temp_callback(self, msg: Temperature):
        self.latest_temp = msg.temperature

    def pressure_callback(self, msg: FluidPressure):
        self.latest_pressure = msg.fluid_pressure

    def log_all(self):
        if self.latest_humidity is not None and self.latest_temp is not None and self.latest_pressure is not None:
           self.get_logger().info(f"temperature = {self.latest_temp}°C, Humidity = {self.latest_humidity}%, Pressure ={self.latest_pressure}hPa")
           self.log_file.write(f"temperature = {self.latest_temp}°C, Humidity = {self.latest_humidity}%, Pressure ={self.latest_pressure}hPa\n")
           self.log_file.flush()



def main():
    rclpy.init()
    node=monitor()
    rclpy.spin(node)
    node.log_file.close()
    node.destroy_node()
    rclpy.shutdown()