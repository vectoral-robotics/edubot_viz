"""
RViz2 visualization for OmniBot bringup phase.

Displays robot model, TF tree, odometry, and optional sensor data.
Typically launched together with omnibot_bringup.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    # Launch arguments
    use_rviz = LaunchConfiguration('use_rviz', default='true')
    rviz_config = LaunchConfiguration(
        'rviz_config',
        default=PathJoinSubstitution([
            FindPackageShare('omnibot_viz'),
            'rviz',
            'bringup_view.rviz'
        ])
    )

    declare_args = [
        DeclareLaunchArgument(
            'use_rviz',
            default_value='true',
            description='Whether to launch RViz2 visualization.'
        ),
        DeclareLaunchArgument(
            'rviz_config',
            default_value=rviz_config,
            description='Path to the RViz2 config file.'
        ),
    ]

    # RViz2 Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2_bringup',
        arguments=['-d', rviz_config],
        output='screen',
        condition=IfCondition(use_rviz)
    )

    return LaunchDescription(declare_args + [rviz_node])
