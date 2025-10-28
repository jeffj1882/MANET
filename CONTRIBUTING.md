# Contributing to MANET

This document outlines the workflow for maintaining and updating the MANET project repository.

## Repository Information

**GitHub Repository:** https://github.com/jeffj1882/MANET
**Owner:** jeffj1882
**Branch:** main

---

## Regular Update Workflow

### When to Commit & Push

Commit and push changes to GitHub after:
- Completing a development milestone
- Adding new documentation
- Creating new features or tools
- Updating hardware configurations
- Completing field test reports
- Making significant bug fixes

### Commit Message Standards

Follow this format for commit messages:

```
<type>: <brief description>

<detailed description if needed>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Types:**
- `feat`: New feature
- `docs`: Documentation changes
- `fix`: Bug fixes
- `refactor`: Code refactoring
- `test`: Adding tests
- `hardware`: Hardware configuration changes
- `incident`: Incident reports or analysis

**Examples:**
```
feat: Add Python SDK integration for device management

- Implement device discovery
- Add channel configuration helpers
- Create message sending utilities
```

```
docs: Update hardware selection guide with field test results

- Add real-world range test data
- Update battery life estimates based on testing
- Include ruggedization recommendations
```

---

## Git Workflow Commands

### Check Status
```bash
cd /Users/jeffjennings/Documents/MANET
git status
```

### Stage Changes
```bash
# Stage specific files
git add <filename>

# Stage all changes
git add .
```

### Commit Changes
```bash
git commit -m "$(cat <<'EOF'
<commit message here>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### Push to GitHub
```bash
git push origin main
```

### Pull Latest Changes
```bash
git pull origin main
```

---

## Branch Strategy

For now, we're using a simple single-branch strategy:
- **main** - Production-ready code and documentation

As the project grows, consider:
- **develop** - Active development branch
- **feature/** - Feature-specific branches
- **hardware/** - Hardware testing branches
- **docs/** - Documentation updates

---

## Development Phases Tracking

Mark progress in `DEVELOPMENT_PLAN.md` as you complete objectives:

### Phase 1: Foundation & Research (Weeks 1-2)
- Update checkboxes as deliverables are completed
- Commit when phase objectives are met
- Push to track progress publicly

### Subsequent Phases
- Follow same pattern for Phases 2-5
- Regular commits show project momentum
- Documentation of lessons learned

---

## File Organization Standards

### Source Code (`/src`)
- Python scripts for Meshtastic integration
- Configuration management tools
- Automated reporting scripts

### Documentation (`/docs`)
- Technical guides
- Hardware specifications
- Operational procedures
- Field test reports

### References (`/references`)
- OSINT materials (check .gitignore for sensitive items)
- Standards and regulations
- Training materials
- Research papers

### Incidents (`/incidents`)
- Incident-specific reports (OSINT standards)
- After-action reviews
- **Note:** Sensitive incident data should be in .gitignore

### Hardware (`/hardware`)
- Device configurations
- Firmware versions
- Antenna specifications
- Deployment diagrams

---

## Security Considerations

### What NOT to Commit

The `.gitignore` file protects:
- API keys and credentials
- Sensitive incident data
- Proprietary reference materials
- Deployed configuration details

### Before Committing
1. Review changes: `git diff`
2. Check for sensitive data
3. Ensure OSINT compliance
4. Verify no credentials included

---

## Updating the Repository - Quick Reference

**After making changes:**
```bash
cd /Users/jeffjennings/Documents/MANET
git status                          # Review changes
git add .                           # Stage all changes
git commit -m "type: description"   # Commit with message
git push origin main                # Push to GitHub
```

**To view repository:**
https://github.com/jeffj1882/MANET

---

## Project Maintenance Schedule

### Daily (during active development)
- Check for uncommitted changes
- Review any updates to Meshtastic platform
- Monitor GitHub issues (when enabled)

### Weekly
- Push completed work to GitHub
- Update DEVELOPMENT_PLAN.md progress
- Review and update documentation
- Check for new reference materials

### Monthly
- Review overall project status
- Update hardware recommendations based on new devices
- Document lessons learned
- Plan next phase objectives

### Quarterly
- Major documentation review
- Update README and DEVELOPMENT_PLAN
- Review security and compliance
- Archive old incidents/reports

---

## Collaboration Guidelines

### For Team Members
- Pull latest changes before starting work
- Create descriptive commit messages
- Document all hardware configurations
- Follow OSINT standards for incident reports
- Ask questions via GitHub Issues

### For External Contributors
- Fork the repository
- Create feature branches
- Submit pull requests with detailed descriptions
- Follow project coding and documentation standards

---

## GitHub Features to Enable (Future)

As the project grows, consider enabling:
- **Issues** - Track bugs, features, and tasks
- **Projects** - Kanban board for development phases
- **Wiki** - Extended documentation
- **Discussions** - Community Q&A
- **Actions** - CI/CD for testing

---

## Contact

**Project Lead:** jeffj1882
**Organization:** Improvised Electronics
**Repository:** https://github.com/jeffj1882/MANET

---

**Version:** 1.0
**Created:** 2025-10-28
**Last Updated:** 2025-10-28
