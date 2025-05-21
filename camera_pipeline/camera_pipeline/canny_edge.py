import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CannyEdgeNode(Node):
    def __init__(self):
        super().__init__('canny_edge')
        self.subscription = self.create_subscription(
            Image,
            'image_blurred',  # Changed to use blurred image
            self.image_callback,
            10)
        self.publisher = self.create_publisher(Image, 'image_processed', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            # Convert to grayscale and apply Canny
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            cv_edge = cv2.Canny(gray, 100, 200)
            edge_msg = self.bridge.cv2_to_imgmsg(cv_edge, "mono8")
            self.publisher.publish(edge_msg)
        except Exception as e:
            self.get_logger().error(str(e))

def main(args=None):
    rclpy.init(args=args)
    node = CannyEdgeNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()