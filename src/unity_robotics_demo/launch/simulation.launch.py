import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    tcp_dir = get_package_share_directory('ros_tcp_endpoint')

    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='unity_robotics_demo',
            executable='serial_publisher',
            name='serial_publisher'),
        launch_ros.actions.Node(
            package='unity_robotics_demo',
            executable='position_publisher',
            name='position_publisher'),
        launch_ros.actions.Node(
            package='ros_tcp_endpoint',
            executable='default_server_endpoint',
            name='default_server_endpoint')
    ])