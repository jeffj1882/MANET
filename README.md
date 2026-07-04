# MANET - Meshtastic Development Project
## Improvised Electronics

> **STATUS: PARKED** — Project stalled since 2025-10-28. No hardware acquired; Phase 1 incomplete. To revive: order 3× Heltec WiFi LoRa 32 V3 (~$105 total), reset phase dates in DEVELOPMENT_PLAN.md, and recommit. See DEVELOPMENT_PLAN.md for details. To archive: `gh repo archive jeffj1882/MANET` (manual decision — not executed automatically).

Mobile Ad-hoc Network (MANET) development for civilian emergency response and disaster communications using Meshtastic LoRa mesh networking platform.

## Project Overview

This project develops resilient communications infrastructure for emergency response, disaster relief, search and rescue, and community preparedness using Meshtastic's open-source mesh networking platform. The system provides secure, off-grid communications for incident response, personnel safety, and coordination when traditional infrastructure is unavailable or compromised.

## Key Features

- **Off-Grid Operations:** No cellular or internet dependency
- **Extended Range:** LoRa technology provides multi-kilometer coverage (5-30km+)
- **Mesh Resilience:** Decentralized architecture with automatic healing
- **Encrypted Communications:** AES-256 encryption for sensitive operations
- **GPS Integration:** Real-time location tracking and incident mapping
- **Civilian Focus:** Designed for disaster response, search & rescue, wildfire response, community preparedness

## Project Structure

```
MANET/
├── README.md                       # This file
├── DEVELOPMENT_PLAN.md             # Complete development framework
├── CONTRIBUTING.md                 # Git workflow and contribution guide
├── CLAUDE.md                       # Project-specific instructions
├── .claude/skills/manet.md         # MANET skill for Claude Code
├── references/                     # OSINT materials and standards
├── docs/                           # Documentation and procedures
│   ├── FIRST_PROJECT_GUIDE.md      # Beginner tutorial (START HERE!)
│   ├── QUICK_REFERENCE.md          # Command cheat sheet
│   └── HARDWARE_SELECTION.md       # Hardware guide
├── src/                            # Source code and scripts
│   └── position_logger.py          # Example: GPS position logger
├── hardware/                       # Hardware configs and specs
└── incidents/                      # Incident-specific reports (OSINT standards)
```

## Quick Start

### New to Meshtastic?

**Start here!** 👉 [First Project Guide](docs/FIRST_PROJECT_GUIDE.md)

Complete beginner-friendly tutorial that walks you through:
- Choosing hardware
- Setting up your first 2-node mesh network
- Sending messages and tracking positions
- Building your first Python application

**Time:** 2-4 hours | **Cost:** $60-150

Also check out the [Quick Reference Card](docs/QUICK_REFERENCE.md) for common commands.

### For MANET Project Development

### Prerequisites
- Python 3.8+
- Meshtastic hardware devices (see DEVELOPMENT_PLAN.md)
- Basic understanding of LoRa mesh networking

### Installation
```bash
# Install Meshtastic Python SDK
pip install meshtastic

# Clone or navigate to project
cd /Users/jeffjennings/Projects/MANET
```

### Initial Setup
1. Review `DEVELOPMENT_PLAN.md` for complete development framework
2. Check `references/` folder for OSINT standards and materials
3. Follow Phase 1 objectives to establish development environment
4. Order hardware from approved vendor list (TBD in Phase 1)

## Development Phases

1. **Foundation & Research** (Weeks 1-2)
2. **Prototype Development** (Weeks 3-6)
3. **Operational Integration** (Weeks 7-10)
4. **Field Testing & Validation** (Weeks 11-14)
5. **Deployment & Training** (Weeks 15-16)

See `DEVELOPMENT_PLAN.md` for detailed objectives and deliverables.

## Target Audience

This system is designed for:
- Emergency response teams (fire, EMS, law enforcement)
- Search and rescue organizations
- Disaster relief agencies (FEMA, Red Cross, etc.)
- Community emergency response teams (CERT)
- Wildfire response teams
- Rural and remote communities
- Event coordinators requiring reliable communications

## Security & Compliance

- All intelligence reports are incident-specific (no synthetic incidents)
- OSINT document standards followed for all analysis
- Encrypted communications for operational security
- Role-based access control for sensitive data
- Compliance with ICS (Incident Command System) standards
- FEMA disaster response protocol compatibility

## Resources

- **Meshtastic Official:** https://meshtastic.org
- **Documentation:** https://meshtastic.org/docs
- **GitHub:** https://github.com/meshtastic
- **Python SDK:** https://github.com/meshtastic/python
- **Community:** Discord, Reddit, GitHub Discussions

## Contributing

This is an internal development project for Improvised Electronics. All contributions should align with:
- Civilian emergency response requirements
- OSINT documentation standards
- Incident-specific intelligence protocols
- Security and operational best practices
- ICS and FEMA disaster response guidelines

**Note:** This project is developed as a demilitarized platform. Military applications may be developed separately in the future.

## License

TBD - Consult with Improvised Electronics legal team

## Contact

Improvised Electronics
Project: MANET Development

---

**Status:** Initial Development Phase
**Last Updated:** 2025-10-28
**Next Review:** Weekly
