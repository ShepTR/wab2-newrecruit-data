<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gameSystem id="6f1f-5f84-d7e5-4889" name="Warhammer Ancient Battles 2.0" revision="1" battleScribeVersion="2.03" authorName="WAB2 New Recruit pilot" xmlns="http://www.battlescribe.net/schema/gameSystemSchema" type="gameSystem" library="true">
  <readme>Pilot data set: Warhammer Ancient Battles 2nd Edition, built from the 2.0 rulebook reference pages and Armies of Antiquity v2.0.</readme>
  <publications>
    <publication id="556c-7119-7234-b625" name="Warhammer Ancient Battles 2nd Edition" shortName="WAB2" publisher="Warhammer Historical Wargames" publicationDate="2010"/>
    <publication id="fcb9-17be-94c2-bcfc" name="Armies of Antiquity v2.0" shortName="AoA2" publisher="Warhammer Historical Wargames" publicationDate="2011"/>
    <publication id="fc9f-8438-629b-e92d" name="Hannibal and the Punic Wars" shortName="HPW" publisher="Warhammer Historical Wargames" publicationDate="2005"/>
  </publications>
  <costTypes>
    <costType id="points" name="pts" defaultCostLimit="-1" hidden="false"/>
  </costTypes>
  <profileTypes>
    <profileType id="a802-40b5-d980-cabc" name="Model">
      <characteristicTypes>
        <characteristicType id="35a2-714d-db3e-3738" name="M"/>
        <characteristicType id="bb04-2b70-ae79-3559" name="WS"/>
        <characteristicType id="ffff-54f0-d131-b6a9" name="BS"/>
        <characteristicType id="9e7c-6fc0-c50c-ee53" name="S"/>
        <characteristicType id="d226-f704-80f9-6e23" name="T"/>
        <characteristicType id="ce59-af10-7f37-4238" name="W"/>
        <characteristicType id="8ec4-e9a6-0b8a-08aa" name="I"/>
        <characteristicType id="ee87-e286-4768-82be" name="A"/>
        <characteristicType id="b6d1-0987-3a4d-d6a9" name="Ld"/>
      </characteristicTypes>
    </profileType>
    <profileType id="5de1-764d-a40b-f6b5" name="Missile Weapon">
      <characteristicTypes>
        <characteristicType id="6962-86a7-af53-83bb" name="Range"/>
        <characteristicType id="e237-5c6b-65a3-8bf7" name="Strength"/>
        <characteristicType id="b819-8576-7e60-dba3" name="Save Modifier"/>
        <characteristicType id="6282-7884-5061-ecf1" name="Notes"/>
      </characteristicTypes>
    </profileType>
    <profileType id="89ad-db9d-72f5-90d2" name="Hand-to-Hand Weapon">
      <characteristicTypes>
        <characteristicType id="fa7e-7b3b-c328-7b67" name="Effects"/>
      </characteristicTypes>
    </profileType>
    <profileType id="96b5-bd5f-9a95-1bd7" name="Armour">
      <characteristicTypes>
        <characteristicType id="80cf-4b2c-fa74-7e4d" name="Infantry Save"/>
        <characteristicType id="227d-844c-2992-a59b" name="Cavalry Save"/>
        <characteristicType id="85c2-9874-4f90-9229" name="Notes"/>
      </characteristicTypes>
    </profileType>
    <profileType id="37e2-4bc8-b9e2-0e43" name="Shield or Barding">
      <characteristicTypes>
        <characteristicType id="8e05-e350-dc3c-2a49" name="Bonus"/>
        <characteristicType id="86a0-abae-4649-7d70" name="Note"/>
      </characteristicTypes>
    </profileType>
    <profileType id="b19e-ee0c-17d1-6e33" name="Equipment and Notes">
      <characteristicTypes>
        <characteristicType id="63ac-8f60-d28a-2232" name="Text"/>
      </characteristicTypes>
    </profileType>
  </profileTypes>
  <categoryEntries>
    <categoryEntry id="44b5-a917-2fd7-20ca" name="Allies and Mercenaries" hidden="false"/>
    <categoryEntry id="5292-e765-10c8-f6e8" name="Archers" hidden="false"/>
    <categoryEntry id="3a7c-df52-a77b-1017" name="Artillery" hidden="false"/>
    <categoryEntry id="4d00-21b7-b56e-3a42" name="Cavalry" hidden="false"/>
    <categoryEntry id="d770-0479-ccc5-fa90" name="Cavalry and Chariots" hidden="false"/>
    <categoryEntry id="d087-5488-98c4-52b6" name="Characters" hidden="false"/>
    <categoryEntry id="f3a3-2277-7808-2250" name="Infantry" hidden="false"/>
    <categoryEntry id="db3d-508f-dcf6-1ae7" name="Men at Arms" hidden="false"/>
    <categoryEntry id="8c10-93c8-bc16-a231" name="Skirmishers" hidden="false"/>
    <categoryEntry id="8726-6b4a-67e5-3134" name="Auxiliaries" hidden="false"/>
    <categoryEntry id="ac7c-c389-6c7b-9f98" name="Legionaries" hidden="false"/>
    <categoryEntry id="099a-3435-f35a-fee2" name="Special Units" hidden="false"/>
    <categoryEntry id="3eca-1d1c-122a-3bef" name="Supporting Infantry" hidden="false"/>
    <categoryEntry id="ce31-a2e9-3e20-4277" name="Warriors" hidden="false"/>
    <categoryEntry id="cdbb-fd56-92b1-73b7" name="Common Troops" hidden="false"/>
    <categoryEntry id="d68a-ed84-1d75-2f64" name="Uncommon Troops" hidden="false"/>
  </categoryEntries>
  <forceEntries>
    <forceEntry id="3083-ceb0-f2dc-6449" name="Army" hidden="false">
      <categoryLinks>
        <categoryLink id="0c16-a38c-825b-8ad7" name="Allies and Mercenaries" hidden="false" targetId="44b5-a917-2fd7-20ca" primary="false"/>
        <categoryLink id="ef03-df8e-2c94-4b6e" name="Archers" hidden="false" targetId="5292-e765-10c8-f6e8" primary="false"/>
        <categoryLink id="7cff-9160-ca04-8bfa" name="Artillery" hidden="false" targetId="3a7c-df52-a77b-1017" primary="false"/>
        <categoryLink id="2320-3827-74f2-18f9" name="Cavalry" hidden="false" targetId="4d00-21b7-b56e-3a42" primary="false"/>
        <categoryLink id="e75c-23e9-d3a1-5776" name="Cavalry and Chariots" hidden="false" targetId="d770-0479-ccc5-fa90" primary="false"/>
        <categoryLink id="0a44-ce29-03ff-7291" name="Characters" hidden="false" targetId="d087-5488-98c4-52b6" primary="false"/>
        <categoryLink id="a7c2-1554-89f9-dd13" name="Infantry" hidden="false" targetId="f3a3-2277-7808-2250" primary="false"/>
        <categoryLink id="98ac-47a5-f36a-27ee" name="Men at Arms" hidden="false" targetId="db3d-508f-dcf6-1ae7" primary="false"/>
        <categoryLink id="d0a7-6ff6-d47a-83ed" name="Skirmishers" hidden="false" targetId="8c10-93c8-bc16-a231" primary="false"/>
        <categoryLink id="8c8d-664d-dc74-8456" name="Auxiliaries" hidden="false" targetId="8726-6b4a-67e5-3134" primary="false"/>
        <categoryLink id="f02d-7940-6e85-dc03" name="Legionaries" hidden="false" targetId="ac7c-c389-6c7b-9f98" primary="false"/>
        <categoryLink id="a8e3-8862-026b-da53" name="Special Units" hidden="false" targetId="099a-3435-f35a-fee2" primary="false"/>
        <categoryLink id="f7ab-21b4-fe88-a7f1" name="Supporting Infantry" hidden="false" targetId="3eca-1d1c-122a-3bef" primary="false"/>
        <categoryLink id="83f9-c4d2-ac4a-cadf" name="Warriors" hidden="false" targetId="ce31-a2e9-3e20-4277" primary="false"/>
        <categoryLink id="4e5e-e9af-badf-2093" name="Common Troops" hidden="false" targetId="cdbb-fd56-92b1-73b7" primary="false"/>
        <categoryLink id="bd11-9d43-6152-da10" name="Uncommon Troops" hidden="false" targetId="d68a-ed84-1d75-2f64" primary="false"/>
      </categoryLinks>
    </forceEntry>
  </forceEntries>
  <sharedRules>
    <rule id="6e8f-14cf-a018-5d1c" name="Allies and Mercenaries (Unreliable)" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects the start of turn.

Many armies include troops who, for various reasons, are less reliable or committed to the general’s cause than the majority. In most cases these will be allies whose loyalty lies with their own commanders, or they may be mercenary troops who fight for pay. Many a misfortune has befallen the general who didn’t pay his hirelings! A player fielding Allies and Mercenaries must throw a D6 for each such unit at the start of his first turn. On a throw of 2-6 the unit will move and fight normally without further difficulty. If a 1 is thrown, the unit refuses to obey the orders of the general, and will not move, nor shoot except at enemies charging it. It will fight as normal to defend itself if attacked. On subsequent turns the roll is repeated, until a result other than 1 is obtained.

Allies and Mercenaries cannot make use of the army general’s leadership nor of the army battle standard. They still take panic tests if the army general dies, or if units not affected by the rule break and flee from combat.

The general or other characters may sometimes be allowed by the army list to join and lead these troops.</description>
    </rule>
    <rule id="2466-e373-b854-9157" name="Ambush" publicationId="556c-7119-7234-b625" page="104" hidden="false">
      <description>1. The unit can be deployed on the battlefield in a concealed position and its location indicated on a map. It can be secretly deployed anywhere out of sight of enemy but not within the opposing deployment zone.
2. Alternatively they can deploy on the battlefield once the enemy force has taken up its position.
3. Concealed units must be placed as soon as enemy can either see them or approach within 8".
4. Concealed units ignore any tests or obligatory reactions that would otherwise result from any psychology rules.
5. Concealed units do have to take account of special rules applying from formations.</description>
    </rule>
    <rule id="32dd-5a9e-0820-caf4" name="Bow (AoA2 amendment)" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Units armed with short or composite bows can use the Massed Missiles rule as explained on p45.

Cavalry or Camelry units armed with composite bows may shoot with them during a charge or counter-charge. Any unsaved wounds so caused are counted towards combat resolution, but do not cause the usual panic test for 25% shooting casualties. All normal shooting modifiers apply, including -1 shooting while moving and -1 for shooting at chargers.

Cavalry and Camelry also armed with any melee wepon other than a hand weapon may not shoot their bows while charging or countercharging, but if their unit is a combined formation with archers in the rear ranks, these may shoot using Combined Formation rule 4 even though moving.

Mounted troops also armed with thrusting spear, kontos or lance may not shoot their bows while charging or countercharging, but if their unit is a Combined Formation with archers in the rear ranks, these may shoot using Combined Formation rule 4 even though moving.

This shooting takes place at short range unless the target flees, or the charge fails, and after shooting by the defenders. Eligible charging units that charge the flank of rear of an engaged unit may shoot but any hits are distributed between both sides following the normal rules for shooting into a combat.

Units can use massed archer to fire at a charger but skirmishing models must have line of sight.</description>
    </rule>
    <rule id="eb86-0081-b1a8-a733" name="Cataphracts" publicationId="556c-7119-7234-b625" page="104" hidden="false">
      <description>1. Cataphracts are close order cavalry.
2. Cataphracts charging or marching reduce their entire movement to half speed if they wheel.
3. Cataphracts are not permitted to countercharge as a response to an enemy charge.
4. Cataphracts armed with kontos can fight with a second rank. This bonus does not apply if Cataphracts have charged that turn.
5. Cataphracts may count a rank bonus of up to +2 when calculating combat results if they have charged into that round of combat.</description>
    </rule>
    <rule id="4afe-776a-d61e-d61d" name="Characters (AoA2 amendment)" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Characters do not take panic tests due to having fleeing friends within 4” at the start of the move.</description>
    </rule>
    <rule id="0729-4967-55df-d1aa" name="Chariot Runners" publicationId="556c-7119-7234-b625" page="105" hidden="false">
      <description>1. Chariot Runners can make formations with chariots.
2. Chariots are allowed to charge through a unit of Chariot Runners.</description>
    </rule>
    <rule id="7637-c605-27c5-0aab" name="Chariots" publicationId="556c-7119-7234-b625" page="114" hidden="false">
      <description>1. 'Number' of models = number of crew.
2. Cause fear in enemy infantry.
3. Are arranged into formed units of three or more models, scythed chariots always fight as one model, light chariots can be formed into dispersed groups similar to skirmishers.
4. Chariots are unable to move over obstacles or through difficult terrain. If forced into difficult terrain, roll a D6 per chariot: heavy/scythed chariots are destroyed on 1, 2 or 3, light chariots on a 1.
5. Scythed chariots march at basic rate +D6".
6. Scythed chariot's movement is reduced to half speed if the model moves in any fashion other than directly forward in a straight line.
7. Each missile armed chariot crewman shoots twice.
8. In combat chariot crews fight as cavalry riders in respect of weaponry.
9. Heavy and scythed chariots cause impact hits when they charge. Heavy chariots score D3 hits. Scythed chariots score D6+2 hits. If a scythed chariot rolls a 1 for its impact hits then it survives, if it rolls 2 or more it is wrecked.
10. If chariots are destroyed by pikemen before striking, they will lose the chance to fight and do not inflict impact hits either.
11. Drilled troops charged to their front can attempt to open their ranks and allow a scythed chariot to pass through. The unit must 'hold' and pass a Leadership (Ld) test. The chariot is moved through the unit.</description>
    </rule>
    <rule id="e22b-5445-d10a-9d89" name="Combined Formations" publicationId="556c-7119-7234-b625" page="105" hidden="false">
      <description>1. Formations that include close and open order troops count as close order.
2. Leadership (Ld) counts as that of the majority type or the higher value where numbers are equal.
3. The whole unit is affected by the psychology and formation rules that apply to the majority type in the unit.
4. Archers in rearward ranks may use massed missiles. The rank of archers closest to the front shoots in its entirety, with subsequent ranks shooting at half-effect.
5. Archers in rearward ranks can respond to a charge by standing &amp; shooting using massed missiles.
6. When working out hits by shooting, the saving throw of the majority is used to resolve all saves. Casualties are removed alternately from the differently armoured models, starting with the mostly poorly armed.
7. Hand-to-hand combat casualties fall amongst the type struck by the enemy.
8. Leaders, standard bearers and musicians must be removed as casualties if they are the last models of their type.</description>
    </rule>
    <rule id="627a-b7a0-2baa-599e" name="Combined Units" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Some armies form composite units with a superior troop type at the front and inferior types filling out the rear ranks. The individual army list will indicate the proportions of the two types allowable. So long as at least half the front rank figures are of the superior type, the superior leadership and saving throw applies to the whole unit. Every second missile casualty scored on the unit removes a superior figure; in combat enemy troops in base contact with the superior type must fight against them, but surplus casualties are “carried over” to the other figures.</description>
    </rule>
    <rule id="eef3-c374-e2ed-8cd9" name="Different Weapons" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Combat.

Some units may have figures armed with a variety of weapons. The normal rules apply to each weapon- so double handed axe men will hit after all other figures have struck, figures armed with throwing weapons in the second rank may strike in the first round of combat, etc. As a result of the different weapons some figures may have different armour saves than others. In close combat always use the saving throw of the majority of the front rank, when resolving missile fire use the Saving roll of the majority of the figures. Usually the owner of the unit decides which figures to remove as casualties, but the other player may elect to make attacks against specific figures if he wishes.</description>
    </rule>
    <rule id="d6b3-51b2-64eb-2b91" name="Drilled" publicationId="556c-7119-7234-b625" page="106" hidden="false">
      <description>1. Drilled troops can turn to face their left or right. It takes a quarter move to make a turn to the left or right.
2. At the beginning of their move, drilled troops can make one change formation or about face manoeuvre without penalty.
3. Drilled troops can both march and change formation in the same Movement phase.
4. Drilled troops can change formation at the start of a charge move if they wish.
5. Drilled troops can make a reform manoeuvre without taking a Leadership (Ld) test so long as there are no enemy within 8".
6. Drilled troops can choose not to pursue an enemy that breaks and flees in combat, or follow-up defeated enemy who give ground.
7. Drilled troops can disengage from combat without taking a Leadership (Ld) test so long as the enemy they are fighting do not have a faster move rate than they do.
8. Drilled units can give ground voluntarily where they pass their Break test.
9. Drilled troops are allowed to open their ranks to avoid charging scythed chariots.</description>
    </rule>
    <rule id="b932-617b-b343-5f35" name="Eastern Shock Cavalry" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>For much of our period, the art of mounted warfare was considerably more advanced outside Western Europe and cavalry were trained to perform a greater number of battlefield evolutions. Troops designated as Eastern Shock Cavalry therefore benefit from the following rules:

They gain a +1 rank bonus for a complete rank after the first in combat resolution, in a turn in which they charged or counter-charged.

They may Give Ground voluntarily if they win a round of combat, but do not break their enemy. They may do so even if they cause the enemy to Give Ground.

Eastern Shock Cavalry that take barding of any sort revert to Shock Cavalry.</description>
    </rule>
    <rule id="01f3-18f2-5b03-2aee" name="Expert Horsemen" publicationId="556c-7119-7234-b625" page="107" hidden="false">
      <description>1. Expert Horsemen do not suffer the -1 to hit penalty when moving and shooting.</description>
    </rule>
    <rule id="4544-4323-a539-1c07" name="Fear" publicationId="556c-7119-7234-b625" page="100" hidden="false">
      <description>1. Test fear against Ld (2D6) - score equal to or less than Ld to pass.
2. Test if charged by a feared enemy within range. If failed, flee if outnumbered. If not outnumbered, 6s are needed to hit in the first round/any shots from a stand &amp; shoot or fire &amp; flee response.
3. Test if attempting to charge a feared enemy as soon as the charge is declared before the enemy responds. If failed the unit may not charge and must remain stationary without shooting.
4. A unit engaged in hand-to-hand combat is automatically broken if outnumbered by a feared enemy.</description>
    </rule>
    <rule id="23ce-0721-aa10-1f4d" name="Feigned Flight" publicationId="556c-7119-7234-b625" page="107" hidden="false">
      <description>1. Can respond to an enemy charging to their front with feigned flight.
2. The unit moves directly away from the enemy exactly as if it had fled or fired &amp; fled.
3. If the unit is contacted by the charging enemy it immediately turns to fight as if it had declared a 'hold' response to the charge.
4. If the unit outdistances the charging enemy, it turns to face them at the end of its move.
5. If charged by an enemy it fears, or which terrifies it, the unit can only make a feigned flight if it first passes its Fear test.</description>
    </rule>
    <rule id="7f5f-ec12-4a6b-0e5d" name="Ferocious Charge / First Charge" publicationId="556c-7119-7234-b625" page="108" hidden="false">
      <description>1. Enemy will automatically break without taking a Break test if the ferocious chargers win the combat round following their first charge/countercharge in the game.
2. Skirmishing enemy will automatically break without taking a Break test if the ferocious chargers win the combat round following a charge/countercharge.
3. If the unit's first charge or countercharge is against skirmishing enemy, this doesn't negate the 'first charge'.
4. If the unit's first charge or countercharge breaks the enemy automatically for some other reason, this doesn't negate the 'first charge'.
5. Roll off for automatically breaks versus automatically passes rules (eg, Stubborn).</description>
    </rule>
    <rule id="2ce5-bb31-5388-d06b" name="Finest Horses" publicationId="556c-7119-7234-b625" page="107" hidden="false">
      <description>1. +1" basic Movement rate.</description>
    </rule>
    <rule id="c932-607c-fb26-8014" name="Frenzy" publicationId="556c-7119-7234-b625" page="100" hidden="false">
      <description>1. Must charge if there are enemy within charge reach when charges are declared.
2. Cannot respond to a charge by either fleeing, or by firing and fleeing.
3. Fight with +1 extra attack.
4. Must pursue.
5. Must follow-up enemy that gives ground.
6. Do not take Panic tests - immune to panic.
7. Immune to other psychology.
8. If broken in combat their frenzy is ended.</description>
    </rule>
    <rule id="c8ec-e096-68e8-216b" name="Hatred" publicationId="556c-7119-7234-b625" page="100" hidden="false">
      <description>1. Take Break tests at Leadership (Ld) value 10, applying the usual modifiers.
2. In the first round of combat re-roll misses.
3. Must pursue unless fighting from defended positions.</description>
    </rule>
    <rule id="27b0-fb8f-0353-5958" name="Levies" publicationId="556c-7119-7234-b625" page="108" hidden="false">
      <description>1. Levies fear enemy they do not outnumber by 2:1, ignoring skirmishers/fleeing troops.
2. Levies cannot make any manoeuvre other than to wheel and if they wheel their entire movement is halved.
3. Close order Levy infantry do not receive +1 combat result bonus for close order ranks.
4. Levies cannot make use of the General's leadership (Ld) value where he is within 12" of the unit.
5. Non-levy units can always re-roll a failed Panic test taken as a result of breaking levies.</description>
    </rule>
    <rule id="5be5-5832-c8fb-3a19" name="Light Troops" publicationId="556c-7119-7234-b625" page="108" hidden="false">
      <description>1. Light infantry or light cavalry can fight either as skirmishers or as open order formed units.</description>
    </rule>
    <rule id="8593-b58d-8b0f-4b05" name="Massed Cavalry" publicationId="556c-7119-7234-b625" page="109" hidden="false">
      <description>1. Massed cavalry are close order cavalry.
2. Massed cavalry charging or marching reduce their entire movement to half speed if they wheel.
3. Massed cavalry count a rank bonus of up to +2 when calculating combat results if they have charged or countercharged into that round of combat.</description>
    </rule>
    <rule id="3dcd-ef3d-8361-45a4" name="Mixed Armour" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects combat and shooting

In some formations, the front ranks were better equipped than the rear ones, so part of the unit may wear armour while the rest does not. When shot at, such a unit uses the saving throw of the better armoured troops, so long as at least half of the front rank is so equipped, while casualties are removed from the rear ranks. In combat blows are struck against the figure in contact with the striker, and the appropriate save used.</description>
    </rule>
    <rule id="0f6b-2358-57a7-2c8d" name="Mixed Weapons" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Combat.

Troops armed with mixed weapons may re-roll any failed to hit rolls once in the first round of combat. Mixed weapons are defined as being armed with a hand weapon, such as a sword, axe or short spear, and javelins, so they may shoot with these in the Shooting phase.</description>
    </rule>
    <rule id="123d-07c6-8e8c-e8db" name="Nomad Cavalry" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Deployment, Shooting and Charge Reaction.

Troops designated as Nomad Cavalry have the Expert Horseman, Parthian Shot, Feigned Flight and Special Deployment rules.</description>
    </rule>
    <rule id="5c5d-7ebc-7040-be5b" name="Oracles" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects combat.

Early Greek and Macedonian armies were prey to superstition and rituals designed to influence the Gods to favour them. To reflect this, these armies use Oracles in place of unit and army standards. Players roll a random number of Oracle points using one D6 for every 1400 points in the army. Fractions are lost, for example a 2,300 point army would roll 1D6 and a 1,500 point army would roll D6 Oracles. An Oracle point is used to affect combat and leadership and upon use, each point is deducted from the Oracle pool.

A unit may use one or two Oracle points to add up to +2 to a combat resolution result. A unit may use an Oracle point to re-roll a failed Leadership test or a failed Break test once.

Single characters, allied units (unless their army list says otherwise) and units in skirmish formation may never make use of Oracle Points.

Oracle points may never be added to combat resolution if a standard is also being counted (for example if one is carried by an allied unit).

Riding Horses/ Riding Camels

This rule affects movement

Units with this special rule arrive on the battlefield mounted, and then dismount to fight. There is no need to models the horses unless you wish to do so. Units Riding Horses may make an additional move of up to 8” as a Special Deployment move. The horses are then taken to the rear and take no further part in the battle. Units Riding Camels make an additional move of up to 6” as a Special Deployment move, and the Tethered Camels rule then applies.</description>
    </rule>
    <rule id="78a9-d49d-4efd-85c1" name="Parthian Shot" publicationId="556c-7119-7234-b625" page="109" hidden="false">
      <description>1. Only skirmishing cavalry units armed with bows, short bows or javelins can employ the Parthian Shot.
2. Troops can move up to their basic Movement rate in the Shooting phase immediately after they have shot.</description>
    </rule>
    <rule id="8703-52e8-b888-e691" name="Phalanx" publicationId="556c-7119-7234-b625" page="110" hidden="false">
      <description>1. Units must contain at least 12 models arranged at least two ranks deep and at least four wide. Frontage must exceed depth by at least one model.
2. The only manoeuvres allowed are reform and wheel.
3. Reforming is at -1 Leadership (Ld) penalty regardless of whether enemy are within 8".
4. A phalanx charging/marching reduces its entire movement to half speed if it wheels.
5. All enemy shooting against the phalanx's front suffer a -1 to hit penalty.
6. A spear-armed phalanx fights with two ranks to its front in the first round of combat if it charges.
7. Enemy cavalry or light chariots suffer -2 to hit in combat against the phalanx front, foot troops or elephants suffer -1.
8. Enemy charging the front lose any strength bonus associated with their weapons as a result of charging.
9. Enemy charging the front lose any bonuses or benefits for formation rules that apply specifically when they charge.
10. If the unit is a trained phalanx then it is allowed to make about face manoeuvres in the usual way.
11. If the unit is a Macedonian phalanx it is allowed to make about face or change formation manoeuvres in the usual way.
12. If the unit is a drilled phalanx then it combines the rules for drilled troops. A drilled phalanx can adopt any formation, can manoeuvre like any non-phalanx unit, and suffers no move penalties for wheeling whilst charging/marching.
13. If the unit is a Medieval phalanx it must have at least three ranks depth. It is allowed to make about face and change formation manoeuvres. It does not benefit from the -1 to hit from enemy missiles rule. It may reform into a stationary square, counting a maximum +1 combat result bonus for ranks.</description>
    </rule>
    <rule id="2266-7ff4-b224-e0a4" name="Rocket Artillery" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Rocket artillery have a crew of between 2 and 5 men, who prepare and hand- or ground-launch the rockets. Rocket artillery bases are 80mm deep and have a width of 20mm per crewman (i.e. a minimum width of 40mm and a maximum width of

100mm). The flight path of the rockets when fired is as wide as the firing base. To fire rocket artillery, choose a fuse length from 2-12 and throw that many D6. Add the resulting dice values to determine the length of flight. Then throw a D6 for direction; 1= 60 degrees left, 2 = 30 degrees left, 3,4 = straight ahead, 5 = 30 degrees right and 6 = 60 degrees right. At the point of landing, the explosion will engulf a circle 20mm in diameter per crewman shooting. All figures within this area are hit, and killed on a roll of 4+. There are no saving throws.

Any unit hit by a rocket strike, and any mounted units at least partially under the missiles’ flight path, must take an immediate terror test, regardless of whose side they are on.</description>
    </rule>
    <rule id="2544-dbe7-a088-2de7" name="Shieldwall" publicationId="556c-7119-7234-b625" page="112" hidden="false">
      <description>1. It takes a unit's entire move to form shieldwall.
2. A shieldwall lasts until the unit moves, or is beaten in a round of hand-to-hand combat.
3. Enemy shots/attacks to the front are at -1 to hit.
4. A unit forming shieldwall has moved for the purposes of missile fire.</description>
    </rule>
    <rule id="71de-f405-b88b-44fe" name="Shock Cavalry" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Some cavalry were notably more effective than others when charging into contact. This might be due to superior training and weapon skill, or pure élan. To reflect this, troops designated as Shock Cavalry gain a +1 rank bonus for a complete rank after the first in combat resolution, in a turn in which they charged or counter-charged.</description>
    </rule>
    <rule id="5907-6b1a-d1dc-ef0e" name="Special Deployment" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Troops with this rule, which automatically includes all Nomad Cabalry, may make a free double-pace or march move at the start of the game, at the same time skirmishers take their optional 4" move.</description>
    </rule>
    <rule id="d475-3b23-c343-2c4d" name="Stakes" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>Only formed units may place stakes. Stakes can be placed when a unit is deployed on the table to tis front only (place an appropriate marker in front of the unit). Only the unit that places the stakes can benefit from them. Stakes give the following benefits:

A unit equipped with stakes may make a free 4” move after deployment is complete and then place their stakes, if the stakes were not deployed during deployment. If not placed at the beginning of turn 1 the stakes are lost.

Mounted models fighting against the front of a unit with stakes suffers a -2 to hit modifier; and lose all bonus related to a charge (the strength bonus of their weapon due to a charge, or ferocious charge).

If a unit is subject to Warband psychology it can ignore warband rule 1 as long as it remains behind their stakes.

Stakes are lost if the unit that placed them moves out of contact with the stakes for any reason. If the stakes are lost the moarker is removed from the game.</description>
    </rule>
    <rule id="3c5c-8535-997a-4c57" name="Stealth" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Movement.

Troops with Stealth may move through difficult ground, such as woods, and obstacles at a normal pace even if formed. However, stealthy units do not retain combat rank bonuses if fighting in difficult ground or across obstacles. Stealthy units must still be able to see their foe before charging, may not march move, and must pay normal movement costs and combat penalties while charging in difficult ground or across obstacles.</description>
    </rule>
    <rule id="69c0-8262-a2f3-e536" name="Strategem" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Deployment.

A character with this special rule may do one of the following, as indicated in his list entry. If both generals have this ability, they cancel each other out and the rule does not apply.

Place one additional terrain feature anywhere on the battlefield outside the enemy deployment zone, after choosing table sides.

Move up to two terrain pieces up to 6” each. This must be done before any units are deployed. Terrain pieces cannot be moved off the table.

May choose to take the first or second turn, in scenarios where a dice roll would normally determine which player goes first.</description>
    </rule>
    <rule id="ce73-f053-8ef6-626c" name="Stubborn" publicationId="556c-7119-7234-b625" page="100" hidden="false">
      <description>1. Do not test for panic for fleeing friends within 4" at the start of the turn.
2. If they fail their Break test they will give ground once where they would otherwise flee.
3. If defeated by enemies who automatically break them, roll a D6. 1-3 the stubborn troops are broken. 4-6 the stubborn troops must take a Break test and can override a failed result by giving ground.</description>
    </rule>
    <rule id="aa68-0f62-aae8-1929" name="Terror" publicationId="556c-7119-7234-b625" page="100" hidden="false">
      <description>1. Test terror against Ld (2D6) - score equal to or less than Ld to pass.
2. Test at the start of turn if there is an enemy which causes terror within 8". If failed the unit flees. This test is only taken once.
3. Test if charged by, or wishing to charge a terrifying enemy. If failed the unit flees. This test is only taken once if infantry.</description>
    </rule>
    <rule id="6253-8439-cb87-599a" name="Tethered Camels" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This is a Psychology rule.

To deprive heavy cavalry of their most effective weapon, namely their charge, infantry of certain armies often dragged their beasts of burden with them onto the battlefield. The smell and sight of camels was foreign to many horses; they might refuse to charge such strange creatures! To show that a unit has camels, place an appropriate number of kneeling or standing camel models in base contact with the rear of a unit when it is deployed. Formed units with Tethered Camels cause Fear in enemy cavalry. If a unit with Tethered Camels charges or flees, the camel models are removed and the unit no longer causes Fear in enemy cavalry.</description>
    </rule>
    <rule id="77d7-a6a9-d7f3-b7bc" name="Used to elephants" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This is a Psychology rule.

In some armies prolonged contact or special training allowed troops to get used to elephants. The types of troops that are considered to be used to elephants are noted in their army list. Infantry that are used to elephants do not fear them, while cavalry fear them instead of being terrified of them. However, note that not even cavalry that are used to elephants are allowed to charge them, and must still flee or fire &amp; flee if charged or stampeded into.

War wagons

A war wagon is represented on the table by a single wagon, a team of 2-4 horses and six crewmen. The crewmen are carrying a mix of melee and missile weapons. If included on the model, a drover can be considered as one of the troops; no matter how many figures are depicted, only six as above are counted. If your crew models are too big to fit inside the wagon, place them alongside and count them as being inside it.

War wagons are deployed as single models counting as a 6 figure formed unit. Each war wagon may have a standard for +10pts and a leader for +5pts. War wagons may never have musicians. Single characters may join and leave single wagons. A maximum of two characters may join a single war wagon.

WAGON MOVEMENT

War wagons may not march, fast march or charge. They do not wheel but may pivot on the spot once prior to their movement. If they pivot before moving their movement distance is halved (i.e. their movement is reduced to 3’’).

They cannot cross obstacles, nor can they enter difficult ground. If forced to move into difficult or very difficult going, the wagon will instead stop at the edge without entering. War wagons cannot flee or fire and flee as a charge reaction.

Equipment: The six crewmen have a mix of melee and missile weapons (counted as halberd and war wagon shooting weapons, see below). Special Rules:

Weapons used from a war wagon are treated the same as if figures on foot used them. The missile weapons carried by three (3) of the crewmen in a medieval war wagon include a mix of crossbows and handguns and share the following statline:

WAR WAGON

 | M | WS | BS | S | T | W | I | A | Ld | Pts
Wagon | 6 |  |  |  | 6 | 4 |  |  |  | 120
Crew | 4 | 3 | 3 | 3 | 3 | 1 | 3 | 1 | 8 | 

Each crewman may fire only once during the shooting phase.

If the war wagon is present in an army from a pre-medieval period then the missile weapons are ordinary composite bows instead.

Armour saves for all crew are increased by +2 in the same way as chariot crews or figures with a large shield or pavise.

One war wagon in every three fielded may include a tarasnices (a palisade gun) for +20 pts. This works in exactly the same way as a carroballista (see page 180) and is assumed to be fired by one of the existing crew as an extra duty. That crewman may not shoot with his personal weapon during the same turn. The tarasnices may only fire from the position it is modelled on the war wagon, with a 90° angle of fire. The crew may only shoot from one of the long sides of the war wagon model, and may choose which one they will shoot from in each shooting phase.

MISSILE FIRE EFFECTS

War Wagons are Large Targets, and troops shooting at them benefit from the +1 to hit bonus as indicated on the chart page 46

 | Range | S | Save
War Wagon Shooting Weapons | 24” | 3 | -2 at short -1 at long

Hits from normal shooting are randomized between the wagon and its crew by the throw of a D6, with a score of 5 or 6 indicating a crewman is hit. A 6 indicates the hit is on a character, should one be present. A score of 14 indicated a hit on the war wagon and is simply ignored.

Hits from war machines, including artillery and multi-barrelled artillery automatically hit the war wagon itself, and are resolved normally. Note that most war machines can remove multiple wounds with a single hit, even against war wagons. War wagons don’t have any saving throws against hits inflicted by war machines.

HAND TO HAND EFFECTS

War wagon crews can attack or be attacked from every face of the model. Attacks on the wagon are resolved using the WS of the crew, but any hits are randomized as above between the crew and the wagon before rolling to wound. The wagon can be damaged by these, representing the attackers attempting to pull down hoardings, topple or disable the wagon or destroy surrounding pavises. Cavalry treat war wagons as defended obstacles (even after a war wagon has lost a round of combat) and warhorses may never attack war wagons or their crew. In a combat involving a war wagon, rank bonuses are never counted during the combat resolution. Close Order combat bonus is counted, but the war wagon does not get it. War Wagons are always considered to be 6 models strong units, even if they have lost crews.

The wagon does not have a flank or rear, is never subject to panic, and does not automatically break when reduced to less than 5 crew. However if it fails a Break Test, it is automatically destroyed and removed from play, and its loss will trigger panic tests for friendly units within 12”. Its victorious opponent does not pursue. Victorious war wagons which pursue their defeated opponents move only D6” and cannot contact a fresh enemy while doing so (they stop 1” short) but destroy the fleeing enemy unit if they catch it.

War Wagons can Give Ground if they qualify, moving back D6”.

A wagon whose crew are all killed is immediately removed from play.

If a wagon that fears its opponents is beaten in combat and would flee according to the rules for Fear, it is instead removed from play.

WAGON TABOR

Several armies used stationary wagons as defensive positions. These wagon fortresses, called Tabors, were helpful in open areas to secure the flanks of the army.

Wagon deployment

The Wagon tabor is composed of any number of wagons, deployed on the table prior to the army deployment. All wagons must form a line with one end touching the owning player table edge, and the wagons forming wagon tabor may be up to 3’’ apart.

The whole tabor must be deployed within the boundaries of the owning player deployment zone.

Defender Deployment

The defenders for each wagon are a separate unit of up to 10 models that may not have a leader, standard or musician. The profile and cost of the defenders is listed in the army list. If no profile or entry for them or the wagons have been given in the army list, use the following generic entry:

WAR WAGON

 | M | WS | BS | S | T | W | I | A | Ld | Pts
Wagon |  |  |  |  | 6 | 4 |  |  |  | 15
Defenders | 4 | 2 | 3 | 3 | 3 | 1 | 2 | 1 | 7 | 6

Equipment: The defenders are armed with hand weapons, bows and light armour. The bows may be replaced by thrusting spears or throwing spears.

The defenders are placed in contact with the wagon. They count as being inside the wagon they are defending (models are placed outside for practical reasons only), and may not leave it voluntary, but may leave as a result of fleeing or pursuing after a failed Leadership test to hold. Wagon defenders can attack and be attacked from all facing.

When they have left their wagon, the defenders are considered to form a skirmishers unit. Unless their wagon has been removed, they must move toward their wagon and occupy it again as soon as possible. They may never declare a charge.

Movement

A Wagon Tabor may not move after deployment.

Wagon Tabors are obstacles to movement and mounted unit may not cross through them. Units on foot may cross through unoccupied wagons, which count as very difficult terrain.

Shooting

Missile armed defenders fire once as if on foot. The wagon tabor is not a large target for shooting. It may shoot all round like crew on an elephant or chariot.

When shooting at a Wagon (except with a war machine or artillery), the defenders count as being in hard cover. Armour Save for Wagon Tabor defenders is increased by +2 in the same way as chariot crews against shooting and melee attacks.

If shooting at a wagon with artillery or a war machine, resolve any hit against the toughness and wounds of the wagon. If the wagon is reduced to zero wounds it is removed from play, and the defending unit is deployed where their wagon was and must take an immediate Panic test.

Combat Effects

In close combat, the Wagon Tabor defenders always count as being behind a defended obstacle, even if they have lost a previous round of combat. Wagon Tabor defenders do not have flanks or rear, and may fight in hand to hand combat with a maximum of five figures for each engaged facing.

An enemy unit may attack an unoccupied wagon. All hits aimed at the wagon hit automatically. When reduced to zero wounds, the wagon is removed from the table.

Victory

For army break points and victory points the whole wagon tabor counts as a single unit. If half the defender models have been removed, the unit counts as being at half strength (and give half their value of victory or army break points). You must eliminate all defenders of the wagon tabor to claim their full value of victory or army break points.</description>
    </rule>
    <rule id="4c9b-509e-486d-f0af" name="Veteran" publicationId="556c-7119-7234-b625" page="112" hidden="false">
      <description>1. Once in the battle, the unit can re-roll all of its 'to hit' dice for either shooting or hand-to-hand combat.</description>
    </rule>
    <rule id="e230-5072-4109-a786" name="Warband" publicationId="556c-7119-7234-b625" page="113" hidden="false">
      <description>1. D6 test at start of turn: 2-6 - pass, 1 - surge forward towards nearest visible enemy by at least basic move and charge if within range.
2. If unit charges and defeats enemy in the first round of combat, enemy units are automatically broken and will flee without taking a Break test if the warband outnumbers the enemy.
3. If unit charges or countercharges an enemy unit and breaks it in the first round of combat, then the warband must pursue.
4. Warbands in close order formation making any move other than straight forward have their movement reduced to half speed. Doesn't apply when surging forward.
5. Formed warbands 4+ models wide add +1 to their Leadership (Ld) value for each rank of at least four models behind the first. Max +3 to a maximum value of 10 for close order infantry, +2 up to a maximum of 10 for cavalry and open order infantry.
6. Character's and General's Leadership (Ld) can be combined with the Warband Ld bonus only if the Character/General is Warband.</description>
    </rule>
    <rule id="1c16-3adf-a97d-1db8" name="Wedge" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This rule affects Movement and Combat

Wedge Formation

A Wedge may be adopted as a cavalry unit deploys. Forming or reforming a Wedge at other times (except in pursuit, see below) takes a full move. A Wedge has one model at the front, two in the second row, and one more in each further row, and up to 15 models maximum. There must be at least six models to count as a Wedge.

A Wedge’s frontal arc of sight is based on the third rank of figures (i.e. the first one that is 3 figures wide).

Figures in a Wedge do not gain a rank bonus in combat, even if it flattens out. Note: the Wedge also represents those cavalry that formed up in diamond formations, though of course you can place your figures in a diamond with your opponent’s consent.

Wedge Movement and Manoeuvre

A Wedge does not turn or wheel, instead it pivots around a central point (at the join between the second and third rows) prior to and during movement (in a similar way to a wheel). It may pivot more than once during a move.

To pivot more than 90* at any one time, a unit must surrender a quarter of its movement allowance. Wedges that have the Drilled ability may pivot more than 90* for no movement cost, to reflect their increased mobility.

A Wedge may pivot, and march move.

A Wedge may only pivot once before charging in order to bring more models into contact (again similar to a wheel).

Note that some models may gain extra movement from this pivoting system, this is one of the major advantages of being in Wedge formation!

Wedge Combat

When a Wedge charges or counter-charges, one model contacts the enemy unit. The model at the apex of the Wedge strikes the enemy and up to nine other models not in contact may attack as well. This represents the unit ‘punching into’ the enemy formation.

After the ten models in the Wedge strike, surviving enemy models that are actually in contact with the apex of the Wedge may then strike back. In addition to these, the total Wedge models that attacked are divided in half (rounding down fractions) and those many extra surviving defenders may strike back. Note it is often best to sum up how many enemy figures could potentially strike back before resolving the Wedge’s attacks, as this eliminates confusion if models are removed and the players forget how many were in contact.

Combats involving chariots or skirmishers are resolved in the same way. Thus a unit of five chariots struck by a ten model Wedge would fight back with all five models, if they survived. A unit of ten skirmishers would most likely only have a potential six models to fight back, as it is most likely that only one model would be in actual base contact.

Characters and a Wedge

A Wedge may contain a maximum of two characters. They must occupy the front two places. If a Wedge flattens out, characters on the contacted side must join in contact with the enemy, blocked characters will fall in behind temporarily. During subsequent turns, they will move into contact as normal. In the case of a challenge, the Wedge character remains where he is, and the other model is repositioned to a suitable place it its formation in order to take part.

Flattening out the Wedge

A Wedge will flatten out if it is charged in the front and cannot countercharge, and will always flatten out if charged in the flank or rear.

A Wedge that loses a round of hand-to-hand combat will always flatten out unless it chooses to Give Ground. A flattened out Wedge loses all Wedge benefits.

Charging skirmishers and units of less than five models will not flatten a Wedge but will move into full contact and engage the Wedge along its angled sides, attempting to get as many figures into contact as possible. In this case only models in the Wedge that are in actual base contact may fight.

A Wedge flattens out into a formation two ranks deep with equal numbers in each rank where possible (so a 15 figure Wedge flattens into two ranks of eight and seven).

It still faces in its original direction once flattened.

If a Wedge is charged in flank or rear while already in combat to the front, it will flatten forwards into the unit it is already in combat with, once the charging units have been moved into contact. This may result in some extra movement for the charging figures, which is acceptable.

If a flattened Wedge is ultimately victorious, the unit may reform back into Wedge as it pursues the enemy, without taking a leadership test, or if it chooses to avoid pursuit, may reform in the player’s next turn, subject to the usual rules for reforming.

Unusual Situations

Because of the unusual angled frontage of a Wedge it is impossible to cover in words all the possible situations that can arise on the tabletop.

In the event of flattening out, the Wedge should never gain any unexpected bonuses and these should be ignored (such as flattening out into difficult terrain so to deny its charging opponent rank bonuses). At these times it may be more convenient to add an extra rank to the Wedge, or realign the units on the tabletop. It should be possible to resolve any situation if the players improvise using common sense and fairness.</description>
    </rule>
    <rule id="e00d-b9ca-4675-4334" name="Xyston" publicationId="fcb9-17be-94c2-bcfc" hidden="false">
      <description>This is a weapon rule

The Xyston was a type of thrusting spear used by Macedonian and Greek cavalry. All the rules for thrusting spears apply, and in addition the user of a xyston strikes first in each round of combat when fighting to the front, unless faced with a kontos or pike.

CONTENTS

Foreword

Creating Armies

Additional Rules

Army Lists

Lydian 700 BC to 500 BC

Etruscan 700 BC to 280 BC

Early Rome 550 BC to 420 BC

Early Hoplite Greek 600 BC to 400 BC

Persians and Medes 550 BC to 420 BC

Italian Hill Tribes 500 BC to 295 BC

Illyrian 500 BC to 10 AD

Thracian 500 BC to 46 AD

Early Carthaginian 500 BC to 270 BC

Republican Indian 500 BC to 320 BC

Classical Indian 500 BC to 180 BC

Gallic 500 BC to 50 BC

Spanish 500 BC to 72 BC

Campanian 500 BC to 150 BC

Later Achaemenid Persian 420 BC to 330 BC

Syracusan 400 BC to 210 BC

Warring States Chinese 400 BC to 200 BC

Later Hoplite Greek 400 BC to 275 BC

Twilight of Greece 300 BC to 146 BC

Republican Rome 400 BC to 100 BC

Macedon 359 BC to 331 BC

The Macedonian Empire 330 BC to 300 BC

Seleucid 300 BC to 83 BC

Armenian 300 BC to 386 AD

Ptolemaic 300 BC to 40 BC

Pyrrhic 300 BC to 275 BC

Bactrian Greek 300 BC to 30 BC

Galatian 279 BC to 25 BC

Later Macedonian 260 BC to 146 BC

Later Carthaginian 270 BC to 203 BC

Pergamene 260 BC to 130 BC

Parthian 250 BC to 225 AD

Numidian 250 BC to 30 BC

Han Chinese 206 BC to 220 AD

Bastarnae 200 BC to 200 AD

Xiongnu 200 BC to 200 AD

Maccabean Revolt 168 BC to 104 BC

Slave Revolt 150 BC to 60 BC

Kushan 140 BC to 400 AD

Pontic 110 BC to 47 BC

Early German 150 BC to 300 AD

British Tribes 100 BC to 75 AD

Dacian 82 BC to 106 AD

Early Imperial Roman 30 BC to 193 AD

Dark Age Britain and Ireland 75 AD to 800 AD

Middle Imperial Roman 193 AD to 350 AD

Palmyran 260 AD to 272 AD

Sassanid Persian 220 AD to 637 AD

Franks 300 AD to 750 AD

Korean 313 AD to 1270 AD

Late Imperial Roman 350 AD to 493 AD

Steppe Nomads 350 AD to 1504 AD

Gothic and Vandal Kingdoms 442 AD to 720 AD

Hindu India 450 AD to 1528 AD

Early Byzantine 475 AD to 660 AD

Tibetan 620 AD to 1000 AD

T’ang China 618 AD to 907 AD

Arab Conquest 632 AD to 672 AD

Slav or Bulgar 643 AD to 1014 AD

Thematic Byzantine 660 AD to 1042 AD

Christian Spanish 711 AD to 1250 AD

Vikings 750 AD to 1100 AD

Arab Caliphate 750 AD to 1055 AD

Rus 750 AD to 1250 AD

Al-Andalus and Granada 755 AD to 1492 AD

Carolingian 768 AD to 814 AD

Japanese 794 AD to 1500 AD

Later Saxon Kingdoms 800 AD to 1100 AD

Later Irish 830 AD to 1500 AD

Norman and Breton 911 AD to 1189 AD

Seljuk Turks 950 AD to 1230 AD

Ghaznavid 960 AD to 1186 AD

Song China 960 AD to 1279 AD

Polish 966 AD to 1500 AD

Capetian France 987 AD to 1328 AD

Medieval Hungarian 1000 AD to 1516 AD

North African Berbers 1042 AD to 1500 AD

Later Byzantine 1042 AD to 1185 AD

Italian City States 1050 AD to 1495 AD

Khwaresmian 1077 AD to 1231 AD

Crusaders 1096 AD to 1291 AD

Russian 1100 AD to 1500 AD

Holy Roman Empire 1138 AD to 1500 AD

The Ordensstaat 1211 AD to 1525 AD

The Baltic Pagans 1193 AD to 1295 AD

Mongol Conquest and Khanates 1206 AD to 1508 AD

Muslim Indian 1206 AD to 1526 AD

Medieval Spanish 1250 AD to 1492 AD

Mamluks 1250 AD to 1517 AD

Medieval Balkan States 1268 AD to 1527 AD

Swiss 1291 AD to 1495 AD

Medieval English 1296 AD to 1453 AD

Medieval French 1328 AD to 1444 AD

Medieval Scotland 1295 AD to 1500 AD

Low Countries 1312 AD to 1453 AD

Timurid 1360 AD to 1450 AD

Hussite 1420 AD to 1434 AD

Ordonnance Burgundian 1471 AD to 1477 AD

War of the Roses 1455 AD to 1487 AD

Late Medieval French 1471 AD to 1477 AD

Ottoman Turks 1281 AD to 1526 AD</description>
    </rule>
    <rule id="e859-c387-61e5-a208" name="Testudo" publicationId="556c-7119-7234-b625" hidden="false">
      <description>A unit at least 2 ranks deep and 4 models wide may form testudo. Declare at the start of the turn. The unit may not charge or march. While in testudo it has a 2+ armour save against missile attacks.</description>
    </rule>
    <rule id="7c78-d18c-1cae-f5bb" name="Centurions" publicationId="556c-7119-7234-b625" hidden="false">
      <description>One model per Legionary unit may be upgraded to a Centurion (leader) for +10 pts instead of +5. A Centurion adds +1 Leadership to the unit. Auxiliary leaders do not give this bonus.</description>
    </rule>
    <rule id="41fc-5de5-0862-91b8" name="Army Standard" publicationId="556c-7119-7234-b625" hidden="false">
      <description>Units within 12" may re-roll failed Break tests. If the Army Standard is captured the enemy scores 400 victory points instead of 200. Roman units hate the unit that captures it until it is recaptured.</description>
    </rule>
    <rule id="6816-77e8-9db0-03b9" name="Army General (Roman list)" publicationId="556c-7119-7234-b625" hidden="false">
      <description>Units within 12" of the General may use his Leadership.</description>
    </rule>
    <rule id="4761-7e9a-03ed-249e" name="Army General (Barbarian list)" publicationId="556c-7119-7234-b625" hidden="false">
      <description>Units within 12" of the Warlord may use his Leadership.</description>
    </rule>
    <rule id="44f9-36d8-df36-fd0f" name="Army Standard (Barbarian list)" publicationId="556c-7119-7234-b625" hidden="false">
      <description>Units within 12" of the Battle Standard may re-roll failed Break tests.</description>
    </rule>
    <rule id="9281-3e2b-d221-8127" name="Mixed Armour (Hannibal)" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Some units have figures with different armour. In close combat use the Saving roll of the wounded figure. Against missile fire use the Saving roll of the majority of the figures in the unit. The owner of the unit decides which figures to remove as casualties.</description>
    </rule>
    <rule id="f1bd-74e6-0edc-2687" name="Hannibal Rules Clarifications" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Hannibal p.106-109 (Rules Clarifications, also published in Spartacus and Armies of Chivalry). Summary:
UNITS: minimum size is five models unless stated; one model per unit may be a Leader, Standard Bearer and Musician (+5 each). Units under five models that lose a round of combat are broken automatically and cannot use Psychology rules. For a character to affect a unit by Psychology he must be in the front rank or engaged as part of that unit. Units subject to frenzy cannot flee or fire and flee as a charge reaction.
CHARACTERS: unattached characters that lose a round of combat automatically break and flee but may rally normally. A character attached to a unit reduced below five models that flees cannot rally. A character may not join an engaged unit (he may charge into the combat) and may not charge an enemy in the rear if he starts his move in front of it.
LEADERSHIP &amp; WARBAND: if a Warband unit is joined by a character without Warband Psychology the unit uses either its own Ld or the character's, not both, and adds the Warband rank bonus. Warband rule 1 characters and cavalry may count a rank bonus up to 3 for a maximum Leadership of 10 (light troops count up to two ranks); no rank bonus means no benefit.
CAVALRY COUNTER CHARGES: a charge reaction only for cavalry charged to the front by enemy cavalry. The unit counts as charging for weapon effects but does not move or strike first; cavalry with a move of less than 6" (e.g. cataphracts) cannot counter charge; cavalry cannot counter charge infantry. Camelry and light chariots count as cavalry. Also counts as charging for Ferocious Charge and Warband.
REFORMING IN COMBAT: a unit fighting to its flank or rear may reform at the end of the Close Combat phase if it did not break and is not engaged on another facing; it faces the engaging unit with its centre in base contact. A reformed unit loses its rank bonus if charged by an enemy unit with five or more models.
COMBINED FORMATION (not used in Hannibal lists): archers lose Light Troop status, may use Massed Archery, may stand and shoot or fire and flee; missile hits use the majority saving throw and casualties are removed in roughly equal proportions; in close combat hits fall on models in contact.
FEROCIOUS CHARGE (not used in Hannibal lists): winning a round of combat makes opponents break automatically (Break-immune units roll a D6: 1-3 broken, 4-6 hold). FEIGNED FLIGHT: cavalry that flee or fire and flee as a charge reaction rally at the end of their move and may reform facing any direction; the charging enemy still counts as charging. PARTHIAN SHOT: a normal move immediately after shooting, in the Shooting phase only, not a charge reaction, and the unit may not march.
MOVEMENT: movement values are unencumbered; deduct armour and barding penalties. Reforming units cannot move more than double their move. Disengaging: move away in a straight line ending with the rear facing the enemy; units fighting to more than one facing cannot disengage. Copses and orchards are difficult terrain for formed units (skirmishers unaffected); shooting through or at targets within suffers -1 to hit.
SHOOTING: all models in a unit on an elevated position can shoot and be targeted by all models in a shooting unit (Massed Archery rules apply to missile weapons in these situations unless agreed otherwise). Crew models aboard elephants, chariots and war-wagons suffer -1 to hit for moving unless stated. Heavy and Scythed Chariots are large targets (+1 to hit).
HAND-TO-HAND: weapons that fight in two ranks do so only to the front. Skirmishing units charging the flank or rear cause no Panic test and do not negate rank bonuses but gain the +1/+2 flank/rear combat result; skirmishers get no unit standard bonus and no musician roll-off. A unit in clear ground fighting an enemy in difficult terrain only loses rank bonus if its models are in contact with enemy models in the difficult ground.
OVERRUN: if all of a unit's opponents are slain in the first round of close combat it may make an Overrun move (2D6" or 3D6" by Movement value) as if it had broken them. An overrun into a fresh enemy is a new charge (fear/terror tests apply) and combat is resolved next turn with charge bonuses.
FALLING BACK IN GOOD ORDER: if one side outnumbers the other by over 2:1 (models, calculated at the end of the combat) and the outnumbering side loses and fails its Break test, it falls back in good order instead of fleeing. Drilled troops, skirmishers and cavalry that lose and pass their Break test may also fall back in good order. Exceptions to a flee: no Panic test for friends within 12"; rally automatically at the end of the move (a unit that was fighting to its flank or rear cannot reform); may be pursued (pursuers count as having charged next combat phase); may not charge next turn but may move and shoot; lost if it falls off the table; units may also fall back from a First Charge or Ferocious Charge.</description>
    </rule>
    <rule id="779b-f052-2311-9f58" name="Hannibal Common Rules" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>What you see is what you get: models must show the options taken unless the opponent agrees otherwise. Mounted models may ride a horse (Movement 8" before armour penalties) or, where stated, a Warhorse (M8 WS3 BS0 S3 I3 A1). All bows in the army lists are composite bows with a range of 24".</description>
    </rule>
    <rule id="4bf4-3725-3f39-3fc8" name="Phalanx (Hannibal)" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Mercenary Hoplites fight in phalanx; as in Alexander the Great, but phalanx units may have standards and benefit from an army standard bearer. May wheel normally; may About Face and Adjust Ranks only (no Right/Left Face). May never change facing when engaged on its flank or rear. To gain phalanx combat benefits the unit must have at least 16 models and at least a +1 combat rank bonus. A phalanx may charge and still fight in two ranks to the front. All enemy attacks (shooting and hand-to-hand) against the front of a phalanx suffer -1 to hit. Mounted units (cavalry, camelry, light chariots) may not willingly charge the front of a phalanx (elephants, scythed and heavy chariots may). A unit with pikes or spears fights in two ranks only. Only one rank may fight to flank or rear. A phalanx attacking across obstacles or difficult terrain loses both combat ranks and phalanx benefits.</description>
    </rule>
    <rule id="a23a-d972-dddf-752d" name="Levies (Hannibal)" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Levy troops fear enemy units they do not outnumber by at least 2:1. Levies do not fear other Levies, fleeing troops or skirmishers.</description>
    </rule>
    <rule id="610e-5657-af1c-01eb" name="Mixed Weapons (Hannibal)" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Celtic and Gallic barbarians fought with a mix of weapons: javelins and a hand weapon (sword, axe or short spear). Troops armed with mixed weapons may re-roll any failed to-hit roll once in the first round of combat. Applies to both cavalry and foot.</description>
    </rule>
    <rule id="c1a1-a05f-40b7-4770" name="Manipular Unit" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>Hastati, principes and triarii are manipular units. Rank support: a manipular unit with a friendly manipular unit in its rear arc (part of the supporter's charge arc in the rear arc of the supported unit, within 4", unengaged, not fleeing, with a rank bonus and not in difficult terrain) may count the rear unit's rank bonus in addition to its own, up to the normal +3 maximum. No support if in column, if its own rank bonus is lost to terrain/obstacles/flank or rear charge, or if the combat includes an elephant. Formation swap: an engaged, non-fleeing manipular unit not in column may swap places at the start of the Roman turn with an unengaged friendly manipular unit completely within its rear arc, within 8" of the front of the engaged unit, that could charge the enemy; a unit may not swap if engaged to more than one facing; the replacing unit counts as charging in the next combat round. A fleeing manipular unit with a supporting unit in its rear adds +2 to its Flee roll. Panic: Principes may re-roll Panic tests caused by broken, destroyed or fleeing friendly hastati units; Triarii may re-roll Panic tests caused by hastati or principes; Roman characters on their own may re-roll Panic tests caused by hastati or principes.</description>
    </rule>
    <rule id="d0cc-9e48-7270-4af6" name="Unbridled Charge" publicationId="fc9f-8438-629b-e92d" hidden="false">
      <description>A Roman or Italian cavalry unit may declare an unbridled charge in lieu of an ordinary charge, only against non-cataphract enemy cavalry (not infantry, cataphracts, camels, chariots or elephants). If it wins a round of combat the charged unit breaks automatically with no Leadership test (units that ignore Break tests roll a D6: 1-3 broken, 4-6 hold). After the charge and combat the Roman cavalry must spend one turn reforming before pursuing or moving, other than fleeing. If charged while reforming it may not fall back in good order.</description>
    </rule>
  </sharedRules>
  <sharedProfiles>
    <profile id="7ff2-453d-751e-5f78" name="Sling" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">18"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3 (rapid fire: short range only, Strength 2)</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Slings can shoot twice at short range (rapid fire) but cannot shoot twice against chargers as a stand &amp; shoot or fire &amp; flee response.</characteristic>
      </characteristics>
    </profile>
    <profile id="e912-2cb4-c863-ad45" name="Staff Sling" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">24"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">4 at short range / 3 at long range</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-1 at short range</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Staff slings cannot move and shoot in the same turn.</characteristic>
      </characteristics>
    </profile>
    <profile id="10ef-3567-0d3f-d9e7" name="Javelin" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">8"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">The to hit penalties for shooting at over half range and for shooting whilst moving do not apply to javelins.</characteristic>
      </characteristics>
    </profile>
    <profile id="42af-0d8f-e233-9a0c" name="Dart" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">12"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">2</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">The to hit penalties for shooting at over half range and for shooting whilst moving do not apply to darts. Darts can shoot massed missiles.</characteristic>
      </characteristics>
    </profile>
    <profile id="9fc1-8ed3-cea0-52e0" name="Stones" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">4"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">The to hit penalties for shooting at over half range do not apply to stones.</characteristic>
      </characteristics>
    </profile>
    <profile id="c963-937b-87a2-24f9" name="Short Bow" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">18"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Units armed with short bows can use massed missiles.</characteristic>
      </characteristics>
    </profile>
    <profile id="5d29-ba1e-8299-8085" name="Bow" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">24"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Units armed with bows can use massed missiles. (Composite bows are Bows.)</characteristic>
      </characteristics>
    </profile>
    <profile id="8fb0-c5a6-7a18-ea82" name="Long Bow" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">30"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-1 at short range</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Units armed with long bows can use massed missiles.</characteristic>
      </characteristics>
    </profile>
    <profile id="019d-351d-ecdc-c800" name="Light Crossbow" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">18"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">3</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1"></characteristic>
      </characteristics>
    </profile>
    <profile id="feb3-06f6-871d-95f9" name="Crossbow" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">30"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">4 at short range / 3 at long range</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-1 at short range</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Crossbows cannot move and shoot in the same turn.</characteristic>
      </characteristics>
    </profile>
    <profile id="d0f6-d0b0-336c-8eea" name="Handgun" publicationId="556c-7119-7234-b625" page="88 (summary p.209)" hidden="false" typeId="5de1-764d-a40b-f6b5" typeName="Missile Weapon">
      <characteristics>
        <characteristic name="Range" typeId="6962-86a7-af53-83bb">18"</characteristic>
        <characteristic name="Strength" typeId="e237-5c6b-65a3-8bf7">4 at short range / 3 at long range</characteristic>
        <characteristic name="Save Modifier" typeId="b819-8576-7e60-dba3">-2 at short range / -1 at long range</characteristic>
        <characteristic name="Notes" typeId="6282-7884-5061-ecf1">Handguns cannot move and shoot in the same turn.</characteristic>
      </characteristics>
    </profile>
    <profile id="a423-b782-e1ce-43e2" name="Hand Weapon" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Troops armed with a hand weapon in each hand get +1 extra attack.</characteristic>
      </characteristics>
    </profile>
    <profile id="a767-c23a-5b8e-1596" name="Dagger" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. +1 armour save modifier.</characteristic>
      </characteristics>
    </profile>
    <profile id="026a-8df7-0a12-0a18" name="Improvised Weapon" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Enemy wounded by daggers or improvised weapons receive a +1 armour save modifier (if they otherwise have no save they save on a 6).
2. Troops so armed are at a disadvantage compared to those properly prepared for combat. (Rulebook: Dagger and Improvised Weapon.)</characteristic>
      </characteristics>
    </profile>
    <profile id="bebe-c4da-722c-c475" name="Double-handed Weapon" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Shields cannot be used in hand-to-hand combat.
2. Always strike last in hand-to-hand combat. If both so armed normal priorities apply.
3. +2 Strength.</characteristic>
      </characteristics>
    </profile>
    <profile id="635a-1d79-5976-954c" name="Halberd" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Shields cannot be used in hand-to-hand combat.
2. +1 Strength.</characteristic>
      </characteristics>
    </profile>
    <profile id="5a59-1efb-14ef-017a" name="Thrusting Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Stationary infantry fight in two ranks to their front.
2. Cavalry +1 strength bonus when they charge or countercharge over open ground.</characteristic>
      </characteristics>
    </profile>
    <profile id="cc82-90f9-0ade-c0e7" name="Throwing Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Infantry fight in two ranks in the first round of combat.
2. Cavalry can re-roll misses in the first round of combat unless charging/countercharging over difficult terrain.
3. Skirmishers can re-roll misses in the first round of combat.</characteristic>
      </characteristics>
    </profile>
    <profile id="26ae-ef02-1f24-a490" name="Heavy Throwing Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Infantry fight in two ranks in the first round of combat.
2. +1 Strength in the first round of combat.
3. Skirmishers can re-roll misses in the first round of combat.</characteristic>
      </characteristics>
    </profile>
    <profile id="8acf-e438-93ac-347e" name="Pike" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Fight in two ranks in all rounds of combat.
2. Always strike first if fighting exclusively to their front. Where both so armed normal initiatives apply.</characteristic>
      </characteristics>
    </profile>
    <profile id="f901-2529-d411-6ed0" name="Kontos" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Cavalry +1 strength bonus when they charge or countercharge over open ground.
2. Always strike first if fighting exclusively to their front except against pikes. Where both kontos armed, normal initiatives apply.</characteristic>
      </characteristics>
    </profile>
    <profile id="a4b8-1d78-eb6b-c4f2" name="Lance" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">1. Cavalry +2 strength bonus when they charge or countercharge over open ground.</characteristic>
      </characteristics>
    </profile>
    <profile id="b36d-1525-b0bc-5c0f" name="No Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">None</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="e1d7-1cd3-1431-4862" name="Light Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">5 or 6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="16c5-d2b2-fa96-9cd2" name="Heavy Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">5 or 6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">4, 5 or 6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="aa63-8f92-57ef-91e7" name="Cataphract Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">-</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="8430-72da-5ac5-d33f" name="Partial Plate Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">4, 5 or 6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="70a8-fcb7-f10e-4737" name="Full Plate Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">3, 4, 5 or 6*</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">* Either with or without shield - carrying a shield adds no bonus to the warrior's armour saving throw. Maximum infantry save is 3+ and cavalry is 2+.</characteristic>
      </characteristics>
    </profile>
    <profile id="b513-5c2a-34df-6a1d" name="Shield" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70"></characteristic>
      </characteristics>
    </profile>
    <profile id="8367-11b2-7778-977f" name="Large Shield" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+2</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70"></characteristic>
      </characteristics>
    </profile>
    <profile id="f587-5eb5-fc55-6409" name="Pavise" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+2</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">When hit to the front by shooting only</characteristic>
      </characteristics>
    </profile>
    <profile id="aa05-2e85-a1d8-8d69" name="Buckler" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Hand-to-hand only unless skirmishers</characteristic>
      </characteristics>
    </profile>
    <profile id="e556-cf0c-4c05-4d8b" name="Full Metal Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70"></characteristic>
      </characteristics>
    </profile>
    <profile id="b16b-db14-3dfe-1470" name="Half Metal Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">When hit to the front</characteristic>
      </characteristics>
    </profile>
    <profile id="967d-06de-de04-9660" name="Full Cloth Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Hand-to-hand only</characteristic>
      </characteristics>
    </profile>
    <profile id="3902-d49b-5509-fb74" name="Half Cloth Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">When hit to the front in hand-to-hand only</characteristic>
      </characteristics>
    </profile>
  </sharedProfiles>
</gameSystem>
