#!/bin/sh
# Build the Vlad the Impaler catalogues on top of a finished output folder and run the post-processing chain (idempotent for the other lists).
OUT=${1:-.}; T="$(dirname "$0")"
python3 "$T/vlad_build.py" "$OUT" || exit 1
for s in add_unit_upgrades replace_options_to_unit profile_swaps equip_defs mount_profiles equip_save collapse_forces light_troops vlad_limits figure_limits prereq_min excl_hide compose_first req_notes sv_stat crew_merge elephant_count; do
  python3 "$T/$s.py" "$OUT" || exit 1
done
python3 "$T/lint_wab2.py" "$OUT" | tail -2
