<<<<<<< HEAD
##### **Trash Glasses:** An AI-powered wearable trash detection system that detects trash in real time using computer vision and automatically reports incidents to a municipal dashboard.

##### 

##### **Problem:** One of the major causes of waste being poorly managed is that the workers do not know where and in which manner the waste is distributed. Which leads to health hazards, contamination of air, water, and soil. Even affecting the economy of a country!

##### 

##### **Solution:** To integrate a pair of glasses with the "Trash Detection Model" with the help of Raspberry Pi. 

##### This detects trash in real time using a YOLOv5 computer vision model.

##### Tags the location with the help of Raspberry Pi GPS Module.

##### Automatically prepares a report at the end of the day and mails it to the municipality.

##### Automatically updates the web dashboard of this model according to the density of the trash that area has.

##### 

##### **Technology Used**

##### \- **YOLOv5** **nano** — lightweight object detection model

##### \- **TACO** **Dataset** — 1,500+ real trash images for training

##### \- **TensorFlow Lite** — optimized model for edge devices

##### \- **Flask** — web dashboard backend

##### \- **Leaflet.js** — interactive map

##### \- **Python, OpenCV, NumPy**

##### 

##### **## HOW TO RUN**

##### 

##### **DASHBOARD:**

##### **" bash**

##### &#x20; **pip install flask requests**

##### &#x20; **python app.py**

##### **"**

##### 

##### **WEBCAM(live detection):**

##### **" bash**

##### &#x20;  **pip install tensorflow opencv-python**

##### &#x20;  **python webcam\_test.py**

##### **"**

##### 

##### **Scope:**

* ##### Integrate it with Raspberry Pi and Camera Module to detect trash
* ##### Connect the GPS Module to extract co-ordinates from NEO-6M Module
* ##### Scale to multiple users across city
* ##### Partner with the municipality for live deployment
* ##### Publish a research paper based on the outcomes

##### 

##### **Author:**

##### Arjun Grover - Student, Lucknow, India

##### Built in order to curb the growing problem of poor waste management

##### 

##### **Contact:**

##### GitHub: github.com/arjungrover11

##### LinkedIn: www.linkedin.com/in/arjun-grover-a300172b7

=======
# TrashGlasses
AI-powered wearable trash detection system with municipal reporting
>>>>>>> 5d46f77a1ea849241a35fdd2ae26b977915abded
