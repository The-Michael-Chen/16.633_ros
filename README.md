# 16.633_ros: The NEET Autonomous Drone Class
This class uses Tello drones to autonomously navigate around a track. The track composes of hoops with april tags that the drones must fly through. This project details a progression of assignments that lead up to the final competition. The assignments can be found in the neet_ass folder as html files. The course covers concepts like optical flow, pinhole camera model, image transformations, and PID controls. This github page is specifically for starting the simulation of the drone inside Gazebo for working with ROS2. 

## Class Package installation instructions:
1. pip install virtualenv
2. create a folder for your class projects
3. python<version> -m venv <virtual-environment-name> (python version 3.8.5)
4. git clone this repository follow instructions on the github page
5. pip install -r requirements.txt

## ROS Setup Process: 
1. Download Docker Desktop [https://www.docker.com/products/docker-desktop/]
2. In your terminal, run `docker pull tiryoh/ros-desktop-vnc:foxy`. You should see an image appear inside the Docker Images tab on your Docker Desktop app
3. Navigate to the project directory
4. To create a Docker container run `docker run -it -p 6080:80 -v $(pwd):/home/ubuntu/Desktop/<project_name> --name <project_name> tiryoh/ros2-desktop-vnc:foxy`
5. Open the docker container in your browser by clicking the port in docker desktop
6. When inside the docker container, open a terminal and navigate to the project directory in your virtual desktop
7. Run git pull this repository: [https://github.com/clydemcqueen/tello_ros]
8. Navigate to the tello_ros_ws and run `source install/setup.bash`
9. Run `colcon build --symlink install`
10. Visit this link [https://github.com/clydemcqueen/tello_ros] and follow the instructions under install "tello_ros".
11. To run the simulation, click on "tello_gazebo" on the github repo page and follow the instructions there. 


## Issue Log:
1. Could not download April Tags plugins:
- Solution: Downgrade python to version 3.7 or 3.6 using a virtual environment 
2. Flow point drifting:
- Solution 1: Make the Flow point be closer to the top of the screen because when the drone flys forwards you are pointing downwards
- Solution 2: Correct your x, y position using the tags before using the flow point 
- Solution 3: Make sure the surroundings are not one plain surface but have distinguishable things like lines or stark different colors to place flow points on 
3. failing to grab video stream: 

## HOW TO NOTES:
    - custom model import tutorial: [https://www.youtube.com/watch?v=fwoTLfypIMw](https://www.youtube.com/watch?v=fwoTLfypIMw)
        - [https://classic.gazebosim.org/tutorials?tut=build_model#Step3:AddtothemodelSDFfile](https://classic.gazebosim.org/tutorials?tut=build_model#Step3:AddtothemodelSDFfile)
        - 
    - drone topic input
        - ros2 service call /drone1/tello_action tello_msgs/TelloAction "{cmd: 'takeoff'}”
    - How to use custom python packages
        - resources
            
            [https://docs.ros.org/en/foxy/How-To-Guides/Using-Python-Packages.html](https://docs.ros.org/en/foxy/How-To-Guides/Using-Python-Packages.html)
            
            [https://docs.ros.org/en/foxy/Tutorials/Intermediate/Rosdep.html](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Rosdep.html)
            
        1. create a subfolder in your package 
        2. add an init python file 
        3. [https://github.com/ros/rosdistro/blob/master/rosdep/python.yaml](https://github.com/ros/rosdistro/blob/master/rosdep/python.yaml)
    - How to read sensor_msg.msg as a opencv image- with the cv_bridge package
        - [https://stackoverflow.com/questions/72690021/how-to-process-a-image-message-with-opencv-from-ros2](https://stackoverflow.com/questions/72690021/how-to-process-a-image-message-with-opencv-from-ros2)
    - Startup process for launching drone in sim
        - ros2 launch tello_gazebo simple_launch.py
    - Simulation time in Gazebo
        - [https://ceti.pages.st.inf.tu-dresden.de/robotics/howtos/SimulationSpeed.html](https://ceti.pages.st.inf.tu-dresden.de/robotics/howtos/SimulationSpeed.html)
    - rc control on the drone
        - rc forward, left, up
