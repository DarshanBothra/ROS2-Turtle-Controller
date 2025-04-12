import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import time

class TurtleOdometer(Node):

    def __init__(self):
        super().__init__('turtle_odometer')
        self.sub = self.create_subscription(Pose, '/turtle1/pose', self.callback, 10)
        self.prev_pose = None
        self.total_distance = 0.0
        self.last_log_time = time.time()

    def callback(self, msg):
        if self.prev_pose is not None:
            dx = msg.x - self.prev_pose.x
            dy = msg.y - self.prev_pose.y
            dist = math.sqrt(dx**2 + dy**2)
            self.total_distance += dist

            current_time = time.time()

            if current_time - self.last_log_time >= 1.0:
                self.get_logger().info(f"Total Distance: {self.total_distance:.2f}")
                self.last_log_time = current_time
        self.prev_pose = msg


def main(args = None):
    rclpy.init(args = args)
    node = TurtleOdometer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()