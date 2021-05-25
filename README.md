

# README.md

This is for the Grab Coke project.
Code necessary will be included in the git repository

For making a complete package of the learning ros package, all the files is kept here to reduce any possible error when taking off uneccessary files

Please click for wiki to have more detail description

**Table of Contents**
* Environment setup
* File changed
* Run the simulation 

## Environment setup

### Preparation required
* Testbed: computers
* Software: Ubuntu OS or windows using virtual machine,ROS noetic, Baxter robot, Gazebo, RVIZ

### Environment preparartion
1. Install  Ubuntu  as  the  LINUX  OS  20.04,  version  older than 18.04 is not prefer
2. Install ROS Noetic with Desktop-full Install to install all required simulator and perception package
3. Download   or   git   clone   the   Baxter   robot   package(https://github.com/jacobsuenws/ProjectGrabCoke.git)

### Environment setup
1. Create  a  project  workspace  folder  call  xxx_ws  (xxx can be anyname without any symbol, for the simulation project_ws is used)
2. Make a folder call src inside the project_ws
3. `Catkin_make` in the project_ws
5. Move the git-cloned project into src folder
6. catkin_make again, install catkin_simple if necessary or error relate to catkinsimple occur

## File changed
The detailed change can be found in the file or in the report
1. Model coke_can is added into the exmple_models package
2. add_coke_can and add_table_and_coke is added as launch file
3. reset_coke_state.cpp is added into package example_gazebo_set_state
4. baxter_on_mobot.launch is modifed to add coke can in to the environment
5. object_finder_as.cpp is modified, need further modification after copying the code in bool ObjectFinder::find_toy_block(float surface_height, geometry_msgs::PoseStamped &object_pose) 
6. acquire_block_client.cpp is modified to change the objectidcodes to COKE_CAN_UPRIGHT
7. fetch_and_stack_client.cpp is modified by changing theobjectidcodes=COKE_CAN_UPRIGHT
8. right_end_effector.xarco is modified to extend the gripper width so the it can grasp the coke can
9. example_object_grabber_action_client.cpp is modified to perform the object in a better orientation
10. rethink_gripper_rt_manip_fncs.cppismodifiedtochange the orientation of the gripper and perform side approach

## Simulation

The simulationn is perform in two environment, first using mobile manipulator, second using default baxter. For grasping using side approach steps 1-3 and 8-9, 12-15 are required only to perform the demo of grasping coke can using side approach. Skip step 4-7 and 10-11 incase of any issue occur.

1. Open terminal, type "source project_ws/devel/setup.bash", do the same step for all opened terminal if the folder is not the default source folder of ROS
```
source project_ws/devel/setup.bash
```
2. Move to project_ws, type "./baxter.sh sim" to setup the ros environment, do the same step for all opened terminal
```
./baxter.sh sim
```
3. Type "roscore" to start ROS
```
roscor
```
4. Open new terminal, type "roslaunch_baxter_varation baxter_on_mobot.launch" to start the gazebo with baxter, coke cans, tables, and the environment
```
roslaunch_baxter_varation baxter_on_mobot.launch
```
5. "rosrun coordinator command_bundler"
```
rosrun coordinator command_bundler
```
6. Open new terminal, type "rosrun coordinator acquire_block_client" to find the coke can, grasping may not be able to finish
```
rosrun coordinator acquire_block_client
```
7. Close all the terminals except the one running roscore
8. Open new terminal, type "roslaunch baxter_gazebo baxter_world.launch" to launnch the gazebo environment and baxter
```
roslaunch baxter_gazebo baxter_world.launch
```
9. Open new terminal, type "roslaunch exmpl_models add_table_and_coke.launch" to add table and coke
```
roslaunch exmpl_models add_table_and_coke.launch
```
10. "rosrun object_finder object_finder_as" to start server
```
rosrun object_finder object_finder_as
```
11. "rosrun object_finder example_object_finder_action_client" to run client specifying the object
```
rosrun object_finder example_object_finder_action_client
```

12. "rosrun example_gazebo_set_state reset_coke_state" to reset the coke can if necessary
```
rosrun example_gazebo_set_state reset_coke_state
```
13. "roslaunch baxter_launch_files baxter_object_grabber_nodes.launch" to launch the object grabber nodes
```
roslaunch baxter_launch_files baxter_object_grabber_nodes.launch
```
14. "rosrun object_grabber example_object_grabber_action_client" to run the grabber action
```
rosrun object_grabber example_object_grabber_action_client
```
15. Repeat step 12-14 to repeat the grasping coke can using side approach
