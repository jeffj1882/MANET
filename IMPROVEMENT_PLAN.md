# MANET — Improvement Plan (2026-07-04)

**Current state:** Docs-only scaffold, stalled for ~8 months. All 4 commits landed on a single day (2025-10-28): README, DEVELOPMENT_PLAN.md, CONTRIBUTING.md, three docs/ guides, a Claude skill, and one 117-line example script (`src/position_logger.py`). Phase 1 of the 16-week plan is incomplete — hardware was never ordered (DEVELOPMENT_PLAN.md §10 items 3-7 unchecked), the `meshtastic` Python package is not installed locally, and `incidents/` and `hardware/` contain nothing but macOS `Icon\r` junk files. The repo itself is degraded: `Icon\r` files leaked into `.git/refs/` (git prints "ignoring ref with broken name refs/heads/Icon?" warnings), `hardware/` and several `Icon\r` files sit untracked, README still points at the old `/Users/jeffjennings/Documents/MANET` path, README's structure listing claims a `CLAUDE.md` that does not exist, and `references/README.md` says the project supports "bomb disposal operations" while README.md declares it a demilitarized civilian platform.

**Goal:** Per DEVELOPMENT_PLAN.md — a functional 3-5 node Meshtastic LoRa mesh (Phase 2 deliverable) with encrypted channels, Python-automated position/status reporting, and range-test documentation, aimed at civilian emergency response / SAR / community preparedness.

## P0

**Revive-or-archive decision** — Files: `/Users/jeffjennings/Projects/MANET/README.md`, `/Users/jeffjennings/Projects/MANET/DEVELOPMENT_PLAN.md`
The 16-week plan expired ~8 months ago with zero hardware acquired. Decide once, then execute one branch:
- *Revive steps:*
  1. Order 3× Heltec WiFi LoRa 32 V3 (~$35 ea) or 2× LilyGO T-Beam Supreme + 1× Heltec, per `/Users/jeffjennings/Projects/MANET/docs/HARDWARE_SELECTION.md` (use the `/ie-logistics` skill's electronics-distributor patterns for sourcing).
  2. `python3 -m venv /Users/jeffjennings/Projects/MANET/.venv && .venv/bin/pip install meshtastic` and commit a `src/requirements.txt` pinning `meshtastic` and `pypubsub`.
  3. Rewrite DEVELOPMENT_PLAN.md §2 phase dates: Phase 1 completion = hardware in hand; Phase 2 = 3-node bench mesh + `position_logger.py` run against real serial hardware.
  4. Update the `**Status:**` / `**Last Updated:**` / `**Next Review:**` block at the bottom of README.md (currently 2025-10-28 / "Weekly" — both false).
- *Archive steps:*
  1. Add a one-paragraph "Status: PARKED — no hardware acquired; docs remain valid as a Meshtastic starter framework" banner at the top of README.md.
  2. `gh repo archive jeffj1882/MANET` (after pushing the cleanup below).
  3. Note the parked state in `~/.claude/projects/-Users-jeffjennings/memory/MEMORY.md` so future portfolio reviews skip re-assessment.
- Acceptance: README.md status block reflects reality (either new phase dates or PARKED banner), and either a hardware order confirmation exists or the GitHub repo shows as archived.

**Repair broken git refs from `Icon\r` pollution** — Files: `/Users/jeffjennings/Projects/MANET/.git/refs/Icon\r`, `.git/refs/heads/Icon\r`, `.git/refs/remotes/Icon\r`, `.git/refs/remotes/origin/Icon\r`, `.git/refs/tags/Icon\r`
1. `cd /Users/jeffjennings/Projects/MANET && find .git/refs -name $'Icon\r' -delete`
2. `git fsck` to confirm no remaining broken names.
3. Verify `git branch -a` no longer prints "ignoring ref with broken name" warnings.
- Acceptance: `git status` and `git branch -a` run warning-free; `git fsck` reports no broken refs.

## P1

**Purge and block macOS `Icon\r` litter repo-wide** — Files: `/Users/jeffjennings/Projects/MANET/.gitignore`, plus `Icon\r` files in repo root, `.claude/`, `.claude/skills/`, `docs/`, `hardware/`, `incidents/`, `references/`, `src/`
1. `find /Users/jeffjennings/Projects/MANET -name $'Icon\r' -not -path '*/.git/*' -delete`
2. Append `Icon\r\r` handling to `.gitignore` (literal line: `Icon?` on its own line, which git matches against `Icon\r`).
3. `git add .gitignore && git commit -m "chore: ignore macOS Icon files"` and push.
- Acceptance: `git status --short` shows no `Icon` entries; re-opening the folder in Finder does not re-dirty the worktree.

**Resolve the civilian-vs-EOD scope contradiction** — Files: `/Users/jeffjennings/Projects/MANET/references/README.md` (lines 3, 11-13: "bomb disposal operations", "HDS training references", "Bomb disposal operational procedures"), `/Users/jeffjennings/Projects/MANET/README.md` (line 124 "demilitarized platform" note)
1. Pick the actual scope. Given IE's business (EOD training) the likely intent is dual: keep the public repo civilian-framed, move EOD/HDS references out.
2. Edit `references/README.md` to drop the bomb-disposal framing (or, if EOD is the real scope, update README.md line 124 and the Target Audience list instead — one direction, not both).
3. Same commit: fix `references/README.md`'s quote of a "CLAUDE.md" that doesn't exist (see next task).
- Acceptance: `grep -ri "bomb disposal\|HDS" /Users/jeffjennings/Projects/MANET --include='*.md' -l` returns nothing (or, if EOD scope chosen, README.md no longer claims demilitarized).

**Create the missing CLAUDE.md or remove references to it** — Files: `/Users/jeffjennings/Projects/MANET/CLAUDE.md` (absent), `/Users/jeffjennings/Projects/MANET/README.md` (line 26 lists it in project structure), `/Users/jeffjennings/Projects/MANET/references/README.md` (quotes it)
1. Write a short CLAUDE.md: project scope, "check references/ before each task" rule, pointer to `.claude/skills/manet.md`, and the Meshtastic SDK version pin.
2. While in README.md, fix the stale path on line 68: `cd /Users/jeffjennings/Documents/MANET` → `/Users/jeffjennings/Projects/MANET` (Documents projects were migrated to ~/Projects on 2026-06-17).
- Acceptance: CLAUDE.md exists; `grep -n "Documents/MANET" README.md` returns nothing.

**Track or delete the empty `hardware/` and `incidents/` directories** — Files: `/Users/jeffjennings/Projects/MANET/hardware/`, `/Users/jeffjennings/Projects/MANET/incidents/`
1. If reviving: add `hardware/README.md` (device inventory table: model, MAC, firmware version, role, antenna) and `incidents/README.md` (report naming convention per the OSINT standards CONTRIBUTING.md references) so the dirs are git-tracked and self-documenting.
2. If archiving: `rmdir` both after Icon cleanup and remove them from README.md's structure diagram.
- Acceptance: `git ls-files hardware/ incidents/` shows the READMEs (revive) or the dirs are gone from disk and README (archive).

## P2

**Harden `position_logger.py` for field use** — Files: `/Users/jeffjennings/Projects/MANET/src/position_logger.py`
1. Add `argparse` for `--port` (serial device path) and `--output` instead of hardcoded `OUTPUT_FILE = "mesh_positions.json"` at line 17 — it currently writes to whatever CWD the script runs from.
2. Replace the full-file rewrite on every packet (`save_positions()` called inside `on_position`, line 69) with an append-only JSONL log or a periodic flush — the current pattern loses history (dict keyed by node overwrites prior fixes) and hammers flash on a Pi base station.
3. Guard `interface.myInfo.my_node_num` access in `on_connect` (line 74) — `myInfo` can be None before node info arrives.
4. Remove emoji from print output (ASCII-only, consistent with the Alarm Board Pro convention).
- Acceptance: `python3 src/position_logger.py --help` shows port/output flags; a simulated two-position sequence from the same node preserves both records in the output log.

**Add message/status reporting script (Phase 2 deliverable)** — Files: new `/Users/jeffjennings/Projects/MANET/src/status_reporter.py`, `/Users/jeffjennings/Projects/MANET/docs/QUICK_REFERENCE.md`
1. Implement the "Python scripts for automated status reporting" task from DEVELOPMENT_PLAN.md Phase 2 (§2, line 64): periodic node health broadcast (battery, SNR, hop count) + received-message logger, reusing the pubsub pattern from `position_logger.py`.
2. Add a usage section to `docs/QUICK_REFERENCE.md`.
- Acceptance: script runs against a connected node and logs a status line per interval; documented in QUICK_REFERENCE.md.

**Range-test documentation template** — Files: new `/Users/jeffjennings/Projects/MANET/docs/RANGE_TEST_TEMPLATE.md`
1. Create a fill-in template capturing the DEVELOPMENT_PLAN.md §7.1 metrics: distance, environment (urban/rural), antenna, SNR/RSSI, delivery %, hop count, battery draw.
2. Reference it from DEVELOPMENT_PLAN.md Phase 2 deliverables when that file is next edited.
- Acceptance: template exists with all §7.1 metric fields; first bench test (2 nodes, same room) recorded as a worked example.

## Quick wins (<30 min)

**Delete broken `Icon\r` git refs** — Files: `.git/refs/**/Icon\r` — Steps: the two-command fix from P0 task 2. Acceptance: no git warnings. (~5 min)

**Fix stale `Documents/MANET` path in README** — Files: `/Users/jeffjennings/Projects/MANET/README.md` line 68 — Steps: 1. Edit path to `~/Projects/MANET`. 2. Commit. Acceptance: grep clean. (~5 min)

**Gitignore + delete Icon files** — Files: `.gitignore` + 8 `Icon\r` files — Steps: per P1 task 1. Acceptance: clean `git status`. (~10 min)

**Push local main** — Files: n/a — Steps: after the above commits, `git push origin main`. Acceptance: `git status` shows branch up to date with origin/main. (~2 min)

## Out of scope

- Phase 3+ deliverables: iOS/Android client apps, GPS incident-mapping system, FEMA/ICS workflow integration — pointless until a physical 3-node mesh exists.
- Military/EOD variant of the platform (README explicitly defers this to a separate future project).
- License selection (README says "consult legal") — business decision, not an engineering task.
- LoRa frequency-regulation research beyond US 915 MHz ISM — only relevant if deployments leave the US.
