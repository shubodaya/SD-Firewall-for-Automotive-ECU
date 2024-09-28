# Automotive Software-Defined Firewall (SDF) Framework
A comprehensive framework for implementing Software-Defined Firewalls (SDF) in automotive Electronic Control Units (ECUs) to enhance security, control, and management of inter-ECU communications.

## Description
This project extends the original [VirtualECU](https://github.com/pschichtel/VirtualECU) repository to focus on the implementation and validation of a Software-Defined Firewall (SDF) specifically designed for securing communication between automotive ECUs. The SD-Firewall protects against unauthorized access, malicious communication, and cybersecurity threats in a virtual automotive network using customized firewall rules. The project runs on a Linux-based virtual environment using Scala, SBT, SocketCAN, and CAN-utils, simulating a robust automotive communication system.

## Key Features:
- Virtual ECU Simulation: Provides a virtual environment for testing firewall rules and ECU interactions without requiring physical hardware.
- Python-Based Firewall: Controls and manages the flow of data between virtual ECUs, enforcing allow/block rules based on security requirements.
- Virtual CAN Networks (vCAN): Simulates the in-vehicle communication system for ECUs, allowing for realistic testing.
- Logging and Monitoring: Captures detailed logs for analysis, ensuring the firewall operates as expected.
- Attack Simulations: Test the firewall under various cybersecurity threat scenarios to ensure robustness and resilience.

## Project Objectives
The goal is to develop a firewall framework that:
* Controls communication between critical ECUs in a vehicle, such as the ABS, ECM, ADAS, and more.
* Protects against potential cybersecurity threats by implementing custom firewall rules for specific ECUs.
* Allows for scalable and flexible testing of automotive firewalls in a virtual environment.

## Methodology
1. System Design
The project begins by identifying key automotive ECUs (ABS, ACM, BCM, ECM, ICU, TCM, and ADAS) that require specific firewall rules to secure communication. The firewall is designed to manage the data flow between these virtual ECUs and mitigate cybersecurity threats.

2. Virtual Environment Setup
Using Scala, SBT, and Linux, a virtual network of ECUs is created where vCAN interfaces simulate real-world communication channels. SocketCAN and CAN-utils are used for monitoring and controlling the CAN traffic.

3. Firewall Implementation
The firewall is developed using Python, where custom rules are written to allow/block communication between ECUs based on security needs. These rules ensure that only necessary and secure communications are allowed, while all suspicious or irrelevant traffic is blocked.

4. Testing and Validation
To validate the effectiveness of the firewall, traffic between the ECUs is simulated under different attack scenarios. The performance of the firewall is observed to ensure that it correctly enforces the rules and blocks unauthorized access.

5. Log Analysis
Event logs from vCAN networks are collected and analyzed to assess the firewall's performance. Any anomalies detected are used to refine the firewall rules.

## Installation
Prerequisites
* Linux-based environment
* Python 3.x
* Scala and SBT for virtual ECU simulation
* SocketCAN and CAN-utils for CAN communication

## Setup Instructions
1. Clone the repository:

bash
git clone https://github.com/yourusername/automotive-sdf-firewall.git
cd automotive-sdf-firewall

2. Install the required Python packages:
bash
pip3 install -r requirements.txt

3. Set up Scala and SBT for virtual ECU simulation.

4. Configure and launch SocketCAN and vCAN interfaces for network communication.

5. Run the firewall script:
bash
python3 firewall.py


## Usage
* Customize the firewall rules in the firewall.py file to meet your specific requirements.
* Simulate traffic between the virtual ECUs and monitor the log files for communication details and firewall performance.
* Use CAN-utils for additional monitoring and CAN frame operations.


## Components
Virtual ECUs
This project simulates the following ECUs:
* Anti-lock Brake System (ABS)
* Airbag Control Module (ACM)
* Body Control Module (BCM)
* Engine Control Module (ECM)
* Infotainment Control Unit (ICU)
* Transmission Control Module (TCM)
* Advanced Driver Assistance Systems (ADAS)
Each ECU represents key vehicle functions and security requirements, ensuring that the firewall is tailored for realistic and complex automotive scenarios.

## Virtual CAN (vCAN) Network
Virtual CAN networks (vCAN) are used to simulate data communication between the ECUs. These virtual networks allow real-time monitoring and testing of ECU traffic, enabling effective testing of the firewall rules.

## Changes from the Original VirtualECU
* Custom configurations and YAML files for specific ECU interactions and firewall rules.
* Enhanced monitoring and logging features for CAN traffic and firewall performance analysis.
* Updated components for better integration and improved functionality in testing firewalls within the virtual environment.

## Attribution
This work is based on the [VirtualECU](https://github.com/pschichtel/VirtualECU) project by pschichtel. Modifications have been made to adapt the framework to the development and testing of firewalls for automotive ECU security.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

## Future Work
The project will be expanded with additional features:
* Integration of physical ECUs for real-world testing.
* Enhanced attack simulations for better testing of firewall robustness.
* Machine learning-based firewall rule adaptation.




