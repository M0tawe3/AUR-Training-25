#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from random import randint
from sensor_msgs.msg import FluidPressure

class pressure_publisher(Node):
    def __init__(self):
        super().__init__("pressure")
        self.publisher_ = self.create_publisher(FluidPressure, "pressure", 10)
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        msg=FluidPressure()
        msg.fluid_pressure = float(randint(900, 1100))
        self.publisher_.publish(msg)
        self.get_logger().info(f"pressure: {msg.fluid_pressure} hPa")

def main():
    rclpy.init()
    node=pressure_publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()