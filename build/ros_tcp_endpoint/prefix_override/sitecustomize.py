import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/michael/ros2_unity_ws/install/ros_tcp_endpoint'
