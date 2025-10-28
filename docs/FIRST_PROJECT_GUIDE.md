# Your First Meshtastic Project
## A Complete Beginner's Guide to Building Your First Mesh Network

**Target Audience:** Complete beginners to Meshtastic
**Time Required:** 2-4 hours
**Difficulty:** Beginner
**Cost:** $60-150 for hardware

---

## Table of Contents

1. [What You'll Build](#what-youll-build)
2. [What You'll Need](#what-youll-need)
3. [Understanding the Basics](#understanding-the-basics)
4. [Step 1: Hardware Setup](#step-1-hardware-setup)
5. [Step 2: Installing Software](#step-2-installing-software)
6. [Step 3: First Device Configuration](#step-3-first-device-configuration)
7. [Step 4: Setting Up Your Second Device](#step-4-setting-up-your-second-device)
8. [Step 5: Testing Your Mesh](#step-5-testing-your-mesh)
9. [Step 6: Building a Python Position Logger](#step-6-building-a-python-position-logger)
10. [Troubleshooting](#troubleshooting)
11. [Next Steps](#next-steps)

---

## What You'll Build

By the end of this guide, you'll have:

✅ **A working 2-node mesh network** that can communicate over LoRa
✅ **Encrypted communications** between your devices
✅ **GPS position tracking** showing locations on your devices
✅ **A Python script** that logs all positions from your mesh to a file
✅ **Understanding** of how to expand your network

**Real-World Application:** This is the foundation for emergency communications, hiking group coordination, community networks, and more.

---

## What You'll Need

### Required Hardware (Choose ONE of these starter combinations)

**Budget Option (~$60-80):**
- 2x Heltec LoRa32 V3 (~$30-40 each)
- 2x USB cables (data-capable, not just charging)
- 2x USB battery banks (optional for portable use)

**Recommended Option (~$120-160):**
- 2x LILYGO T-Beam Supreme (~$60-80 each)
- Built-in GPS
- Better battery life
- More robust

**Premium Option (~$140-180):**
- 2x RAK WisBlock Starter Kits (~$70-90 each)
- Modular design
- Best battery life (nRF52840)
- Expandable with sensors

### Required Software

- Computer (Windows, Mac, or Linux)
- Python 3.8 or newer
- Web browser
- USB drivers (we'll install these)

### Optional but Helpful

- External antennas (3-5dBi) for better range
- Weatherproof cases for outdoor testing
- Smartphone with Meshtastic app (iOS/Android)

---

## Understanding the Basics

### What is Meshtastic?

Meshtastic creates a **mesh network** using LoRa (Long Range) radio technology. Think of it like walkie-talkies, but smarter:

- **No cell towers or internet needed** - Works completely off-grid
- **Automatic message routing** - Devices relay messages for each other
- **Extended range** - 1-30+ km depending on environment
- **Encrypted** - Your communications are private
- **Low power** - Devices can run for days or weeks on battery

### How Does a Mesh Network Work?

```
You → [Device A] )))))) [Device B] → Friend
                  ↓
              [Device C]
                  ↓
              [Device D] → Another Friend
```

If you send a message to "Another Friend" and they're out of range:
1. Your device (A) sends to Device C (in range)
2. Device C automatically relays to Device D
3. Device D delivers to your friend

**Everyone in the mesh helps everyone else communicate.**

### Key Concepts

**Node:** A single device in your mesh (also called a "radio" or "device")

**Channel:** Like a radio station frequency. All devices on the same channel can communicate.

**PSK (Pre-Shared Key):** The encryption password for your channel.

**Hop Limit:** Maximum number of times a message can be relayed (default: 3 hops).

**LoRa Region:** Your geographic region's radio frequency (US=915MHz, EU=868MHz).

---

## Step 1: Hardware Setup

### ⚠️ CRITICAL SAFETY WARNING

**NEVER power on a LoRa device without an antenna attached!**

This can permanently damage the radio chip. The antenna MUST be connected BEFORE you plug in USB or power.

### Hardware Setup Checklist

For EACH device:

1. **Attach Antenna**
   - Screw on or connect the antenna firmly
   - For devices with external antenna connectors, ensure tight connection
   - Default antennas are usually adequate for testing

2. **Verify USB Cable**
   - Not all USB cables support data transfer
   - Test your cable by connecting to a phone/device and trying to transfer a file
   - If it only charges, get a different cable

3. **Connect to Computer**
   - Plug USB cable into device
   - Plug other end into computer
   - Device should power on (LED light or screen activity)
   - You should hear a USB connection sound (Windows/Mac)

### Troubleshooting Hardware Connection

**No power when connected:**
- Try different USB port
- Try different cable
- Some devices have power switches - check for a button

**USB not recognized:**
- We'll install drivers in the next step
- This is normal for first connection

---

## Step 2: Installing Software

### Install Python (if not already installed)

**Check if Python is installed:**
```bash
python3 --version
```

If you see `Python 3.8` or higher, you're good! If not:

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

**Mac:**
```bash
brew install python3
# Or download from python.org
```

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Install Meshtastic Python CLI

Open terminal/command prompt and run:

```bash
pip3 install --upgrade "meshtastic[cli]"
```

**Verify installation:**
```bash
meshtastic --version
```

You should see version information. If you get "command not found", try:
```bash
python3 -m meshtastic --version
```

### Install USB Drivers (if needed)

**Windows:** Most modern Windows systems auto-detect. If not:
- Download CP210x USB to UART Bridge driver
- Download CH9102 driver
- Install both (devices use different chips)

**Mac:**
```bash
pip3 install -U --pre pyserial
```

**Linux:**
```bash
# Add your user to dialout group for serial port access
sudo usermod -a -G dialout $USER
# Log out and log back in for this to take effect
```

### Test Connection

With ONE device connected:

```bash
meshtastic --info
```

**If successful:** You'll see device information, firmware version, and configuration.

**If unsuccessful:** See [Troubleshooting Section](#troubleshooting)

---

## Step 3: First Device Configuration

Now we'll configure your first device. Keep it connected via USB.

### Set Your Identity

```bash
meshtastic --set-owner "Your Name"
meshtastic --set-owner-short "YN"
```

Replace "Your Name" with your actual name (or callsign). The short name should be 3-4 characters.

### Set Your Region (REQUIRED)

**This is critical!** Your device won't transmit without a region set.

```bash
# United States
meshtastic --set lora.region US

# Europe
meshtastic --set lora.region EU_868

# Other regions (check: meshtastic --set lora.region --help)
# UK, ANZ (Australia/NZ), CN, JP, IN, etc.
```

### Configure Primary Channel

Create an encrypted channel with a random password:

```bash
meshtastic --ch-set name "My First Mesh" --ch-index 0
meshtastic --ch-set psk random --ch-index 0
```

### Set Device Role

```bash
meshtastic --set device.role CLIENT
```

**CLIENT** is the standard role for most devices (recommended for beginners).

### Verify Configuration

```bash
meshtastic --info
```

Look for:
- ✅ Your name appears as owner
- ✅ Region is set (not "unset")
- ✅ Channel 0 has a name
- ✅ Device role is CLIENT

### Save the Channel Configuration

We need to apply the same channel settings to your second device. Generate a configuration URL:

```bash
meshtastic --qr
```

This displays:
1. A QR code (you can scan with phone app)
2. **A URL** - Copy this entire URL! It looks like:
   ```
   https://meshtastic.org/e/#CgUYAyIBAQ...
   ```

**Save this URL somewhere!** You'll need it for Device 2.

Alternatively, export full configuration:

```bash
meshtastic --export-config > device1-config.yaml
```

---

## Step 4: Setting Up Your Second Device

Now let's configure your second device to join the mesh.

### Disconnect Device 1

```bash
# Unplug Device 1 from USB
```

### Connect Device 2

Plug in your second device via USB.

### Apply Basic Configuration

```bash
# Set owner (different name!)
meshtastic --set-owner "Friend Name"
meshtastic --set-owner-short "FN"

# Set region (MUST match Device 1)
meshtastic --set lora.region US

# Set role
meshtastic --set device.role CLIENT
```

### Apply Channel Configuration from Device 1

**Option A: Use the URL**

```bash
meshtastic --seturl "https://meshtastic.org/e/#CgUYAyIBAQ..."
```

Replace the URL with the one you saved from Device 1.

**Option B: Use config file**

```bash
meshtastic --configure device1-config.yaml
```

**Important:** This copies ALL settings from Device 1. You may want to reset the owner name afterward:

```bash
meshtastic --set-owner "Friend Name"
meshtastic --set-owner-short "FN"
```

### Verify Device 2

```bash
meshtastic --info
```

Check that:
- ✅ Region matches Device 1
- ✅ Channel 0 name matches Device 1
- ✅ Different owner name

---

## Step 5: Testing Your Mesh

### Test 1: Send a Text Message

**With Device 2 still connected to computer:**

```bash
meshtastic --sendtext "Hello from Device 2!"
```

**Now connect Device 1 (disconnect Device 2 if you only have one USB port):**

```bash
meshtastic --nodes
```

You should see Device 2 in the node list!

```bash
meshtastic --listen
```

Leave this running. You'll see messages as they arrive (JSON format).

**From another terminal (with Device 2 connected):**

```bash
meshtastic --sendtext "Can you hear me?"
```

**Device 1 terminal should show the message arrive!**

Press `Ctrl+C` to stop listening.

### Test 2: View Node List

Both devices should see each other:

```bash
meshtastic --nodes
```

Output should show:
```
Connected device: /dev/ttyUSB0

┌─────────────┬────────────┬─────────┬──────────────┬────────────────┐
│ User        │ ID         │ SNR     │ Last Heard   │ Since          │
├─────────────┼────────────┼─────────┼──────────────┼────────────────┤
│ Your Name   │ !12345678  │ N/A     │ N/A          │ 2 minutes      │
│ Friend Name │ !87654321  │ 8.5     │ 10 seconds   │ 1 minute       │
└─────────────┴────────────┴─────────┴──────────────┴────────────────┘
```

**SNR (Signal to Noise Ratio):** Higher is better. 5+ is good.

### Test 3: Position Sharing (GPS-equipped devices only)

If your devices have GPS (like T-Beam):

```bash
# Check if position is available
meshtastic --info
```

Look for latitude/longitude. If you see `lat=0.0`, GPS hasn't locked yet. Take device outside with clear sky view.

Once GPS has a lock:

```bash
meshtastic --nodes
```

You should see position coordinates for devices with GPS!

### Test 4: Range Test

**Indoors test:** Devices in same room - should work perfectly

**Short range test:**
- Device 1: Leave on desk connected to computer
- Device 2: Carry to opposite side of house/building
- Send messages back and forth

```bash
# From Device 2's location
meshtastic --sendtext "Testing from far room"

# Check on Device 1
meshtastic --listen
```

**Outdoor range test:**
- Device 1: Leave at base location with computer
- Device 2: Put in backpack with battery bank
- Walk away (100m, 500m, 1km+)
- Send test messages at each distance
- Note: Range varies GREATLY by environment

**Expected range:**
- Indoors/urban: 500m - 2km
- Suburban: 2km - 5km
- Rural line-of-sight: 5km - 15km+
- With elevated antenna: 15km - 30km+

---

## Step 6: Building a Python Position Logger

Let's build your first Meshtastic Python application! This script will log all position updates from your mesh to a JSON file.

### Create the Script

Create a file called `position_logger.py`:

```python
#!/usr/bin/env python3
"""
Meshtastic Position Logger
Logs all GPS positions from mesh nodes to a JSON file
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
```

### Run the Logger

1. **Connect Device 1 to your computer**

2. **Run the script:**
   ```bash
   python3 position_logger.py
   ```

3. **You should see:**
   ```
   🚀 Meshtastic Position Logger Starting...
   ✅ Connected to Meshtastic device
   📡 My Node: 123456789
   👂 Listening for position updates...
   💾 Logging to: mesh_positions.json
   ```

4. **Trigger position updates:**
   - Take Device 2 (with GPS) outside
   - Wait for GPS lock
   - Walk around with Device 2
   - You'll see position updates appear in the logger!

5. **View logged positions:**
   ```bash
   cat mesh_positions.json
   ```

### Understanding the Output

The `mesh_positions.json` file will look like:

```json
{
  "!12345678": {
    "name": "Your Name",
    "latitude": 37.774929,
    "longitude": -122.419418,
    "altitude": 52,
    "timestamp": "2025-10-28T14:23:45.123456",
    "last_updated": 1730136225
  },
  "!87654321": {
    "name": "Friend Name",
    "latitude": 37.775123,
    "longitude": -122.419789,
    "altitude": 48,
    "timestamp": "2025-10-28T14:24:12.654321",
    "last_updated": 1730136252
  }
}
```

### Extending the Logger

**Ideas for enhancements:**

1. **Add mapping visualization:**
   - Use the coordinates to plot on a map
   - Libraries: `folium`, `matplotlib`

2. **Distance calculations:**
   - Calculate distance between nodes
   - Use `geopy` library

3. **Alert system:**
   - Notify when nodes go out of range
   - Send email/SMS when specific nodes appear

4. **Web dashboard:**
   - Build a Flask/FastAPI web interface
   - Real-time map updates

---

## Troubleshooting

### Device Not Detected

**Problem:** `meshtastic --info` says "No devices found"

**Solutions:**

1. **Check USB cable supports data**
   - Try transferring a file with another device
   - If it only charges, get a new cable

2. **Install drivers (Windows):**
   - Download CP210x driver
   - Download CH9102 driver
   - Restart computer after installing

3. **Check permissions (Linux):**
   ```bash
   sudo usermod -a -G dialout $USER
   # Log out and log back in
   ```

4. **Manually specify port:**
   ```bash
   # List ports
   ls /dev/tty*  # Linux/Mac
   # or Device Manager → Ports (Windows)

   # Connect to specific port
   meshtastic --port /dev/ttyUSB0  # Linux
   meshtastic --port COM4           # Windows
   ```

### No Messages Being Received

**Problem:** Devices don't see each other

**Check:**

1. **Region settings match:**
   ```bash
   meshtastic --get lora.region
   ```
   Both devices MUST have the same region.

2. **Channel encryption matches:**
   ```bash
   meshtastic --info
   ```
   Look at "Primary channel" settings. PSK should match.

3. **Devices are in range:**
   - Start with devices in the same room
   - Move farther apart gradually

4. **Antennas are connected:**
   - Loose antenna = no transmission
   - Verify antenna is screwed on tight

### GPS Not Getting Lock

**Problem:** Latitude/longitude show 0.0

**Solutions:**

1. **Go outside** - GPS requires clear sky view
2. **Wait 5-15 minutes** - Cold start takes time
3. **Check GPS is enabled:**
   ```bash
   meshtastic --get position.gps_enabled
   meshtastic --set position.gps_enabled true
   ```
4. **Verify GPS hardware** - Not all devices have GPS

### Python Script Errors

**Problem:** `position_logger.py` crashes or doesn't work

**Check:**

1. **Meshtastic module installed:**
   ```bash
   pip3 install --upgrade meshtastic
   ```

2. **Device is connected:**
   - Only one program can access the device at a time
   - Close any other terminals running `meshtastic` commands

3. **Python version:**
   ```bash
   python3 --version
   # Should be 3.8 or higher
   ```

### Messages Delayed or Lost

**Problem:** Messages take a long time or don't arrive

**Causes:**
- **Out of range** - Move devices closer
- **Interference** - Try different location
- **Too many hops** - Direct connection is faster
- **Network congestion** - Too many devices talking at once

**Check signal quality:**
```bash
meshtastic --nodes
```
Look at SNR (Signal to Noise Ratio):
- **10+ = Excellent**
- **5-10 = Good**
- **0-5 = Marginal**
- **Negative = Very poor**

---

## Next Steps

### Expand Your Knowledge

Now that you have a working mesh, explore these topics:

**1. Add More Nodes**
- Each additional node extends your range
- Share your channel URL with friends
- Build a community mesh

**2. Advanced Configuration**
- Secondary encrypted channels for private groups
- Optimize for battery life or range
- Set up MQTT gateway for internet connectivity

**3. Build More Applications**

**Auto-Responder Bot:**
```python
def on_text(packet, interface):
    if 'decoded' in packet and 'text' in packet['decoded']:
        message = packet['decoded']['text']
        sender = packet['from']
        if message.lower() == "ping":
            interface.sendText("pong", destinationId=sender)
```

**Telemetry Monitor:**
- Track battery levels across your mesh
- Monitor channel utilization
- Environmental sensors (temperature, humidity)

**MQTT Bridge:**
- Connect mesh to internet services
- Home automation integration
- Remote monitoring

**4. Optimize Your Network**

**For Maximum Range:**
```bash
meshtastic --ch-longslow              # Slower but farther
meshtastic --set lora.tx_power 0     # Max power for region
# Add external antennas
```

**For Battery Life:**
```bash
meshtastic --set position.gps_update_interval 900
meshtastic --set position.position_broadcast_smart_enabled true
meshtastic --set power.wait_bluetooth_secs 900
```

**5. Join the Community**

- **Discord:** https://discord.gg/meshtastic
- **GitHub:** https://github.com/meshtastic
- **Reddit:** r/meshtastic
- **Documentation:** https://meshtastic.org

### Suggested Second Project

**Build a Solar-Powered Remote Node:**

1. Get a nRF52-based device (RAK or T-Echo)
2. Add 5-10W solar panel
3. Mount in weatherproof case
4. Place on roof or hilltop
5. Configure as ROUTER role

This creates permanent infrastructure to extend your mesh!

### Contributing to MANET Project

This tutorial is part of the MANET project at Improvised Electronics:

- **Repository:** https://github.com/jeffj1882/MANET
- **Project Goals:** Civilian emergency communications
- **Current Phase:** Phase 1 - Foundation & Research

**Ways to contribute:**
- Share your first project experience
- Document your hardware testing results
- Submit range test data
- Create additional tutorials
- Report issues or improvements

---

## Summary

Congratulations! You've completed your first Meshtastic project. You now have:

✅ Two devices communicating over LoRa mesh
✅ Understanding of basic configuration
✅ Experience with CLI commands
✅ A working Python application
✅ Foundation for building more complex projects

**Key Takeaways:**

- Meshtastic provides off-grid, long-range communication
- Mesh networks automatically route messages
- Configuration must match between devices (region, channel)
- Python SDK enables powerful custom applications
- Community and documentation are excellent resources

**Your mesh journey has just begun!**

---

## Additional Resources

### Official Documentation
- Getting Started: https://meshtastic.org/docs/getting-started/
- Python SDK: https://meshtastic.org/docs/software/python/cli/
- Configuration: https://meshtastic.org/docs/configuration/

### MANET Project Files
- [Hardware Selection Guide](HARDWARE_SELECTION.md)
- [Development Plan](../DEVELOPMENT_PLAN.md)
- [Contributing Guide](../CONTRIBUTING.md)

### Video Tutorials
- Search YouTube for "Meshtastic tutorial"
- Official Meshtastic channel has great walkthroughs

### Hardware Vendors
- RAK Wireless: https://store.rakwireless.com
- LILYGO: https://www.lilygo.cc
- Heltec: https://heltec.org

---

**Document Version:** 1.0
**Created:** 2025-10-28
**Author:** Improvised Electronics / MANET Project
**License:** Open for educational use
**Feedback:** https://github.com/jeffj1882/MANET/issues
