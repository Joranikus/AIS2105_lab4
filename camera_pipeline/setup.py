from setuptools import setup
import os
from glob import glob

package_name = 'camera_pipeline'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Camera processing pipeline with Gaussian blur and Canny edge detection',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gaussian_blur = camera_pipeline.gaussian_blur:main',
            'canny_edge = camera_pipeline.canny_edge:main',
        ],
    },
)