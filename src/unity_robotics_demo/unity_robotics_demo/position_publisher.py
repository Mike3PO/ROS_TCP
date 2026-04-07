import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64

class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')

        self.dt = 0.05

        self.target_angle = Float64()
        self.input_angle = Float64()

        self.input_sub = self.create_subscription(
            Float64,
            '/angle_input',
            self.input_callback,
            10
        )

        self.pub = self.create_publisher(
            Float64,
            '/target_angle',
            10
        )

        self.timer = self.create_timer(self.dt, self.control_loop)

    def input_callback(self, msg):
        altered_data = (-msg.data)/7
        self.input_angle = msg
        self.input_angle.data = altered_data
        print("Received input:",msg.data)

    def control_loop(self):
        # self.target_position.x = self.input_vector.x
        # self.target_position.y = self.input_vector.y
        # self.target_position.z = self.input_vector.z
        self.target_angle.data = self.input_angle.data

        self.pub.publish(self.target_angle)

def main(args=None):
    rclpy.init(args=args)
    node = PositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()