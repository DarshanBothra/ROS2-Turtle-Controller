from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package = 'turtlesim',
                executable='turtlesim_node',
                name='turtlesim'
            ),
            Node(
                package='turtle_controller',
                executable='turtle_navigator',
                name = 'turtle_navigator',
                paramters = [{'target_x': 8.0, 'target_y': 2.0}]
            ),
            Node(
                package='turtle_controller',
                executable='turtle_odometer',
                name = 'turtle_odometer'
            )
        ]
    )