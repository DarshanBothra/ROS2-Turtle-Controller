import math 
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TrutleNavigator(Node):

    def __init__(self):
        super().__init__('turtle_navigator')
        self.declare_parameter('target_x', 5.5)
        self.declare_parameter('target_y', 5.5)
        self.target_x = self.get_parameter('target_x').value
        self.target_y = self.get_parameter('target_y').value
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose = None
        self.timer = self.create_timer(0.1, self.navigate)

    def pose_callback(self, msg):
        self.pose = msg

    def navigate(self): # Propositional Controller
        if self.pose is None:
            return
        
        dx = self.target_x - self.pose.x
        dy = self.target_y - self.pose.y

        distance = math.sqrt(dx**2 + dy**2)

        if distance < 0.1:
            self.cmd_pub.publish(Twist())
            self.get_logger().infO("Target reached")
            return
        
        angle_to_target = math.atan2(dy, dx)
        angle_error = angle_to_target - self.pose.theta

        vel_msg = Twist()
        vel_msg.linear.x = 1.5*distance
        vel_msg.angular.z = 6.0*angle_error
        self.cmd_pub.publish(vel_msg)


def main(args = None):
    rclpy.init(args = args)
    node = TrutleNavigator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()