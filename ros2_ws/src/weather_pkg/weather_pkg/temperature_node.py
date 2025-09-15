#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from random import randint
from sensor_msgs.msg import Temperature

class temp_publisher(Node):
    def __init__(self):
        super().__init__("temperature")
        self.publisher_ = self.create_publisher(Temperature, "temp", 10)
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        msg=Temperature()
        msg.temperature = float(randint(15, 40))
        self.publisher_.publish(msg)
        self.get_logger().info(f"temperature: {msg.temperature} °C")

def main():
    rclpy.init()
    node=temp_publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()