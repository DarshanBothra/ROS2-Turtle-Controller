from launch import LaunchDescription
import launch_ros
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [Node(
                package = 'turtlesim',
                executable='turtlesim_node',
                name='turtlesim'
            ),
            Node(
                package='turtle_controller',
                executable='turtle_navigator',
                name = 'turtle_navigator',
                parameters = [{'target_x': 8.0, 'target_y': 10.0}]
            ),
            Node(
                package='turtle_controller',
                executable='turtle_odometer',
                name = 'turtle_odometer'
            )
        ])