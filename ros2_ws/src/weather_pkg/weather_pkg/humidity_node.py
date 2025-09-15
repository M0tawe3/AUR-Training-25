#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from random import randint
from sensor_msgs.msg import RelativeHumidity

class humidity_publisher(Node):
    def __init__(self):
        super().__init__("humidity")
        self.publisher_ = self.create_publisher(RelativeHumidity, "humidity", 10)
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        msg=RelativeHumidity()
        msg.relative_humidity = float(randint(20, 100))
        self.publisher_.publish(msg)
        self.get_logger().info(f"humidity: {msg.relative_humidity} %")

def main():
    rclpy.init()
    node=humidity_publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()