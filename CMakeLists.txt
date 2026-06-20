cmake_minimum_required(VERSION 3.5)
project(edubot_viz)

find_package(ament_cmake REQUIRED)

# Install launch and rviz directories
install(
  DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
