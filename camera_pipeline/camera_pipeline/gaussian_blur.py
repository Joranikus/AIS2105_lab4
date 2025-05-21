import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class GaussianBlurNode(Node):
    def __init__(self):
        super().__init__('gaussian_blur')
        self.subscription = self.create_subscription(
            Image,
            'image_rect',  # Changed to use rectified image
            self.image_callback,
            10)
        self.publisher = self.create_publisher(Image, 'image_blurred', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            # Apply Gaussian blur
            cv_blurred = cv2.GaussianBlur(cv_image, (5, 5), 0)
            blur_msg = self.bridge.cv2_to_imgmsg(cv_blurred, "bgr8")
            self.publisher.publish(blur_msg)
        except Exception as e:
            self.get_logger().error(str(e))

def main(args=None):
    rclpy.init(args=args)
    node = GaussianBlurNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    