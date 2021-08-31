# Robot localization using EKF


One of the most important parts of mobile robotics is the ability to achieve Autonomous Navigation. That is, a robot is able to move by itself with only the help of its sensors and actuators. In order to achieve autonomous navigation, the Localization of the robot plays a key role. Robot Localization is the ability of the robot to know where it is in the environment.
To achieve this I'm using the robot_localization package, developed by Tom Moore. The main goal of this package is to provide accurate data about where the robot is and what it's doing, based on the input of as many sensors as we want.

## Requirements:

 ROS
(Tested on ros Noetic (recommended) but it should work on all previous distributions.)

## Installation
Clone workspace
```sh
$ git clone https://github.com/rulshid/Robot-localization-using-EKF.git
```
Install robot_localization package.
```sh
$ sudo apt-get install ros-noetic-robot_localization.
```

```sh
$ cd Ekf_test_ws
```
Note : It is always better to remove build and devel folders before executing $ catkin_make
```sh
$ catkin_make
```
In case of any dependency error - try installing all required packages by using rosdep.
```sh
 $ rosdep install --from-paths src --ignore-src -y
```
Source the environment.
```sh
 $ source devel/setup.bash
```

## Usage
Launch all required nodes by using following command.
```sh
$ roslaunch ekf_test1 final.launch 
```
This will take :`/sensors/gnss/odom`, `/sensors/odom` data as input give output  estimated position and orientation as output in `/odometry/filered` data topic.
In the rviz we are visualizing data from `/sensors/gnss/odom`, `/odometry/filered` and `/sensor/odom/ground_truth`
The output will be similar to : https://www.youtube.com/watch?v=IUcd2TAj12A

## Technical description
The localization of car provided in the task is implemented by using the Robot_localization package .
The main task was the fusion of /sensor/gnss/odom and /sensor/odom to obtain the estimated state of the robot.
I have given the  .bag file as the input to the ekf_localization_node , the data flow is shown below 

![rosgraph](https://user-images.githubusercontent.com/40757610/130339464-60963dd7-52ef-4c7a-bcff-1b99ac557031.png)

The ekf_node is taking parameters from the src/params/ekf_parameters.yaml files
parameters are set by the guidelines based on the knowledge from :
https://github.com/methylDragon/ros-sensor-fusion-tutorial/blob/master/01%20-%20ROS%20and%20Sensor%20Fusion%20Tutorial.md

## Performance analysis
Please check: https://www.youtube.com/watch?v=IUcd2TAj12A
The Output obtained from the current configuration for the extended Kalman filter gave me good results. These results can be further improved by tuning the process_noise_covariance matrix.
Graphical representation of filterd pos(output from ekf- odometry/filtered ) and pos based on gnss (sensors/gnss/odom) 
![image](https://user-images.githubusercontent.com/40757610/130339649-cb5daf4e-969e-4402-8bb0-7d20d8fa24d3.png)

Graphical representation of filterd pos(output from ekf- odometry/filtered ) and sensors/odom/ground_truth/pos
![imagett4](https://user-images.githubusercontent.com/40757610/130340498-d6e66d96-2668-40b2-86e8-065f13b82b8a.png)
