import can
import logging
from firewall_dict import firewall_rules, ecu_names, CAN_INTERFACES

# Setup logging to file
logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize CAN interfaces
INTERFACES = {interface: can.interface.Bus(channel=interface, interface='socketcan') for interface in CAN_INTERFACES.keys()}

# Helper function to get ECU name from a message ID
def get_ecu_name(message_id):
    return ecu_names.get(message_id, None)

# Function to get the reason for a firewall rule
def get_firewall_reason(source, destination):
    for rule in firewall_rules:
        if rule["Source ECU"] == source and rule["Destination ECU"] == destination:
            return rule["Reason"]
    return "No reason provided"

# Function to check if traffic is allowed based on firewall rules
def is_traffic_allowed(source, destination):
    for rule in firewall_rules:
        if rule["Source ECU"] == source and rule["Destination ECU"] == destination:
            return rule["Allowed"] == "Yes"
    return False

# Function to process incoming CAN messages
def process_message(source_interface, message):
    source_ecu = get_ecu_name(message.arbitration_id)
    if not source_ecu:
        return

    log_msg = f"Processing message from {source_ecu} on {source_interface}"
    print(log_msg)
    logging.info(log_msg)

    # Flag to check if message was forwarded
    forwarded = False

    for interface, ecus in CAN_INTERFACES.items():
        if interface == source_interface:
            # Messages received on the same interface
            for dest_ecu in ecus:
                if dest_ecu != source_ecu:  # Avoid processing message to the same ECU
                    if is_traffic_allowed(source_ecu, dest_ecu):
                        # Forward the message on the same interface
                        reason = get_firewall_reason(source_ecu, dest_ecu)
                        log_msg = f"Forwarding message from {source_ecu} to {dest_ecu} on {interface}: {reason}"
                        print(log_msg)
                        logging.info(log_msg)
                        try:
                            INTERFACES[interface].send(message)
                            forwarded = True
                        except can.CanError:
                            log_msg = f"Failed to send message on {interface}"
                            print(log_msg)
                            logging.error(log_msg)
                    else:
                        # Block the message on the same interface
                        reason = get_firewall_reason(source_ecu, dest_ecu)
                        log_msg = f"Blocking message from {source_ecu} to {dest_ecu} on {interface}: {reason}"
                        print(log_msg)
                        logging.info(log_msg)
        else:
            # Forward to other interfaces
            for dest_ecu in ecus:
                if is_traffic_allowed(source_ecu, dest_ecu):
                    # Forward the message
                    reason = get_firewall_reason(source_ecu, dest_ecu)
                    log_msg = f"Forwarding message from {source_ecu} to {dest_ecu} on {interface}: {reason}"
                    print(log_msg)
                    logging.info(log_msg)
                    try:
                        INTERFACES[interface].send(message)
                        forwarded = True
                    except can.CanError:
                        log_msg = f"Failed to send message on {interface}"
                        print(log_msg)
                        logging.error(log_msg)
                else:
                    reason = get_firewall_reason(source_ecu, dest_ecu)
                    log_msg = f"Blocking message from {source_ecu} to {dest_ecu} on {interface}: {reason}"
                    print(log_msg)
                    logging.info(log_msg)

    if not forwarded:
        log_msg = f"Message from {source_ecu} on {source_interface} was not forwarded or blocked"
        print(log_msg)
        logging.info(log_msg)

def log_to_vcan3(message):
    """Send log messages to vcan3"""
    if 'vcan3' in INTERFACES:
        try:
            INTERFACES['vcan3'].send(message)
        except can.CanError:
            log_msg = f"Failed to send log message on vcan3"
            print(log_msg)
            logging.error(log_msg)

# Main function to listen on all CAN interfaces
def main():
    try:
        while True:
            for interface, bus in INTERFACES.items():
                message = bus.recv(timeout=1.0)  # Adjust timeout as needed
                if message:
                    process_message(interface, message)
                    # Log every message to vcan3
                    log_to_vcan3(message)
    except KeyboardInterrupt:
        print("Stopping CAN monitoring")
    finally:
        # Properly close the CAN interfaces
        for interface, bus in INTERFACES.items():
            bus.shutdown()

if __name__ == "__main__":
    main()
