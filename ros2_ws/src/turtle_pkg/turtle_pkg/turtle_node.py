#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class turtle_control(Node):
    def __init__(self):
        super().__init__("turtle_node")
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        msg=Twist()
        msg.linear.x = 3.0
        msg.angular.z = 1.5
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node=turtle_control()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()