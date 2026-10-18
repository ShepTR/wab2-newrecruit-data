# WAB 2.0 data set for New Recruit — pilot (4 armies)

Built from your **Armies of Antiquity v2.0 .docx** (army lists) and the **WAB 2nd Edition rulebook PDF** (weapons, armour, psychology and formation rules). Layout follows the example Warhammer Armies Project repo: one game system (`.gst`) plus one catalogue (`.cat`) per army.

## Files
| File | Contents |
|---|---|
| `Warhammer_Ancient_Battles_2.gst` | Game system: profile types, 11 missile weapons, 11 hand-to-hand weapons, 6 armour types, 8 shield/barding entries, 43 special rules, categories, and one force entry per army (variant) carrying the AoA2 composition percentages |
| `Early_Imperial_Roman.cat` | AoA2 list 44 (21 units). Early and Later Army are separate force entries |
| `Gallic.cat` | AoA2 list 12 (8 units) |
| `Parthian.cat` | AoA2 list 32 (7 units) |
| `Medieval_English.cat` | AoA2 list 92 (14 units, includes Gascon allies and the Cannon) |
| `extraction_review.txt` | For every unit: the rules, weapons and "+N pts" options the script detected. **Review this.** |
| `tools/` | The build and lint scripts, so the remaining 97 lists can be generated the same way |

## How to use
1. Choose the force entry matching the army (e.g. "Gallic", or "Early Imperial Roman - Later Army 110 AD to 193 AD"). Its percentages are enforced against the roster points limit.
2. Add units from the matching catalogue.

## Checks done
- All files are well-formed XML, 1,142 ids unique, all 346 links resolve (run `python3 tools/lint_wab2.py .`).
- Stats and points were parsed straight from the .docx tables.
- Rulebook reference data (weapons, armour, 23 rules) was transcribed from the printed Reference pages (book pp.205-212), not from OCR.

## Not yet verified
- **Not loaded in New Recruit yet.** The structure copies the example repo, but I couldn't test it here. If anything fails to load, send me the error.
- **Equipment options are auto-extracted** from the printed "(+N)" text. Labels can read oddly, and options that exclude each other (e.g. horse vs warhorse vs chariot) are not enforced. Notes as printed are on every unit under "Equipment and options (as printed in AoA2)".
- **Unit sizes are not enforced.** AoA2 gives no minimum, so troop units have min 1 model.
- **Not enforced:** "one machine per 800/1200 points" artillery limits, "0-1" limits across different units (the King and General can both be taken), and allied contingents from other lists. Allies are described in each list's "List Notes" rule only.
- **Troop-type rules are not defined as rules:** Light Infantry, Light Cavalry, Skirmishers, Open Order, Camelry, Riding Horses. Their text is still shown in the notes. AoA2's War wagons and Wagon tabor are not included.

## Source quirks to check against the book
- Gallic Standard Bearer is printed at 103 pts against the Chieftain's 90. Copied as printed.
- Parthian Horse Archers are "Nomad Horsemen"; AoA2 defines "Nomad Cavalry". Linked to Nomad Cavalry on the assumption it's a typo.
- Parthian standard bearer text reads "as a hand weapon" (likely "has").
- Medieval English "Hobilars" and similar entries' options were detected from sentence text; check the Irish Horse upgrade.

## Added: rulebook army lists (book pp.172-189)
| File | Contents |
|---|---|
| `Roman_Army_List.cat` | 15 units: Army General, Army Standard Bearer, Legate, Tribune, 3 Legionary types, 3 Auxiliary types, Scorpio, Ballista, Tormenta, Marines, Camelry. Force entry "Roman Army List": Characters max 25%, Legionaries min 25%, Auxiliaries max 75%, Special Units max 25% |
| `Barbarian_Army_List.cat` | 12 units: Warlord, Battle Standard, Shaman, Chieftain, Warriors, Fanatic Warriors, Chariots, Noble Cavalry, Light Cavalry, Skirmishers, Mountain Tribesmen, Warhounds. Force entry "Barbarian Army List": Characters max 33%, Warriors min 33%, Cavalry and Chariots max 33%, Supporting Infantry max 33% |

Troop stats and points were transcribed by hand from the page images. Warhorse stats, the tribal variants (Gauls, Germans, Dacians, Ancient Britons, p.189) and the Roman allies rule are text only in each list's "List Notes" and are not enforced. Troop units have a 5-model minimum. Options are not mutually exclusive. Re-run with `python3 tools/rb_build.py .` after build_wab2.py.

## Source status
- **Official:** `Roman_Army_List.cat`, `Barbarian_Army_List.cat` (WAB 2nd Edition rulebook) and all rulebook reference data in the .gst.
- **Unofficial (AoA2 .docx, fan-made):** `Early_Imperial_Roman.cat`, `Gallic.cat`, `Parthian.cat`, `Medieval_English.cat`. Kept as a pilot, to be replaced by official lists. The other 97 AoA2 lists are deliberately not built.

## Added: Hannibal & the Punic Wars (Warhammer Historical, 2005)
Official supplement, written for the earlier WAB rules (before the 2010 2nd Edition rulebook). Lists, stats and points were transcribed by hand from page images (book pp.20-27, 51-62, 70-81, 106-109).

| File | Contents | Force entries (percentages enforced) |
|---|---|---|
| `Carthaginian_Hannibal.cat` | 37 units | First Punic War; 2nd Punic War in Spain, in Italy, in Africa; Third Punic War |
| `Republican_Roman_Hannibal.cat` | 34 units | First Punic War; 2nd Punic War in Spain, Italy; 2nd and 3rd Punic Wars in Africa; Campaigns in the West; Campaigns in the East |
| `Spanish_Hannibal.cat` | 13 units | Iberians, Celtiberians, Lusitanians |
| `Numidian_Hannibal.cat` | 10 units | Numidian |
| `Ligurian_Hannibal.cat` | 9 units | Ligurian |
| `Gallic_Hannibal.cat` | 8 units | Gallic |

All force entries are named "Hannibal: ...". The .gst also gained a Hannibal publication, Phalanx / Levies / Stealth / Mixed Weapons / Mixed Armour / Manipular Unit / Unbridled Charge rules (Hannibal versions, named "(Hannibal)" where they differ from the rulebook), and "Hannibal Rules Clarifications" (summary of pp.106-109).

Notes:
- **Common / Uncommon Troops** are categories. Which units are Common or Uncommon in each war, and the "R:" restrictions, are in each catalogue's "List Notes" and are not enforced. Only the percentage limits are. Punic Heavy Cavalry has two entries (Uncommon, and "Common - Africa").
- Not enforced: "R:" restrictions, "may not outnumber" limits, 0-1 limits across units, allies, the optional rules (Pikes, Mercenaries, Fortified Camp, Penal Legions, Amphibious Caetrati beyond a +1 option).
- The Spanish and Roman lists use Infantry/Cavalry/Special categories exactly as printed; "Celtiberian Warriors" has a second Special Units entry for Iberian armies.
- Not built: the Alexander the Great, Fall of the West, Byzantium and Siege & Conquest supplements, and the 97 unbuilt AoA2 lists.
- Tools: `tools/hb_build.py` (run after `build_wab2.py` and `rb_build.py`).

## Army compositions belong to their faction
The game system has ONE neutral force, "Army" (like the example repo's "Standard"). The faction is the catalogue you pick. Composition percentages are modifiers on that force's category links: they test the primary catalogue (lists with one composition) or the required "Army composition" picker (lists with several wars/campaigns: Early Imperial Roman, Carthaginian, Republican Roman, Spanish). The picker only shows the wars of the chosen catalogue. This follows the Badab War / 40k 3rd Edition pattern and is not yet tested in New Recruit; report what you see.

Build order: `build_wab2.py`, `rb_build.py`, `hb_build.py`, then `add_unit_upgrades.py`, `collapse_forces.py` and `carth_restrictions.py` (last; replaces the obsolete `relocate_forces.py`, which put forces in the catalogues and did not scope in New Recruit).

## Leader, standard bearer and musician
Every non-character troop unit has Leader, Standard bearer and Musician as options (max one each per unit, +5 pts each, as in the rulebook and Hannibal; Roman Legionaries use a Centurion at +10). They are free for the Republican Roman Hastati, Principes and Triarii (Hannibal p.55). Added by `tools/add_unit_upgrades.py`; not added to war machines and crews, elephants or war-hound packs. If the source book prices them differently for a unit, tell me which.

## Disclaimer
Unofficial fan project, not affiliated with or endorsed by Games Workshop or Warhammer Historical Wargames. Stats, points and rules text are hand-transcribed from the books named above for use in the New Recruit army builder, and remain the property of their respective owners. You need the books to play.

## Carthaginian per-war restrictions (Hannibal pp.20-21)

`tools/carth_restrictions.py` encodes the five Carthaginian armies' unit lists. Units stay selectable but **fail validation** when they are not on the chosen war's list (an availability `max 0` constraint on each unit, relaxed by modifiers for the wars it is listed in), or when an "R:" prerequisite is missing (at least one unit of a listed type must already be in the army). Common/Uncommon tier is switched per war with category add/remove modifiers (e.g. Punic Heavy Cavalry is Uncommon in the First and Third wars, Common in Africa; the old duplicate "Common - Africa" entry is gone). Mercenary General is only valid in the First Punic War; Elephants are limited to one in Italy. Not encoded: skirmisher minimum, "may not be the largest skirmisher unit", "may not outnumber" and one-per-unit rules (see List Notes). Other armies have their own restrictions and are not covered yet. Units not on the chosen war's list are also hidden from the add list (modifier on `hidden`); units whose "R:" prerequisite is missing stay visible and fail validation. Untested in New Recruit.

## Leader / Standard bearer / Musician

These options sit on the unit entry, so the +5 (Centurion +10; free for Hastati, Raw Hastati, Principes and Triarii) is charged once per unit, not per model. `tools/move_upgrades_to_unit.py` migrated the earlier model-level versions.

## Equipment options are all-or-nothing

Every equipment option on a non-character unit ("replaces x", "may have x", armour, shields, Drilled and so on) applies to every model in the unit. They are unit-level checkboxes whose cost is the per-model cost multiplied by the number of models (`tools/replace_options_to_unit.py`). Characters keep their own per-model options. This is deliberately strict (all models armed alike); relax it for any list that allows mixed equipment.

## Equipment definitions, Armour Save and encumbrance (rulebook pp.91-98)

- `tools/equip_defs.py` rewrites the shared weapon, armour, shield and barding definitions with the rulebook wording (Shield +1 pip to the armour save, Large Shield +2, Buckler and Pavise conditions, maximum save 3+ or 2+ for barded cavalry), adds Horse, Warhorse and Encumbrance rules, and links a definition to every equipment option.
- `tools/equip_save.py` gives each model an **Armour Save** line (with a "with conditional bonuses" column for buckler, pavise, half barding and cloth barding) and reduces **M** for encumbrance (infantry with a 4+ or better save -1", cavalry with a 3+ save -1", metal barding another -1"). Both update as options are ticked. Printed M values in the lists are unencumbered, so the shown M can be lower than the printed one.
- Which models count as cavalry (extra pip) is decided by the unit or model name; see `tools/cavalry_units.txt`. Models that are skirmishers get the buckler pip against all attacks.
- Build order: ... `add_unit_upgrades.py`, `replace_options_to_unit.py`, `profile_swaps.py`, `equip_defs.py`, `equip_save.py`, `collapse_forces.py`, `carth_restrictions.py`.

## Republican Roman per-war lists (Hannibal pp.51-52)
`tools/roman_restrictions.py` (run after `collapse_forces.py`) does for the Republican Roman catalogue what `carth_restrictions.py` does for the Carthaginians: for each of the six wars/campaigns, units move between Common and Uncommon, units not on that war's list fail validation and are hidden, "R:" prerequisites (Spanish/Tarentine/Numidian Cavalry need Roman and Italian Cavalry, Gallic/Illyrian Cavalry need their infantry, East: Spanish Cavalry needs Spanish Infantry) are enforced, Leves and Velites exclude each other in Spain and Italy, and the Elephant is 0-1 and East only. Characters are unrestricted; Balearic Slingers are named in no composition and are left unrestricted; Italian Extraordinarii follow Italian Spearmen and Raw Hastati follow Hastati.

## Spanish sub-lists (Hannibal pp.70-71)
`tools/spanish_restrictions.py` (run after `collapse_forces.py`): each sub-list (Iberians, Celtiberians, Lusitanians) may only use the units the book names for it; others fail validation and are hidden. Celtiberian Warriors are Infantry for the Celtiberians and Special Units for the Iberians (one entry; the old duplicate "Special - Iberians" entry was merged). Lusitanians are limited to one unit per two Caetrati units. "No Caetrati unit may outnumber the smallest Celtiberian/Lusitanian unit" is a validation constraint (`tools/spanish_outnumber.py`): the Caetrati unit size may not exceed the models in the Celtiberian/Lusitanian units taken (exact with one such unit, lenient with several).

## Light Troops rule on units
`tools/light_troops.py` links the "Light Troops" rule (rulebook p.108) to every unit of the official lists whose text says Light Infantry or Light Cavalry (31 units), plus the units named Light Cavalry. The Numidian Elephant is skipped (its escorts are the light infantry). The unofficial AoA2 pilot catalogues are not covered.
