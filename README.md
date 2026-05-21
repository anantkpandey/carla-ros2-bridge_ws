# ROS2 + CARLA Autonomous Stack

## Goal
Build an autonomous driving stack using ROS2 and CARLA.

## Current Progress
✅ ROS2 Jazzy setup  
✅ CARLA bridge configured  
✅ Workspace builds successfully  
✅ Custom package: my_autonomous_stack

## Project Structure

```text
carla-ros2-bridge_ws/
├── src/
│   ├── my_autonomous_stack/   # My work
│   └── ros-bridge/            # CARLA ROS bridge
├── README.md
└── .gitignore
```

## Planned Features
- [ ] Camera subscriber
- [ ] LiDAR integration
- [ ] Lane detection
- [ ] Object detection
- [ ] Localization
- [ ] Navigation

## Tech

- ROS2 Jazzy
- CARLA
- Python
- RViz
- Colcon
- Ubuntu

## Setup

```bash
git clone <repo-url>
cd carla-ros2-bridge_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash

