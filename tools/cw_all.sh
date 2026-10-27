#!/bin/sh
# Rebuild the Chariot Wars catalogues on top of a finished output folder and run the whole post-processing chain for them.
# Usage: sh tools/cw_all.sh <outdir>   (outdir already contains the rulebook and Hannibal catalogues; the chain is idempotent for them)
OUT=${1:-.}; T="$(dirname "$0")"
python3 "$T/cw_build.py" "$OUT" || exit 1
for s in add_unit_upgrades replace_options_to_unit profile_swaps equip_defs mount_profiles equip_save collapse_forces light_troops cw_limits prereq_min excl_hide compose_first rules_limits req_notes sv_stat crew_merge elephant_count loadout_split; do
  python3 "$T/$s.py" "$OUT" || exit 1
done
python3 "$T/lint_wab2.py" "$OUT" | tail -2
