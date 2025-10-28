# Hardware Selection Guide
## Meshtastic MANET for Emergency Response

**Target User:** Emergency Response Personnel, Search & Rescue Teams, Community Preparedness
**Project:** Improvised Electronics MANET Development

---

## Overview

This guide outlines hardware considerations for deploying Meshtastic mesh networks in emergency response and disaster scenarios. Hardware must be reliable, ruggedized, and suitable for challenging field environments.

## Hardware Categories

### 1. Base Station Units
**Purpose:** Command post, incident command center, vehicle-mounted operations base

**Requirements:**
- High-gain antenna for extended range
- Continuous power (vehicle/solar/AC)
- Weather-resistant enclosure
- Mounting options (tripod, vehicle, building)

**Recommended Devices:**
- **RAK WisBlock Meshtastic Starter Kit**
  - Modular design
  - External antenna support
  - GPS module option
  - ~$80-120

- **Heltec WiFi LoRa 32 V3**
  - Built-in display
  - WiFi for configuration
  - Good community support
  - ~$30-40

- **LilyGO T-Beam Supreme**
  - Integrated GPS
  - High-quality components
  - External antenna capable
  - ~$60-80

### 2. Mobile Personnel Units
**Purpose:** Individual responders, team leaders, field personnel

**Requirements:**
- Compact, lightweight
- Extended battery life (8-24 hours)
- Clip-on or pocket-sized
- Durable construction
- Simple interface

**Recommended Devices:**
- **RAK Meshtastic Sensor Node**
  - Small form factor
  - Low power consumption
  - ~$50-70

- **Heltec Wireless Stick Lite V3**
  - Ultra-compact
  - USB-C charging
  - No display (phone interface)
  - ~$20-25

- **LilyGO T-Echo**
  - E-ink display
  - Excellent battery life
  - Rugged design
  - ~$60-80

### 3. Vehicle-Mounted Units
**Purpose:** Mobile repeaters, response vehicle communications, mobile command centers

**Requirements:**
- Vehicle power integration
- High-gain antenna mounting
- Vibration resistance
- Extended range
- Weatherproof

**Recommended Devices:**
- **RAK WisBlock + External Antenna**
  - Professional grade
  - Modular expansion
  - ~$100-150

- **Heltec V3 + Vehicle Mount Kit**
  - Cost-effective
  - Proven reliability
  - ~$50-80 (with mount)

### 4. Portable Repeater/Range Extender
**Purpose:** Extend mesh range, bridge gaps, temporary infrastructure

**Requirements:**
- Solar charging capable
- Long battery life (24-72 hours)
- Weather resistant
- Autonomous operation
- Mounting options

**Recommended Devices:**
- **RAK WisBlock Solar**
  - Built-in solar charging
  - Modular design
  - ~$120-180

- **Custom Solar Solution**
  - Heltec V3 + Solar panel + Battery bank
  - ~$80-120

---

## Hardware Specifications Comparison

| Device | Price | Battery Life | GPS | Display | Range* | Best For |
|--------|-------|--------------|-----|---------|--------|----------|
| RAK WisBlock | $80-120 | 24-48hr | Optional | No | Excellent | Base stations |
| Heltec V3 | $30-40 | 12-24hr | No | Yes | Good | All-purpose |
| T-Beam Supreme | $60-80 | 18-36hr | Yes | Yes | Excellent | Mobile personnel |
| RAK Sensor Node | $50-70 | 48-96hr | No | No | Good | Long operations |
| Wireless Stick Lite | $20-25 | 8-16hr | No | No | Fair | Budget/testing |
| T-Echo | $60-80 | 72-168hr | Optional | E-ink | Good | Extended missions |

*Range depends on antenna, environment, and configuration

---

## Antenna Considerations

### Standard vs. External Antennas

**Built-in Antennas:**
- Convenient, no setup required
- Typical range: 1-5km depending on environment
- Suitable for dense mesh deployments

**External Antennas:**
- Significantly extended range: 5-30km+
- Better for base stations and vehicles
- Requires mounting and cable routing
- Higher cost

### Recommended External Antennas

**Base Station/Vehicle:**
- **433/868/915 MHz 5dBi Omnidirectional**
  - Good all-around performance
  - ~$15-30

- **433/868/915 MHz 8-12dBi High Gain**
  - Maximum range
  - Requires elevation
  - ~$30-60

**Mobile:**
- **Flexible 3dBi Antenna**
  - Durable, bend-resistant
  - Better than built-in
  - ~$10-20

---

## Ruggedization & Enclosures

### Environmental Protection Requirements

Emergency response operations often occur in:
- Adverse weather (rain, snow, heat, cold)
- Dusty/dirty environments
- Wet/muddy conditions
- Rough handling scenarios
- Extended outdoor deployments

### Enclosure Options

**Budget Option:**
- Pelican-style cases with foam cutouts
- DIY waterproofing
- ~$20-40 per unit

**Professional Option:**
- IP67-rated electronic enclosures
- Custom-fitted
- Cable glands for antennas
- ~$40-100 per unit

**Tactical Option:**
- MOLLE-compatible pouches
- Impact-resistant shells
- Quick-release mounting
- ~$50-80 per unit

### Considerations
- Antenna placement (inside vs. external)
- Charging port access
- Heat dissipation
- Weight and bulk

---

## Power Solutions

### Battery Options

**Portable Units:**
- 18650 lithium cells (2000-3500mAh)
- USB power banks (10000-20000mAh)
- Hot-swappable battery systems

**Base Stations:**
- Deep-cycle marine batteries
- LiFePO4 battery banks
- Vehicle power integration (12V)

**Solar:**
- 5-20W solar panels
- MPPT charge controllers
- Weatherproof connectors

### Power Budget Planning

Typical Meshtastic device consumption:
- Sleep mode: 0.1-1mA
- Receive: 30-50mA
- Transmit: 100-150mA
- GPS active: +30-50mA

Example: 3000mAh battery with moderate use (10 messages/hour)
- Expected runtime: 24-36 hours
- With GPS: 18-24 hours
- Sleep optimization: 48+ hours

---

## Frequency Considerations

### LoRa Frequency Bands by Region

**United States:**
- 915 MHz (ISM band)
- FCC Part 15 compliant
- No license required
- Max 1W EIRP

**Europe:**
- 868 MHz (ISM band)
- ETSI compliant
- Max 25mW EIRP (restrictions apply)

**Other Regions:**
- Check local regulations
- Meshtastic supports multiple frequency plans

**Important:** Ensure hardware matches your operational region's frequency band.

---

## Initial Procurement Recommendation

### Phase 1 Development Kit (Budget: ~$500-700)

**Minimum Viable Network:**
1. **Base Station:** RAK WisBlock + 5dBi antenna ($120)
2. **Mobile Units:** 3x Heltec V3 ($120)
3. **Portable:** 1x T-Beam Supreme ($75)
4. **Accessories:** Cases, cables, batteries ($100)
5. **Solar Kit:** Panel + controller ($85)

**Total:** ~$500

### Expanded Testing Kit (Budget: ~$1200-1500)

Add to above:
- 3 additional mobile units (various types)
- 1 vehicle-mounted repeater
- Professional enclosures
- External antennas
- Extended battery systems

---

## Vendor List

### Primary Vendors
- **RAK Wireless:** https://store.rakwireless.com
- **Heltec:** https://heltec.org (or Amazon/AliExpress)
- **LilyGO:** https://www.lilygo.cc (or Amazon/AliExpress)

### Accessories
- **Antennas:** Amazon, eBay, RF parts suppliers
- **Enclosures:** Pelican, Nanuk, Amazon
- **Solar:** Amazon, Voltaic Systems
- **Batteries:** 18650BatteryStore, Amazon

### Note
- Lead times vary (1-4 weeks)
- Consider shipping costs
- Bulk orders may get discounts

---

## Testing & Validation Checklist

Before deploying hardware:

- [ ] Verify frequency band matches region
- [ ] Flash latest Meshtastic firmware
- [ ] Test battery life under load
- [ ] Verify range in operational environment
- [ ] Test ruggedized enclosures
- [ ] Validate GPS accuracy (if applicable)
- [ ] Check antenna connections and SWR
- [ ] Conduct mesh healing tests
- [ ] Verify encryption functionality
- [ ] Test in temperature extremes
- [ ] Validate mounting solutions
- [ ] Confirm charging systems work

---

## Maintenance & Spares

### Recommended Spares
- 20% extra devices for failures/expansion
- Spare antennas (most common failure)
- Extra batteries
- Charging cables
- Enclosure seals/gaskets

### Maintenance Schedule
- Weekly: Battery charging, firmware updates
- Monthly: Antenna connections, enclosure integrity
- Quarterly: Full system health check
- Annually: Battery replacement planning

---

## Next Steps

1. Review this guide with project requirements
2. Select hardware based on operational needs
3. Order Phase 1 development kit
4. Document hardware receipt and testing
5. Update this guide based on testing results

---

**Document Version:** 1.0
**Created:** 2025-10-28
**Review Date:** Post Phase 1 testing
**Status:** Preliminary recommendations - validate before procurement
