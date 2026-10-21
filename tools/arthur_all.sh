#!/bin/sh
# Build the The Age of Arthur catalogues on top of a finished output folder and run the post-processing chain (idempotent for the other lists).
OUT=${1:-.}; T="$(dirname "$0")"
python3 "$T/arthur_build.py" "$OUT" || exit 1
for s in add_unit_upgrades replace_options_to_unit profile_swaps equip_defs mount_profiles equip_save collapse_forces light_troops arthur_limits req_notes sv_stat crew_merge elephant_count catalogue_tags; do
  python3 "$T/$s.py" "$OUT" || exit 1
done
python3 "$T/lint_wab2.py" "$OUT" | tail -2
