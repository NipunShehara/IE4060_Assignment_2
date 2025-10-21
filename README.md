# IE4060_Assignment_2

# tb3-maze-nav

Drop this repository under `~/ros2_ws/src`, then:

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash

# Set TB3 model once
echo 'export TURTLEBOT3_MODEL=burger' >> ~/.bashrc
source ~/.bashrc

# 1) Start Gazebo + TB3 + world
ros2 launch tb3_maze_bringup sim_world.launch.py

# 2) Run SLAM and drive around to create a map (in another terminal)
ros2 launch tb3_maze_bringup slam.launch.py
# Save when ready
ros2 run nav2_map_server map_saver_cli -f ~/maze_map

# 3) Start Nav2 using the saved map
ros2 launch tb3_maze_bringup nav2.launch.py map:=~/maze_map.yaml

# 4) Send goals from RViz (Nav2 Goal tool)

# Optional: policy fallback (reactive or Torch model if provided)
ros2 run tb3_maze_bringup policy_node

# Optional: measure a run to a given (x,y)
ros2 run tb3_maze_bringup metrics_node --ros-args -p goal_x:=1.0 -p goal_y:=1.0 -p tolerance:=0.1
