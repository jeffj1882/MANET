#!/usr/bin/env python3
"""
Meshtastic Position Logger
Logs all GPS positions from mesh nodes to a JSON file

Part of the MANET First Project Guide
https://github.com/jeffj1882/MANET
"""

import json
import time
from datetime import datetime
from pubsub import pub
import meshtastic.serial_interface

# Configuration
OUTPUT_FILE = "mesh_positions.json"
positions = {}

def load_existing_positions():
    """Load previously logged positions if file exists"""
    try:
        with open(OUTPUT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_positions():
    """Save positions to JSON file"""
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(positions, f, indent=2)
    print(f"Saved {len(positions)} node positions to {OUTPUT_FILE}")

def on_position(packet, interface):
    """Called when a position update is received"""
    if 'decoded' in packet and 'position' in packet['decoded']:
        node_id = packet['from']
        pos = packet['decoded']['position']

        # Get node name if available
        node_name = "Unknown"
        if node_id in interface.nodes:
            node_name = interface.nodes[node_id].get('user', {}).get('longName', 'Unknown')

        # Extract position data
        latitude = pos.get('latitude', 0)
        longitude = pos.get('longitude', 0)
        altitude = pos.get('altitude', 0)

        # Only log if we have actual coordinates
        if latitude != 0 or longitude != 0:
            timestamp = datetime.now().isoformat()

            # Store position
            positions[node_id] = {
                'name': node_name,
                'latitude': latitude,
                'longitude': longitude,
                'altitude': altitude,
                'timestamp': timestamp,
                'last_updated': packet.get('rxTime', 0)
            }

            print(f"📍 Position update from {node_name} ({node_id}):")
            print(f"   Lat: {latitude:.6f}, Lon: {longitude:.6f}, Alt: {altitude}m")
            print(f"   Time: {timestamp}")

            # Save to file
            save_positions()

def on_connect(interface, topic=pub.AUTO_TOPIC):
    """Called when connected to device"""
    print(f"✅ Connected to Meshtastic device")
    print(f"📡 My Node: {interface.myInfo.my_node_num}")
    print(f"👂 Listening for position updates...")
    print(f"💾 Logging to: {OUTPUT_FILE}")
    print("-" * 60)

def main():
    """Main function"""
    print("🚀 Meshtastic Position Logger Starting...")
    print("-" * 60)

    # Load existing positions
    global positions
    positions = load_existing_positions()
    if positions:
        print(f"📂 Loaded {len(positions)} existing positions")

    # Subscribe to events
    pub.subscribe(on_position, "meshtastic.receive.position")
    pub.subscribe(on_connect, "meshtastic.connection.established")

    # Connect to device
    try:
        interface = meshtastic.serial_interface.SerialInterface()
    except Exception as e:
        print(f"❌ Failed to connect to device: {e}")
        print("Make sure:")
        print("  1. Device is connected via USB")
        print("  2. No other program is using the device")
        print("  3. You have permission to access serial ports")
        return

    # Keep running
    print("\nPress Ctrl+C to stop logging")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping logger...")
        save_positions()
        interface.close()
        print("✅ Logger stopped. Positions saved to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
