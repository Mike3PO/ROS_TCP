import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Vector3

class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')

        self.dt = 0.05

        self.target_position = Vector3()
        self.input_vector = Vector3()

        self.input_sub = self.create_subscription(
            Vector3,
            '/user_input',
            self.input_callback,
            10
        )

        self.pub = self.create_publisher(
            Vector3,
            '/target_position',
            10
        )

        self.timer = self.create_timer(self.dt, self.control_loop)

    def input_callback(self, msg):
        self.input_vector = msg

    def control_loop(self):
        self.target_position.x = self.input_vector.x
        self.target_position.y = self.input_vector.y
        self.target_position.z = 0.0

        self.pub.publish(self.target_position)

def main(args=None):
    rclpy.init(args=args)
    node = PositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()