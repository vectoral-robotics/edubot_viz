# edubot_viz

RViz configurations for the [EduBot](https://github.com/vectoral-robotics) robot — by Vectoral.

## What it is

`edubot_viz` bundles the RViz2 configurations and small launch wrappers used to
visualize EduBot — one view for general bringup and one tuned for navigation
(costmaps, paths, goal tools). It is included by
[`edubot_bringup`](https://github.com/vectoral-robotics/edubot_bringup) when
`use_rviz:=true`, and is also built into the dashboard's web-RViz container.

- `rviz/` — `bringup_view.rviz`, `navigation_view.rviz`
- `launch/` — `bringup_view.launch.py`, `navigation_view.launch.py`

## Installation

Requires ROS 2 Humble.

```bash
cd ~/ros2_ws/src
git clone https://github.com/vectoral-robotics/edubot_viz.git
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select edubot_viz
source install/setup.bash
```

## Usage

```bash
# General bringup view
ros2 launch edubot_viz bringup_view.launch.py

# Navigation view (costmaps, paths, goal tools)
ros2 launch edubot_viz navigation_view.launch.py
```

## Contributing

- Work on a short-lived feature branch and open a pull request against `main`
  (which is protected); changes land via PR review.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org)
  (`feat:`, `fix:`, `docs:`, …). See `CLAUDE.md` for repo conventions.

## License

PolyForm Perimeter 1.0.0 (source-available) — see [LICENSE](LICENSE).
