# edubot_viz — Claude guidelines

ROS2 package holding the RViz configurations and view launch files for EduBot
(`rviz/`, `launch/`). Part of the EduBot ROS2 stack; also built into the RViz
container by `edubot_dashboard`.

These guidelines will grow over time. For now the most important rule:

## Commits

All commits MUST follow the [Conventional Commits](https://www.conventionalcommits.org) spec.

Format:

    <type>(<optional scope>): <short summary>

Common types: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

- Imperative mood ("add", not "added").
- Summary under ~72 characters, lower case, no trailing period.
- Scope is optional and names the affected area.

Example:

    feat(rviz): add navigation view config
