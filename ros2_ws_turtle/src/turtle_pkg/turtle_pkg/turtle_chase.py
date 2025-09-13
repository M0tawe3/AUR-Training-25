#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random
from math import sqrt
from std_msgs.msg import Int32
from turtlesim.srv import Kill, Spawn
from turtlesim.msg import Pose

class turtle_chase(Node):
    def __init__(self):
        super().__init__("turtle_chase")

        self.client_s = self.create_client(Spawn, "spawn")
        self.client_k = self.create_client(Kill, "kill")

        names = ['enemy1', 'enemy2', 'enemy3']
        for name in names:
            self.spawn(name)

        self.score = 0
        self.enemy_positions = {}
        
        self.subscriber_player = self.create_subscription(Pose, "/turtle1/pose", self.player_callback, 10)
        self.subscriber_1 = self.create_subscription(Pose, "/enemy1/pose", self.enemy1_callback, 10)
        self.subscriber_2 = self.create_subscription(Pose, "/enemy2/pose", self.enemy2_callback, 10)
        self.subscriber_3 = self.create_subscription(Pose, "/enemy3/pose", self.enemy3_callback, 10)
        self.publisher_ = self.create_publisher(Int32, "/score", 10)

        self.create_timer(2.5, self.publish_score)
        self.create_timer(0.1, self.check_collision)

    def spawn_callback(self, future):
        response = future.result()

    def kill_callback(self, future, name):
        response = future.result()
        self.spawn(name)    

    def player_callback(self, msg: Pose):
        self.position = [msg.x, msg.y]

    def enemy1_callback(self, msg: Pose):
        self.enemy_positions['enemy1'] = [msg.x, msg.y]

    def enemy2_callback(self, msg: Pose):
        self.enemy_positions['enemy2'] = [msg.x, msg.y]

    def enemy3_callback(self, msg: Pose):
        self.enemy_positions['enemy3'] = [msg.x, msg.y]

    def publish_score(self):
        msg = Int32()
        msg.data = self.score
        self.publisher_.publish(msg)

    def spawn(self, name):
        req = Spawn.Request()
        req.x = random.uniform(0.0, 11.0)
        req.y = random.uniform(0.0, 11.0)
        req.theta = 0.0
        req.name = name
        future = self.client_s.call_async(req)
        future.add_done_callback(self.spawn_callback)

    def kill(self, name):
        req = Kill.Request()
        req.name = name
        future = self.client_k.call_async(req)
        future.add_done_callback(lambda f: self.kill_callback(f, name))

    def check_collision(self):
        for name,pose in list(self.enemy_positions.items()):
            dist = sqrt((pose[0] - self.position[0])**2 + (pose[1] - self.position[1])**2)
            if dist <= 0.5:
                self.kill(name)
                self.score +=   1


def main():
    rclpy.init()
    node=turtle_chase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()