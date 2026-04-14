import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import serial
import time

class SerialPublisher(Node):
    def __init__(self):
        super().__init__('serial_publisher')
        self.publisher_ = self.create_publisher(Float64, 'angle_input', 10)

        # self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

        self.timer = self.create_timer(0.01, self.read_serial)
        self.angle = 0
        self.increasing = True
        time.sleep(2)

    def read_serial(self):
        # if self.ser.in_waiting:
        #     line = self.ser.readline().decode().strip()
        #     try:
        #         msg = Float64()
        #         msg.data = float(line)
        #         self.publisher_.publish(msg)
        #         self.get_logger().info(f"Published: {msg.data}")
        #     except:
        #         pass
        if self.angle == 255:
            self.increasing = False
        elif self.angle == 0:
            self.increasing = True
        self.angle = self.angle + 1 if self.increasing else self.angle - 1
        msg = Float64()
        msg.data = float(self.angle)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published:\t{msg.data}")

def main():
    rclpy.init()
    node = SerialPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()