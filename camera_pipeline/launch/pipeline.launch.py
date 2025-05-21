from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Rectification node
        Node(
            package='image_proc',
            executable='rectify_node',
            name='rectify_node',
            remappings=[
                ('image', '/image_raw'),
                ('camera_info', '/camera_info'),
                ('image_rect', '/image_rect')
            ]
        ),
        
        # Gaussian Blur node
        Node(
            package='camera_pipeline',
            executable='gaussian_blur',
            name='gaussian_blur',
            remappings=[
                ('image_rect', '/image_rect'),
                ('image_blurred', '/image_blurred')
            ]
        ),
        
        # Canny Edge node
        Node(
            package='camera_pipeline',
            executable='canny_edge',
            name='canny_edge',
            remappings=[
                ('image_blurred', '/image_blurred'),
                ('image_processed', '/image_output')
            ]
        )
    ])