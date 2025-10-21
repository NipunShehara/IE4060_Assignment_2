from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    map_yaml = LaunchConfiguration('map')
    return LaunchDescription([
        DeclareLaunchArgument('map', default_value=os.path.expanduser('~/maze_map.yaml')),

        Node(package='nav2_map_server', executable='map_server', name='map_server',
             parameters=[{'use_sim_time': True, 'yaml_filename': map_yaml}]),

        Node(package='nav2_amcl', executable='amcl', name='amcl',
             parameters=[{'use_sim_time': True}]),

        Node(package='nav2_controller', executable='controller_server', name='controller_server',
             parameters=['config/nav2.yaml']),

        Node(package='nav2_planner', executable='planner_server', name='planner_server',
             parameters=['config/nav2.yaml']),

        Node(package='nav2_smoother', executable='smoother_server', name='smoother_server',
             parameters=['config/nav2.yaml']),

        Node(package='nav2_bt_navigator', executable='bt_navigator', name='bt_navigator',
             parameters=['config/nav2.yaml']),

        Node(package='nav2_behavior_tree', executable='behavior_server', name='behavior_server',
             parameters=['config/nav2.yaml']),

        Node(package='nav2_lifecycle_manager', executable='lifecycle_manager', name='lifecycle_manager_navigation',
             parameters=[{'use_sim_time': True, 'autostart': True,
                          'node_names': ['map_server','amcl','controller_server','planner_server',
                                         'smoother_server','bt_navigator','behavior_server']}])
    ])
