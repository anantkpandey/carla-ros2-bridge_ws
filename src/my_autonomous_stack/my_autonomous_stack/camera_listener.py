import rclpy
from rclpy.node import Node

class CameraListener(Node):
    def __init__(self):
        super().__init__('camera_listener')
        self.get_logger().info("My first ROS node is alive!")

def main(args=None):
    rclpy.init(args=args)
    node = CameraListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()