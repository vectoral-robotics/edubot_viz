"""
RViz2 visualization for EduBot navigation phase.

Displays map, costmaps, TF, robot model, odometry, and navigation goals.
Intended to be used together with the edubot_navigation bringup.
"""

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution


def generate_launch_description():
    # Launch arguments
    use_rviz = LaunchConfiguration("use_rviz", default="true")
    rviz_config = LaunchConfiguration(
        "rviz_config",
        default=PathJoinSubstitution(
            [FindPackageShare("edubot_viz"), "rviz", "navigation_view.rviz"]
        ),
    )

    declare_args = [
        DeclareLaunchArgument(
            "use_rviz", default_value="true", description="Whether to launch RViz2 visualization."
        ),
        DeclareLaunchArgument(
            "rviz_config", default_value=rviz_config, description="Path to the RViz2 config file."
        ),
    ]

    # RViz2 Node
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2_navigation",
        arguments=["-d", rviz_config],
        output="screen",
        condition=IfCondition(use_rviz),
        parameters=[{"use_sim_time": LaunchConfiguration("use_sim_time", default="false")}],
    )

    return LaunchDescription([*declare_args, rviz_node])
