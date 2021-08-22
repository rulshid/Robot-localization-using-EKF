# Robot-localization-using-EKF
One of the most important parts of mobile robotics is the ability to achieve Autonomous Navigation. That is, a robot is able to move by itself with only the help of its sensors and actuators. In order to achieve autonomous navigation, the Localization of the robot plays a key role. Robot Localization is the ability of the robot to know where it is in the environment.
Here we are going to use the robot_localization package, developed by Tom Moore. The main goal of this package is to provide accurate data about where the robot is and what it's doing, based on the input of as many sensors as we want. we can also use sensor fusion to increase data efficiency!!

# Requirements:
- ROS
(Tested on ros Noetic (recommended) but it should work on all previous distributions.)

# Installation:


- Install robot_localization package.
  $ sudo apt-get install ros-noetic-robot_localization.
- Download this repository as a zip
- Extract the .zip file.
- $ cd Crover_task_ws
 (It is always better to remove build and devel folders before executing $ catkin_make)
 - $ catkin_make
 - In case of any dependency error - try installing all required packages by using rosdep. 
 - $ rosdep install --from-paths src --ignore-src -y
 - Source the environment.
 - $ source devel/setup.bash
 
 now just run : $ roslaunch ekf_test1 final.launch 
 Then the output will be similar to : https://www.youtube.com/watch?v=IUcd2TAj12A




