firewall_rules = [
    {"Source ECU": "ABS", "Destination ECU": "ACM", "Allowed": "Yes", "Reason": "ABS needs to communicate with ACM for safety."},
    {"Source ECU": "ABS", "Destination ECU": "BCM", "Allowed": "No", "Reason": "ABS do not need to interact with BCM."},
    {"Source ECU": "ABS", "Destination ECU": "ECM", "Allowed": "Yes", "Reason": "ABS needs engine data from ECM for braking control."},
    {"Source ECU": "ABS", "Destination ECU": "ICU", "Allowed": "No", "Reason": "ABS do not need infotainment data."},
    {"Source ECU": "ABS", "Destination ECU": "TCM", "Allowed": "Yes", "Reason": "ABS needs transmission data from TCM."},
    {"Source ECU": "ABS", "Destination ECU": "ADAS", "Allowed": "Yes", "Reason": "ABS provides critical data to ADAS for advanced driving features."},
    {"Source ECU": "ACM", "Destination ECU": "ABS", "Allowed": "Yes", "Reason": "ACM needs to receive data from ABS for airbag deployment."},
    {"Source ECU": "ACM", "Destination ECU": "BCM", "Allowed": "Yes", "Reason": "ACM communicates with BCM for various body functions."},
    {"Source ECU": "ACM", "Destination ECU": "ECM", "Allowed": "Yes", "Reason": "ACM requires ECM data for comprehensive safety systems."},
    {"Source ECU": "ACM", "Destination ECU": "ICU", "Allowed": "Yes", "Reason": "ACM can send status updates to the infotainment system."},
    {"Source ECU": "ACM", "Destination ECU": "TCM", "Allowed": "Yes", "Reason": "ACM may need TCM data for certain safety features."},
    {"Source ECU": "ACM", "Destination ECU": "ADAS", "Allowed": "Yes", "Reason": "ACM might send data to ADAS for integrated safety systems."},
    {"Source ECU": "BCM", "Destination ECU": "ABS", "Allowed": "No", "Reason": "BCM does not need to interact with ABS."},
    {"Source ECU": "BCM", "Destination ECU": "ACM", "Allowed": "Yes", "Reason": "BCM needs to interact with ACM for body functions."},
    {"Source ECU": "BCM", "Destination ECU": "ECM", "Allowed": "No", "Reason": "BCM does not need to interact with ECM."},
    {"Source ECU": "BCM", "Destination ECU": "ICU", "Allowed": "No", "Reason": "BCM does not need to interact with ICU."},
    {"Source ECU": "BCM", "Destination ECU": "TCM", "Allowed": "No", "Reason": "BCM does not need to interact with TCM."},
    {"Source ECU": "BCM", "Destination ECU": "ADAS", "Allowed": "No", "Reason": "BCM does not interact directly with ADAS."},
    {"Source ECU": "ECM", "Destination ECU": "ABS", "Allowed": "Yes", "Reason": "ECM needs to communicate with ABS for braking control."},
    {"Source ECU": "ECM", "Destination ECU": "ACM", "Allowed": "Yes", "Reason": "ECM needs to provide data to ACM for safety systems."},
    {"Source ECU": "ECM", "Destination ECU": "BCM", "Allowed": "No", "Reason": "ECM does not need to interact with BCM."},
    {"Source ECU": "ECM", "Destination ECU": "ICU", "Allowed": "No", "Reason": "ECM does not need to interact with ICU."},
    {"Source ECU": "ECM", "Destination ECU": "TCM", "Allowed": "Yes", "Reason": "ECM needs to communicate with TCM for transmission control."},
    {"Source ECU": "ECM", "Destination ECU": "ADAS", "Allowed": "Yes", "Reason": "ECM provides engine data necessary for ADAS functionality."},
    {"Source ECU": "ICU", "Destination ECU": "ABS", "Allowed": "No", "Reason": "ICU does not need to interact with ABS."},
    {"Source ECU": "ICU", "Destination ECU": "ACM", "Allowed": "Yes", "Reason": "ICU can send information to ACM for display or alerts."},
    {"Source ECU": "ICU", "Destination ECU": "BCM", "Allowed": "No", "Reason": "ICU does not need to interact with BCM."},
    {"Source ECU": "ICU", "Destination ECU": "ECM", "Allowed": "No", "Reason": "ICU does not need to interact with ECM."},
    {"Source ECU": "ICU", "Destination ECU": "TCM", "Allowed": "No", "Reason": "ICU does not need to interact with TCM."},
    {"Source ECU": "ICU", "Destination ECU": "ADAS", "Allowed": "Yes", "Reason": "ICU receives data from ADAS to display driver assistance information."},
    {"Source ECU": "TCM", "Destination ECU": "ABS", "Allowed": "Yes", "Reason": "TCM communicates with ABS for transmission and braking coordination."},
    {"Source ECU": "TCM", "Destination ECU": "ACM", "Allowed": "Yes", "Reason": "TCM may provide data to ACM for enhanced safety features."},
    {"Source ECU": "TCM", "Destination ECU": "BCM", "Allowed": "No", "Reason": "TCM does not need to interact with BCM."},
    {"Source ECU": "TCM", "Destination ECU": "ECM", "Allowed": "Yes", "Reason": "TCM communicates with ECM for transmission and engine coordination."},
    {"Source ECU": "TCM", "Destination ECU": "ICU", "Allowed": "No", "Reason": "TCM does not need to interact with ICU."},
    {"Source ECU": "TCM", "Destination ECU": "ADAS", "Allowed": "Yes", "Reason": "TCM provides vehicle control data to ADAS for stability and performance."},
    {"Source ECU": "ADAS", "Destination ECU": "ECM", "Allowed": "Yes", "Reason": "ADAS requires engine data from ECM for advanced driving assistance."},
    {"Source ECU": "ADAS", "Destination ECU": "ABS", "Allowed": "Yes", "Reason": "ADAS needs ABS data for safety features like collision avoidance."},
    {"Source ECU": "ADAS", "Destination ECU": "TCM", "Allowed": "Yes", "Reason": "ADAS needs TCM data for vehicle control and stability."},
    {"Source ECU": "ADAS", "Destination ECU": "BCM", "Allowed": "No", "Reason": "ADAS does not directly interact with BCM."},
    {"Source ECU": "ADAS", "Destination ECU": "ICU", "Allowed": "Yes", "Reason": "ADAS may send data to ICU for displaying driver assistance information."},
    {"Source ECU": "ADAS", "Destination ECU": "ACM", "Allowed": "No", "Reason": "ADAS does not need to interact with ACM."}
]


# ECU ID mappings
ecu_names = {
    0x07C2: "BCM",    # Body Control Module
    0x07E2: "ABS",    # Anti-lock Break System 
    0x07D4: "ACM",    # Airbag Control Module
    0x07E4: "ADAS",   # Advanced Driver Assistance Systems
    0x07E0: "ECM",    # Engine Control Module
    0x07B8: "ICU",    # Infotainment Control Unit
    0x07E1: "TCM"     # Transmission Control Module
}

# Define CAN interfaces
CAN_INTERFACES = {
    'vcan0': ['ECM', 'TCM', 'ABS'],
    'vcan1': ['ACM', 'BCM', 'ICU'],
    'vcan2': ['ADAS']
}

# Rate limits (unchanged)
rate_limits = {
    "ABS": 10,  
    "ACM": 10,
    "BCM": 10,
    "ECM": 10,
    "ICU": 10,
    "TCM": 10,
    "ADAS": 10
}



