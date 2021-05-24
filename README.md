

# README.md

This is for the Grab Coke project.
Code necessary will be included in the git repository

**Table of Contents**
* Environment setup
* File changed
* Run the simulation 

# Environment setup

## Preparation required
* Testbed: computers
* Software: Ubuntu OS or windows using virtual machine,ROS noetic, Baxter robot, Gazebo, RVIZ

## Environment preparartion
1. Install  Ubuntu  as  the  LINUX  OS  20.04,  version  older than 18.04 is not prefer
2. Install ROS Noetic with Desktop-full Install to install all required simulator and perception package
3. Download   or   git   clone   the   Baxter   robot   package(https://github.com/jacobsuenws/ProjectGrabCoke.git)

## Environment setup
1. Create  a  project  workspace  folder  call  xxx_ws  (xxx can be anyname without any symbol, for the simulation project_ws is used)
2. Make a folder call src inside the projectws
3. `Catkin_make` in the project_ws
5. Move the git-cloned project into src folder
6. catkin_make again, install catkin_simple if necessary or errorrelate to catkinsimple occur

# File changed
1. Model coke_can is added into the exmple_models package
2. add_coke_can and add_table_and_coke is added as launch file
3. reset_coke_state.cpp   is   added   into   package   example_gazebo_set_state
