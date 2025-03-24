# Body Posture and Screen Viewing Distance Monitoring System

## Overview
The **Body Posture and Screen Viewing Distance Monitoring System** is a Raspberry Pi-based solution that helps users maintain proper posture and optimal screen viewing distance. The system uses **Ultrasonic sensors, and flux sensors** to monitor a user's sitting posture and screen distance, providing real-time feedback through an alert system.

## Features
- **Posture Detection**: Monitors the user's body posture using image processing with flux sensor.
- **Screen Distance Monitoring**: Measures the distance between the user and the screen using an ultrasonic sensor.
- **Real-Time Feedback**: Alerts users when incorrect posture is detected or when they are too close to the screen.
- **User-Friendly Interface**: Simple installation and easy-to-use system.
- **Cost-Effective**: Designed to be an affordable solution for all users.

## Components
- **Hardware**:
  - Raspberry Pi Pico
  - Flux Sensor (for posture detection)
  - Ultrasonic Sensor (for distance measurement)
  
- **Software**:
  - Python (for processing sensor data and generating alerts)
  - Thonny IDE (for coding and debugging)

## Installation
### Hardware Setup:
1. **Connect Raspberry Pi Pico** to the laptop using a data cable.
2. **Attach the Flux Sensor** to detect spine posture.
3. **Mount the Ultrasonic Sensor** near the screen to measure viewing distance.

### Software Setup:
1. Install **Thonny IDE** on your computer.
2. Install necessary Python libraries
3. Upload the Python script to Raspberry Pi Pico.
4. Run the script to start monitoring posture and screen distance.

## How It Works
1. **Posture Monitoring**:
   - The flux sensor detects the sitting angle.
   - If the angle is incorrect (bending < 90 degrees), an alert is triggered.
2. **Screen Distance Monitoring**:
   - The ultrasonic sensor measures the distance to the screen.
   - If the distance is less than 30 cm, a warning is displayed.
3. **Alerts**:
   - If poor posture or incorrect distance is detected, the system provides real-time feedback via audio alerts.

## Results
- Detects incorrect posture and warns users to correct their sitting position.
- Alerts users if they are sitting too close to the screen, reducing the risk of eye strain.
- Encourages healthy ergonomic habits for better productivity and well-being.


