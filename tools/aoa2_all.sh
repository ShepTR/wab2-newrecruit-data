#!/bin/sh
# Build the unofficial Armies of Antiquity v2 catalogues on top of a finished output folder and run the post-processing chain.
OUT=${1:-.}; T="$(dirname "$0")"
python3 "$T/aoa2_build.py" "$OUT" || exit 1
for s in add_unit_upgrades replace_options_to_unit profile_swaps equip_defs mount_profiles equip_save collapse_forces req_notes sv_stat crew_lines elephant_count; do
  python3 "$T/$s.py" "$OUT" || exit 1
done
python3 "$T/lint_wab2.py" "$OUT" | tail -2
