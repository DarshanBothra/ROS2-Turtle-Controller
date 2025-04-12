# Turtle Controller using ROS2 (rclpy)

This package includes two ROS2 nodes written in Python using the rclpy package to write, control and monitor the turtle in the 'turtlesim' node simulator

## Nodes

- 'turtle_navigator': Moves the turtle to a desired target <x, y> using propositional controller (navigator)
- 'turtle_odomoter': Tracks the total distance traveled by the turtle and also displays the euclidian distance after every 1 second of luanching the turtle node

## Launch command

    Following commands are for linux terminal only

- inside the ros2 workspace build the ros project
    colcon build

- create a folder src in the ros2 workspace
    mkdir src

- clone the github repository (contains the files regarding this ros2 project)
    git clone https://github.com/DarshanBothra/ROS2-Turtle-Controller/turtle_controller

## Build the package:

- inside ros2 workspace
    cd ~/<ros2_workspace_name>
    colcon build
    source install/setup.bash

## How to Run

- after completing the above steps run the following command
    cd ~/<ros2_workspace_name>
    ros2 launch turtle_controller turtle_launch.py

## Change the x, y parameters

- open the /turtles_controller/launch/turtle_launch.py file
- change the 'paramters = [{'target_x': 8.0, 'target_y': 8.0}]' argument in second Node object of the generate_launch_description function to whatever coordinates (in floating point number) you like

## Bonus part

Bonus part has also been completed where after every one second the position of turtle will be displayed


'''
