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
- Not built here: the Alexander the Great, Byzantium and Siege & Conquest supplements, and the 97 unbuilt AoA2 lists.
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

## Rulebook check against the clean scans (WAB2 Edit_1/Edit_2)
The two 85-page scans in the Dropbox folder (rules chapters, special rules, reference pages and templates; no army lists) were OCRed and compared with the game system: all 22 rulebook special rules, the missile weapon table, the weapon and armour text, the armour save and encumbrance logic. One difference was found and fixed: Fear point 4 reads "a unit DEFEATED in hand-to-hand combat is automatically broken if outnumbered by a feared enemy" (it said "engaged"). Light Troops now carries the book's "must fight as one or the other for the whole battle" sentence.

## Cross-unit limits (Hannibal) — `tools/hannibal_limits.py`
Enforced as validation constraints (New Recruit shows a warning when broken):
- Unit ratios: Carthaginian Spanish Caetrati ≤ Spanish Scutarii units; Oscan Hoplites ≤ Oscan Warriors units; Ballista ≤ Citizen/Levy/Trained African units; Balearic/Ligurian/Sardinian/Moorish skirmishers ≤ Skirmisher units; Roman Principes ≤ Hastati (+Raw) units; Triarii ≤ Principes units (one per two Principes once Velites are present); Spanish Caetrati ≤ one per two Scutarii units.
- Minimums: Triarii at least 1; Leves at least 1 in the First Punic War and Second Punic War in Spain/Italy unless Velites are taken.
- Figure caps: Numidian Trained Infantry and Imitation Legionaries ≤ Warriors figures; Gallic Fanatics ≤ Warrior figures and need a Chariots unit; Italian Extraordinarii and Spanish Caetrati unit size ≤ Spearmen / Scutarii figures.
Not enforceable in New Recruit (check by hand): "may not outnumber any other cavalry unit", "may not be the largest skirmisher unit", and "smallest unit" comparisons when several comparator units exist (the sum of their figures is used, so these are lenient).

## Allies and optional rules (not built in)
Allied contingents and the Hannibal optional rules (Pikes, Mercenaries, Fortified Camp, Penal Legions, Amphibious Caetrati, Sertorius revolts, Numidian Imitation Legionaries as an army-wide option) are not modelled as pick-lists. To field allies, build a separate small roster from the allied army's own catalogue and treat it as the allied contingent, applying the allies limits from the book by hand (Roman p.61, Carthaginian p.26). Imitation Legionaries are available as a normal Numidian unit.

## Added: Chariot Wars (Warhammer Historical)
Seven catalogues, transcribed from the book's army lists (book page = PDF page - 2) and checked row by row against the page images: `Sumerian_Akkadian_Chariot_Wars.cat` (pp.6-11), `Egyptian_New_Kingdom_Chariot_Wars.cat` (pp.12-18), `Hammurabic_Babylonian_Chariot_Wars.cat` (pp.19-24), `Hittite_Chariot_Wars.cat` (pp.25-32, also Hurrian/Syrian/Canaanite/Phoenician), `Trojan_War_Chariot_Wars.cat` (pp.41-46, Mycenaean/Minoan/Trojan), `Israelite_Chariot_Wars.cat` (pp.47-52) and `Assyrian_Chariot_Wars.cat` (pp.53-61). The book's Assyrian Task Force and Babylonian Rebel Force pages are scenario examples, not army lists, and are not built.
- Build: `sh tools/cw_all.sh <outdir>` runs `cw_build.py` (data in `cw_data.py`), the equipment/save/encumbrance chain, `collapse_forces.py`, `light_troops.py` and `cw_limits.py`. The game system is now revision 5 (all catalogues reference it).
- Compositions: each list has its own percentage limits (Hittite requires at least 25% Chariotry; Trojan, Israelite and Assyrian allow up to half Chariotry/Cavalry; Babylonian, Hittite, Trojan, Israelite allow up to half Allies & Mercenaries). The Army composition picker appears only for the Assyrian Empire list, which can be taken as an Assyrian or a Babylonian army: Assyrian-only units (Four-horse Heavy Chariots, Assyrian Cavalry, Qurubuti, Assyrian Kisir Sharruti Infantry, Heavy Slingers, Urartians) and Babylonian-only units (Babylonian Cavalry and Infantry, Elamites, Medes, Hoplites) fail validation in the other; Assyrian Terror and Highly Professional apply to Assyrian armies only (text on the rules).
- Enforced as validation constraints: chariot units of at least 3 models; 0-1 General across alternative generals (King/Prince, Lugal/King, Pharaoh/General, etc.); Hittite 0-1 cavalry unit (Scout or Successor); Israelite Sacred Ark instead of the Army Standard Bearer and only without Chariots; Hammurabic Chariot Runners up to one unit per Chariots unit; the Mounted Scouts minimum of three.
- Rules defined from the book: the common rules (pp.3, chariot characters, chariot runners, mixed weapons, throw sticks), Onager Chariots, Egyptian Charioteers, Chariot Archers, Mounted Archers, Amorite Chief, Vassal King, Legendary Warriors, Sacred Ark, Camels, Elamite Chariots, Heavy Slingers, Mule Carts and the Chariot Wars Phalanx. Warband "psychology rules 1 & 2" is its own rule (not the full Warband rule).
- Not enforced (documented only): Chariot Runners per Chariots unit for the Egyptian and Hittite lists (earlier periods may use them without chariots), Mounted Scouts not exceeding the number of characters, Archers mixed into Trojan spearmen (1 in 4), the Sumerian Army Standard Bearer accompanying a Royal Guard or Spearmen unit, allies and the Chaldean variant options as a unit-mix choice.

## Added: Fall of the West (Warhammer Historical, 2002)
Three catalogues from the book's Army Selection (book pp.44-48; special rules p.58; checked against the page images): `Late_Roman_Fall_of_the_West.cat`, `Late_Barbarian_Fall_of_the_West.cat` and `Warlord_Fall_of_the_West.cat`. Build with `sh tools/fw_all.sh <outdir>` (data in `fw_data.py`, `fw_build.py`, then the usual chain and `fw_limits.py`). The game system is now revision 7.
- Compositions: Roman picker (Limitanei, Comitatenses), Barbarian picker (Sea Raiders, Western, Central, Eastern, North African); Warlord has none. Percentages are by points as printed (Roman cavalry 20-60% in Limitanei, 20-50% in Comitatenses; Sea Raiders no cavalry; Western cavalry up to 20%, Central 40%, Eastern/North African 100% with infantry up to 25%).
- Enforced: Palantina not in Limitanei; Steppe and Noble Steppe Cavalry only in Central and Eastern Barbarians; North African Camelry only in the North African army; Comitatus only with a Barbarian Warlord; Militia or Bacaudae have no Standard bearer or Musician option; Steppe and Noble Steppe Cavalry together up to 20% of the army in the Central list (half of the 40% cavalry allowance; a flat cap, so it is lenient when less cavalry is taken); Warlord army takes one General (Roman Army General or Barbarian Warlord); 0-1 General/Standard/Warbanner/Priest, 0-2 Heavy Shock Cavalry, Noble Steppe Cavalry and Currus Drepanus.
- Rules from p.58 are defined (Lassoes, Barbarian Cunning, Nomad Cavalry, Shield Wall, the revised Mixed Weapons), plus Comitatus Oath, Priest, Heavy Shock Cavalry, Currus Drepanus.
- Roman artillery (Scorpio, Ballista, Tormenta) is copied from the rulebook Roman list (pp.179-181) into the Late Roman and Warlord Special Units (up to 25% of points). Tormenta: one per two bolt shooters, worked out as 2 x Tormenta <= Scorpio units + Ballista units (a self-referencing modifier; untested in New Recruit). Not enforced: the rulebook's "no more special units than legionary and auxiliary units" rule.
- Skirmish formation: Pedes, Palantina and Veterans (Roman) and Warriors (Barbarian) have a free "Skirmish formation" option that links Light Troops, turns off the other equipment options, swaps Large shield and throwing spear for Shield and Javelin and sets the Roman save to 6+. Only one Pedes unit and one Warrior unit may skirmish; Palantina and Veterans are unrestricted.
- One soldier in four may take a bow: Pedes, Palantina and Veterans have a separate Archer model (+1 pt over the base model, light armour and drilled still apply) capped at one archer per three regular models, i.e. one in four of the unit. A unit still needs five regular models.
- Not modelled: the Skirmish scenarios, campaigns and Order of Battle sections are not army lists and are not built.

## Added: Armies of Antiquity (Warhammer Historical, 1999)
Twenty-two catalogues named "(Armies of Antiquity)", one per army list, transcribed from the page images (book page = pdf page - 2): Sumerian, Egyptian, Hittite, Trojan War, Assyrian, Persian (Achaemenid), Ancient Greek, Alexander & Successors, Ancient Indian, Republican Roman, Carthaginian, Late Roman, Cataphract, Byzantine, Nomadic Hordes, Arabs & Saracens, Saxon, Viking, Normans, Crusaders, Ancient Chinese and Samurai. Files are `<List>_Armies_of_Antiquity.cat`. Build with `sh tools/aoa_all.sh <outdir>` (data in `aoa_data.py`, `aoa_build.py`, the usual chain, then `aoa_limits.py` using the helpers in `limlib.py`). Where a list overlaps a Chariot Wars, Hannibal or later list it is built anyway, as its own catalogue.
- Compositions: one fixed composition per list with the percentages by points as printed (a single "Army" force; no picker). Quality tiers printed as one row (Late Roman Guard / Comitatense / Limitanei, Cataphract Guard / Levy / Militia, Saxon Select Fyrd / Fyrd, Crusader Secular / Military Order, and so on) are separate units.
- Enforced: Egyptian Chariot Runners, Persian Guard Cavalry, Greek Theban/Thessalian/Thracian cavalry, Alexander Elite Light Cavalry and Saxon Select Fyrd limited to the number of the matching parent units; Nomadic Noble Cavalry figures at most one third of the horse archer figures; Chinese war machines up to one per Halberdier or Spearman unit (per machine type) and no Heavy Cavalry (cataphracts) together with Heavy Chariots; Alexander Royal Guard Phalanx not with Hypaspists, and Indian and African elephants not together; Crusader Military Order foot only with Military Order knights; Greek units have no standard bearer option (Oracles) and the Sacred Band option may be taken once in the roster.
- Points-based limits ("one per 500 / 1,000 points"): artillery, scythed chariots, war wagons and elephants have a maximum of floor(roster points / 500 or 1,000), reduced by the other units that share the allowance. The roster points total includes the unit being added, so it is slightly lenient. This uses a repeat on the roster points cost and has not been tested in New Recruit.
- Rules defined from the book: Hittite Three-man and Hurrian Chariots, Warriors of Legend, Terrifying Reputation, Highly Professional, Spara, Parthian Shot, Feigned Flight, Expert Horsemen, Nomad Cavalry, Wedge Formation, the Phalanx, Warband psychology rule 1, the Carthaginian Allies & Mercenaries test, both Shield Walls, Cataphracts, Strategicon, Bedouin and Turkish Cavalry, Saxon Huscarls, Beserkers, Ferocious Charge, Honourable, Katana (with Samurai armour, naginata and sashimono), Warrior Monks' dodge, Ninja scouts and Samurai Peasants. Reused from earlier books: Army General, Army Standard, Drilled, Stubborn, Warband, Onager Chariots, Egyptian Charioteers, Chariot Runners, Chariot Archers, Heavy Slingers, Camels.
- Not enforced (documented in each catalogue's List Notes): allies from other lists (build a separate small roster), combined formations (archers or crossbowmen in the same unit as spearmen, Late Roman and Byzantine cataphract archers), Beserkers per Huscarl unit, artillery not exceeding the number of infantry units (Cataphract, Byzantine), the Persian Levy spara at +1/2 pt (entered as +1 pt), the Crusader requirement for two Military Order knight units, "must have a General" (Norman, Chinese, Samurai), Samurai Hero 0-7 and Characters 25% (enforced as a unit limit and a percentage), Sashimonos, Late Roman Craig Davey Guard option, mixed weapons within a unit, and Appendix One's optional new game rules.
- Printed values worth checking: Byzantine General and Standard Bearer print Movement 8 (entered as 4, with the warhorse as an option); Cataphract Skirmishers print Movement 8 (entered as 4); Indian Standard Bearer light armour printed as an extra cost although it is base equipment (entered as the heavy armour upgrade).
- Not built: Appendix Two (the Praetorian Guard and the Frankish, Gallic and other tribal variants of the Barbarian list) and the Enemies of Antiquity table; they modify lists that are already built.

## Added: Shieldwall (Warhammer Historical, 2002)
Six catalogues named "(Shieldwall)", one per race, each with an **Army composition** picker for the kingdom: Northmen (Norwegians, Danes, Hiberno-Norse, Orkneyinga, Kingdom of the Isles), English (Wessex, Mercia, Northumbria, Anglia, Kent & the Home Counties), Caledonians (Dal Riata, Alba, Picts, Scotland, Strathclyde), Welsh (Gwynedd, Powys, Southern Kingdoms, Dumnonia), Hibernians (Munster, Leinster, Connacht, Ulster) and Western Franks (Carolingian French, Flanders, Normandy, Bretons, Capetian French). Files are `<Race>_Shieldwall.cat`. Build with `sh tools/sw_all.sh <outdir>` (data in `sw_data.py`, `sw_build.py`, the usual chain, then `sw_limits.py`). Page numbers are the printed book pages. The Dogs of War mercenaries (pp.77-79) are built as units inside each catalogue and are available only in the compositions that may select them.
- Enforced: the percentages by points per composition; which units, mercenaries and options each kingdom may use (options that exist in only some kingdoms are hidden otherwise); one General (Konnungr or Jarl, Cyning or Eorl) and 0-1 units; Army Standard Bearer options once per army; Berserkers at most one group per unit of Hirdmen; no more units of Hirdmen than Bondir (Orkneyinga and Isles); English Characters 25% instead of 33% when the army includes Huscarls; per-kingdom costs and characteristics (Flanders Milites and Liberi, Normandy/Bretons/Capetian mounted Milites, Breton BS 4, Men of the Marches Ld 7). Caledonian and Frankish Common/Uncommon pools differ between kingdoms, so those units also sit in pool categories (for example "Common Warriors: Milites and Pueri") that carry the percentage.
- Rules defined from the book: the common rules (pp.4-5: Shieldwall, Cavalry Counter Charges, rank bonuses & difficult terrain, reforming in combat, Fall Back in Good Order, mounted models), Fury of the Norsemen, Werod, Warband psychology rule 2, Berserkers, Godi, English Army General, Combined Units, Huscarl Hatred, Veterans (Wessex), Abbod, Offeiriad, Bishop, Jomsviking Bribe, Unreliable Mercenaries, Mercenary Rally, Raiders, Choice of Terrain (Welsh) and Hibernian Ambush.
- The Danes (p.9) were added from a photographed page supplied separately. Not built: Narrative Campaigns and the optional rules (p.90).
- Not enforced (documented in the List Notes): mixed weapons within a unit (Different Weapons), bow-armed Bondir not exceeding other Bondir, no more than half of the Geburs bow-armed, "every other unit" of Doer-chele/Priodaur/Bonnedig/Pueri/Liberi may take bows, at least half of the Southern Kingdoms' Priodaur bow-armed, the Wessex limit on mounted Thegns against dismounted Thegns, the Righ always accompanying the Toisech, combined Huscarl/Thegn/Ceorl and Gebur units, Hibernian Ri Tuathe as General only without a Ri Ruirech, Dumnonian poisoned javelins, the Capetian charge die, and allies (build a separate small roster).
- Printed values worth checking: the Gasraidh and the dismounted Stipendarii rows print one value fewer than the table header (Toughness 3 entered); the Devroet print M4 although mounted on warhorses (M8 entered); Coloni and Cottereaux equipment text mentions a buckler that is not in their printed equipment line; the Welsh Priodaur/Bonnedig/Teulu Leadership values are as printed.

## Added: El Cid (Warhammer Historical, 2007)
Three catalogues named "(El Cid)", each with an **Army composition** picker: Christian Spain (Asturias & Early Kingdoms, Age of El Cid, Reconquista), Al-Andalus (Caliphate of Cordoba, Taifa Kings, Later Taifas) and African Invaders (Almoravids, Almohads). Files `Christian_Spain_El_Cid.cat`, `Al_Andalus_El_Cid.cat`, `African_Invaders_El_Cid.cat`. Build with `sh tools/el_all.sh <outdir>` (data in `el_data.py`, `el_build.py`, the usual chain, then `el_limits.py`). The Aliados y Mercenarios units (pp.54-55) are built inside each catalogue.
- Enforced: percentages by points per composition (the Common/Uncommon pools differ by composition, so units also sit in pool categories such as "Common Troops: Reconquista"); which units and options each period may use; 0-1 units; Ballesteros no more than Hidalgos plus Military Order Knights; Militia Crossbowmen no more than Peones (0-1 in the Age of El Cid); Mercenary Crossbowmen no more than Mercenary Knights; Andalusian Crossbowmen 0-1 in the Taifa Kings; at most one Army General across the Rey/Caliph/Emir and the "if no other Army General" options; no Berber Shaykh with a Christian Captain; no Imam when a Christian Captain is General; Emir/Venerable Emir 0-1 together; single Stubborn Mercenary Spearmen unit; Crusading Bishop Ld 9.
- Rules defined from the book: common rules (pp.3-4), Combined Formation, Bloodthirsty, Cantador, Bishop, Crusading Bishop, Andalusian Horsemen, Qadi, mounted light crossbow, Imam, African Drummers, Camel Riders and Aliados y Mercenarios.
- Not built: Andalusian Allies (documented in the List Notes only), campaigns and scenarios.
- Not enforced: at least half of cavalry models being Andalusian Jinetes, up to half the Jinete units with bows, up to half the Berber Spearmen units Stubborn (Almohads), mixed weapons, Aliados y Mercenarios unit led by the Army General.
- Issues and printed oddities are listed in `issues/El_Cid.txt`.

## Added: Alexander the Great (Warhammer Historical)
Eight catalogues named "(Alexander the Great)": Rise of Macedon, Alexandrian Imperial, Greek Mercenaries, Thracians (Coalition / Getic / Highland pickers), Illyrians, The End of Persia, The Frontier Horsemen and the Indian army (Classical / Mountain / Republican / Mauryan pickers). Game system revision 11.
- Enforced: percentages by points per list/composition; per-composition availability (Thracian King/Warlord, Noble/Getae cavalry, wagons, Mountain tribes; Indian chariot types, War Wagons, King/Senapati/Warlord, Bodyguards, elephants, Brahman Priests, laager wagons); 0-1 units; one General; Hypaspist/Thessalian/Prodromoi/Agrianian/Getae/Slave/escort ratios; once-per-army upgrades (Agema, Pharsalian squadron, Army Battle Standard); Mauryan Hereditary cost and stat changes.
- Rules defined from the book: common rules, Macedonian & Trained Phalanx, Alexander's Eagle, Polemarch, Rhomphaia, Rolling Wagons, The Great King, Half-Barded Armour, End of Persia scythed chariots, Indian elephants, Brahman Priest, Rathamasaula, War Wagons, wagon laager, Large Chariots and escorts.
- Not built: allies (documented only), historical characters, campaigns, scenarios and optional rules.
- Issues are listed in `issues/Alexander_the_Great.txt`.

## Added: Armies of Chivalry (Warhammer Historical, 2004)
Nineteen catalogues named "(Armies of Chivalry)": English Hundred Years War (Continental / Home), Scotland & the Borders, French Hundred Years War, Free Companies, The Low Countries, Holy Roman Empire (Early/Later x Imperial/Feudal/Clerical/City pickers), Teutonic Order, Poland, Moldavia & Wallachia, Medieval Russian States (Eastern / Western), Hungary, Ottoman Turks (Ghazi / Conquest), Last Byzantines (Nikaean / Trapezuntine / Morean / Epirote / Palaeologan), Hussites, Swiss, French Ordonnance, Burgundy, Wars of the Roses (Lancaster / York / Richard III / Henry Tudor / Yorkist Pretenders) and Italian Condotta (Early / Late). Game system revision 12.
- Mounted and dismounted troops are separate unit entries ("X (Mounted)" / "X (Dismounted)"), both counted in Cavalry. Armour classes use the existing profiles (light 6+, heavy 5+, partial plate 4+, full plate 3+ / 4+ mounted).
- Enforced: percentages by points per composition; per-composition availability; 0-1 units; one General (and Alderman/Captain/Colonello/Magister "+25 as General" if none); once-per-army upgrades (Elite, Casa, Banderium, Gewalthut, Oriflamme, Familia Ducale); flat per-unit costs (stakes, camels, Gewalthut, Captains); "one gun per N army points" limits; Knights to Noble Commanders (Poland), Skirmishers to Pikemen (Swiss) and Handgunners to Pikemen (Low Countries) ratios.
- Rules defined from the book: common rules, Impetuous, First Charge, Allies & Mercenaries, Open Order, Skirmishers, Combined Formation, Mixed Order, Medieval Phalanx, Mounted Infantry, artillery, multi-barrelled artillery, war wagons, wagon tabor, Bishop, Oriflamme, Arrogant Pride, Plançon, Noble Commander, Cantonal Standards, Mehterhane, Ghazi and others.
- Not built: allies (documented only), scenarios (Shrewsbury etc.), campaign material and optional rules.
- Issues are listed in `issues/Armies_of_Chivalry.txt`.

## Added: Spartacus (Warhammer Historical)
Three catalogues named "(Spartacus)": Spartacus's Slave Revolt (Early Revolt / Germano-Gallic Slave Army / Late Revolt pickers), Late Republican Roman Consular Army and Sicilian Slave Revolt (First Sicilian / Titus Minutius / Second Sicilian pickers). Files `Slave_Revolt_Spartacus.cat`, `Late_Republican_Roman_Spartacus.cat`, `Sicilian_Slave_Revolt_Spartacus.cat`. Game system revision 13. Build with `sh tools/sp_all.sh <outdir>`.
- Enforced: percentages by points per composition; per-composition availability; one General (Consul or Crassus; leader or Praetor as General options); Looted Light Bolt Thrower per army points; Gladiators and Bodyguard model limits per army points; once-per-army Fiery Rollers and Dogs.
- Not built: allies (documented only), scenarios, campaign.
- Issues are listed in `issues/Spartacus.txt`.

## Added: Byzantium: Beyond the Golden Gate (Warhammer Historical, 2005)
Nine catalogues named "(Byzantium)": Early Byzantines (Justinian / Heraclian), Sassanid Persians (Early / Later), Germanic Kingdoms (Vandals, Visigoths, Merovingian Franks, Ostrogoths, Gepids & Lombards), Steppe Nomads (Avars, Early and Later Khazars, Magyars, Pechenegs, Cumans), Bulgars & Slavs (Early/Later Slavs and Bulgars), Early Caliphates (Arab Conquest, Umayyad, Early and Later Abbasid, Aghlabids, Tulunids & Ikhshidids, Early Fatimid, Hamdanids), Thematic Byzantines (Isaurian & Phrygian / Macedonian), Rus (Early Pagan, Era of the Princes, Great Rus, Mongol Invasion) and Late Byzantines (Macedonian Successors / Komnenian). Files `*_Byzantium.cat`. Game system revision 14. Build with `sh tools/bz_all.sh <outdir>`.
- Enforced: percentages by points per composition; per-composition availability of units and options; per-composition cost and stat changes; one General (inherent or option); once-per-army options; unit maximums per composition; points-based limits for elephants and scythed chariots.
- Not built: allies drawn from other lists (documented only), Combined Formations, Rivalry, Stratagem, scenarios and Appendix I.
- Issues are listed in `issues/Byzantium.txt`.

## Added: Vlad the Impaler (Warhammer Historical, 2007)
Nine catalogues named "(Vlad the Impaler)": Kingdom of Hungary (Arpad & Angevin, Period of the New Men, Hungarian-Crusader), Moldavia and Walachia (Walachian Great Host, Moldavian Great Host, Small Host Army), Ottomans (Gazi State, Ottoman Empire), Serbia (Kingdom, Empire, Despotates), Return of the Bulgars, Albania, Byzantine Empire (Paleologan Byzantines, Epiros & Thessaly, Morea), Achaian Franks and the Catalan Company. Files `*_Vlad.cat`. Game system revision 15. Build with `sh tools/vlad_all.sh <outdir>`.
- Enforced: percentages by points per composition (including Crusaders, Small Host and Great Host, Kapikulu & Special Troops and Vassals as separate allocations); per-composition availability of units and options; one General (inherent or option); once-per-army options; unit maximums per composition; points-based limits for artillery, wagons and Sailors; ratios such as Imam per Iayalar and Pronija Retainers per Provincial Pronija.
- Not built: allies drawn from other lists (documented only), scenarios (pp.99-130), the optional medieval rules (Battles, Battle Leaders), sample rosters.
- Also in this commit: the Themata Army Standard Bearer heavy armour in the Byzantium catalogue was corrected to +2 pts.
- Issues are listed in `issues/Vlad_the_Impaler.txt`.
