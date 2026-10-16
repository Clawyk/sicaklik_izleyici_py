import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class SicaklikSensoru(Node):
    def __init__(self):
        super().__init__('sicaklik_sensoru')
        self.publisher = self.create_publisher(Float32, 'sicaklik', 10)
        self.timer = self.create_timer(1.0, self.sicaklik_yayinla)

    def sicaklik_yayinla(self):
        msg = Float32()
        msg.data = random.uniform(20.0, 40.0)
        self.publisher.publish(msg)
        self.get_logger().info(f'Sicaklik: {msg.data:.2f} C')


def main(args=None):
    rclpy.init(args=args)
    node = SicaklikSensoru()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
