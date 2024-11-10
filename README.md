Robotic-Arm-Inverse-Kinematics
==============================
Geogebra demo: [https://www.geogebra.org/calculator/vapprkva](https://www.geogebra.org/calculator/vapprkva)
Blog post: [https://matthew-bird.com/blogs/Robotic-Arm-Inverse-Kinematics.html](https://matthew-bird.com/blogs/Robotic-Arm-Inverse-Kinematics.html)

<img width="400" alt="IMG_0333" src="https://github.com/user-attachments/assets/c1c4891e-bdc1-4a67-addd-e75461d12742">

## Introduction
This blog post is about figuring out the inverse kinematics behind finding the angles required for each of the 6 axes of a 6 axis robotic arm. 

I used cartesian coordinates, with the origin at the center of the base of the robotic arm and the positive y-axis as the front of the robotic arm, for the math. The first axis is the base axis, rotating in the yaw direction like a lazy susan. The second and third axes rotate in the pitch direction. These three axes give us control over the translation of our end point. The second and third axes allow the arm to reach a large circular range of positions in a 2d plane, while the first axis converts this into a sphere in 3d space. 

<ins>Coverage provided by second and third axes</ins>

<img width="400" alt="IMG_0333" src="https://github.com/user-attachments/assets/e0f3d8f1-95cb-4180-9233-661935cdc951">

The fourth, fifth, and sixth axes are dedicated to controlling the orientation of the robotic arm holder, and are pitch, yaw, and roll respectively. I chose this order of orientations because setting pitch to the fourth axis allows us to completely ignore the orientation of the third axis, setting roll to the last axis allows us to completely ignore it as it doesn’t change anything, and the fifth axis is left with yaw. 

## Calculations
### Axes 4, 5, and 6
The pitch of the axes 4, 5 and 6 has to equal the pitch of axis 4 as the pitch of axis 4 carries over to axes 5 and 6. Because we know the pitch of the axes 5 and 6, we can limit the potential positions at which the point can exist to a circle. ([visual](https://www.geogebra.org/calculator/yavmhzjd))

To find the radius of the circle and the position of the circle, we first find out how far away from the target point the point can be horizontally and vertically. By constructing a right angle triangle as shown below, we can find out the horizontal and vertical distance of any point from the target point. The radius will equal to the horizontal distance and the position of the center of the circle will equal the Z position of the target point (which is also the center of the sphere) subtracted by/added to the vertical distance. 

<img width="400" alt="IMG_0333" src="https://github.com/user-attachments/assets/81f0ad50-3b5c-43cf-ae9d-f052e283b7dd">

To find the exact point, we can make use of the desired yaw of the final point and find the corresponding point on the circle as shown below. 

<img width="800" alt="IMG_0333" src="https://github.com/user-attachments/assets/6526a48d-3608-48c6-8ce7-181ce740d43c">

We repeat the same process to get to the point at axis 4, except this time we use the yaw of the first axis. 

![image](https://github.com/user-attachments/assets/17027738-ea18-4df1-97ae-68d6951f2a4e)

### Axes 1, 2, and 3
To get the yaw value of axis one, since the yaw is transferred to axes 2 and 3, we can just take the arctan of the position of axis 4 to get our yaw.

<img width="400" alt="IMG_0333" src="https://github.com/user-attachments/assets/c434d048-3ed1-4642-a285-061ced7c8130">

To get the members of the robotic arm to their correct positions, we need to get the angles ⍺ & β  from the image below. Finding the angles directly allows us to [directly find the coordinates of B](https://docs.google.com/document/u/0/d/1Np-hgKrQbotTc_-zsZkRBA5jJFR4E49Fd7QHk0cFpcA/edit), saving a lot of time and effort.

<img width="400" alt="IMG_0333" src="https://github.com/user-attachments/assets/6dff0d6b-53a1-4fbe-baf7-a931dbc04f85">

To do so, we can construct a triangle between (0,0), (x1, y1), and B. A quick application of the pythagorean theorem, cosine rule, and tangent function gives us the following values. 

![image](https://github.com/user-attachments/assets/087f0588-7003-41c0-8730-bd6f61d1d296)

With this, we have all the values we need to provide to the motors in our robotic arm for achieving any position and rotation in 3d space. 
