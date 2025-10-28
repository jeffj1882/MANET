# Meshtastic Quick Reference Card

Quick command reference for Meshtastic CLI operations.

## Connection

```bash
# Auto-detect and connect
meshtastic --info

# Specific port
meshtastic --port /dev/ttyUSB0      # Linux
meshtastic --port COM4              # Windows

# Network (WiFi)
meshtastic --host 192.168.1.100
meshtastic --host meshtastic.local

# Bluetooth
meshtastic --ble-scan               # Find devices
meshtastic --ble Meshtastic_1234    # Connect
```

## First-Time Setup

```bash
# 1. Set region (REQUIRED FIRST!)
meshtastic --set lora.region US     # or EU_868, UK, ANZ, etc.

# 2. Set owner
meshtastic --set-owner "Your Name"
meshtastic --set-owner-short "YN"

# 3. Configure channel
meshtastic --ch-set name "My Mesh" --ch-index 0
meshtastic --ch-set psk random --ch-index 0

# 4. Set role
meshtastic --set device.role CLIENT

# 5. Verify
meshtastic --info
```

## Information

```bash
meshtastic --info         # Full device info
meshtastic --nodes        # List all nodes
meshtastic --qr           # Channel QR code
meshtastic --support      # Diagnostic info
```

## Configuration

```bash
# Get settings
meshtastic --get all
meshtastic --get lora
meshtastic --get device.role

# Set settings
meshtastic --set device.role CLIENT
meshtastic --set lora.hop_limit 3
meshtastic --set position.gps_update_interval 300

# Export/Import
meshtastic --export-config > backup.yaml
meshtastic --configure backup.yaml
```

## Messaging

```bash
# Send text
meshtastic --sendtext "Hello mesh"

# Send to specific node
meshtastic --sendtext "Hi" --dest !a1b2c3d4

# Send with acknowledgment
meshtastic --sendtext "Important" --dest !a1b2c3d4 --ack

# Listen for messages
meshtastic --listen
```

## Channels

```bash
# List channels
meshtastic --info

# Add secondary channel
meshtastic --ch-add "Private" --ch-index 1

# Configure channel
meshtastic --ch-set name "Team" --ch-index 1
meshtastic --ch-set psk random --ch-index 1

# Modem presets
meshtastic --ch-longfast    # Default (balanced)
meshtastic --ch-longslow    # Max range
meshtastic --ch-shortfast   # Min latency

# Remove channel
meshtastic --ch-del --ch-index 1
```

## GPS / Position

```bash
# Request position from node
meshtastic --request-position --dest !a1b2c3d4

# Set fixed position (no GPS hardware)
meshtastic --setlat 37.7749 --setlon -122.4194 --setalt 50

# Remove fixed position
meshtastic --remove-position

# Configure GPS updates
meshtastic --set position.gps_update_interval 300
meshtastic --set position.position_broadcast_secs 900
meshtastic --set position.position_broadcast_smart_enabled true
```

## Device Management

```bash
# Reboot
meshtastic --reboot

# Shutdown
meshtastic --shutdown

# Factory reset (WARNING: Erases all settings!)
meshtastic --factory-reset

# Reset node database
meshtastic --reset-nodedb
```

## Python SDK Quick Start

### Basic Connection

```python
import meshtastic.serial_interface

# Connect
interface = meshtastic.serial_interface.SerialInterface()

# Send message
interface.sendText("Hello mesh!")

# Close
interface.close()
```

### Event-Driven Pattern

```python
from pubsub import pub
import meshtastic.serial_interface

def on_receive(packet, interface):
    print(f"Received: {packet}")

# Subscribe to events
pub.subscribe(on_receive, "meshtastic.receive")
pub.subscribe(on_receive, "meshtastic.receive.text")
pub.subscribe(on_receive, "meshtastic.receive.position")

# Connect (stays open for async events)
interface = meshtastic.serial_interface.SerialInterface()
```

### Configuration

```python
# Get local node
node = interface.getNode('^local')

# Modify settings
node.localConfig.device.role = Config.DeviceConfig.Role.CLIENT
node.localConfig.lora.region = Config.LoRaConfig.RegionCode.US
node.localConfig.position.gps_update_interval = 300

# Save changes
node.writeConfig("device")
node.writeConfig("lora")
node.writeConfig("position")
```

## Device Roles

```bash
# Standard roles
meshtastic --set device.role CLIENT         # Default (recommended)
meshtastic --set device.role CLIENT_MUTE    # No rebroadcasting
meshtastic --set device.role ROUTER         # Always-on infrastructure
meshtastic --set device.role REPEATER       # Hidden infrastructure
meshtastic --set device.role TRACKER        # GPS-optimized
meshtastic --set device.role SENSOR         # Telemetry-optimized
```

**Best Practice:** Use CLIENT for most devices.

## Common Settings

### Range Optimization

```bash
meshtastic --ch-longslow              # Slower but farther
meshtastic --set lora.tx_power 0      # Max power
meshtastic --set lora.hop_limit 3     # Default (optimal)
```

### Battery Optimization

```bash
meshtastic --set position.gps_update_interval 900
meshtastic --set position.position_broadcast_smart_enabled true
meshtastic --set power.wait_bluetooth_secs 900
meshtastic --set power.ls_secs 300
```

### Privacy

```bash
# Reduce position precision (0=disabled, 32=full)
meshtastic --ch-set module_settings.position_precision 13 --ch-index 0

# Create private channel
meshtastic --ch-add "Private" --ch-index 1
meshtastic --ch-set psk random --ch-index 1
```

## Frequency Regions

| Region | Frequency | Max Power | License |
|--------|-----------|-----------|---------|
| US | 915 MHz | 1W EIRP | Not required |
| EU_868 | 868 MHz | 25mW | Not required |
| UK | 868 MHz | 25mW | Not required |
| ANZ | 915 MHz | 1W EIRP | Not required |
| CN | 470 MHz | Varies | Check local |
| JP | 920 MHz | Varies | Check local |

## Troubleshooting

### Device Not Found

```bash
# Linux: Add user to dialout group
sudo usermod -a -G dialout $USER
# Log out and log back in

# Manually specify port
meshtastic --port /dev/ttyUSB0
```

### Messages Not Received

```bash
# Check region matches
meshtastic --get lora.region

# Check channel info
meshtastic --info  # Look at Primary channel

# Check node list
meshtastic --nodes
```

### GPS Not Working

```bash
# Enable GPS
meshtastic --set position.gps_enabled true

# Go outside (clear sky view)
# Wait 5-15 minutes for lock
```

## Signal Quality (SNR)

From `meshtastic --nodes`:

- **10+ dB** = Excellent
- **5-10 dB** = Good
- **0-5 dB** = Marginal
- **Negative** = Very poor

## Resources

- **Official Docs:** https://meshtastic.org/docs
- **Python SDK:** https://github.com/meshtastic/python
- **Discord:** https://discord.gg/meshtastic
- **MANET Project:** https://github.com/jeffj1882/MANET

---

**Tip:** Chain commands to minimize reboots:
```bash
meshtastic --set device.role CLIENT --set lora.region US --set lora.hop_limit 3
```

**Safety:** Always attach antenna before powering on device!
