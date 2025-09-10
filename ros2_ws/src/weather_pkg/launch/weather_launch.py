from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="weather_pkg",
            executable="temperature"
        ),

        Node(
            package="weather_pkg",
            executable="humidity"
        ),

        Node(
            package="weather_pkg",
            executable="pressure"
        ),

        Node(
            package="weather_pkg",
            executable="monitor"
        )
    ])