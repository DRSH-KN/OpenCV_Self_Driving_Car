Project: https://scienceinmyroom.blogspot.com/p/opencv-based-self-driving-car-using.html
A low Computing, Optimised OpenCV Library Based Self Driving Car That Detects and Navigates A Lane Through A Algorithm Called Pixel Summation. 
Low Computing Accounts for the Hardware Chosen: RaspberryPie 4 Model B and Software Technique Used: Computer Vision Library + Summation Algorithm, which makes it possible for a fast response application, i.e Self Driving.

However, Lower Models of RaspberryPie Can be used too. The Software uses relatively basic Techniques to detect lane, where simple Image Processing and Pre-processing Functions are employed to process the image frame from the camera, reduced to, small resolution, and Finally Lane is detected. The software working on low resolution makes it even better. What is Questionable is its detection reliability!! Well, according to my tests, i carried from my project, 98% times the detection seem reliable, if failed, the car is handled to slow down and resense.

Pixel Summation works by adding pixels of specific color, and finding the curvature of the lane by measuring the weight of higher pixel density on a particular direction. SIMPLE RIGHT!??

The Question Remains, If simple Computer Vison based processing can make detections soo accurate, why dont they use it in real applications, instead of Machine Learning and Deep Learning Neural Networks??
The answer lies in the fact that, image processing functions are well accurate but depend on lighting. Lighting cannot be controlled by the camera, which gives the ambiguity of failure with OpenCV.
Anyway, Great Project Guys. Must Try it!!

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFLVeSknDvlWhl1Vym6j-mc8VjNZ9i_zyPQHMOaBQaspKpEca1vonEk2CxNuM9nxrVtoUfQ71uBhx5aR_ncMr2ircn2kYTmxjzWRc2h3u0DqX3c4iUYwEytl-BNe43IcShxshwvHDwUftDOpNYlkeVLYIrPi2gPi8u0xVdR5cNOK0XyVERzS3fNNOcJ9Q/w554-h416/IMG_20231104_204959.jpg">

Features
**********
1. Detects White Lane with upto 180 degree curvature.
2. Has the speed variance of 20-80% of motors
3. Doesnt use any detection filters of OPENCV, Just Simple Pre-Processing Algorithms
4. Quick to react to changes and high error tolerance.

Guide
*******
1. Install All the necessary libraries in your python environment.
2. Constuct a simple robot with Basic Gear Motors of 12 Volts, with two units to control.
3. Use an PWN Controlled H-Bridge To control the motors
4. The H-Bridge can be controlled through Arduino or Directly Through RaspberryPie, both available.
5. Use a simple 5MP Camera module to capture image frame.
6. Try And Execute
7. More Information, Visit my Blog to see Full Project: https://scienceinmyroom.blogspot.com/p/opencv-based-self-driving-car-using.html
