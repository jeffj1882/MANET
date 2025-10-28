# MANET Skill for Claude Code

This directory contains the MANET skill for Claude Code - a comprehensive Meshtastic development assistant.

## What is this Skill?

The MANET skill transforms Claude Code into an expert Meshtastic development assistant with deep knowledge of:

- **Meshtastic Python SDK** - Complete API coverage with code examples
- **Hardware Selection** - Device recommendations for any use case
- **Mesh Networking** - Configuration, optimization, troubleshooting
- **Project Automation** - MANET repository management with git workflows

## How to Use

The skill is automatically available in Claude Code when working in this project directory.

### Quick Examples

**Ask for code:**
```
"Generate a Python script to log all position updates from the mesh"
"Create an auto-responder bot that replies to 'ping' with 'pong'"
"Write a telemetry monitor for battery levels"
```

**Get hardware advice:**
```
"Recommend hardware for solar-powered remote deployment"
"What's the best device for emergency response teams?"
"Compare nRF52 vs ESP32 for battery life"
```

**Configuration help:**
```
"How do I set up encryption on a secondary channel?"
"Optimize my device for maximum range"
"Configure power-saving for 24-hour battery life"
```

**Troubleshooting:**
```
"My device isn't detected on USB"
"Messages aren't being received between nodes"
"Battery draining too fast"
```

**Project management:**
```
"Update Phase 1 progress in DEVELOPMENT_PLAN.md"
"Commit recent changes to GitHub"
"Create a new hardware configuration file"
```

## What the Skill Knows

### Python SDK Expertise

The skill has comprehensive knowledge of:
- SerialInterface, TCPInterface, BLEInterface
- Messaging (sendText, sendData, sendPosition)
- Event-driven patterns with pub/sub
- Configuration management
- Node discovery and mesh topology
- Telemetry and sensor data
- GPS and waypoint management

### Hardware Database

Knows specifications for:
- RAK WisBlock (modular nRF52840)
- LILYGO T-Beam/T-Echo/LoRa32
- Heltec LoRa32/Mesh Node
- Seeed Card Tracker T1000-E
- B&Q Consulting Station G2
- And many more devices

### Best Practices

The skill applies industry best practices:
- Region configuration before transmitting
- Proper device role selection
- Channel encryption and privacy
- Power optimization techniques
- Range maximization strategies
- Network performance tuning

### Project-Aware Features

When in the MANET project, the skill automatically:
- Tracks development phase progress
- Follows CONTRIBUTING.md commit standards
- Updates DEVELOPMENT_PLAN.md checkboxes
- Organizes files in proper directories
- Commits and pushes to GitHub

## Skill Contents

The `manet.md` file contains:

1. **Core Expertise** - Python SDK, hardware, configuration
2. **Code Templates** - Ready-to-use examples for common tasks
3. **Troubleshooting Guide** - Solutions to common problems
4. **Optimization Techniques** - Range, battery, performance
5. **Project Awareness** - MANET-specific features
6. **Quick Commands** - Examples of what you can ask
7. **Response Guidelines** - How the skill behaves

## Maintenance

This skill is maintained as part of the MANET project:
- **Repository:** https://github.com/jeffj1882/MANET
- **Project Lead:** jeffj1882
- **Organization:** Improvised Electronics

### Updating the Skill

The skill should be updated when:
- Meshtastic Python SDK releases new versions
- New hardware devices become available
- Best practices evolve
- MANET project requirements change
- Community feedback suggests improvements

### Contributing

To improve the skill:
1. Edit `.claude/skills/manet.md`
2. Test with Claude Code
3. Commit changes: `git commit -m "docs: Update MANET skill - <description>"`
4. Push to GitHub: `git push origin main`

## Technical Details

- **File:** `manet.md` (453 lines, ~14KB)
- **Format:** Markdown with embedded code examples
- **Type:** Claude Code skill prompt
- **Scope:** General Meshtastic development (not limited to civilian emergency)

## Resources Referenced

The skill draws from:
- Meshtastic official documentation (https://meshtastic.org/docs)
- Python SDK repository (https://github.com/meshtastic/python)
- Community best practices (Discord, GitHub)
- MANET project standards (DEVELOPMENT_PLAN.md, CONTRIBUTING.md)

## Examples of What You Can Build With This Skill

**Position Tracking System:**
- Real-time location monitoring for all mesh nodes
- JSON export for mapping applications
- Historical position database

**Telemetry Dashboard:**
- Battery level monitoring
- Channel utilization tracking
- Environmental sensor data collection

**Auto-Responder Bot:**
- Reply to specific commands
- Weather information via API integration
- Status reports on request

**MQTT Gateway:**
- Bridge mesh network to MQTT broker
- Internet connectivity for remote monitoring
- Integration with home automation systems

**Range Testing Suite:**
- Automated signal strength logging
- Distance vs. reliability analysis
- Optimal placement recommendations

---

**Version:** 1.0
**Created:** 2025-10-28
**Status:** Active
**Last Updated:** 2025-10-28
