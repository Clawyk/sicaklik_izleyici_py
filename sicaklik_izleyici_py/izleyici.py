import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SicaklikIzleyici(Node):
    def __init__(self):
        super().__init__('sicaklik_izleyici')
        self.subscription = self.create_subscription(
            Float32,
            'sicaklik',
            self.sicaklik_kontrol,
            10
        )

    def sicaklik_kontrol(self, msg):
        sicaklik = msg.data
        self.get_logger().info(f'Okunan sicaklik: {sicaklik:.2f} C')

        if sicaklik > 30.0:
            self.get_logger().warning('UYARI: Sicaklik 30 C degerini asti!')


def main(args=None):
    rclpy.init(args=args)
    node = SicaklikIzleyici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
