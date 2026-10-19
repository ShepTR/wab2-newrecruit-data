<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gameSystem id="6f1f-5f84-d7e5-4889" name="Warhammer Ancient Battles 2.0" revision="14" battleScribeVersion="2.03" authorName="WAB2 New Recruit pilot" xmlns="http://www.battlescribe.net/schema/gameSystemSchema" type="gameSystem" library="true">
  <readme>Pilot data set: Warhammer Ancient Battles 2nd Edition, built from the 2.0 rulebook reference pages and Armies of Antiquity v2.0.</readme>
  <publications>
    <publication id="556c-7119-7234-b625" name="Warhammer Ancient Battles 2nd Edition" shortName="WAB2" publisher="Warhammer Historical Wargames" publicationDate="2010"/>
    <publication id="fcb9-17be-94c2-bcfc" name="Armies of Antiquity v2.0" shortName="AoA2" publisher="Warhammer Historical Wargames" publicationDate="2011"/>
    <publication id="fc9f-8438-629b-e92d" name="Hannibal and the Punic Wars" shortName="HPW" publisher="Warhammer Historical Wargames" publicationDate="2005"/>
    <publication id="513c-2d0a-024a-da5a" name="Chariot Wars" shortName="CW" publisher="Warhammer Historical Wargames" publicationDate="2007"/>
    <publication id="37b4-aae5-6830-d590" name="Fall of the West" shortName="FotW" publisher="Warhammer Historical Wargames" publicationDate="2002"/>
    <publication id="aab0-aa1e-0319-4ffe" name="Armies of Antiquity" shortName="AoA" publisher="Warhammer Historical Wargames" publicationDate="1999"/>
    <publication id="af20-e256-4a51-93aa" name="Shieldwall" shortName="SW" publisher="Warhammer Historical Wargames" publicationDate="2002"/>
    <publication id="2127-dab1-0af6-7421" name="El Cid" shortName="EC" publisher="Warhammer Historical Wargames" publicationDate="2007"/>
    <publication id="0641-2ee1-c462-c414" name="Alexander the Great" shortName="AG" publisher="Warhammer Historical Wargames" publicationDate="2008"/>
    <publication id="da79-edc9-ea11-dbc4" name="Armies of Chivalry" shortName="AC" publisher="Warhammer Historical Wargames" publicationDate="2004"/>
    <publication id="eb14-e889-c793-0fc4" name="Spartacus" shortName="SP" publisher="Warhammer Historical Wargames" publicationDate="2008"/>
    <publication id="15ea-5299-d0f5-5dbb" name="Byzantium: Beyond the Golden Gate" shortName="BZ" publisher="Warhammer Historical Wargames" publicationDate="2005"/>
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
    <profileType id="0dbe-f4ed-ef08-8e86" name="Armour Save">
      <characteristicTypes>
        <characteristicType id="603e-2898-6af9-6cf1" name="Save"/>
        <characteristicType id="5882-dd5a-bc28-4024" name="With conditional bonuses"/>
        <characteristicType id="d5e4-804e-6192-0114" name="Notes"/>
      </characteristicTypes>
    </profileType>
  </profileTypes>
  <categoryEntries>
    <categoryEntry id="fb15-1790-2ccc-50c8" name="Army composition" hidden="false"/>
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
    <categoryEntry id="38c4-e0a7-a7f3-dc77" name="Allies &amp; Mercenaries" hidden="false"/>
    <categoryEntry id="a178-280d-202c-b3d0" name="Chariotry" hidden="false"/>
    <categoryEntry id="e85f-5baa-0bfe-26d6" name="Chariotry &amp; Cavalry" hidden="false"/>
    <categoryEntry id="368d-33dc-12e4-8b16" name="Barbarian Cavalry" hidden="false"/>
    <categoryEntry id="773a-1fbb-6862-e9c1" name="Barbarian Infantry" hidden="false"/>
    <categoryEntry id="3ae2-1ee1-7d21-6c5b" name="Roman Cavalry" hidden="false"/>
    <categoryEntry id="87bc-1d1e-35cf-c4e8" name="Roman Infantry" hidden="false"/>
    <categoryEntry id="0c18-c369-b2f7-93f2" name="Steppe Cavalry" hidden="false"/>
    <categoryEntry id="ca02-eacc-ee23-4d57" name="Allies &amp; Tribal Mercenaries" hidden="false"/>
    <categoryEntry id="5f09-a420-168c-b2d9" name="Archers &amp; Unusual Troops" hidden="false"/>
    <categoryEntry id="1357-310c-56af-a94b" name="Elephants, Chariots &amp; Cavalry" hidden="false"/>
    <categoryEntry id="7f33-e2a4-4915-c8f4" name="Levies &amp; Mercenaries" hidden="false"/>
    <categoryEntry id="9028-a3e9-f537-115c" name="Light Infantry" hidden="false"/>
    <categoryEntry id="6c4c-d645-e7f7-f2d8" name="Persian Troops" hidden="false"/>
    <categoryEntry id="88db-8178-1680-7486" name="Phalanx" hidden="false"/>
    <categoryEntry id="1da8-c9f1-705c-6a6f" name="Samurai" hidden="false"/>
    <categoryEntry id="897c-92a0-c2d2-53ca" name="Special Troops" hidden="false"/>
    <categoryEntry id="2151-69a6-7085-b914" name="Special Troops &amp; Allies" hidden="false"/>
    <categoryEntry id="3124-ccb8-55cc-4fb3" name="Special Troops &amp; Mercenaries" hidden="false"/>
    <categoryEntry id="2040-2309-97cc-fd89" name="Special Troops, Allies &amp; Mercenaries" hidden="false"/>
    <categoryEntry id="0654-a713-ca15-c866" name="War Machines" hidden="false"/>
    <categoryEntry id="6eb7-9942-f37d-32df" name="Common Warriors: Milites and Liberi" hidden="false"/>
    <categoryEntry id="59cd-febb-ea2a-b90a" name="Common Warriors: Milites and Pueri" hidden="false"/>
    <categoryEntry id="b2e8-8a8b-a1b9-30a4" name="Common Warriors: Toisech and Soer-chele" hidden="false"/>
    <categoryEntry id="0f53-e23c-3ec0-9fe3" name="Common Warriors: Toisech, Eachraidh, Soer-chele and Doer-chele" hidden="false"/>
    <categoryEntry id="a6c2-7b01-428a-5002" name="Common Warriors: Toisech, Soer-chele and Doer-chele" hidden="false"/>
    <categoryEntry id="c9c8-3285-67ba-9053" name="Uncommon Warriors: Coloni and Dogs of War" hidden="false"/>
    <categoryEntry id="3b71-8f3d-d210-a108" name="Uncommon Warriors: Doer-chele, Eachraidh and Dogs of War" hidden="false"/>
    <categoryEntry id="5603-085f-62f4-c42f" name="Uncommon Warriors: Eachraidh and Dogs of War" hidden="false"/>
    <categoryEntry id="fcf2-d68f-f22f-4460" name="Uncommon Warriors: Liberi, Coloni and Dogs of War" hidden="false"/>
    <categoryEntry id="491c-de44-9505-3e4b" name="Uncommon Warriors: Pueri, Coloni and Dogs of War" hidden="false"/>
    <categoryEntry id="ad27-4da1-3028-5533" name="Uncommon Warriors: Pueri, Liberi, Coloni and Dogs of War" hidden="false"/>
    <categoryEntry id="2bde-edde-d265-2a6a" name="Coloni" hidden="false"/>
    <categoryEntry id="bb52-a098-8217-fad7" name="Common Warriors" hidden="false"/>
    <categoryEntry id="9568-2556-e209-055d" name="Doer-chele" hidden="false"/>
    <categoryEntry id="a57d-15cd-e77c-b15b" name="Dogs of War" hidden="false"/>
    <categoryEntry id="1cc6-442e-e168-ff3b" name="Eachraidh" hidden="false"/>
    <categoryEntry id="f27b-2cf4-9b3d-b4e8" name="Fianna" hidden="false"/>
    <categoryEntry id="b697-d3d4-1f93-7bb9" name="Liberi" hidden="false"/>
    <categoryEntry id="4695-1bd4-a060-f529" name="Milites" hidden="false"/>
    <categoryEntry id="c5fb-f798-53f2-3293" name="Pueri" hidden="false"/>
    <categoryEntry id="045c-f9f8-81f6-9a17" name="Soer-chele" hidden="false"/>
    <categoryEntry id="0c80-93da-4649-b3ed" name="Teulu" hidden="false"/>
    <categoryEntry id="5ad7-c087-1636-0808" name="Toisech" hidden="false"/>
    <categoryEntry id="b2c1-cc28-9aef-021d" name="Uncommon Warriors" hidden="false"/>
    <categoryEntry id="2cd3-c879-de42-09e1" name="Common Troops: Almohads" hidden="false"/>
    <categoryEntry id="dbb8-9f3f-9f8f-11d4" name="Common Troops: Almoravids" hidden="false"/>
    <categoryEntry id="a586-ba18-2b12-17d7" name="Common Troops: Asturias" hidden="false"/>
    <categoryEntry id="7e2f-27c5-2dfa-e4c4" name="Common Troops: Caliphate" hidden="false"/>
    <categoryEntry id="74ba-c414-a747-826c" name="Common Troops: El Cid" hidden="false"/>
    <categoryEntry id="0f38-8e4a-4501-637d" name="Common Troops: Later Taifas" hidden="false"/>
    <categoryEntry id="b872-0eb8-f3ff-3328" name="Common Troops: Reconquista" hidden="false"/>
    <categoryEntry id="1934-e02e-865a-2b1c" name="Common Troops: Taifa Kings" hidden="false"/>
    <categoryEntry id="0ac0-dae6-4188-ea2f" name="Uncommon Troops: Almohads" hidden="false"/>
    <categoryEntry id="8b91-1442-3cda-0b13" name="Uncommon Troops: Almoravids" hidden="false"/>
    <categoryEntry id="8407-d89b-e464-8d60" name="Uncommon Troops: Asturias" hidden="false"/>
    <categoryEntry id="bba4-74e9-5777-576d" name="Uncommon Troops: Caliphate" hidden="false"/>
    <categoryEntry id="3c53-38ef-b9fd-a47c" name="Uncommon Troops: El Cid" hidden="false"/>
    <categoryEntry id="ca86-292e-7943-d805" name="Uncommon Troops: Later Taifas" hidden="false"/>
    <categoryEntry id="6c2a-b2f2-0777-f4d5" name="Uncommon Troops: Reconquista" hidden="false"/>
    <categoryEntry id="575e-eca8-12af-72bd" name="Uncommon Troops: Taifa Kings" hidden="false"/>
    <categoryEntry id="0362-7f31-842f-ced0" name="Aliados y Mercenarios" hidden="false"/>
    <categoryEntry id="2ba8-a026-3d74-e93b" name="Allies &amp; War Machines" hidden="false"/>
    <categoryEntry id="773a-59d9-404b-4250" name="Cavalry &amp; Chariots" hidden="false"/>
    <categoryEntry id="bb2d-5030-2e22-377f" name="Elephants" hidden="false"/>
    <categoryEntry id="52c5-947d-93d4-f122" name="Infantry &amp; Skirmishers" hidden="false"/>
    <categoryEntry id="5669-adf9-cb02-de9e" name="Levies" hidden="false"/>
    <categoryEntry id="460c-f01b-046e-880c" name="Persians" hidden="false"/>
    <categoryEntry id="80e0-112f-b3d4-3e5c" name="Phalangites" hidden="false"/>
    <categoryEntry id="c943-6d8d-bb33-47ee" name="Special Troops, Mercenaries &amp; Allies" hidden="false"/>
    <categoryEntry id="ebc5-3647-ff9c-c887" name="Wagons" hidden="false"/>
    <categoryEntry id="d4df-79ed-bbda-72fa" name="Cavalry/Support" hidden="false"/>
    <categoryEntry id="5719-2c0d-4245-2e4e" name="Janissaries" hidden="false"/>
    <categoryEntry id="28b5-6150-ecee-a852" name="Mercenaries" hidden="false"/>
    <categoryEntry id="3c17-30e5-7804-209e" name="Ottoman Cavalry" hidden="false"/>
    <categoryEntry id="a468-171c-369f-4b6c" name="Turkoman &amp; Akincis Cavalry" hidden="false"/>
    <categoryEntry id="a520-8c56-9ab1-1f32" name="Vassals" hidden="false"/>
    <categoryEntry id="8914-868d-c4b1-e363" name="Vassals, Allies &amp; Mercenaries" hidden="false"/>
    <categoryEntry id="32ce-bec3-9d66-e1ab" name="Volunteers" hidden="false"/>
    <categoryEntry id="839f-50bc-1cf6-bbba" name="Gallic and Germanic Slaves" hidden="false"/>
    <categoryEntry id="9037-b2f4-17ba-8c97" name="Auxiliaries &amp; Support Troops" hidden="false"/>
    <categoryEntry id="3434-abc8-b5fb-2dc2" name="Conscript Legionaries" hidden="false"/>
    <categoryEntry id="4b11-a070-f0c8-92f2" name="Experienced Legionaries" hidden="false"/>
    <categoryEntry id="7af6-6c4c-dd00-596a" name="Slave Infantry" hidden="false"/>
    <categoryEntry id="bfb2-2e9c-2a30-fac2" name="Ghulams" hidden="false"/>
    <categoryEntry id="496f-313e-c4d8-b20a" name="Light Cavalry" hidden="false"/>
  </categoryEntries>
  <forceEntries>
    <forceEntry id="3083-ceb0-f2dc-6449" name="Army" hidden="false">
      <categoryLinks>
        <categoryLink id="ba32-164b-3eb5-3a3c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="false">
          <constraints>
            <constraint field="selections" scope="parent" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="7131-83f0-eac6-ea76" type="max"/>
            <constraint field="selections" scope="parent" value="0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="ec67-0ca5-e0c4-a5d8" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="ec67-0ca5-e0c4-a5d8" value="1">
              <conditionGroups>
                <conditionGroup type="or">
                  <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="77be-8814-23e3-4ce5" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="178c-ffbc-b301-16ba" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eb28-6ed4-bf69-dbe1" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="50be-dbef-ae9e-f1d0" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b904-05df-7dcd-cae7" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b90f-6192-92f7-0af0" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f89e-42a7-5272-fedd" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3f52-7e73-22e8-f61e" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f430-9d85-c97c-11e8" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="acdb-8982-b749-a280" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cdd7-93bb-92d6-0aa4" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6864-b22f-4cf1-3e9e" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b1a-f9b9-37a6-7802" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33f0-e587-bc7b-5859" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0845-3db9-de0b-c8ff" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bf13-8303-e9bf-b20f" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1cbf-30f4-5071-3d11" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5e9a-ae2b-8768-10d4" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="d045-979c-ce47-fbe4" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f4b0-39b0-06f0-415e" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5253-c9ff-87dd-a7b4" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0636-e4a8-1ccf-14d8" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b6b1-1a8a-7f57-8453" type="instanceOf"/>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="85c6-18d9-9371-f27a" type="instanceOf"/>
                  </conditions>
                </conditionGroup>
              </conditionGroups>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="0c16-a38c-825b-8ad7" name="Allies and Mercenaries" hidden="false" targetId="44b5-a917-2fd7-20ca" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="f74a-7438-43a8-644d" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="5637-6150-b5a7-08d5" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b9ef-b43e-36be-5a69" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="0">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4d74-a514-2459-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2d05-8c94-0564-9abf" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9640-4e8c-c5b2-04ae" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="25b3-496d-3222-47d5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5556-d8cc-caed-c0be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ecf2-89d2-d755-4394" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3084-ae79-fd51-a95f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a0f-273a-eb20-824c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-0500-bed2-fcce" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39e0-d11d-3ba7-3303" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f74a-7438-43a8-644d" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6c96-52e8-a508-6265" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="5637-6150-b5a7-08d5" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c16d-100c-f576-e8f5" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="ef03-df8e-2c94-4b6e" name="Archers" hidden="false" targetId="5292-e765-10c8-f6e8" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="94b7-e85e-c6be-7dfc" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="ae4a-e3c1-cedd-c368" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="94b7-e85e-c6be-7dfc" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7576-1447-92b5-2d67" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="94b7-e85e-c6be-7dfc" value="40">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9da3-d00a-b05f-b9ea" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="94b7-e85e-c6be-7dfc" value="10">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="52f6-e805-2e4a-6d4e" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="ae4a-e3c1-cedd-c368" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9640-4e8c-c5b2-04ae" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="ae4a-e3c1-cedd-c368" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7576-1447-92b5-2d67" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="ae4a-e3c1-cedd-c368" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9da3-d00a-b05f-b9ea" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="7cff-9160-ca04-8bfa" name="Artillery" hidden="false" targetId="3a7c-df52-a77b-1017" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="98a6-15e9-d534-2f30" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="98a6-15e9-d534-2f30" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b9ef-b43e-36be-5a69" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="98a6-15e9-d534-2f30" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4d74-a514-2459-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="98a6-15e9-d534-2f30" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9640-4e8c-c5b2-04ae" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="98a6-15e9-d534-2f30" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="98a6-15e9-d534-2f30" value="100">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="2320-3827-74f2-18f9" name="Cavalry" hidden="false" targetId="4d00-21b7-b56e-3a42" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c498-30a0-abb8-9a0e" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="0b6e-4b03-466f-bf4f" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f7ce-737d-155e-b5c0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="903f-cf5e-5a96-3642" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a32d-ef40-094e-5557" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1ea2-ee62-2aab-f4b7" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eaae-80c3-653b-cdff" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="390d-7fcd-6e5f-de36" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="84b5-af35-ff08-b1fb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6445-92bb-a222-2769" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="71b6-a7b0-f3d0-d621" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ffe3-1936-272b-1780" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cbde-3cfc-f625-caa3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e15-d81e-9e7c-dca8" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9cd7-9074-1079-a416" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c9b6-0f75-a848-579d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="15">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4cdd-c505-ebb3-6e24" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="35">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7576-1447-92b5-2d67" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="30">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9da3-d00a-b05f-b9ea" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="52f6-e805-2e4a-6d4e" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4289-2356-a73d-68eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ccaa-7c64-def4-a6e3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bc4f-5679-701f-016a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a7a7-9dea-53a5-b5fc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="74f5-b5d8-4625-3175" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="673a-6d66-308a-29cd" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bd14-1b77-1a71-685e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9d7f-dae0-fa10-cc77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6b4f-8c2d-cd11-2788" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="37d6-fcaa-7fa8-9e5d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0d41-30d7-3a48-ffee" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f0ed-e71d-802a-591d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7031-7960-f06a-2500" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1631-2694-7938-a545" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4ddc-9a9c-c7de-308e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a33-2077-d386-77ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d4b1-de1b-4481-449a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ad99-93a0-2c6b-b892" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="019a-902d-4fdd-a496" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9498-7200-5dc8-05df" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1641-9429-747c-1ebb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8bd5-46cb-b7af-2992" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="de2b-e55a-8b42-4ccd" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8ee1-e71d-1b68-a7be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6343-0cab-f06f-390e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2dc2-6d88-66c5-5a76" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5556-d8cc-caed-c0be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ecf2-89d2-d755-4394" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3e50-2f84-bbf9-96e2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d55b-fc6d-7011-d15a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7446-6ca8-8d88-8066" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8015-2c61-6ba2-2789" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8761-3b5e-85b6-ea12" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e22d-ef1e-7c89-bd4e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0488-c965-72de-ddfa" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e4-5cf0-bf08-4f86" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e717-d341-836f-2587" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="fe01-c909-2892-dfdb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8987-b1ad-4139-fbf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8555-2a5b-4626-576c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="168a-0d36-17dc-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="274d-e7f2-1169-b937" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b761-0cdc-ecd9-115d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="0">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="deb1-afb0-adb0-35f5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c498-30a0-abb8-9a0e" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6c96-52e8-a508-6265" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="563b-400b-59e4-fb06" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="25b3-496d-3222-47d5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="8962-12c2-9bdf-5a66" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30c3-6521-02cf-92ff" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7afc-8c40-ab61-1fb5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="c53d-dd59-2fda-d3ce" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e16a-1045-813d-8a7e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="e3fb-07d7-d4f8-72ef" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4289-2356-a73d-68eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ccaa-7c64-def4-a6e3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a7a7-9dea-53a5-b5fc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b854-9a67-fa30-a582" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0903-cb0d-bae2-7501" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="75c7-d343-1140-dd39" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3245-e0f6-f847-1b74" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="673a-6d66-308a-29cd" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7031-7960-f06a-2500" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1631-2694-7938-a545" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9498-7200-5dc8-05df" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1641-9429-747c-1ebb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6ef0-a7a4-52dc-958a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5a92-461b-a7d4-c2d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="337f-56e7-8271-9da5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5913-f885-5429-d735" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="dfad-e049-0e8d-eb05" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="acaa-43b1-c815-72f2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0b6e-4b03-466f-bf4f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39e0-d11d-3ba7-3303" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="e75c-23e9-d3a1-5776" name="Cavalry and Chariots" hidden="false" targetId="d770-0479-ccc5-fa90" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="7ce4-868d-cff5-30d1" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="7ce4-868d-cff5-30d1" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6d4b-7fde-55a6-b187" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7ce4-868d-cff5-30d1" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2d05-8c94-0564-9abf" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7ce4-868d-cff5-30d1" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="18f0-175f-4e79-c39a" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="0a44-ce29-03ff-7291" name="Characters" hidden="false" targetId="d087-5488-98c4-52b6" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="835a-e3d9-7c19-a1aa" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6d4b-7fde-55a6-b187" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="070d-d2cd-a6e4-9986" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4dfd-fa14-099f-810e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e5cb-4ef8-1220-da2e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7ea3-93b7-6770-5e52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bbe9-5425-84d2-0602" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b9ef-b43e-36be-5a69" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4d74-a514-2459-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2d05-8c94-0564-9abf" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="18f0-175f-4e79-c39a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="e317-4c41-6256-6973" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9640-4e8c-c5b2-04ae" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="563b-400b-59e4-fb06" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="25b3-496d-3222-47d5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7337-545b-6742-671e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d8dc-445d-2169-6605" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e6af-de44-a4b3-e983" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="259a-a6ef-99fa-f122" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3657-6674-fa87-e835" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c4b2-abeb-f8cf-0988" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="92e7-f4c4-c2b8-248f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f7ce-737d-155e-b5c0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="903f-cf5e-5a96-3642" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a32d-ef40-094e-5557" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33a4-8318-706d-35c0" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4c6e-ae33-4b0c-cc05" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3cbd-723c-2d07-a742" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="088f-a5dc-272e-eb17" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="24a5-de3b-051c-598f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1fec-1a3c-8f39-9165" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cfe2-fbc9-d618-9b51" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f937-8a87-b29a-7dbe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3050-88a2-6512-4266" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="806d-b96b-32c3-fefe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5302-8994-908a-5bf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cd81-de2d-3324-8ef5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="28dc-fd35-1d26-7e77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a8ef-819c-e704-677f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="328b-e11d-b8f6-018a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1ea2-ee62-2aab-f4b7" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f311-3602-fff3-d7eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bfb9-d9ae-bab5-e025" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="da14-812b-9f0f-b0a6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2d17-3611-d106-f4c6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d265-0a84-8b65-6ff7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2c1-ac13-d737-e9a7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6391-39aa-7a7c-838f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f0e3-1e52-8d8c-bc44" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b68c-1a9f-6ab8-aeb4" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cad2-fb2e-4857-a0eb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1f3e-ee53-0849-f772" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6cdb-0884-d537-7b7b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="677a-dd5f-38aa-b0b9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d328-acd5-abe6-f9f8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0c0d-204f-6a50-9878" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ca2f-c852-f793-2c5b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8911-38f7-f066-9682" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb0e-4009-8866-37d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="82e2-17f3-9229-da71" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b25c-d287-98e6-0348" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bbb-4938-22b7-f448" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e001-92db-8133-4ba9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bb97-f0e3-0c62-fe56" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2501-daac-06e2-9700" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bd7-798e-a0b7-097b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700e-e22c-373d-9eb5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e2-c8d5-1d5a-828f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="060c-b6b4-1093-2f6e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2de-f5e9-c065-f082" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d447-6b15-fb75-1c8b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb5b-a35e-5109-e891" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8196-da29-92e0-00c6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="12b1-6fe7-9a7c-bd6a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-4351-d097-a665" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1707-4e96-c7d2-2edc" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="741c-fd3d-4d6f-cb25" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700f-ca38-3250-8b1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0632-d00f-88f4-ca36" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cbde-3cfc-f625-caa3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e15-d81e-9e7c-dca8" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9cd7-9074-1079-a416" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e16a-1045-813d-8a7e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c9b6-0f75-a848-579d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4cdd-c505-ebb3-6e24" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cc81-2a63-ef23-1ff6" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cf07-8103-8a22-6cd8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2df5-5c3e-f0ee-3910" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="17d8-e6c6-69e6-dd80" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1775-8ccf-e2d9-bd8e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7576-1447-92b5-2d67" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9da3-d00a-b05f-b9ea" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="20">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="52f6-e805-2e4a-6d4e" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4289-2356-a73d-68eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ccaa-7c64-def4-a6e3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bc4f-5679-701f-016a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a7a7-9dea-53a5-b5fc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b854-9a67-fa30-a582" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0903-cb0d-bae2-7501" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="75c7-d343-1140-dd39" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3245-e0f6-f847-1b74" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="74f5-b5d8-4625-3175" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="673a-6d66-308a-29cd" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2aa-65a8-fbd1-ad0e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bd14-1b77-1a71-685e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9d7f-dae0-fa10-cc77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6b4f-8c2d-cd11-2788" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="37d6-fcaa-7fa8-9e5d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0d41-30d7-3a48-ffee" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f0ed-e71d-802a-591d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7031-7960-f06a-2500" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1631-2694-7938-a545" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4ddc-9a9c-c7de-308e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a33-2077-d386-77ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d4b1-de1b-4481-449a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ad99-93a0-2c6b-b892" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="019a-902d-4fdd-a496" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9498-7200-5dc8-05df" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1641-9429-747c-1ebb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="30">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="30">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8bd5-46cb-b7af-2992" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="de2b-e55a-8b42-4ccd" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9072-5a61-28d2-ef0b" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8ee1-e71d-1b68-a7be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6343-0cab-f06f-390e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2dc2-6d88-66c5-5a76" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5556-d8cc-caed-c0be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ecf2-89d2-d755-4394" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6ef0-a7a4-52dc-958a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3e50-2f84-bbf9-96e2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d55b-fc6d-7011-d15a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7446-6ca8-8d88-8066" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8015-2c61-6ba2-2789" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c16d-100c-f576-e8f5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3084-ae79-fd51-a95f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a0f-273a-eb20-824c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7e35-7fef-9e15-7fe6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7927-bc89-6620-fe52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-0500-bed2-fcce" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8761-3b5e-85b6-ea12" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e22d-ef1e-7c89-bd4e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="495a-5036-c4d2-91ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0488-c965-72de-ddfa" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e4-5cf0-bf08-4f86" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e717-d341-836f-2587" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="fe01-c909-2892-dfdb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8987-b1ad-4139-fbf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8555-2a5b-4626-576c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="168a-0d36-17dc-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="274d-e7f2-1169-b937" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b761-0cdc-ecd9-115d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5a92-461b-a7d4-c2d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="337f-56e7-8271-9da5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="deb1-afb0-adb0-35f5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5913-f885-5429-d735" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="dfad-e049-0e8d-eb05" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="acaa-43b1-c815-72f2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39e0-d11d-3ba7-3303" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6c96-52e8-a508-6265" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="835a-e3d9-7c19-a1aa" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="d28f-0a2b-884a-cebb" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="a7c2-1554-89f9-dd13" name="Infantry" hidden="false" targetId="f3a3-2277-7808-2250" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="959b-b12c-054a-e973" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="9f0e-4146-4168-a5b3" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="563b-400b-59e4-fb06" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="25b3-496d-3222-47d5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="00e3-617c-a758-7e27" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6445-92bb-a222-2769" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="8962-12c2-9bdf-5a66" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7afc-8c40-ab61-1fb5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="c53d-dd59-2fda-d3ce" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bfb9-d9ae-bab5-e025" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="35">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7576-1447-92b5-2d67" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="40">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9da3-d00a-b05f-b9ea" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="100">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="52f6-e805-2e4a-6d4e" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4289-2356-a73d-68eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ccaa-7c64-def4-a6e3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bc4f-5679-701f-016a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a7a7-9dea-53a5-b5fc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b854-9a67-fa30-a582" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0903-cb0d-bae2-7501" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="75c7-d343-1140-dd39" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3245-e0f6-f847-1b74" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="673a-6d66-308a-29cd" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bd14-1b77-1a71-685e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9d7f-dae0-fa10-cc77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6b4f-8c2d-cd11-2788" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="37d6-fcaa-7fa8-9e5d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0d41-30d7-3a48-ffee" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f0ed-e71d-802a-591d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7031-7960-f06a-2500" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1631-2694-7938-a545" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4ddc-9a9c-c7de-308e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a33-2077-d386-77ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d4b1-de1b-4481-449a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ad99-93a0-2c6b-b892" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="019a-902d-4fdd-a496" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9498-7200-5dc8-05df" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1641-9429-747c-1ebb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5556-d8cc-caed-c0be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ecf2-89d2-d755-4394" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6ef0-a7a4-52dc-958a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3e50-2f84-bbf9-96e2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7446-6ca8-8d88-8066" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8015-2c61-6ba2-2789" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3084-ae79-fd51-a95f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a0f-273a-eb20-824c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7927-bc89-6620-fe52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="fe01-c909-2892-dfdb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8987-b1ad-4139-fbf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="168a-0d36-17dc-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="274d-e7f2-1169-b937" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5a92-461b-a7d4-c2d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="337f-56e7-8271-9da5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="dfad-e049-0e8d-eb05" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="acaa-43b1-c815-72f2" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39e0-d11d-3ba7-3303" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="959b-b12c-054a-e973" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6c96-52e8-a508-6265" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b9ef-b43e-36be-5a69" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4d74-a514-2459-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2d05-8c94-0564-9abf" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="18f0-175f-4e79-c39a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f7ce-737d-155e-b5c0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="903f-cf5e-5a96-3642" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a32d-ef40-094e-5557" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33a4-8318-706d-35c0" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4c6e-ae33-4b0c-cc05" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3cbd-723c-2d07-a742" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="088f-a5dc-272e-eb17" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="24a5-de3b-051c-598f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1fec-1a3c-8f39-9165" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cfe2-fbc9-d618-9b51" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f937-8a87-b29a-7dbe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1ea2-ee62-2aab-f4b7" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9a90-5e6c-502f-f214" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b87-c61b-cf53-c7b6" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f311-3602-fff3-d7eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9159-464d-82b0-35eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="390d-7fcd-6e5f-de36" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33ef-50ae-81a9-b2b9" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6314-5351-1265-115d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="84b5-af35-ff08-b1fb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="71b6-a7b0-f3d0-d621" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7a69-583d-d406-fbfc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3372-fa50-189e-8e4c" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ffe3-1936-272b-1780" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b54a-4a3e-53ff-e612" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4289-2356-a73d-68eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bc4f-5679-701f-016a" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a7a7-9dea-53a5-b5fc" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0903-cb0d-bae2-7501" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="75c7-d343-1140-dd39" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="74f5-b5d8-4625-3175" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="673a-6d66-308a-29cd" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f0ed-e71d-802a-591d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="66">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1e32-53e2-a02f-2141" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7031-7960-f06a-2500" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1631-2694-7938-a545" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4ddc-9a9c-c7de-308e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a33-2077-d386-77ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d4b1-de1b-4481-449a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ad99-93a0-2c6b-b892" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d55b-fc6d-7011-d15a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8761-3b5e-85b6-ea12" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e22d-ef1e-7c89-bd4e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="495a-5036-c4d2-91ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0488-c965-72de-ddfa" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e4-5cf0-bf08-4f86" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e717-d341-836f-2587" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8555-2a5b-4626-576c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b761-0cdc-ecd9-115d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9f0e-4146-4168-a5b3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="deb1-afb0-adb0-35f5" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="98ac-47a5-f36a-27ee" name="Men at Arms" hidden="false" targetId="db3d-508f-dcf6-1ae7" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="960a-16c9-6ffd-5743" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="960a-16c9-6ffd-5743" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9640-4e8c-c5b2-04ae" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="d0a7-6ff6-d47a-83ed" name="Skirmishers" hidden="false" targetId="8c10-93c8-bc16-a231" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="dfcb-64eb-5fb6-b8c6" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="dfcb-64eb-5fb6-b8c6" value="20">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2d05-8c94-0564-9abf" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="dfcb-64eb-5fb6-b8c6" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="e317-4c41-6256-6973" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="dfcb-64eb-5fb6-b8c6" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cbde-3cfc-f625-caa3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="dfcb-64eb-5fb6-b8c6" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e15-d81e-9e7c-dca8" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="dfcb-64eb-5fb6-b8c6" value="10">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4cdd-c505-ebb3-6e24" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8c8d-664d-dc74-8456" name="Auxiliaries" hidden="false" targetId="8726-6b4a-67e5-3134" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="6e22-bafa-840f-aecc" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="6e22-bafa-840f-aecc" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="92e7-f4c4-c2b8-248f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6e22-bafa-840f-aecc" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9159-464d-82b0-35eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6e22-bafa-840f-aecc" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6314-5351-1265-115d" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="f02d-7940-6e85-dc03" name="Legionaries" hidden="false" targetId="ac7c-c389-6c7b-9f98" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="e9c7-e7d1-5102-93d6" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="e9c7-e7d1-5102-93d6" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="92e7-f4c4-c2b8-248f" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="a8e3-8862-026b-da53" name="Special Units" hidden="false" targetId="099a-3435-f35a-fee2" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="7205-4ae8-6709-c2a3" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="abf8-3982-14a4-3dcc" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="563b-400b-59e4-fb06" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="92e7-f4c4-c2b8-248f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f7ce-737d-155e-b5c0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="903f-cf5e-5a96-3642" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a32d-ef40-094e-5557" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3050-88a2-6512-4266" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="806d-b96b-32c3-fefe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6314-5351-1265-115d" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="84b5-af35-ff08-b1fb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="71b6-a7b0-f3d0-d621" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b854-9a67-fa30-a582" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4ddc-9a9c-c7de-308e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a33-2077-d386-77ca" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d4b1-de1b-4481-449a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ad99-93a0-2c6b-b892" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="019a-902d-4fdd-a496" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c16d-100c-f576-e8f5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3084-ae79-fd51-a95f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a0f-273a-eb20-824c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7e35-7fef-9e15-7fe6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7927-bc89-6620-fe52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-0500-bed2-fcce" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="0">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e4-5cf0-bf08-4f86" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e717-d341-836f-2587" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="fe01-c909-2892-dfdb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8987-b1ad-4139-fbf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8555-2a5b-4626-576c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b761-0cdc-ecd9-115d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5a92-461b-a7d4-c2d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="337f-56e7-8271-9da5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39e0-d11d-3ba7-3303" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7205-4ae8-6709-c2a3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6c96-52e8-a508-6265" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="abf8-3982-14a4-3dcc" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="019a-902d-4fdd-a496" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="f7ab-21b4-fe88-a7f1" name="Supporting Infantry" hidden="false" targetId="3eca-1d1c-122a-3bef" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="0c6d-10e4-2b68-5b6d" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="0c6d-10e4-2b68-5b6d" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6d4b-7fde-55a6-b187" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0c6d-10e4-2b68-5b6d" value="20">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="18f0-175f-4e79-c39a" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="83f9-c4d2-ac4a-cadf" name="Warriors" hidden="false" targetId="ce31-a2e9-3e20-4277" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="8d53-1118-c560-34fe" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="cd38-de38-cd76-80bb" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="8d53-1118-c560-34fe" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="e3fb-07d7-d4f8-72ef" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6d4b-7fde-55a6-b187" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="e317-4c41-6256-6973" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9cd7-9074-1079-a416" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e16a-1045-813d-8a7e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c9b6-0f75-a848-579d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cd38-de38-cd76-80bb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4cdd-c505-ebb3-6e24" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="4e5e-e9af-badf-2093" name="Common Troops" hidden="false" targetId="cdbb-fd56-92b1-73b7" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c8b8-8db6-9e7d-37d6" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="070d-d2cd-a6e4-9986" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4dfd-fa14-099f-810e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e5cb-4ef8-1220-da2e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7ea3-93b7-6770-5e52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bbe9-5425-84d2-0602" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7337-545b-6742-671e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d8dc-445d-2169-6605" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e6af-de44-a4b3-e983" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="259a-a6ef-99fa-f122" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="65">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3657-6674-fa87-e835" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c8b8-8db6-9e7d-37d6" value="65">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c4b2-abeb-f8cf-0988" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="bd11-9d43-6152-da10" name="Uncommon Troops" hidden="false" targetId="d68a-ed84-1d75-2f64" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="d64a-6c53-6d6f-8996" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="070d-d2cd-a6e4-9986" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4dfd-fa14-099f-810e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e5cb-4ef8-1220-da2e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7ea3-93b7-6770-5e52" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bbe9-5425-84d2-0602" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7337-545b-6742-671e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d8dc-445d-2169-6605" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e6af-de44-a4b3-e983" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="5">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="259a-a6ef-99fa-f122" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3657-6674-fa87-e835" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d64a-6c53-6d6f-8996" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c4b2-abeb-f8cf-0988" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="dd90-6b31-9267-af1f" name="Allies &amp; Mercenaries" hidden="false" targetId="38c4-e0a7-a7f3-dc77" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="3e5e-a95c-b649-aedb" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33a4-8318-706d-35c0" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4c6e-ae33-4b0c-cc05" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3cbd-723c-2d07-a742" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="088f-a5dc-272e-eb17" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="24a5-de3b-051c-598f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1fec-1a3c-8f39-9165" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cfe2-fbc9-d618-9b51" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f937-8a87-b29a-7dbe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b87-c61b-cf53-c7b6" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="00e3-617c-a758-7e27" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f311-3602-fff3-d7eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9159-464d-82b0-35eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="84b5-af35-ff08-b1fb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7afc-8c40-ab61-1fb5" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b54a-4a3e-53ff-e612" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0903-cb0d-bae2-7501" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="75c7-d343-1140-dd39" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bd14-1b77-1a71-685e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9d7f-dae0-fa10-cc77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6b4f-8c2d-cd11-2788" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="37d6-fcaa-7fa8-9e5d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="3e5e-a95c-b649-aedb" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0d41-30d7-3a48-ffee" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="a387-9976-014e-3da4" name="Chariotry" hidden="false" targetId="a178-280d-202c-b3d0" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="4118-2620-90e6-848e" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="39a2-1292-00da-7f3b" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="4118-2620-90e6-848e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33a4-8318-706d-35c0" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4118-2620-90e6-848e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3cbd-723c-2d07-a742" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4118-2620-90e6-848e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="24a5-de3b-051c-598f" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4118-2620-90e6-848e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9a90-5e6c-502f-f214" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4118-2620-90e6-848e" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b87-c61b-cf53-c7b6" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4118-2620-90e6-848e" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f311-3602-fff3-d7eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="39a2-1292-00da-7f3b" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="088f-a5dc-272e-eb17" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="39a2-1292-00da-7f3b" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="00e3-617c-a758-7e27" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="ccb7-f528-5524-db2a" name="Chariotry &amp; Cavalry" hidden="false" targetId="e85f-5baa-0bfe-26d6" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c584-4303-6f82-8dc3" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="4c6e-ae33-4b0c-cc05" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1fec-1a3c-8f39-9165" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cfe2-fbc9-d618-9b51" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f937-8a87-b29a-7dbe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9159-464d-82b0-35eb" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c584-4303-6f82-8dc3" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b54a-4a3e-53ff-e612" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="659c-9c69-5c97-667c" name="Barbarian Cavalry" hidden="false" targetId="368d-33dc-12e4-8b16" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="932a-c0fb-085d-7f11" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="932a-c0fb-085d-7f11" value="0">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="5302-8994-908a-5bf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="932a-c0fb-085d-7f11" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cd81-de2d-3324-8ef5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="932a-c0fb-085d-7f11" value="40">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="28dc-fd35-1d26-7e77" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="932a-c0fb-085d-7f11" value="100">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a8ef-819c-e704-677f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="932a-c0fb-085d-7f11" value="100">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="328b-e11d-b8f6-018a" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="21a2-03af-8d6e-3ef0" name="Barbarian Infantry" hidden="false" targetId="773a-1fbb-6862-e9c1" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="4d62-832f-b418-eb23" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="450f-72ed-5cb8-487f" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="4d62-832f-b418-eb23" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="a8ef-819c-e704-677f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="4d62-832f-b418-eb23" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="328b-e11d-b8f6-018a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="450f-72ed-5cb8-487f" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cd81-de2d-3324-8ef5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="450f-72ed-5cb8-487f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="28dc-fd35-1d26-7e77" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="af16-2e71-4dd2-f159" name="Roman Cavalry" hidden="false" targetId="3ae2-1ee1-7d21-6c5b" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="a668-c96b-2f24-6ae7" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="1cf1-4503-e254-13c7" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="a668-c96b-2f24-6ae7" value="60">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3050-88a2-6512-4266" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="a668-c96b-2f24-6ae7" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="806d-b96b-32c3-fefe" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1cf1-4503-e254-13c7" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3050-88a2-6512-4266" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1cf1-4503-e254-13c7" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="806d-b96b-32c3-fefe" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="767a-2c03-190f-bef3" name="Roman Infantry" hidden="false" targetId="87bc-1d1e-35cf-c4e8" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="09c9-d250-57fc-8b1e" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="09c9-d250-57fc-8b1e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3050-88a2-6512-4266" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="09c9-d250-57fc-8b1e" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="806d-b96b-32c3-fefe" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="ec5f-cf1f-db9d-d6ad" name="Steppe Cavalry" hidden="false" targetId="0c18-c369-b2f7-93f2" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c59c-b61d-f34c-81ed" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c59c-b61d-f34c-81ed" value="20">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="28dc-fd35-1d26-7e77" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="3f7b-e17e-45df-7e19" name="Allies &amp; Tribal Mercenaries" hidden="false" targetId="ca02-eacc-ee23-4d57" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="d36d-1736-6d58-a8d5" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="d36d-1736-6d58-a8d5" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9a90-5e6c-502f-f214" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="5643-de3b-f97e-6b6d" name="Archers &amp; Unusual Troops" hidden="false" targetId="5f09-a420-168c-b2d9" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="211f-aa1e-0a06-d992" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="211f-aa1e-0a06-d992" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3372-fa50-189e-8e4c" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="28e4-002f-cfd3-2a56" name="Elephants, Chariots &amp; Cavalry" hidden="false" targetId="1357-310c-56af-a94b" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="dbea-21fc-2ce9-288f" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="dbea-21fc-2ce9-288f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33ef-50ae-81a9-b2b9" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="9fa9-ea5c-5190-4fe2" name="Levies &amp; Mercenaries" hidden="false" targetId="7f33-e2a4-4915-c8f4" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="fd21-0ec9-fa49-e6a0" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="fd21-0ec9-fa49-e6a0" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7897-407e-afad-c641" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="37b7-9f9d-0946-d6bb" name="Light Infantry" hidden="false" targetId="9028-a3e9-f537-115c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="83ad-6ad5-bd88-3e30" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="83ad-6ad5-bd88-3e30" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eaae-80c3-653b-cdff" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="9bb4-7a18-6067-79cf" name="Persian Troops" hidden="false" targetId="6c4c-d645-e7f7-f2d8" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="951e-051d-3682-cab0" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="951e-051d-3682-cab0" value="75">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7897-407e-afad-c641" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="3377-b416-f52a-7e73" name="Phalanx" hidden="false" targetId="88db-8178-1680-7486" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="51a7-e7b4-11d6-0df9" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="51a7-e7b4-11d6-0df9" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eaae-80c3-653b-cdff" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="e118-6673-811e-7920" name="Samurai" hidden="false" targetId="1da8-c9f1-705c-6a6f" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="4ce6-2e8c-d2c6-d18f" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="4ce6-2e8c-d2c6-d18f" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bfb9-d9ae-bab5-e025" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8658-805c-e082-86e8" name="Special Troops" hidden="false" targetId="897c-92a0-c2d2-53ca" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="1995-38ba-b786-301f" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7897-407e-afad-c641" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="8962-12c2-9bdf-5a66" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cf07-8103-8a22-6cd8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2df5-5c3e-f0ee-3910" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="17d8-e6c6-69e6-dd80" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="1995-38ba-b786-301f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1775-8ccf-e2d9-bd8e" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="77cd-100e-73e4-2464" name="Special Troops &amp; Allies" hidden="false" targetId="2151-69a6-7085-b914" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="e85b-ebde-1e90-74c0" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="e85b-ebde-1e90-74c0" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="390d-7fcd-6e5f-de36" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="e85b-ebde-1e90-74c0" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="ffe3-1936-272b-1780" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="d0ec-a22c-5728-1ee4" name="Special Troops &amp; Mercenaries" hidden="false" targetId="3124-ccb8-55cc-4fb3" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="32b0-9b07-0b6f-b9bd" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="32b0-9b07-0b6f-b9bd" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7a69-583d-d406-fbfc" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="de3e-35c0-9be2-da07" name="Special Troops, Allies &amp; Mercenaries" hidden="false" targetId="2040-2309-97cc-fd89" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="df04-06ba-7c3f-8303" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="df04-06ba-7c3f-8303" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30c3-6521-02cf-92ff" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="df04-06ba-7c3f-8303" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="c53d-dd59-2fda-d3ce" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="c622-07a6-fa90-1e87" name="War Machines" hidden="false" targetId="0654-a713-ca15-c866" primary="false"/>
        <categoryLink id="c488-466e-a240-ce17" name="Common Warriors: Milites and Liberi" hidden="false" targetId="6eb7-9942-f37d-32df" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="0521-be64-6f01-d145" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="0521-be64-6f01-d145" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e2-c8d5-1d5a-828f" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="fbb5-5f98-93bd-ab98" name="Common Warriors: Milites and Pueri" hidden="false" targetId="59cd-febb-ea2a-b90a" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="d73f-1d76-8093-ba5e" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="d73f-1d76-8093-ba5e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="060c-b6b4-1093-2f6e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="d73f-1d76-8093-ba5e" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2de-f5e9-c065-f082" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="b199-ceb8-fa78-28a0" name="Common Warriors: Toisech and Soer-chele" hidden="false" targetId="b2e8-8a8b-a1b9-30a4" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="4ccf-f005-1c1f-dfd1" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="4ccf-f005-1c1f-dfd1" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ca2f-c852-f793-2c5b" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="86af-2c73-8c86-e5a5" name="Common Warriors: Toisech, Eachraidh, Soer-chele and Doer-chele" hidden="false" targetId="0f53-e23c-3ec0-9fe3" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="3270-7bb8-c987-a613" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="3270-7bb8-c987-a613" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8911-38f7-f066-9682" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="6db6-6553-9e74-244c" name="Common Warriors: Toisech, Soer-chele and Doer-chele" hidden="false" targetId="a6c2-7b01-428a-5002" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="2313-7f11-82b4-ecad" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="2313-7f11-82b4-ecad" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="677a-dd5f-38aa-b0b9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="2313-7f11-82b4-ecad" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d328-acd5-abe6-f9f8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="2313-7f11-82b4-ecad" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0c0d-204f-6a50-9878" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="6651-5818-08fe-0044" name="Uncommon Warriors: Coloni and Dogs of War" hidden="false" targetId="c9c8-3285-67ba-9053" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="d5a7-a4a3-053c-a6e2" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="d5a7-a4a3-053c-a6e2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2de-f5e9-c065-f082" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="6c2f-7fad-eab6-f035" name="Uncommon Warriors: Doer-chele, Eachraidh and Dogs of War" hidden="false" targetId="3b71-8f3d-d210-a108" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="3ef0-4470-e9fe-b352" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="3ef0-4470-e9fe-b352" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="ca2f-c852-f793-2c5b" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="b812-7770-e185-0e2e" name="Uncommon Warriors: Eachraidh and Dogs of War" hidden="false" targetId="5603-085f-62f4-c42f" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="73a0-0096-537d-224b" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="73a0-0096-537d-224b" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="677a-dd5f-38aa-b0b9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="73a0-0096-537d-224b" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d328-acd5-abe6-f9f8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="73a0-0096-537d-224b" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0c0d-204f-6a50-9878" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="36ab-710b-0581-1d1c" name="Uncommon Warriors: Liberi, Coloni and Dogs of War" hidden="false" targetId="fcf2-d68f-f22f-4460" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="2381-1253-1f72-a915" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="2381-1253-1f72-a915" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="060c-b6b4-1093-2f6e" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="c907-3d5d-9a0e-7134" name="Uncommon Warriors: Pueri, Coloni and Dogs of War" hidden="false" targetId="491c-de44-9505-3e4b" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="e526-193c-058e-02c9" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="e526-193c-058e-02c9" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="67e2-c8d5-1d5a-828f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="e526-193c-058e-02c9" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d447-6b15-fb75-1c8b" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="0ef8-6a9f-c830-5d22" name="Uncommon Warriors: Pueri, Liberi, Coloni and Dogs of War" hidden="false" targetId="ad27-4da1-3028-5533" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="a0e2-e5e1-4ad8-c4d1" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="a0e2-e5e1-4ad8-c4d1" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700e-e22c-373d-9eb5" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="bd98-3948-a66f-55fb" name="Coloni" hidden="false" targetId="2bde-edde-d265-2a6a" primary="false"/>
        <categoryLink id="44fd-f1b3-146a-af1c" name="Common Warriors" hidden="false" targetId="bb52-a098-8217-fad7" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="e0cc-b055-706c-9741" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="bd2c-3f66-10f6-3862" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="e0cc-b055-706c-9741" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cad2-fb2e-4857-a0eb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="e0cc-b055-706c-9741" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1f3e-ee53-0849-f772" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="e0cc-b055-706c-9741" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bb97-f0e3-0c62-fe56" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="e0cc-b055-706c-9741" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bd7-798e-a0b7-097b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="da14-812b-9f0f-b0a6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2d17-3611-d106-f4c6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d265-0a84-8b65-6ff7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2c1-ac13-d737-e9a7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6391-39aa-7a7c-838f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f0e3-1e52-8d8c-bc44" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b68c-1a9f-6ab8-aeb4" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6cdb-0884-d537-7b7b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb0e-4009-8866-37d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="82e2-17f3-9229-da71" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b25c-d287-98e6-0348" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bbb-4938-22b7-f448" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e001-92db-8133-4ba9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="bd2c-3f66-10f6-3862" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2501-daac-06e2-9700" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="b15f-d321-d2c6-05e4" name="Doer-chele" hidden="false" targetId="9568-2556-e209-055d" primary="false"/>
        <categoryLink id="96d3-3948-d9bc-fd52" name="Dogs of War" hidden="false" targetId="a57d-15cd-e77c-b15b" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c81f-d959-5a72-c54f" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c81f-d959-5a72-c54f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8911-38f7-f066-9682" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="466f-84c2-cb10-1ca8" name="Eachraidh" hidden="false" targetId="1cc6-442e-e168-ff3b" primary="false"/>
        <categoryLink id="48b1-ead2-2757-808b" name="Fianna" hidden="false" targetId="f27b-2cf4-9b3d-b4e8" primary="false"/>
        <categoryLink id="4d8e-aa31-05a6-1e34" name="Liberi" hidden="false" targetId="b697-d3d4-1f93-7bb9" primary="false"/>
        <categoryLink id="5eb6-ae94-8951-3bc8" name="Milites" hidden="false" targetId="4695-1bd4-a060-f529" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="35c6-fd61-0a28-30b8" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="35c6-fd61-0a28-30b8" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700e-e22c-373d-9eb5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="35c6-fd61-0a28-30b8" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d447-6b15-fb75-1c8b" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="db6c-c290-af63-4565" name="Pueri" hidden="false" targetId="c5fb-f798-53f2-3293" primary="false"/>
        <categoryLink id="4f96-0524-ca26-f847" name="Soer-chele" hidden="false" targetId="045c-f9f8-81f6-9a17" primary="false"/>
        <categoryLink id="611b-b30c-8eed-182f" name="Teulu" hidden="false" targetId="0c80-93da-4649-b3ed" primary="false"/>
        <categoryLink id="da38-cc94-a682-09a3" name="Toisech" hidden="false" targetId="5ad7-c087-1636-0808" primary="false"/>
        <categoryLink id="814a-654d-7408-69a4" name="Uncommon Warriors" hidden="false" targetId="b2c1-cc28-9aef-021d" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="9a05-798d-10bc-17d2" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="da14-812b-9f0f-b0a6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2d17-3611-d106-f4c6" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="d265-0a84-8b65-6ff7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2c1-ac13-d737-e9a7" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6391-39aa-7a7c-838f" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f0e3-1e52-8d8c-bc44" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b68c-1a9f-6ab8-aeb4" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cad2-fb2e-4857-a0eb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1f3e-ee53-0849-f772" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6cdb-0884-d537-7b7b" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb0e-4009-8866-37d5" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="82e2-17f3-9229-da71" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b25c-d287-98e6-0348" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bbb-4938-22b7-f448" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e001-92db-8133-4ba9" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="bb97-f0e3-0c62-fe56" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2501-daac-06e2-9700" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="9a05-798d-10bc-17d2" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="4bd7-798e-a0b7-097b" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8d83-86a9-1331-6caa" name="Common Troops: Almohads" hidden="false" targetId="2cd3-c879-de42-09e1" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="e167-f620-50a5-2865" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="e167-f620-50a5-2865" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0632-d00f-88f4-ca36" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="4883-0e15-b985-1c1c" name="Common Troops: Almoravids" hidden="false" targetId="dbb8-9f3f-9f8f-11d4" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="da8f-7092-2d54-57c4" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="da8f-7092-2d54-57c4" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700f-ca38-3250-8b1c" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="68a4-cb5c-731e-9c6e" name="Common Troops: Asturias" hidden="false" targetId="a586-ba18-2b12-17d7" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="2887-cb62-6a39-4ddc" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="2887-cb62-6a39-4ddc" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb5b-a35e-5109-e891" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="5dd1-9da5-d04a-bfa0" name="Common Troops: Caliphate" hidden="false" targetId="7e2f-27c5-2dfa-e4c4" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="434e-5c93-0c4b-1f92" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="434e-5c93-0c4b-1f92" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-4351-d097-a665" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="6831-c900-bcfe-fa41" name="Common Troops: El Cid" hidden="false" targetId="74ba-c414-a747-826c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c4d4-3f2c-3e02-a2b0" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c4d4-3f2c-3e02-a2b0" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8196-da29-92e0-00c6" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="7109-0f06-183c-7ad8" name="Common Troops: Later Taifas" hidden="false" targetId="0f38-8e4a-4501-637d" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="fd59-34fb-af1c-a2b6" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="fd59-34fb-af1c-a2b6" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="741c-fd3d-4d6f-cb25" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="178a-411d-2084-13d2" name="Common Troops: Reconquista" hidden="false" targetId="b872-0eb8-f3ff-3328" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="cf25-9cfe-5046-1e43" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="cf25-9cfe-5046-1e43" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="12b1-6fe7-9a7c-bd6a" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="577d-54a0-ad57-3a04" name="Common Troops: Taifa Kings" hidden="false" targetId="1934-e02e-865a-2b1c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="a415-521e-501f-f00f" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="a415-521e-501f-f00f" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1707-4e96-c7d2-2edc" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="e0dc-75e5-3ff6-e5fd" name="Uncommon Troops: Almohads" hidden="false" targetId="0ac0-dae6-4188-ea2f" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c040-cf52-d54d-7fca" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c040-cf52-d54d-7fca" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="0632-d00f-88f4-ca36" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="330c-b072-8f7d-072f" name="Uncommon Troops: Almoravids" hidden="false" targetId="8b91-1442-3cda-0b13" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="d232-8dc2-5612-9089" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="d232-8dc2-5612-9089" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="700f-ca38-3250-8b1c" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="0bb2-0b7b-2e63-261e" name="Uncommon Troops: Asturias" hidden="false" targetId="8407-d89b-e464-8d60" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="0a40-0b67-bb7b-1d34" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="0a40-0b67-bb7b-1d34" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="eb5b-a35e-5109-e891" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="884d-513a-f68a-950b" name="Uncommon Troops: Caliphate" hidden="false" targetId="bba4-74e9-5777-576d" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="abc7-6449-945c-5441" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="abc7-6449-945c-5441" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8a97-4351-d097-a665" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="4175-09d7-1636-99df" name="Uncommon Troops: El Cid" hidden="false" targetId="3c53-38ef-b9fd-a47c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="9b8e-3d30-ffc9-4144" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="9b8e-3d30-ffc9-4144" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8196-da29-92e0-00c6" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="b7d5-4a4c-5387-f4d2" name="Uncommon Troops: Later Taifas" hidden="false" targetId="ca86-292e-7943-d805" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="1313-0427-1123-4176" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="1313-0427-1123-4176" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="741c-fd3d-4d6f-cb25" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8744-51c4-a516-c28b" name="Uncommon Troops: Reconquista" hidden="false" targetId="6c2a-b2f2-0777-f4d5" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="50cb-9851-3a21-f1c9" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="50cb-9851-3a21-f1c9" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="12b1-6fe7-9a7c-bd6a" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="e854-ec39-d1cf-ce92" name="Uncommon Troops: Taifa Kings" hidden="false" targetId="575e-eca8-12af-72bd" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="4172-0d76-fe29-86c5" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="4172-0d76-fe29-86c5" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1707-4e96-c7d2-2edc" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="9669-9661-23fc-5b43" name="Aliados y Mercenarios" hidden="false" targetId="0362-7f31-842f-ced0" primary="false"/>
        <categoryLink id="a517-c3c4-1f49-1121" name="Allies &amp; War Machines" hidden="false" targetId="2ba8-a026-3d74-e93b" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="ca90-c30f-9939-5100" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="ca90-c30f-9939-5100" value="15">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cc81-2a63-ef23-1ff6" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="5771-4c66-e8a1-9e2f" name="Cavalry &amp; Chariots" hidden="false" targetId="773a-59d9-404b-4250" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="8c9c-61af-065d-a5e3" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="8c9c-61af-065d-a5e3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cf07-8103-8a22-6cd8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="8c9c-61af-065d-a5e3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2df5-5c3e-f0ee-3910" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="8c9c-61af-065d-a5e3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="17d8-e6c6-69e6-dd80" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="8c9c-61af-065d-a5e3" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1775-8ccf-e2d9-bd8e" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="13b8-7130-60c0-06a9" name="Elephants" hidden="false" targetId="bb2d-5030-2e22-377f" primary="false"/>
        <categoryLink id="a5ce-e0f7-7519-deee" name="Infantry &amp; Skirmishers" hidden="false" targetId="52c5-947d-93d4-f122" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="6df0-42d7-b403-73af" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="6df0-42d7-b403-73af" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="cf07-8103-8a22-6cd8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6df0-42d7-b403-73af" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2df5-5c3e-f0ee-3910" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6df0-42d7-b403-73af" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="17d8-e6c6-69e6-dd80" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6df0-42d7-b403-73af" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="1775-8ccf-e2d9-bd8e" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="284d-6df2-9525-6823" name="Levies" hidden="false" targetId="5669-adf9-cb02-de9e" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="cdf5-e1d3-1e25-0437" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="cdf5-e1d3-1e25-0437" value="50">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cc81-2a63-ef23-1ff6" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="6f49-4959-d246-74fd" name="Persians" hidden="false" targetId="460c-f01b-046e-880c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="976d-46c8-a23f-d770" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="976d-46c8-a23f-d770" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cc81-2a63-ef23-1ff6" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="a31b-d2a2-4ff7-4033" name="Phalangites" hidden="false" targetId="80e0-112f-b3d4-3e5c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="ede8-d516-4685-c12b" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="ede8-d516-4685-c12b" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cbde-3cfc-f625-caa3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="ede8-d516-4685-c12b" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e15-d81e-9e7c-dca8" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="d398-2b70-730c-718e" name="Special Troops, Mercenaries &amp; Allies" hidden="false" targetId="c943-6d8d-bb33-47ee" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="ad5d-0900-5569-6341" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="ad5d-0900-5569-6341" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cbde-3cfc-f625-caa3" type="instanceOf"/>
              </conditions>
            </modifier>
            <modifier type="set" field="ad5d-0900-5569-6341" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e15-d81e-9e7c-dca8" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="908f-8eeb-11de-5b69" name="Wagons" hidden="false" targetId="ebc5-3647-ff9c-c887" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="c082-9fc8-0a1a-60be" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="c082-9fc8-0a1a-60be" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="9cd7-9074-1079-a416" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c082-9fc8-0a1a-60be" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e16a-1045-813d-8a7e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="c082-9fc8-0a1a-60be" value="10">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c9b6-0f75-a848-579d" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="698f-53e8-452d-5d4b" name="Cavalry/Support" hidden="false" targetId="d4df-79ed-bbda-72fa" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="1932-c30b-a51d-e0c2" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="1932-c30b-a51d-e0c2" value="33">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1e32-53e2-a02f-2141" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="fce3-5938-06d5-b96b" name="Janissaries" hidden="false" targetId="5719-2c0d-4245-2e4e" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="9609-8e9f-7452-1b42" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="9609-8e9f-7452-1b42" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="5a30-de1c-19c9-923d" name="Mercenaries" hidden="false" targetId="28b5-6150-ecee-a852" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="cec0-4755-633e-4df5" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="f8bf-1d62-1d6a-ee6f" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="cec0-4755-633e-4df5" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cec0-4755-633e-4df5" value="75">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3549-bcb3-8293-99a8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="39d6-d375-a0e0-0c70" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="00fc-33ad-c2e1-77ab" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="e2a6-c0e4-9477-6726" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7eaf-25a5-ba49-f1b0" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6597-d9f0-0473-0952" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7a5a-d8f2-87ba-b178" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="f8bf-1d62-1d6a-ee6f" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="326b-6891-0466-e32a" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="f84b-0ef3-be36-320b" name="Ottoman Cavalry" hidden="false" targetId="3c17-30e5-7804-209e" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="bb58-b01f-e8fb-e915" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="bb58-b01f-e8fb-e915" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="f0e3-fc94-9fec-c811" name="Turkoman &amp; Akincis Cavalry" hidden="false" targetId="a468-171c-369f-4b6c" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="f15b-710f-81c5-fc28" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="2875-4399-5a02-26c6" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="f15b-710f-81c5-fc28" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="2875-4399-5a02-26c6" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2aa-65a8-fbd1-ad0e" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="32f4-4d18-d49b-b9a7" name="Vassals" hidden="false" targetId="a520-8c56-9ab1-1f32" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="05fc-80d6-e5c6-32e1" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="05fc-80d6-e5c6-32e1" value="100">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2aa-65a8-fbd1-ad0e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="05fc-80d6-e5c6-32e1" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="a4c1-a245-f9c4-ab86" name="Vassals, Allies &amp; Mercenaries" hidden="false" targetId="8914-868d-c4b1-e363" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="6025-f75e-a457-0695" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="6025-f75e-a457-0695" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="3245-e0f6-f847-1b74" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6025-f75e-a457-0695" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="74f5-b5d8-4625-3175" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="351e-e5e6-f3e0-8d0b" name="Volunteers" hidden="false" targetId="32ce-bec3-9d66-e1ab" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="266d-a0f3-e925-5a4c" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="266d-a0f3-e925-5a4c" value="15">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="c2aa-65a8-fbd1-ad0e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="266d-a0f3-e925-5a4c" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="7957-daa2-010c-e9e8" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="75aa-2ce9-b06b-2228" name="Gallic and Germanic Slaves" hidden="false" targetId="839f-50bc-1cf6-bbba" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="6024-9dfc-1245-c637" type="max"/>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="cf13-2229-caf3-9261" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="6024-9dfc-1245-c637" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6024-9dfc-1245-c637" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="de2b-e55a-8b42-4ccd" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cf13-2229-caf3-9261" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="cf13-2229-caf3-9261" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8bd5-46cb-b7af-2992" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="cf21-aad0-1651-b15c" name="Auxiliaries &amp; Support Troops" hidden="false" targetId="9037-b2f4-17ba-8c97" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="a716-b4f8-329d-f1b6" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="a716-b4f8-329d-f1b6" value="20">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9072-5a61-28d2-ef0b" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="ea98-df1d-c673-104b" name="Conscript Legionaries" hidden="false" targetId="3434-abc8-b5fb-2dc2" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="1536-76e8-05f0-5374" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="1536-76e8-05f0-5374" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9072-5a61-28d2-ef0b" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="5429-cb8b-549b-075e" name="Experienced Legionaries" hidden="false" targetId="4b11-a070-f0c8-92f2" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="2934-8aef-fd22-02ec" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="2934-8aef-fd22-02ec" value="25">
              <conditions>
                <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9072-5a61-28d2-ef0b" type="instanceOf"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8d7a-6540-8417-26e5" name="Slave Infantry" hidden="false" targetId="7af6-6c4c-dd00-596a" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="0" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="0cf8-8ecd-54be-8dc8" type="min"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="45bc-c434-d0fe-493d" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8bd5-46cb-b7af-2992" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="de2b-e55a-8b42-4ccd" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="60">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8ee1-e71d-1b68-a7be" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="60">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="6343-0cab-f06f-390e" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="0cf8-8ecd-54be-8dc8" value="60">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="2dc2-6d88-66c5-5a76" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="8306-b6af-9fbe-cd01" name="Ghulams" hidden="false" targetId="bfb2-2e9c-2a30-fac2" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="7a41-18ec-7420-8712" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="7a41-18ec-7420-8712" value="40">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="fe01-c909-2892-dfdb" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7a41-18ec-7420-8712" value="66">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8987-b1ad-4139-fbf1" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7a41-18ec-7420-8712" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="8555-2a5b-4626-576c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7a41-18ec-7420-8712" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="168a-0d36-17dc-5a06" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7a41-18ec-7420-8712" value="33">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="274d-e7f2-1169-b937" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="7a41-18ec-7420-8712" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="b761-0cdc-ecd9-115d" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
        <categoryLink id="271c-0fd2-45bb-53a5" name="Light Cavalry" hidden="false" targetId="496f-313e-c4d8-b20a" primary="false">
          <constraints>
            <constraint field="limit::points" scope="roster" value="100" percentValue="true" shared="false" includeChildSelections="true" includeChildForces="false" id="6cf9-4f1b-6b11-4f91" type="max"/>
          </constraints>
          <modifiers>
            <modifier type="set" field="6cf9-4f1b-6b11-4f91" value="50">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="aa01-56d3-21c9-cf1c" type="atLeast"/>
              </conditions>
            </modifier>
            <modifier type="set" field="6cf9-4f1b-6b11-4f91" value="25">
              <conditions>
                <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="f50b-9084-3f14-b738" type="atLeast"/>
              </conditions>
            </modifier>
          </modifiers>
        </categoryLink>
      </categoryLinks>
    </forceEntry>
  </forceEntries>
  <selectionEntries>
    <selectionEntry id="070d-d2cd-a6e4-9986" name="First Punic War" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Carthaginian_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d5ab-8c9a-52ff-acf3" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="4dfd-fa14-099f-810e" name="Second Punic War in Spain" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Carthaginian_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="13ac-7375-5022-8891" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e5cb-4ef8-1220-da2e" name="Second Punic War in Italy" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Carthaginian_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2f3b-b407-d605-04a5" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7ea3-93b7-6770-5e52" name="Second Punic War in Africa" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Carthaginian_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ae56-ced9-388c-932e" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="bbe9-5425-84d2-0602" name="Third Punic War in Africa" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Carthaginian_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="30b1-e14e-f544-81c3" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="c0c5-6aa4-8e63-8037" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="b9ef-b43e-36be-5a69" name="Early Army 30 BC to 110 AD" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Imperial_Roman.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="77be-8814-23e3-4ce5" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="5661-d7a5-6977-6c18" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="4d74-a514-2459-5a06" name="Later Army 110 AD to 193 AD" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Imperial_Roman.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="77be-8814-23e3-4ce5" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="1993-ef2e-5c11-ab57" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7337-545b-6742-671e" name="First Punic War" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="69f4-dc0f-11d4-1306" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d8dc-445d-2169-6605" name="Second Punic War in Spain" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="0ac3-7087-69d9-598d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e6af-de44-a4b3-e983" name="Second Punic War in Italy" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="910b-c540-9d7c-bee2" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="259a-a6ef-99fa-f122" name="Second and Third Punic Wars in Africa" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="1e44-e4aa-580e-2884" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3657-6674-fa87-e835" name="Campaigns in the West" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a3f6-1eec-4159-c4b9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="c4b2-abeb-f8cf-0988" name="Campaigns in the East" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Republican_Roman_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9c9b-cdcf-a528-ea88" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f905-f731-bbc8-5672" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="f7ce-737d-155e-b5c0" name="Iberians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Spanish_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="178c-ffbc-b301-16ba" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2613-a790-c620-b7bb" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="903f-cf5e-5a96-3642" name="Celtiberians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Spanish_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="178c-ffbc-b301-16ba" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f51c-a84e-c2b9-9847" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="a32d-ef40-094e-5557" name="Lusitanians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Spanish_Hannibal.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="178c-ffbc-b301-16ba" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b359-82fc-1669-3cd9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="cfe2-fbc9-d618-9b51" name="Assyrian" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Assyrian_Chariot_Wars.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eb28-6ed4-bf69-dbe1" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="e45e-9371-31e4-d58d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="f937-8a87-b29a-7dbe" name="Babylonian" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Assyrian_Chariot_Wars.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="eb28-6ed4-bf69-dbe1" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2c97-1f55-aed9-39f0" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3050-88a2-6512-4266" name="Limitanei" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Roman_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="50be-dbef-ae9e-f1d0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="404a-14f0-bfc3-9ac7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="806d-b96b-32c3-fefe" name="Comitatenses" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Roman_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="50be-dbef-ae9e-f1d0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f53b-f64f-1a69-6dc7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="5302-8994-908a-5bf1" name="Sea Raiders" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Barbarian_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="05e7-ca12-2723-f6c2" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="cd81-de2d-3324-8ef5" name="Western Barbarians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Barbarian_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="4097-f6c0-1864-c7cd" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="28dc-fd35-1d26-7e77" name="Central Barbarians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Barbarian_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="3a93-0fd8-0892-c6e8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="a8ef-819c-e704-677f" name="Eastern Barbarians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Barbarian_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="41de-73b7-b3f3-c449" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="328b-e11d-b8f6-018a" name="North African" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Barbarian_Fall_of_the_West.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="35a7-4fe9-8ce7-4dc8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6f4e-45f0-1f96-e59e" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="da14-812b-9f0f-b0a6" name="Norwegians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Northmen_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="57b0-86c5-ec8a-8b9c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="2d17-3611-d106-f4c6" name="Danes" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Northmen_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="341e-d743-301b-68ee" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d265-0a84-8b65-6ff7" name="Hiberno-Norse" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Northmen_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="c9e8-db0d-c1e2-953b" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e2c1-ac13-d737-e9a7" name="Orkneyinga" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Northmen_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ec53-4cc3-32fd-3132" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6391-39aa-7a7c-838f" name="Kingdom of the Isles" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Northmen_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="2544-bf63-92be-1e97" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="be94-cddc-4581-e804" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="f0e3-1e52-8d8c-bc44" name="Wessex" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="c3fb-f7a3-59a1-bb88" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="b68c-1a9f-6ab8-aeb4" name="Mercia" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="cd13-02ce-a35c-346b" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="cad2-fb2e-4857-a0eb" name="Northumbria" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="626a-75f3-ede4-2565" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="1f3e-ee53-0849-f772" name="Anglia" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="11a0-dc2f-b570-00ca" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6cdb-0884-d537-7b7b" name="Kent &amp; the Home Counties" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="7874-ab14-bb42-91bc" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a694-f835-a22f-2bfc" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="677a-dd5f-38aa-b0b9" name="Dal Riata" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Caledonians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2a74-c135-9730-2b55" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d328-acd5-abe6-f9f8" name="Alba" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Caledonians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="bf9d-f9b6-882f-1be4" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="0c0d-204f-6a50-9878" name="The Picts (the Cruithne)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Caledonians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a120-e56d-0b96-bb56" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="ca2f-c852-f793-2c5b" name="Scotland" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Caledonians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="5bef-8f12-21fd-f44d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8911-38f7-f066-9682" name="Strathclyde" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Caledonians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b97e-a61f-c356-33c6" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="04cd-91f0-b77c-73c1" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="eb0e-4009-8866-37d5" name="Gwynedd" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Welsh_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b904-05df-7dcd-cae7" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="9fb7-c5b2-876e-00d7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="82e2-17f3-9229-da71" name="Powys" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Welsh_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b904-05df-7dcd-cae7" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="79cd-8000-94e5-4f6b" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="b25c-d287-98e6-0348" name="Southern Kingdoms" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Welsh_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b904-05df-7dcd-cae7" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="06ad-d008-015a-5001" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="4bbb-4938-22b7-f448" name="Dumnonia" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Welsh_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b904-05df-7dcd-cae7" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="51fc-56f1-bf0b-f373" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e001-92db-8133-4ba9" name="Munster" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Hibernians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b90f-6192-92f7-0af0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="3b88-258d-af38-8269" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="bb97-f0e3-0c62-fe56" name="Leinster" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Hibernians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b90f-6192-92f7-0af0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="0019-bfe2-2f7b-e9b7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="2501-daac-06e2-9700" name="Connacht" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Hibernians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b90f-6192-92f7-0af0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="fa9b-56ba-27c5-91cb" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="4bd7-798e-a0b7-097b" name="Ulster" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Hibernians_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b90f-6192-92f7-0af0" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="7fae-add6-49b2-a05a" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="700e-e22c-373d-9eb5" name="Carolingian French" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Western_Franks_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b59c-4bd8-02c0-4981" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="67e2-c8d5-1d5a-828f" name="County of Flanders" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Western_Franks_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a614-f068-9d83-90d6" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="060c-b6b4-1093-2f6e" name="Duchy of Normandy" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Western_Franks_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="afda-111c-e47f-d481" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="c2de-f5e9-c065-f082" name="The Bretons" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Western_Franks_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="df65-fbb0-5f8f-c036" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d447-6b15-fb75-1c8b" name="Capetian French" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Western_Franks_Shieldwall.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="09db-2845-0f7d-ed78" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="86b6-8686-c15b-fcd9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="eb5b-a35e-5109-e891" name="Asturias" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Christian_Spain_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f89e-42a7-5272-fedd" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="0cd4-764b-23ef-1e3d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8196-da29-92e0-00c6" name="El Cid" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Christian_Spain_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f89e-42a7-5272-fedd" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="4562-9eb6-c424-6040" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="12b1-6fe7-9a7c-bd6a" name="Reconquista" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Christian_Spain_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f89e-42a7-5272-fedd" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="8ed5-10d6-aa35-bdd9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8a97-4351-d097-a665" name="Caliphate" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Al_Andalus_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3f52-7e73-22e8-f61e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b41b-fc19-7a17-9bd9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="1707-4e96-c7d2-2edc" name="Taifa Kings" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Al_Andalus_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3f52-7e73-22e8-f61e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6ced-0076-91c2-faae" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="741c-fd3d-4d6f-cb25" name="Later Taifas" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Al_Andalus_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="3f52-7e73-22e8-f61e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ceae-05cf-5c16-01ea" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="700f-ca38-3250-8b1c" name="Almoravids" hidden="true" collective="false" import="true" type="upgrade">
      <comment>African_Invaders_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f430-9d85-c97c-11e8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="aeb5-d672-04d3-8843" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="0632-d00f-88f4-ca36" name="Almohads" hidden="true" collective="false" import="true" type="upgrade">
      <comment>African_Invaders_El_Cid.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f430-9d85-c97c-11e8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d66b-c691-6ad9-d167" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="9cd7-9074-1079-a416" name="Coalition" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Thracians_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="acdb-8982-b749-a280" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="acb7-2f50-0258-0414" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e16a-1045-813d-8a7e" name="Getic" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Thracians_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="acdb-8982-b749-a280" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="fac5-61f4-5311-201d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="c9b6-0f75-a848-579d" name="Highland" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Thracians_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="acdb-8982-b749-a280" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="29a3-c21a-7784-eb0c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="cf07-8103-8a22-6cd8" name="Classical" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Indian_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cdd7-93bb-92d6-0aa4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b3e9-8ef8-8bf5-e26e" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="2df5-5c3e-f0ee-3910" name="Mountain" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Indian_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cdd7-93bb-92d6-0aa4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2cc3-c893-219a-7130" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="17d8-e6c6-69e6-dd80" name="Republican" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Indian_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cdd7-93bb-92d6-0aa4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d925-e12d-7546-5f7f" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="1775-8ccf-e2d9-bd8e" name="Mauryan" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Indian_Alexander.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="cdd7-93bb-92d6-0aa4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="3819-cf4c-dc32-2ca8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7576-1447-92b5-2d67" name="Continental" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_HYW_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6864-b22f-4cf1-3e9e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="e7b4-2ec1-5958-d0bd" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="9da3-d00a-b05f-b9ea" name="Home" hidden="true" collective="false" import="true" type="upgrade">
      <comment>English_HYW_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6864-b22f-4cf1-3e9e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="56bd-e053-21c5-9fc2" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3549-bcb3-8293-99a8" name="Early Imperial" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ef15-8020-193e-f4c8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="39d6-d375-a0e0-0c70" name="Early Feudal" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="30e1-3082-8fce-924d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="00fc-33ad-c2e1-77ab" name="Early Clerical" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="296e-f68c-958a-cdef" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e2a6-c0e4-9477-6726" name="Early City" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="5570-2008-1023-eab8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7eaf-25a5-ba49-f1b0" name="Later Imperial" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="462c-ad34-cfa3-f507" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6597-d9f0-0473-0952" name="Later Feudal" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="3c9d-59de-fdcc-d73c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7a5a-d8f2-87ba-b178" name="Later Clerical" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="1f87-93aa-6533-5408" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="326b-6891-0466-e32a" name="Later City" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Holy_Roman_Empire_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6e3b-d217-f208-09da" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="72ae-adeb-83f7-7d10" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="0903-cb0d-bae2-7501" name="Moldavia" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Moldavia_Wallachia_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b1a-f9b9-37a6-7802" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="89a5-4e68-a015-3b9e" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="75c7-d343-1140-dd39" name="Wallachia" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Moldavia_Wallachia_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0b1a-f9b9-37a6-7802" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="3b6a-6dd3-887d-3498" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3245-e0f6-f847-1b74" name="Eastern Russian States" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Russian_States_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33f0-e587-bc7b-5859" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ab83-dfab-87a0-13b9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="74f5-b5d8-4625-3175" name="Western Russian States" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Russian_States_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="33f0-e587-bc7b-5859" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a5f9-b372-c3ab-b7e5" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="c2aa-65a8-fbd1-ad0e" name="Ghazi Ottomans" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Ottoman_Turks_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0845-3db9-de0b-c8ff" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="7bae-c8dc-e5f6-ba42" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7957-daa2-010c-e9e8" name="Conquest Ottomans" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Ottoman_Turks_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0845-3db9-de0b-c8ff" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b2f1-c9ce-5ef0-f2b5" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="bd14-1b77-1a71-685e" name="Nikaean Byzantines (1204-1261)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Last_Byzantines_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6708-d3cf-6ce3-54cc" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="9d7f-dae0-fa10-cc77" name="Trapezuntine Byzantines (1204-1461)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Last_Byzantines_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="4ff9-74b3-7cb0-c4af" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6b4f-8c2d-cd11-2788" name="Morean Byzantines (1204-1461)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Last_Byzantines_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f0e6-acbe-c3c0-0d02" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="37d6-fcaa-7fa8-9e5d" name="Epirote Byzantines (1204-1318)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Last_Byzantines_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ebbb-3475-7ded-eda7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="0d41-30d7-3a48-ffee" name="Palaeologan Byzantines (1259-1453)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Last_Byzantines_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="58af-eba5-d2ee-2b19" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="db03-d0cf-e64f-9677" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="4ddc-9a9c-c7de-308e" name="Lancaster" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Wars_of_the_Roses_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6e91-0445-1c77-cd85" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7a33-2077-d386-77ca" name="York" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Wars_of_the_Roses_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="685a-4030-4265-368c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d4b1-de1b-4481-449a" name="Richard III" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Wars_of_the_Roses_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="515e-769f-ca8b-0090" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="ad99-93a0-2c6b-b892" name="Henry Tudor" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Wars_of_the_Roses_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d638-f939-4da6-e634" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="019a-902d-4fdd-a496" name="Yorkist Pretenders" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Wars_of_the_Roses_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="01be-d673-a909-91cf" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="ab92-d15e-ddd5-6065" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="9498-7200-5dc8-05df" name="Early Army (1320-1400)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Italian_Condotta_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bf13-8303-e9bf-b20f" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="9888-cba4-eafb-5e36" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="1641-9429-747c-1ebb" name="Late Army (1400-1495)" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Italian_Condotta_Chivalry.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="bf13-8303-e9bf-b20f" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="4844-a07d-96b3-4e03" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="45bc-c434-d0fe-493d" name="Early Revolt Army" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1cbf-30f4-5071-3d11" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2471-7fc7-583a-45c2" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8bd5-46cb-b7af-2992" name="Germano-Gallic Slave Army" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1cbf-30f4-5071-3d11" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f5df-15c4-0428-e9a0" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="de2b-e55a-8b42-4ccd" name="Late Revolt Army" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="1cbf-30f4-5071-3d11" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="49c1-f51a-d8f1-9b16" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8ee1-e71d-1b68-a7be" name="First Sicilian Slave Revolt" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Sicilian_Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5e9a-ae2b-8768-10d4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="50ab-61e9-34e8-d2f8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6343-0cab-f06f-390e" name="Titus Minutius" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Sicilian_Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5e9a-ae2b-8768-10d4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="574a-e373-e3a6-9471" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="2dc2-6d88-66c5-5a76" name="Second Sicilian Slave Revolt" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Sicilian_Slave_Revolt_Spartacus.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5e9a-ae2b-8768-10d4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="1f82-41e0-70d0-8142" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="5556-d8cc-caed-c0be" name="Justinian Dynasty" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="d045-979c-ce47-fbe4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6016-6d2a-bfd8-c4b2" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="ecf2-89d2-d755-4394" name="Heraclian Dynasty" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="d045-979c-ce47-fbe4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d946-96f6-d1c3-10fd" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="aa01-56d3-21c9-cf1c" name="Early Sassanid Persians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Sassanid_Persians_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f4b0-39b0-06f0-415e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="7eb9-d2a6-a4a7-792f" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="f50b-9084-3f14-b738" name="Later Sassanid Persians" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Sassanid_Persians_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="f4b0-39b0-06f0-415e" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="56ba-5fc0-e583-d47a" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6ef0-a7a4-52dc-958a" name="African Vandal Kingdom" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Germanic_Kingdoms_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="48f9-e22f-3e7b-1110" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3e50-2f84-bbf9-96e2" name="Gallic and Spanish Visigoths" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Germanic_Kingdoms_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="41e8-e0fb-083e-6812" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="d55b-fc6d-7011-d15a" name="Early Merovingian Franks" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Germanic_Kingdoms_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="cab0-cb92-4b98-d7e7" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7446-6ca8-8d88-8066" name="Italian Ostrogoths" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Germanic_Kingdoms_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="bd1f-638d-ba4b-8785" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8015-2c61-6ba2-2789" name="Gepids and Early Lombards" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Germanic_Kingdoms_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="a058-c4af-57bc-05ae" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="7c6e-cb5c-bdeb-fb55" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="c16d-100c-f576-e8f5" name="Avars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="bba2-c9ef-4fb5-02b3" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="3084-ae79-fd51-a95f" name="Early Khazars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2a30-3bfc-b8ed-b390" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7a0f-273a-eb20-824c" name="Later Khazars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="e97b-3ee1-4af7-269a" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7e35-7fef-9e15-7fe6" name="Magyars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="91f9-9c56-8273-fb40" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="7927-bc89-6620-fe52" name="Pechenegs" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="55fd-94a1-dfa4-d4bf" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8a97-0500-bed2-fcce" name="Early Cumans" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Steppe_Nomads_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="6fbc-9802-5235-3cfa" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2e8a-497f-f60e-f043" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8761-3b5e-85b6-ea12" name="Early Balkan Slavs" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Bulgars_and_Slavs_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5253-c9ff-87dd-a7b4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="fc9a-295e-5f9f-0bfc" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e22d-ef1e-7c89-bd4e" name="Later Balkan Slavs" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Bulgars_and_Slavs_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5253-c9ff-87dd-a7b4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="b7e1-23a1-2da0-e001" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="495a-5036-c4d2-91ca" name="Early Balkan Bulgars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Bulgars_and_Slavs_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5253-c9ff-87dd-a7b4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6032-b0e9-2912-0c9b" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="0488-c965-72de-ddfa" name="Later Balkan Bulgars" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Bulgars_and_Slavs_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="5253-c9ff-87dd-a7b4" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="c636-9c87-a8f1-52b9" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="67e4-5cf0-bf08-4f86" name="Arab Conquest" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="1984-6590-c662-da6f" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="e717-d341-836f-2587" name="Umayyad Caliphate" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="7ce3-54d2-6167-ca2c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="fe01-c909-2892-dfdb" name="Early Abbasid Caliphate" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="a143-adbb-78bd-8141" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8987-b1ad-4139-fbf1" name="Later Abbasid Caliphate" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="6b4c-7921-ee45-6bac" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="8555-2a5b-4626-576c" name="Aghlabids" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d08a-b7ed-ffb6-59b8" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="168a-0d36-17dc-5a06" name="Tulunids &amp; Ikhshidids" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="eeed-6c65-a686-c992" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="274d-e7f2-1169-b937" name="Early Fatimid Caliphate" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="d077-9edb-ed8f-520d" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="b761-0cdc-ecd9-115d" name="Hamdanids" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Early_Caliphates_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="9fbc-64f6-d134-a385" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="e7d4-d577-7ad4-6b77" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="5a92-461b-a7d4-c2d5" name="Isaurian &amp; Phrygian Dynasties" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Thematic_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0636-e4a8-1ccf-14d8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="f8d9-4ea9-11df-c587" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="337f-56e7-8271-9da5" name="Macedonian Dynasty" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Thematic_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="0636-e4a8-1ccf-14d8" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="fa0a-0085-d06f-6995" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="deb1-afb0-adb0-35f5" name="Early Pagan Rus" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Rus_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b6b1-1a8a-7f57-8453" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="2c82-a306-7686-8c79" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="5913-f885-5429-d735" name="Era of the Princes" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Rus_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b6b1-1a8a-7f57-8453" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="023c-47a9-1ebd-7f3a" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="dfad-e049-0e8d-eb05" name="Great Rus" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Rus_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b6b1-1a8a-7f57-8453" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="5012-d671-e685-08bd" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="acaa-43b1-c815-72f2" name="Mongol Invasion" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Rus_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="b6b1-1a8a-7f57-8453" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="49ed-532f-32b0-511b" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="39e0-d11d-3ba7-3303" name="Macedonian Successors" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="85c6-18d9-9371-f27a" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="c4b6-4af5-277f-c57c" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
    <selectionEntry id="6c96-52e8-a508-6265" name="Komnenian Dynasty" hidden="true" collective="false" import="true" type="upgrade">
      <comment>Late_Byzantines_Byzantium.cat</comment>
      <modifiers>
        <modifier type="set" field="hidden" value="false">
          <conditions>
            <condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" childId="85c6-18d9-9371-f27a" type="instanceOf"/>
          </conditions>
        </modifier>
      </modifiers>
      <categoryLinks>
        <categoryLink id="39a0-6a91-873c-0e63" name="Army composition" hidden="false" targetId="fb15-1790-2ccc-50c8" primary="true"/>
      </categoryLinks>
    </selectionEntry>
  </selectionEntries>
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
4. A unit defeated in hand-to-hand combat is automatically broken if outnumbered by a feared enemy. No Break test is taken, so Break test modifiers and special rules do not apply.</description>
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
      <description>1. Light infantry or light cavalry can fight either as skirmishers or as open order formed units. They must fight as one or the other for the whole battle: if deployed as skirmishers they must fight as skirmishers, if deployed as an open order formed unit they must fight as one.</description>
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
    <rule id="aceb-51bd-e1cd-6b4d" name="Horse" hidden="false">
      <description>Mounted models ride a horse (Movement 8" before armour and barding penalties). A cavalry model's armour save is one pip better than the infantry equivalent (p.95). (Rulebook p.95-96; Hannibal p.7)</description>
    </rule>
    <rule id="48fa-efd4-2ade-8c63" name="Warhorse" hidden="false">
      <description>A warhorse is a heavier mount: M8 WS3 BS0 S3 I3 A1, in place of the ordinary horse. As for a horse, the rider's armour save is one pip better than the infantry equivalent (p.95). (Hannibal p.7)</description>
    </rule>
    <rule id="79c0-ca85-a46c-5e3e" name="Encumbrance" hidden="false">
      <description>Movement values printed in army lists are unencumbered. Infantry with an armour save of at least 4+ lose 1"; cavalry with a save of 3+ (ignoring barding) lose 1"; cavalry with metal barding lose a further 1" regardless of save. The M value shown on the model already includes this and updates as you choose equipment. (Rulebook p.96)</description>
    </rule>
    <rule id="8947-c655-aa5c-cc07" name="Chariot Wars Common Rules" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Multiple troop types: when you pick a unit all models must be of the same type unless the list allows mixed units. What You See is What You Get: models must show the options taken unless the opponent agrees otherwise. Unit sizes: minimum five infantry or five cavalry models, or three chariot models; no upper limit; one model may be a Leader, one a Standard Bearer and another a Musician (+5 pts each). Throw sticks have the same effect as a javelin. Characters in chariots: the cost of the chariot is not included in the character's entry but is bought from a later entry in the same list; the points spent count against the points that may be spent on characters. The character replaces one crew member; characteristics of character and chariot remain unchanged and each is attacked separately. Roll to hit as normal for missile fire, then roll again for each hit scored; on a 1-4 the chariot is hit, on a 5-6 the character is hit. In hand-to-hand an enemy model in base contact can choose to attack the chariot or the character. A character mounted in a chariot with a shield bearer may add +2 to his armour save; in any other circumstances +1. A character in a chariot has the chariot's armour save if it is better than his own. Wounds are tracked separately. The character may dismount and fight on foot if the chariot is destroyed, but only if a suitable model is available; if no model is available the character is lost with the chariot. If the character is killed the chariot may move and fight on its own.</description>
    </rule>
    <rule id="592c-3ef3-9392-535a" name="Army General (Chariot Wars)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Friendly units within 12" may use the Army General's Leadership.</description>
    </rule>
    <rule id="e5a3-e042-9a2a-f11f" name="Chariot Runners (Chariot Wars)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Runners in skirmish formation may move into gaps between a unit of chariots and still count as being in unit coherency as long as they are within 2" of a chariot model in the unit or within 2" of another model in the unit. Chariot runners can use this tactic to charge an enemy that is already engaged by the chariots, by charging into the gaps between chariot models. Chariots can charge through a unit of chariot runners that is in skirmish formation, even if the gaps between the runners are not wide enough to let them through; simply push the runners aside until there is a wide enough gap for the chariot to fit through. These rules replace the Armies of Antiquity rules which allow chariot runners that are touching a chariot model to fight.</description>
    </rule>
    <rule id="931b-4f0e-3aed-df29" name="Mixed Weapons (Chariot Wars)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Tribal contingents were rarely uniformly equipped; players may mix warriors in the unit so some are armed with different weapons. Whatever the models are carrying, a unit armed with mixed weapons counts as having hand weapons, javelins and bucklers.</description>
    </rule>
    <rule id="2370-1c8e-57c4-1fdf" name="Warband Psychology (rules 1 &amp; 2)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>"Subject to Warband psychology rules 1 &amp; 2": 1. D6 test at start of turn: 2-6 pass, 1 surge forward towards nearest visible enemy by at least basic move and charge if within range. 2. If the unit charges and defeats the enemy in the first round of combat, the enemy are automatically broken and flee without a Break test if the warband outnumbers the enemy.</description>
    </rule>
    <rule id="6ba3-a540-14db-0a9b" name="Onager Chariots" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Sumerian chariots were pulled by onagers (wild asses). At the start of the Sumerian player's turn roll a dice for each chariot unit. On a 1 the onagers are giving their drivers trouble and a further D6 is rolled: 1-3 "Giddy-up damn you!" the onagers refuse to move at all this turn and remain stationary; 4-6 "Whooa boy, whooooooa!" the onagers set off at a fair old clip: the unit must advance D6" straight ahead. The crew may turn this move into a charge if they wish, in which case the D6 roll is doubled; the unit must charge straight ahead and cannot wheel.</description>
    </rule>
    <rule id="6b39-e5a3-cab0-28f7" name="Egyptian Charioteers" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Egyptian charioteers do not suffer -1 to hit for shooting on the move and are able to shoot as they charge. This attack is made after any enemy charge reactions (any enemy that fire as a charge reaction do so before the charioteers). The attack counts as having taken place at short range. Enemy units that take 25% casualties must pass a Panic test or flee.</description>
    </rule>
    <rule id="83ab-9c36-3a60-49fd" name="Chariot Archers (Assyrian)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Chariot archers do not suffer the -1 to hit for shooting on the move. Automatic hits inflicted by a charging heavy chariot are added to the hits scored by the crew and happen at the same time.</description>
    </rule>
    <rule id="e590-c292-dd09-5f64" name="Mounted Archers (second rank)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Mounted archers in the second rank of the unit may shoot over the first rank.</description>
    </rule>
    <rule id="2a25-789d-aa6c-b353" name="Amorite Chief" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>The Amorite Chief may only lead Amorites. Any Amorite unit within 12" of the Chief may use his Leadership when it takes a Leadership test.</description>
    </rule>
    <rule id="5557-b840-a37f-3fe7" name="Vassal King" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Any units within 12" of the Vassal King who are of the same nationality as him may use his Leadership when taking a Leadership test.</description>
    </rule>
    <rule id="8b88-2e3d-2a93-1269" name="Legendary Warriors" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Heroes were mighty warriors of near legendary ability. They may re-roll one failed to hit and one failed to wound roll each combat phase. In addition they may re-roll a failed armour save if the wound suffered is their last one remaining (they can re-roll their last armour save). The General is the foremost hero in the army and benefits from this rule.</description>
    </rule>
    <rule id="b26f-4ed9-3173-6c4c" name="Sacred Ark" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>The Sacred Ark may be chosen instead of an army standard bearer, only if the army does not include any chariots. The Ark and the Priests form a single unit and may not join other units. They should be placed on a single base and move and manoeuvre in the same manner as a heavy chariot. They may not charge. Any unit within 6" of the Ark may automatically rally. Any unit within sight of the Ark may re-roll any Break or Rally tests. If the Ark flees or is captured or destroyed, all units within sight must take an immediate Panic test. The Priests are treated as stubborn.</description>
    </rule>
    <rule id="61e0-6659-ac78-a422" name="Camels" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Each camel carries two riders. Camels cause fear in cavalry and chariots.</description>
    </rule>
    <rule id="70b4-7598-a2ca-a328" name="Elamite Chariots" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Elamite chariots are four-horse heavy chariots, crewed by a driver armed with a sword. Elamite chariots may transport up to three infantry models per chariot. Only Babylonian armies may include Elamite Chariots or Cavalry.</description>
    </rule>
    <rule id="eb7b-7b63-2ee3-f972" name="Heavy Slingers" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>Models in a unit can have different weapon combinations. Armoured slingers in the second rank may shoot at full effect as long as the unit does not move. Slingers may shoot even if not in skirmish formation. Enemy units may not use shields against sling shot hits. A unit of heavy slingers contains archers and slingers in equal proportions.</description>
    </rule>
    <rule id="bcac-aba6-f4aa-7196" name="Mule Carts" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>The entire unit must be equipped with the required number of cart models (each cart carries up to five soldiers). The infantry automatically dismount from the carts to fight or shoot, even if charged. The carts are non-combatant and always placed directly behind dismounted infantry; they do not count as chariots. When mounted on carts the unit may march move but may not charge. Dismounted infantry must remount to be able to flee. If the unit pursues they do so as infantry and the carts follow up behind.</description>
    </rule>
    <rule id="196f-b39b-7a43-d796" name="Phalanx (Chariot Wars)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>As long as the unit has at least sixteen models and a rank bonus of at least +1: cavalry may not charge the front of the phalanx; phalanx models may charge and still fight in two ranks; all enemy attacks (shooting and hand-to-hand combat) at the front of the phalanx suffer -1 to hit. The only formation change allowed is an about face (180 degree turn). Phalanxes may wheel but cannot march or charge if they do so; they may drift 1" to the right when they march or charge. As soon as the unit is reduced to fewer than sixteen models or loses its rank bonus these rules no longer apply.</description>
    </rule>
    <rule id="878c-407a-114d-66ce" name="Terror (Assyrian)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>The Assyrians cause fear in all units in an enemy army that have a Leadership value of 7 or less, after any modifications have been applied. This rule no longer applies once an Assyrian chariot, cavalry or infantry unit has been broken in combat. Does not apply to Babylonian armies, or any army that includes Elamites or Hoplites.</description>
    </rule>
    <rule id="b2d7-83e6-e431-118f" name="Highly Professional (Assyrian)" publicationId="513c-2d0a-024a-da5a" hidden="false">
      <description>The Assyrians may always choose who moves first or second in a battle if this would normally be decided randomly. In battles where who moves first is not determined by a dice roll, the Assyrians follow the normal rules. Does not apply to Babylonian armies.</description>
    </rule>
    <rule id="8ccd-25c2-3a7e-7c24" name="Army General (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Any unit within 12" of the General may use his Leadership value when it takes a Leadership test.</description>
    </rule>
    <rule id="bcc5-1eb9-ce57-964e" name="Comitatus Oath" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Must be led by the army general. Barbarian bodyguards took oaths of allegiance extremely seriously. If the General is killed roll a D6: on a 4+ they immediately attack the nearest enemy and are immune to Psychology and Break tests. If they eliminate their opponent they attack the next nearest enemy unit and so on.</description>
    </rule>
    <rule id="2e5c-aa07-52a2-c8ca" name="Priest (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Any unit that includes a pagan priest hates all its enemies. Any unit that includes a Catholic priest hates enemies who are pagans or Arian Christians. Any unit that includes an Arian priest hates enemies who are pagans or Catholic Christians. If an army includes a priest, his opponent must declare a religious alignment.</description>
    </rule>
    <rule id="f007-958e-9638-949c" name="Shield Wall (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>In the Army lists some units of Roman infantry can form a shield wall. They may do this instead of moving. As long as the unit is in a shield wall all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer a -1 to hit modifier. The unit benefits from the shield wall as long as it does not move or lose a round of close combat.</description>
    </rule>
    <rule id="2a50-c575-d45e-dd54" name="Mixed Weapons (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Whatever the models are actually carrying they count as being armed with javelins if they are in skirmish formation and throwing spears otherwise. This replaces the mixed weapons rule of the Barbarian Army list in the Warhammer Ancient Battles rulebook (which counted javelins in any formation); players using the rulebook Barbarian list may use this interpretation at +1 pt per model it applies to.</description>
    </rule>
    <rule id="6edd-d63a-1760-87a2" name="Nomad Cavalry (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>a) Nomad cavalry may make a free march move after both sides have deployed; they may not use it to charge and may not shoot after making it. b) They do not suffer the -1 to hit for shooting if they moved in the same turn, but this does not allow them to shoot if they charge or march. c) They make a normal move immediately after shooting (Shooting phase only, not a charge reaction, and the unit may not have marched). d) If they flee or fire and flee as a charge reaction they rally immediately at the end of their move and may reform facing any direction; the charging enemy still counts as charging and the Nomad cavalry may fight in the close combat phase if encountered.</description>
    </rule>
    <rule id="e2de-9291-819a-1494" name="Lassoes" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Some steppe cavalry can use lassoes. A lasso attack is an additional special attack made by a successfully charging cavalryman before normal combat. Roll a D6: on a 6+ the lasso attack is successful and an enemy model in base contact with the attacker loses one attack for that round of combat. Lassoes cannot be used in subsequent rounds of combat or by a model that has been charged.</description>
    </rule>
    <rule id="aa30-06e2-0905-d2f4" name="Barbarian Cunning" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>The Barbarian player may hide a unit in a piece of suitable rough terrain on his half of the battlefield, noting its position on paper. The concealed unit is revealed and placed at the Barbarian General's choice or when a Roman comes within 6" of the concealing terrain. Warbands must still check for undisciplined movement but, provided they have a character leading them, may re-roll the dice once.</description>
    </rule>
    <rule id="2a7f-d713-cbde-4620" name="Heavy Shock Cavalry" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>Heavy shock cavalry fought in a dense formation and count their rank bonus as light infantry do (maximum +2). They lose half their movement if they wheel more than 1" in a move.</description>
    </rule>
    <rule id="f514-6383-2718-838a" name="Camelry Fear (Fall of the West)" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>North African camelry cause fear in enemy cavalry.</description>
    </rule>
    <rule id="d022-f542-22e9-c212" name="Currus Drepanus" publicationId="37b4-aae5-6830-d590" hidden="false">
      <description>D3+2 automatic hits when charging in addition to normal attacks. Destroyed if it breaks from close combat (it is not automatically destroyed after charging). Moves as a chariot.</description>
    </rule>
    <rule id="1cd2-0c21-7bd6-f879" name="Hittite Three-man Chariots" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Hittite chariots are sturdier than those of other nations: Movement 7 and Strength 4. They may have three crewmen, or the three-man chariot may represent a two-man chariot giving a lift to a chariot runner. If the chariot model has three crewmen fixed in the chariot, use it as a three-man chariot (the runner is a permanent crew member and does not dismount): +1 Attacks and +5 pts. If the third crewman can be detached, or a runner can be placed in the chariot or on its base, transport runners as described in the rulebook; if the runner joins its chariot unit when the unit is engaged in hand-to-hand combat, any runners touching a chariot or enemy model may fight as well.</description>
    </rule>
    <rule id="6f9d-2037-787a-adf7" name="Hurrian Chariots" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Hurrian, Syrian and Canaanite chariots do not suffer -1 to hit for moving while shooting.</description>
    </rule>
    <rule id="c479-ceb6-482e-7d7e" name="Warriors of Legend" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Generals and Heroes chosen from this list are mighty warriors of near legendary ability. They may re-roll one failed to-hit and one failed to-wound roll in each combat phase. In addition they may re-roll a failed armour save if the wound suffered is their last one remaining.</description>
    </rule>
    <rule id="326e-0e90-0928-e295" name="Independent Character" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>The character is independent: he moves and fights as a lone character and is not required to join a unit.</description>
    </rule>
    <rule id="ca78-5220-e828-9b8d" name="Terrifying Reputation" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>The Assyrians cause fear in all units in an enemy army with a Leadership value of 7 or less, after any modifications have been applied. This rule no longer applies once an Assyrian chariot, cavalry or infantry unit has been broken in combat.</description>
    </rule>
    <rule id="6879-9143-6a24-a233" name="Highly Professional (Armies of Antiquity)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>The Assyrians may always choose who moves first in a battle if this would normally be decided randomly. In battles where who moves first is not determined by a dice roll, the Assyrians follow the normal rules.</description>
    </rule>
    <rule id="b20f-96aa-dc28-41b2" name="Spara" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Infantry units in the Persian army may be equipped with large shields called spara, stood up to form a barrier in the same way as medieval pavises. Spara bearers count as having a shield unless the spara is set up. A spara may be set up instead of the bearer moving. While set up the unit counts as being behind hard cover to its front against missile fire, and behind a defended obstacle if attacked by opponents to their front in hand-to-hand combat. The spara barrier is knocked down if the unit moves or loses a round of combat.</description>
    </rule>
    <rule id="7c39-bba6-ad12-4167" name="Wedge Formation" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Shock cavalry units drawn from the army list that have between five and ten models may fight in a wedge formation: one model in the first rank, two in the second, etc. The unit's front, flank and rear arcs are based on the models in the rear rank. As long as at least one model is in contact with the enemy, all models in the unit may fight, even if not in base contact; for every two unengaged models in the wedge that this allows to fight, one enemy model in the unit touching the wedge, but not in base contact, may fight. This applies even if the wedge is charged or attacked to the front or rear.</description>
    </rule>
    <rule id="2581-05b8-6274-a9b9" name="Phalanx (Armies of Antiquity)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>As long as the unit has at least 16 models and a rank bonus of at least +1: cavalry may not charge the front of the phalanx; models in a phalanx may charge and still fight in two ranks; all enemy attacks (shooting and hand-to-hand) at the front of the phalanx suffer -1 to hit. The only formation change allowed is an about face (180 degrees). Phalanxes may wheel but may not march or charge if they do; they may slide one inch to the right when they march or charge. When reduced below 16 models or losing the rank bonus (including when attacked in the flank or rear) these rules no longer apply. The Carthaginian phalanx may have unit standards and an Army Standard Bearer (the Oracles rule does not apply).</description>
    </rule>
    <rule id="74dd-cf08-7426-ea66" name="Warband Psychology (rule 1)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Subject to Warband psychology rule 1: a D6 test at the start of each turn; 2-6 pass, on a 1 the unit surges forward towards the nearest visible enemy by at least its basic move and charges if within range.</description>
    </rule>
    <rule id="f2a2-98e9-40de-0c25" name="Allies &amp; Mercenaries (Carthaginian)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>The first time a unit wishes to move, charge or shoot, roll a D6. On a 1 the unit stays stationary and may not shoot. Once a unit has passed the test it need not test again.</description>
    </rule>
    <rule id="6ddf-3db2-3e52-0e51" name="Shield Wall (Late Roman)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Units of heavy infantry may form a shield wall instead of moving. While in a shield wall all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer -1 to hit. The unit benefits from the shield wall as long as it does not move or lose a round of close combat.</description>
    </rule>
    <rule id="58b8-64f8-99b7-1a45" name="Cataphracts (Armies of Antiquity)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Cataphract cavalry count their rank bonus, up to a maximum bonus of +3, and may not march.</description>
    </rule>
    <rule id="99b5-fa85-ec63-767a" name="City Militia (Cataphract)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Militia cause fear in all enemy troops apart from skirmishers.</description>
    </rule>
    <rule id="cd49-22c5-e500-fc61" name="Byzantine Cataphracts" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Count a rank bonus of +1 when charging. May combine with Cataphract Archers (the archers making up the rear ranks; casualties are taken against the front rank models first).</description>
    </rule>
    <rule id="27e1-4538-e1ef-9512" name="Strategicon" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>If the army includes a General, choose one at the start of battle: Flank March (play the Flank Attack scenario with the Byzantines as the flankers); Hidden Ambush Force (one unit set up in hiding out of sight of the opponent's deployment zone, deployed at the start of your first turn); Scouts (your opponent must set up first).</description>
    </rule>
    <rule id="f4c9-d539-9ae2-9b73" name="Bedouin and Turkish Cavalry" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Cavalry in the list may turn during their move without penalty and may change formation once during their move by any number of ranks with no penalty (including while marching). Bow-armed Turkish cavalry may make a normal move immediately after shooting in the shooting phase (Parthian Shot; not a charge reaction; may not march).</description>
    </rule>
    <rule id="8a59-0960-c17e-f215" name="Huscarls (Armies of Antiquity)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>A Saxon army may include a single unit of Huscarls, alone or split up and added to Fyrd units in the front rank only. While at least half (rounding up) of the front rank are Huscarls the unit is not subject to Warband psychology, has Leadership 9 and is stubborn; below 50% it is subject to Warband psychology with Leadership 6 (Select Fyrd) or 5 (Fyrd). Half of missile casualties on a combined unit fall on Huscarls; enemy models in base contact with a Huscarl must fight him. If the General is slain, Huscarls (and units where they make up at least half of the front rank) become subject to hatred for the rest of the battle.</description>
    </rule>
    <rule id="cb57-abf1-3fa0-2280" name="Shield Wall (Saxon)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Units of Huscarls and Fyrd spearmen may form a shield wall instead of moving. While in a shield wall all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit, as long as the unit does not move or lose a round of close combat.</description>
    </rule>
    <rule id="b4f6-c85e-1ebf-f6e6" name="Fyrd Warband Psychology" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Subject to Warband psychology unless within 12" of the army's General.</description>
    </rule>
    <rule id="5474-516e-fb2f-5403" name="Viking Huscarls" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Cause fear in enemy troops with Leadership of 7 or less. Different models may be armed with different weapons in the same unit. A unit of Huscarls can contain up to three Beserkers.</description>
    </rule>
    <rule id="70da-b988-fb78-e8b9" name="Beserkers" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Beserkers are not hidden in the unit and are represented by ferocious models in the front rank. They may be removed as casualties at the player's choice. If an enemy unit is within 12" of the unit at the start of a Viking turn, roll 2D6 for each Beserker: if the roll is equal to or greater than the distance to the nearest enemy he charges immediately (automatically if the unit is within 2" of an enemy or in close combat). They always charge the closest enemy (random if tied). The Beserker causes D6 automatic Strength 5 hits and is then removed from play.</description>
    </rule>
    <rule id="6bf4-fcf8-567e-9e2c" name="Ferocious Charge" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>If a unit noted as having a ferocious charge charges and wins the round of combat, its opponent automatically breaks with no Leadership test. Enemy units that normally ignore Break tests roll a D6: on 1-3 they are broken anyway, on 4-6 they hold.</description>
    </rule>
    <rule id="3f06-a726-c44a-7e59" name="Knights Rank Bonus" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>May count a rank bonus of up to +1 even though cavalry.</description>
    </rule>
    <rule id="f906-03d2-d699-9e8e" name="Honourable" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Samurai characters in a position to charge an enemy character must do so, and must accept a challenge issued by an enemy character (if several are eligible, any one may be chosen). Infantry units in the army may not declare a charge until after a Samurai unit has declared a charge or fought a round of combat as a defender; they may declare in the same turn, after the Samurai.</description>
    </rule>
    <rule id="738a-244a-2378-ff5e" name="Katana" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>A character or Samurai armed with a katana counts as having a shield as well (it can parry), and the katana adds +1 Strength if he is on foot (a mounted Samurai uses the sword one-handed and gets no bonus). With an additional hand weapon he loses the +1 Strength bonus but may still parry. Samurai armour gives a 5+ armour save but counts as light armour for movement; a naginata is treated as a halberd on foot and a thrusting spear when mounted; Samurai count as armed with a longbow (infantry have ordinary bows). Any Samurai or Ashigaru unit may carry Sashimonos for +15 pts per unit and may re-roll a failed Break test.</description>
    </rule>
    <rule id="e06c-41a1-2112-c8e3" name="Warrior Monks Dodge" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Warrior monks receive a 5+ special dodge save that is not modified by the strength of their opponent's attack.</description>
    </rule>
    <rule id="8ca1-afd6-c2e9-56fe" name="Ninja Scouts" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>Ninja scouts always set up last. They may deploy anywhere on the table outside the enemy's deployment zone and out of sight of the enemy.</description>
    </rule>
    <rule id="d638-2367-3540-5a2f" name="Peasants (Samurai)" publicationId="aab0-aa1e-0319-4ffe" hidden="false">
      <description>May only declare a charge if led by a Samurai Hero.</description>
    </rule>
    <rule id="5b7f-5d28-c1dc-0d4e" name="Shieldwall Common Rules" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>The army lists in Shieldwall are used in the same way as the Roman &amp; Barbarian lists in Warhammer Ancient Battles; each has its own force composition and additional rules. UNIT SIZES: the minimum size for a regiment is five infantry or cavalry models; there is no upper limit. One model per unit may be upgraded to a leader (+5 pts), one to a standard bearer (+5 pts) and one to a musician (+5 pts) unless stated otherwise. WHAT YOU SEE IS WHAT YOU GET: unless your opponent agrees otherwise, the models you use must show the options you take. SHIELDWALL: units may form a shieldwall instead of moving. As long as the unit is in a shieldwall, all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer a -1 to hit modifier. The unit benefits from the shieldwall as long as it does not move or lose a round of close combat. Characters on foot in a unit with Shieldwall gain the benefits as well. CAVALRY COUNTER CHARGES: a new charge reaction that may only be taken by cavalry units that are charged to the front by enemy cavalry. The unit counts as charging for the purposes of using its weapons (e.g. +1 S with thrusting spears). Cavalry with a move of less than 6" may not counter-charge. The unit does not move, and does not count as charging for deciding who strikes first. Cavalry may not counter-charge infantry. RANK BONUSES &amp; DIFFICULT TERRAIN: units may only count their rank bonus in close combat if both they and their opponent are in clear, open terrain and neither is behind an obstacle (hills and fords count as clear terrain and do not negate a rank bonus). REFORMING IN COMBAT: a unit fighting to the flank or rear may reform at the end of the Close Combat phase as long as it did not break and is not also engaged on another facing. It must reform so that it faces the unit engaging it, with its centre in base contact with the centre of the enemy unit. A reformed unit still loses its rank bonus for the duration of the combat if it was charged by an enemy unit containing five or more models. SKIRMISHERS AND RANK BONUSES: formed units do not lose their rank bonus if charged by a unit of five or more models in skirmish formation (also to cavalry in skirmish formation, but not to chariots). FALL BACK IN GOOD ORDER: a side that outnumbers the other by over two to one (overwhelming odds) and loses a combat and fails its Break test falls back in good order instead of fleeing; drilled troops, units in skirmish formation and cavalry that lose a combat but pass their Break test may fall back in good order if they wish. The fall back move is made as for a flee move, except: friends within 12" do not take a Panic test; the unit rallies automatically at the end of the move and may immediately reform; it may be pursued but if caught is not wiped out (the pursuer counts as having charged in the next Close Combat phase); it may not declare a charge in its next turn but may otherwise move and shoot normally; a unit that falls back off the table is lost; units can fall back in good order from a Ferocious Charge. MOUNTED MODELS (models chosen from the Shieldwall lists): a model may be mounted on a horse (M8 prior to armour penalties) or on a warhorse (M8 WS3 BS0 S3 I3 A1); mounted models may not use a double-handed weapon. ARMY STANDARD BEARER: may not take double-handed weapons or additional hand weapons as options. LEADERSHIP &amp; WARBAND PSYCHOLOGY: if a unit with Warband psychology is joined by a character who does not have Warband psychology, the unit must use either its own Ld or the character's; it cannot use the character's Ld and add on the Warband rank bonus.</description>
    </rule>
    <rule id="50ff-a1ae-ebe2-ce60" name="Fury of the Norsemen" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Such units cause fear in any unit that has a Ld value, before modification, of 7 or less. The affected unit may use its modified Leadership value when taking the test.</description>
    </rule>
    <rule id="3f29-4904-5cf6-b01c" name="Werod" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>If the general is killed whilst with such a unit roll a D6. On a 4+ the unit immediately tries to charge the nearest enemy unit in sight, if not engaged. The unit is immune to psychology and Break tests. If its opponent is eliminated, the unit charges the next nearest enemy unit, etc.</description>
    </rule>
    <rule id="ff60-649f-f2b4-afff" name="Warband Psychology (rule 2)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Subject to Warband psychology rule 2: if the unit charges and defeats the enemy in the first round of combat, the enemy are automatically broken and flee without a Break test if the warband outnumbers the enemy.</description>
    </rule>
    <rule id="d9ef-387b-7921-7ad7" name="Berserkers (Shieldwall)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>A unit of Hirdmen can contain up to three Berserkers. They must be placed with a unit at the beginning of the battle, do not count as hidden, and must be represented by a suitably ferocious model in the front rank of the unit. You may choose to remove a Berserker model as a casualty if the unit suffers missile or close combat casualties, but do not have to unless the Berserker(s) is the only model(s) left in the unit or it was targeted in close combat. Berserkers may not leave their unit, other than when they berserk. If there is an enemy unit visible within the charge arc of the unit containing the Berserkers at the start of a Viking turn and within 12" then there is a chance the Berserkers will go berserk: roll 2D6 for each model; if the number rolled is equal to or greater than the distance to the nearest enemy the Berserker charges immediately (move the Berserker into contact with the enemy as he charges). If the unit is engaged in close combat at the start of its turn the Berserker automatically goes berserk at the start of the Viking player's turn. Berserkers always charge the closest enemy (randomly determined if two enemy units are equally close). The Berserker automatically causes D6 Strength 5 hits on the enemy unit which he attacks and is then removed from play. If the enemy unit suffers 25% casualties from the attacks, it must take an immediate Panic test.</description>
    </rule>
    <rule id="ba81-d615-6a3f-6e6f" name="Godi" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>The Godi and any unit he is with is immune to psychology and Break tests. As soon as the Godi is killed the unit tests as normal.</description>
    </rule>
    <rule id="cb54-b0ce-0f8d-0360" name="Army General (English)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Army General. Any friendly English unit within 12" of the Army General ignores Warband Psychology rule 2.</description>
    </rule>
    <rule id="9aa9-17bb-cd04-d691" name="Abbod" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>A unit that the Abbod accompanies re-rolls any misses in the first round of any combat.</description>
    </rule>
    <rule id="42a5-442a-0bfc-beac" name="Combined Units (English)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Prior to deployment, the English army may split up the single unit of Huscarls, and any units of Thegns, and combine them with units of Ceorls such that no more than 25% of the unit are Huscarls, or 50% are Thegns. Thegns and Huscarls may not be mixed. Huscarls and Thegns must be positioned in the front ranks. If the unit then contains more than one leader, musician or standard, the excess models are replaced by rank &amp; file figures. As long as half or more of the front rank are Huscarls or Thegns, the unit uses the Leadership and Psychology rules of these figures rather than the Leadership and Psychology rules of the Ceorls. Half of all missile hits inflicted on a combined unit count as being inflicted on the Huscarls or Thegns. In close combat, enemy models in base combat with a Huscarl or Thegn must fight against them, with the exception of challenges. If excess casualties are inflicted, these carry over to lesser troops. The last Huscarls/Thegns removed are the leader, musician and standard; this occurs even if there are other models remaining in the unit. The armies of Anglia and Northumbria may combine spear and shield-armed Gebur with Thegns and Huscarls in the same way as Ceorls.</description>
    </rule>
    <rule id="bbb7-1d61-ce60-ce1b" name="Huscarl Hatred" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>If the Army General dies, then Huscarls become subject to Hatred for the rest of the battle as described in the Warhammer Ancient Battles rules.</description>
    </rule>
    <rule id="81ca-cd37-1415-3d03" name="Veterans (Wessex)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>All units of Thegns may, once per battle, choose to re-roll all their to hit dice for close combat or for shooting. However, the unit must re-roll all of its dice (not just the failures) and must abide by the result.</description>
    </rule>
    <rule id="b82d-b3f0-21e3-a3bb" name="Offeiriad" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>You may re-roll rally attempts of any unit the Priest is accompanying.</description>
    </rule>
    <rule id="09b9-3a2a-db1c-7c94" name="Bishop" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Any unit the Bishop is with may re-roll failed Panic tests.</description>
    </rule>
    <rule id="d1cb-5db0-db8d-c679" name="Jomsviking Bribe" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Each turn roll a dice. On a 1 the Jomsvikings or Adventurers have accepted a bribe from the enemy and may not move that turn.</description>
    </rule>
    <rule id="b84a-af9a-c600-836a" name="Unreliable Mercenaries" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Although in the main loyal and obedient, sometimes mercenaries would think they knew better than their employer! Roll a dice the first time a player wishes to move, charge, or shoot with each unit. If a 1 is rolled the unit remains stationary and may not shoot, but may defend itself if attacked in close combat, including shooting against a charging unit. On a 2-6, the unit may act as the player wishes. Once a unit has successfully moved or shot, it no longer needs to take this test and may be moved normally.</description>
    </rule>
    <rule id="3fe9-fce0-4973-895a" name="Mercenary Rally" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Any unit that chooses to flee or fire &amp; flee as a charge reaction rallies automatically at the end of its move and may reform facing in any direction. This means that should the charging enemy encounter them, the unit is not destroyed, and may instead fight in the Close Combat phase. Their opponents still count as charging.</description>
    </rule>
    <rule id="5cea-a513-0909-077b" name="Raiders" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>Although strategically the Caledonians were more often than not on the defensive, tactically they were frequently the attackers. The commander of a Caledonian army may always choose whether he moves first or second.</description>
    </rule>
    <rule id="3966-f0f3-411e-050f" name="Choice of Terrain (Welsh)" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>If players agree to randomly choose the terrain, the player commanding a Welsh army may always select one additional item of terrain which he may place anywhere other than the opponent's deployment zone.</description>
    </rule>
    <rule id="8faa-d305-c4fb-a0dd" name="Hibernian Ambush" publicationId="af20-e256-4a51-93aa" hidden="false">
      <description>At the beginning of the battle, before units are placed, a commander of an Hibernian army may keep one unit off the battlefield. The commander writes down where the unit is hidden: either a village, wood, etc, or an area of ground hidden by a hill or similar. Once all units have been deployed the commander of the Hibernian army may either place the unit in his own deployment area or keep it in ambush. As soon as an enemy unit is within 8" he must deploy the unit, although he may deploy the unit earlier if he wishes. If the unit is deployed in the Hibernian player's turn it may charge, move, fire and attack normally in that turn. Whilst hidden a unit is immune to all psychology tests.</description>
    </rule>
    <rule id="0322-f14d-c228-0f49" name="El Cid Common Rules" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The army lists in El Cid are used in the same way as the Roman and Barbarian lists in Warhammer Ancient Battles; each has a number of army options for a period of history, each with its own force composition and additional rules. UNIT SIZES: minimum five infantry or cavalry models, no upper limit; one model per unit may be a Leader (+5 pts), one a Standard Bearer (+5 pts), one a Musician (+5 pts) unless stated otherwise. WYSIWYG: the models must show the options taken. CAVALRY COUNTER CHARGES: a cavalry unit charged to the front by enemy cavalry may counter charge: it counts as charging for its weapons (e.g. +1S for thrusting spears) but does not move and does not count as charging for deciding who strikes first; cavalry with a move of less than 6" may not counter charge, and cavalry may not counter charge infantry. RANK BONUSES &amp; DIFFICULT TERRAIN: a rank bonus counts only if both units are in clear, open terrain (hills and fords count as clear) and neither is behind an obstacle. REFORMING IN COMBAT: a unit fighting to the flank or rear may reform at the end of the Close Combat phase if it did not break and is not engaged on another facing, facing the unit engaging it with its centre in base contact with the enemy centre; it still loses its rank bonus if charged by an enemy unit of five or more models. SKIRMISHERS &amp; RANK BONUS: formed units do not lose their rank bonus if charged by a unit of five or more models in skirmish formation (including cavalry, but not chariots). FALL BACK IN GOOD ORDER: overwhelming odds (over 2:1 in models) - the side with overwhelming odds that loses and fails its Break test falls back in good order instead of fleeing; drilled troops, skirmishers and cavalry that lose a combat but pass their Break test may choose to fall back in good order; no Panic tests for friends within 12", automatic rally at the end of the move with an immediate reform, may be pursued but are not wiped out (the pursuer counts as having charged next turn), may not charge next turn, a unit falling off the table is lost, and units can fall back from a Ferocious Charge. Missile hits against mixed units use the saving throw of the majority of models (best save if equal) and casualties are removed in roughly equal proportions. MOUNTED MODELS: a horse raises Movement to 8" before armour penalties; a warhorse has the profile M8 WS3 BS0 S3 I3 A1. BOWS: all bows in the army lists are composite bows unless noted. COMBINED FORMATION: see the Combined Formation rule. Andalusian Allies: units from the Al-Andalus list that become subject to the Aliados y Mercenarios rules (documented only, not built).</description>
    </rule>
    <rule id="e569-be7e-a7ca-2582" name="Combined Formation (El Cid)" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Units that can do this are indicated in the army list; typically archers take up the rear ranks of the unit, shooting over the heads of the troops in front. The archers lose their Light Troop status if applicable and are treated as normal troops for movement and rank bonuses. The archers may shoot using the Massed Archery rules (rulebook p.23) as well as any special rules of the unit. A unit may stand &amp; shoot or fire &amp; flee using massed archery.</description>
    </rule>
    <rule id="fc2c-25be-aca9-5a52" name="Bloodthirsty" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Bloodthirsty troops and characters are fervent, religiously-motivated warriors. 1. At the start of each turn roll a D6 for each unit not bound by a compulsory movement rule: on 2-6 it moves normally; on a 1 it must surge forward: charge the nearest enemy if within reach, otherwise move towards the nearest enemy at least 4" if possible (faster if the player wishes); if blocked it moves as far as it can; if facing away it turns or wheels to face the nearest enemy and moves as far as it can towards them. 2. Bloodthirsty troops and characters must always pursue an enemy that flees or falls back in good order and may not hold back. 3. They may not disengage from combat or voluntarily fall back in good order. 4. In the Ransom scenario they must roll a 6 to capture an enemy character alive (on a 1-5 the enemy is killed instead).</description>
    </rule>
    <rule id="882d-f357-ae46-9d92" name="Cantador (El Cid)" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The Cantador may lead a single formed unit (not skirmishers). After deployment, but before the first move, roll a D6: 1 - his voice is drowned out, no effect. 2-3 - the unit may add D3" to its movement for ONE move, march or charge during the battle (declared before the dice are thrown; doubled for charging or marching). 4-5 - the unit may re-roll failed Panic tests during the battle. 6 - the unit and any attached characters may re-roll any misses in the unit's first round of combat (warhorses may not).</description>
    </rule>
    <rule id="23dc-67a3-0cbf-922a" name="Bishop (El Cid)" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Any unit led by the Bishop may re-roll failed Panic tests.</description>
    </rule>
    <rule id="0609-a21f-82bb-7825" name="Crusading Bishop" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The Bishop may be upgraded to a Crusading Bishop for +40 pts: Leadership 9, and subject to Hatred of the enemy (Hatred does not extend to warhorses); any unit he leads is also subject to Hatred of the enemy. Crusading Bishops are Bloodthirsty, as is the unit they lead. A Crusading Bishop cannot re-roll failed Panic tests.</description>
    </rule>
    <rule id="ba99-7c39-57da-7739" name="Andalusian Horsemen" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Cavalry noted as Andalusian Horsemen may reform their unit formation without penalty after movement, including after a march or double pace move but not charging. A unit reforming in skirmish formation must possess a Musician as normal (rulebook p.56). A reforming unit cannot fire in the Shooting phase. The unit reforms around its leader, musician or standard bearer, and no model may move more than its permitted distance. Mounted characters accompanying an Andalusian Horsemen unit do not impede the unit's ability to reform.</description>
    </rule>
    <rule id="91dc-bc7f-6e61-fce7" name="Qadi" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The Qadi can lead a single formed unit (not skirmishers). This unit may re-roll failed Rally attempts during the battle, as long as the Qadi is still alive and leading. Later Taifas: if no other Army General is chosen the Qadi may be made Army General for +50 pts; any unit led by the Qadi-General may also re-roll failed Panic tests, but the Qadi-General loses the ability to re-roll failed Rally attempts.</description>
    </rule>
    <rule id="a61b-ef36-0ee7-03bd" name="Mounted Crossbow (El Cid)" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The light crossbow used by Andalusian mounted crossbowmen has a range of 24", Strength 3 and a -1 save modifier. If they move in their Movement phase they are unable to fire that turn (they are assumed to have halted to reload).</description>
    </rule>
    <rule id="ec92-bdab-f6d9-5400" name="Imam" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>The Imam may lead a unit of either Black Guard or Berber Spearmen (with or without Berber Archers). He cannot lead any other unit. The Imam is subject to Hatred of the enemy as described in the psychology section of the game rules. Any unit led by the Imam also becomes subject to Hatred of the enemy.</description>
    </rule>
    <rule id="e40f-cfd7-e44a-a935" name="African Drummers" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Almoravid and Almohad armies included large numbers of Saharan drummers. Certain units may feature two Musician models (rather than one) for the normal cost of +5 pts per model. Any unit so equipped automatically wins a drawn combat by one point, rather than resorting to a musical roll-off. Only Hasham Guard Cavalry, Berber Cavalry, Camel Riders, Black Guard, Berber Spearmen and Berber Archers may take an additional drummer. A Berber Archer or combined Berber Archers/Spearmen unit with two drummers may use Massed Archery even if it has moved up to its normal movement in a turn; a -1 to hit penalty still applies to units that move &amp; shoot.</description>
    </rule>
    <rule id="af14-6533-0978-e4a9" name="Camel Riders (El Cid)" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Camels cause fear in all cavalry (and chariots, should they happen to meet one).</description>
    </rule>
    <rule id="b1ff-eb23-2666-9b4f" name="Aliados y Mercenarios" publicationId="2127-dab1-0af6-7421" hidden="false">
      <description>Aliados y Mercenarios units may have a Leader, Standard &amp; Musician as normal. A single Aliados y Mercenarios unit may be personally led by the Army General and is then exempt from these special rules and treated like a regular unit from the General's army. Aliados y Mercenarios units may not benefit from the special abilities of the Army General or Army Battle Standard, although they may be led by any appropriate character and use his Leadership and any special abilities. Roll a dice the first time a player wishes to move, charge or shoot with each unit of Aliados y Mercenarios: on a 1 the unit remains stationary and may not shoot, but can defend itself if attacked in close combat, including shooting against a charging unit; on a 2-6 the unit can act as the player wishes. Once it has successfully moved or shot, it no longer has to take this test. Aliados y Mercenarios units are treated as part of their employer's army for taking and causing Panic tests.</description>
    </rule>
    <rule id="78e0-cd04-42e9-2ef6" name="Alexander Common Rules" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>The army lists in Alexander the Great are used like those in the other Warhammer Ancient Battles books. UNIT SIZES: minimum five models (three chariots), no upper limit unless stated; one model per unit may be a Leader (+5 pts), a Standard Bearer (+5 pts) and a Musician (+5 pts) unless stated otherwise. COMBINED FORMATION: a unit that mixes weapon types in ranks (archers behind pikemen etc.) uses the Combined Formations rule. CAVALRY COUNTER CHARGES: a cavalry unit charged to the front by enemy cavalry may counter charge (counts as charging for its weapons but does not move; cavalry with a move of less than 6" and cavalry against infantry may not). SKIRMISHERS &amp; RANK BONUS: formed units do not lose their rank bonus when charged by skirmishers in open order. ELEPHANTS: elephants cannot be pursued; elephants, chariots and characters have flanks and a rear; rampaging elephants count as 50% victory points. XYSTON: a cavalry thrusting spear that always strikes first, even when not charging; a kontos or pike strikes first against a xyston. Mounted models with xyston or kontos may not carry shields; mounted models may not use large shields; foot models may not combine a pike with a large shield. The Army Standard Bearer may not take a xyston, spear, pike, kontos etc. OPTIONAL RULES (book only, not built): Mixed Armour, Elephants (skirmishers vs elephants, proximity, un-crewed), Subordinate Generals, Persian Prepared Ground and scythed chariot Out of Control.</description>
    </rule>
    <rule id="504d-f71e-c900-68c0" name="Macedonian &amp; Trained Phalanx" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Macedonian phalanx and trained phalanx: the benefits need at least 16 models in the unit and a +1 rank bonus. The unit may About Face but not Right Face or Left Face. A Drilled phalanx keeps its benefits until reduced below 12 models and may turn 90 degrees. Oracles: a Macedonian army using oracles gets D6 per 1,000 pts.</description>
    </rule>
    <rule id="756b-19a8-cf22-849b" name="Alexander's Eagle" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Alexander may choose to re-roll the Oracle dice at the start of the game (he must abide by the second roll), or force the other player to deploy first.</description>
    </rule>
    <rule id="ba06-a87d-0499-a33f" name="Kontos (Alexander)" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>A kontos strikes first against a xyston, and cannot be used with a shield when mounted.</description>
    </rule>
    <rule id="819d-6e18-7167-0bd7" name="Polemarch" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>If a Polemarch is present Greek mercenary troops make Leadership tests using their paymaster's Army General and gain all benefits of the Army Battle Standard; if he is killed all Greek mercenaries must pass a Panic test (ignored if the Army General is killed). Greek mercenaries otherwise use the paymaster's General and Army Battle Standard.</description>
    </rule>
    <rule id="ce45-0e3c-abca-7474" name="Rhomphaia" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Halberd; +1 Strength; counts as shieldless. Only Mountain (Highland) tribesmen may take it.</description>
    </rule>
    <rule id="4df7-6545-dfb1-f93f" name="Rolling Wagons" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Wagons may not move normally; they are rolled downhill in the Shooting phase. They must be placed on a hill and a warrior unit must be within 3" to launch them. They move straight ahead 3D6" and are removed at the end of the roll or on hitting an obstacle. Units in the path suffer D6 Strength 5 impact hits. Large targets; drilled troops may open lanes. Troops fighting behind wagons count as in soft cover. Highland armies only.</description>
    </rule>
    <rule id="559c-3a07-4304-5c6b" name="The Great King" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>If the Great King flees off the table the army checks for panic as if he was killed. Units within 12" gain +1 Leadership (instead of using his Leadership for psychology and Break tests). Certain units may only be included if the Great King is the General. He may only join Persian troops, and automatically flees if involved in a losing close combat that involves the enemy army general.</description>
    </rule>
    <rule id="6d2f-c8b3-c4ec-9f1b" name="Half-Barded Armour" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Half-barding gives +1 save to the front only, and -1 Movement.</description>
    </rule>
    <rule id="2573-5bb3-cca6-01c0" name="Scythed Chariots (End of Persia)" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>May be fielded in units of fewer than three models, with no leaders, musicians or standards. A scythed chariot counts as three models for unit size. Maximum four scythed chariot models per 2,000 pts. 7 M, 5 S, 4 T, 1 W, 3 I, D6+2 A, Ld 5; the driver has WS3 BS3 S3 T3 W1 I3 A1 Ld7, a dagger and heavy armour.</description>
    </rule>
    <rule id="9a32-e18e-c8e3-bbb1" name="Elephants (Alexander)" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Elephants cannot be pursued; they have flanks and a rear; a rampaging elephant gives 50% victory points. Indian elephants carry no towers; crews gain a 5+ save. Used to elephants troops are unaffected by elephant fear.</description>
    </rule>
    <rule id="a838-e8d1-fa66-78d9" name="Brahman Priest" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>The Priest must be attached to an infantry unit at the start of the game and may not leave. If he is killed D6 members of his following immediately commit suicide and are removed; at the start of each turn D6 followers commit suicide or desert. A Brahman or unit led by one will not pursue a broken enemy. Brahman priests hate all foreigners and may not accompany an army that includes Persian or Greek allies.</description>
    </rule>
    <rule id="110a-952b-20cc-42bb" name="Rathamasaula" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Man-pushed anti-elephant cart: no impact hits on normal troops, but against elephants D3 wounds with no saves. Charges up to 8" depending on remaining crewmen; cannot march. The crew may not fight on the turn it charges; if charged the crew defend from behind and are -1 to hit.</description>
    </rule>
    <rule id="a935-01a1-127e-bb6b" name="War Wagons" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Treated as Heavy chariots but do not cause fear, no double moves or impact hits. The wagon's attacks represent the oxen: front only, hits only on 6s. Crewmen attack separately and fight from inside the wagon with a 5+ save. Not with elephants or large chariots. Each wagon counts as one model; crews may not have standards, musicians or leaders.</description>
    </rule>
    <rule id="b95a-4789-9033-2aa6" name="Wagon Laager (Republican)" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Wagons are deployed up to 12" from the baseline end-to-end in a straight line. They may not be moved, are immune to psychology, and cannot be broken. Each may hold up to four skirmishing infantry or characters. Units behind wagons count as in soft cover but may not use massed archery; large targets; defenders gain a 5+ save. Attackers need 6s to hit units behind unoccupied wagons or skirmishers inside until they win a round of combat. Empty wagons are destroyed if an enemy unit of five or more models remains in contact at the end of the Combat phase.</description>
    </rule>
    <rule id="7e6b-2cc6-a121-3cd7" name="Large Chariots" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>Count as Heavy Chariots and cause D3 Strength 4 impact hits. Two unarmed drivers, two warriors and two shield bearers, giving a 3+ save.</description>
    </rule>
    <rule id="d563-3461-c705-d0af" name="Elephant and Chariot Escorts" publicationId="0641-2ee1-c462-c414" hidden="false">
      <description>One unit of escorts per chariot unit or elephant. Each elephant escort unit up to eight escorts, each chariot or wagon escort unit up to four escorts per chariot or wagon in the unit.</description>
    </rule>
    <rule id="2faa-4857-3fcc-9243" name="Armies of Chivalry Common Rules" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>UNITS: the minimum size for a unit is five models unless stated otherwise; every unit may upgrade one model to a Leader, one to a Standard Bearer and one to a Musician (+5 pts each). Units of fewer than five models, and unattached characters, that lose a round of hand-to-hand combat are broken automatically and cannot use Psychology rules. A character must be in the front rank of a unit to affect it with a psychology rule. Units subject to Frenzy cannot Flee or Fire &amp; Flee as a charge reaction. MOVEMENT: Movement is the unencumbered rate; deduct the armour and barding penalties. OVERRUN: if all of a unit's opponents are slain in the first round of combat it may make a 2D6" or 3D6" Overrun move as if it had broken them (a fresh enemy is charged automatically). FALLING BACK IN GOOD ORDER: sides with overwhelming odds (over 2:1), Drilled troops, skirmishers and cavalry may fall back in good order (no panic, rally automatically, may not charge next turn). TROOP TYPES: Close Order troops use the standard movement rules and rank bonus up to +3; Open Order infantry ignore difficult terrain and obstacles (no marching while doing so), may reform at the end of their move (then cannot shoot) and get +1 rank bonus (some +2, in open ground only); Skirmishers fear formed troops (but need no Fear test to flee or fire &amp; flee as a charge reaction). COMBINED FORMATION, MIXED ORDER, DIFFERENT WEAPONS and MEDIEVAL PHALANX: see the individual rules. ARMOUR: Light 6+ (no penalty); Heavy 5+ (-1" with a shield); Partial plate 4+ (the shield only helps on foot; -1"); Full plate 3+ on foot, 4+ mounted (-1"); mounted models gain +1 to their armour save. Pavise: counts as a large shield (+2) against missiles. BARDING (mounted only, -1" Movement): cloth +1 save in hand-to-hand; half-barding +1 save to the front facing; plate +1 save in hand-to-hand and against missiles. MEDIEVAL MASSED FIRE: the first archer or crossbowman in each file fires at full effect and half of the other archers (rounded down) may also fire; crossbowmen and handgunners may only fire if they remain stationary; in difficult terrain only the front rank fires. Light crossbow: 24", S3, move and shoot. Handgun: 24", S4 (S3 at long range), -2 (-1) save modifier, move or shoot. STAKES: negate strength bonuses for mounted attackers and First Charge; only formed units place them, at deployment or after a free 4" move. MOUNTED &amp; DISMOUNTED: units begin the game mounted or dismounted and cannot change; both count towards the Cavalry allocation; warhorse M8 WS3 I3 A1. ARTILLERY, WAR WAGONS and WAGON TABOR: see their rules. ALLIES &amp; MERCENARIES: see that rule. Optional rules and the campaign/scenario material of the book are not built.</description>
    </rule>
    <rule id="ab33-a6c2-7dfe-9869" name="Impetuous" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Roll a D6 for each Impetuous unit in the Compulsory Movement phase: on a 1 it must charge the closest enemy unit in its charge arc (or move at least its base Movement towards it). Impetuous units must always pursue defeated enemies and after an Overrun, may never disengage (but may fall back in good order), and characters that join them become Impetuous.</description>
    </rule>
    <rule id="bd4c-eca0-b780-4ba5" name="First Charge (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Mounted units only: a modified Ferocious Charge. The unit automatically breaks (1) skirmishers it defeats in any charge or counter-charge, and (2) the first formed enemy unit it successfully charges or counter-charges. Later charges against formed units still count as charges but do not auto-break. Charging stakes or a defended obstacle expends the ability. Characters with the unit share the benefit; individual characters never have it.</description>
    </rule>
    <rule id="1011-1e73-6be9-a6cc" name="Allies and Mercenaries (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Allies &amp; Mercenaries may have a Leader, Standard and Musician, but may not benefit from the Army General or Army Battle Standard (they may be led by an appropriate character). The first time each unit moves, charges or shoots roll a D6: on a 1 it stays put (it may still defend itself); once it has acted it is moved normally. They count as part of the army for Panic tests.</description>
    </rule>
    <rule id="6b07-0a99-df48-7a76" name="Open Order" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Open Order troops move by the standard rules; infantry ignore difficult terrain and obstacles (no marching), may reform at the end of their move (then they cannot shoot), and count a +1 rank bonus in open ground and difficult terrain (some units up to +2 in open ground only). Open Order cavalry only get the rank bonus given in their list.</description>
    </rule>
    <rule id="10cb-8ff1-1102-5f18" name="Skirmishers (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Skirmish Order: individual models need their own line of sight; skirmishers fear formed troops (but need not take a Fear test to flee or fire &amp; flee as a charge reaction). Charging a flank or rear does not cause a Panic test.</description>
    </rule>
    <rule id="7acf-f489-43af-c5c6" name="Combined Formation (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Units may mix troop types (archers or retainers in the rear ranks). Archers lose Open Order and are Close Order for movement and rank bonuses; missile hits use the saving throw of the majority of models in the unit; special abilities apply until no model with them remains.</description>
    </rule>
    <rule id="5112-f682-7dc3-3910" name="Mixed Order (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Missile troops form the front rank(s). On entering close combat they may stay in front (and stand &amp; shoot, with second-rank spearmen fighting) or retire to the rear (no shooting, but up to two ranks of spearmen or one of other infantry fight). Bringing them forward again takes a whole turn. The unit uses the majority Leadership, or the accompanying character's if higher.</description>
    </rule>
    <rule id="2b47-9dc0-d5cf-1540" name="Medieval Phalanx" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>May wheel, About Face and adjust ranks but cannot Right/Left Face or change facing when engaged on the flank or rear. With at least 16 models and a +1 rank bonus: may charge and still fight in two ranks, hand-to-hand attacks from foot troops against its front are -1 to hit (not missiles), and mounted attackers get no strength bonuses from weapons and are -2 to hit.</description>
    </rule>
    <rule id="cdf2-4e23-32cc-339e" name="Mounted Infantry" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>May make a regular cavalry move (not march) after deployment before Turn 1; then they abandon their horses and fight as infantry.</description>
    </rule>
    <rule id="c8d7-4111-29b3-cb24" name="Hatred (Tartars and Akinjis)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Hate Tartars and Akinjis.</description>
    </rule>
    <rule id="1923-23ba-d0c2-bab8" name="Stubborn (if dismounted)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Stubborn while on foot.</description>
    </rule>
    <rule id="066d-f6c4-1088-879a" name="Stubborn (if with Knights)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Stubborn while with a unit of Knights.</description>
    </rule>
    <rule id="4bf3-0ece-03cb-1bfb" name="Stubborn (if led by Kniaz)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Stubborn if led by a Kniaz.</description>
    </rule>
    <rule id="72e2-57f0-74f2-870c" name="Stubborn (if with Royal Banderium)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Stubborn if with the Royal Banderium.</description>
    </rule>
    <rule id="b0d6-18a7-6e51-a304" name="Stubborn (if in Mixed Order)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Crossbowmen and Handgunners in Mixed Order are Stubborn.</description>
    </rule>
    <rule id="c716-8a8d-ed35-c7c4" name="Arrogant Pride" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>If a unit containing French Knights and/or Esquires charges an enemy unit, any unit containing mounted French Knights and/or Esquires within 12" of the charging unit automatically charges its nearest enemy (or, if none is in charge distance, moves at least 4" towards the nearest enemy within its charge arc).</description>
    </rule>
    <rule id="dfee-081f-7d45-f669" name="Keeper of the Oriflamme" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>The Oriflamme may be carried as the army's battle standard in a King-led army (+50 pts). It may only be accompanied by a unit of Gendarmes/Knights; that unit is immune to panic; if surrendered to a victorious opponent the banner is worth 250 Victory points; its powers are lost when the Battle Standard Bearer is killed.</description>
    </rule>
    <rule id="6de6-220a-e377-6b25" name="Plançon" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>The plançon confers a +1 Strength bonus on all hits.</description>
    </rule>
    <rule id="546e-6751-754c-671b" name="Bishop (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Knights, Men-at-Arms or a Combined Formation of Knights and Men-at-Arms led by a Bishop are Stubborn; Archers or Infantry led by a Bishop may re-roll failed Panic tests.</description>
    </rule>
    <rule id="c996-7318-dfa3-c667" name="Peasants (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Peasants/levies fear enemies they do not outnumber by at least two to one; they do not fear other peasants/levies or skirmishers.</description>
    </rule>
    <rule id="00c5-ce8b-a5a1-9fb4" name="Noble Commander (Poland)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Substituted for unit Leaders in units of Knights; roll a D6 for each before deployment: 1 Young Hotspur (+1 Attack; Impetuous roll 1 or 2); 2 Venerable Leader (Ld 9); 3 Potential Usurper (Ld 7 for him and the unit, which cannot use the General's Ld); 4 Defiant/Reluctant Leader (unit is subject to Allies &amp; Mercenaries); 5 Charismatic Leader (Knights may re-roll misses once); 6 Notable Reputation (+1 WS and fear).</description>
    </rule>
    <rule id="e62c-c6c3-91f0-78ba" name="Superior Shock Cavalry" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Superior Shock Cavalry (Junior Druzhniks): see the Eastern Shock Cavalry rule; as the army list entry.</description>
    </rule>
    <rule id="17a4-ae40-439d-071c" name="Hidden Ambush Force" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>At the start of deployment units with this rule are set up in hiding anywhere on the table out of sight and not in the opposing deployment zone, writing down their positions; they deploy at the start of the player's first turn.</description>
    </rule>
    <rule id="2a62-c9cc-2d6a-188a" name="Frenzy (Religious Personality)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>The Religious Personality and his unit are subject to frenzy; frenzy is lost when he dies or the unit is broken. Other Crusading Peasant units within 12" may use his Leadership.</description>
    </rule>
    <rule id="8861-cbab-8921-6290" name="Ghazi" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Ghazis may re-roll their first failed Panic test.</description>
    </rule>
    <rule id="2660-c4f0-54b9-1d22" name="Mehterhane" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Must be placed in the same unit as the Army General; the unit is immune to panic and each Mehterhane model adds 1" to the General's Leadership radius (max +3").</description>
    </rule>
    <rule id="4ee9-84dc-36b3-e440" name="Janissary Panic" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Janissaries may re-roll their first failed Panic test.</description>
    </rule>
    <rule id="b809-c689-b4e0-d956" name="Ottoman Wagon Tabor" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>In Conquest Ottoman armies the Janissaries may deploy inside a Wagon Tabor in place of the regular defenders; the General, the Army Standard Bearer and all Janissaries must deploy inside.</description>
    </rule>
    <rule id="d388-3995-bc20-74ea" name="Chicken" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Francs-archers fear any formed troops with a Leadership of 7 or more.</description>
    </rule>
    <rule id="1f4f-7b67-7be8-c31a" name="Cantonal Standards" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>The Gewalthut must begin the game as the largest unit in the army; while it is in good order all formed Swiss infantry within 12" may re-roll failed Break tests; it gains +1 combat results as if it had an Army Standard; if it loses its standards they are worth 300 Victory points.</description>
    </rule>
    <rule id="dfeb-8f7d-cb3d-409f" name="Artillery (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Light cannons (no indirect fire). Models are based singly; crew move at their basic Movement (no marching). Guns within 5" form a battery; all artillery may have a Leader but not a Standard or Musician. Characters may join a gun or battery (never harmed by a misfire). Cannons cannot fire at chargers. Artillery dice rolled twice (misfire / bounce); misfire 1-3 malfunction, 4 damp powder, 5 gunner killed and Panic, 6 destroyed. Fewer than three crew: fires every other turn. A Master Gunner may re-roll one Artillery dice misfire. A gun passed through by enemy troops is lost.</description>
    </rule>
    <rule id="3546-8072-f93d-9bd9" name="Multi-barrelled Artillery (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>Ribaud/organ gun: template placed in front of the gun and moved D6"; models touched are hit on 4+ at Strength 4 (-1 save). Can stand &amp; shoot when charged.</description>
    </rule>
    <rule id="3e37-dc67-7f91-7046" name="War Wagon (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>A wagon, 2-4 horses and six crewmen (three halberd, three missile). May never charge or fast march; halved movement if it turns. Missile crew fire twice per Shooting phase (-1 if moved); crew saves +2 as a large shield or pavise; the wagon gets no save but is immune to individual missile weapons; tall - can see and be seen over low obstacles. May be single models (no Leader, Standard or Musician) or units of at least three. A tarasnices (+20 pts) fires as a carroballista.</description>
    </rule>
    <rule id="b1b5-e018-17f8-3d3e" name="Wagon Tabor (Chivalry)" publicationId="da79-edc9-ea11-dbc4" hidden="false">
      <description>The Tabor is deployed as one unit, placed first, with wagons up to 3" apart and the wagons at each end touching the owner's table edge; it may not move after deployment. Each wagon's defenders (5-10) are a separate unit with Different Weapons, placed in base contact, counted as inside the wagon, and cannot leave voluntarily; defenders' armour saves are +2 as a large shield or pavise.</description>
    </rule>
    <rule id="f3d5-9740-06a8-2e5f" name="Spartacus Common Rules" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>The minimum size of a unit is five models; there is no upper limit. One model in each unit may be upgraded to a Leader (+5 pts), Standard Bearer (+5 pts) and Musician (+5 pts) unless mentioned otherwise. Where a unit is armed with mixed weapons, the Mixed Weapons rule of the WAB rulebook applies (page 127); Improvised Weapons are on page 45. Percentages are by points. The Army Standard Bearer follows the Roman Army Standard rules (WAB rulebook page 119).</description>
    </rule>
    <rule id="fb40-2bcc-1dd0-5369" name="Hates Romans" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Where this special rule is noted, the unit or character is subject to the Hatred rules sections 2 and 3 but not 1 (ie, re-roll misses in the first round of combat and must pursue towards the Roman units).</description>
    </rule>
    <rule id="c1e4-f4e9-0d11-e603" name="Looting" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>In the event of a Slave unit catching and destroying a fleeing Roman unit better equipped with shields and weapons than them, they may take the opportunity to loot the bodies and continue the battle using that equipment instead. Should the Slave unit subsequently flee for any reason, they lose this bonus equipment and revert to their original equipment options. The looting does not include armour.</description>
    </rule>
    <rule id="6986-5bfa-aff4-9ac3" name="I'm Spartacus!" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>If Spartacus is in a unit and should lose his final wound, then on a 4+ he is not really dead - he may be exchanged with another model in the unit and is left with one wound. If Spartacus is not in a unit and loses his final wound, or is killed/ran down due to pursuit, then on a roll of 6 he is not really dead but replaces the nearest friendly model and is left with one wound remaining.</description>
    </rule>
    <rule id="eb8a-fc36-21c7-e98f" name="All is lost!" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>If Spartacus is finally killed, then Spartacus's entire army has to carry out a Leadership test with -1 to their Ld.</description>
    </rule>
    <rule id="a383-ce74-110c-0860" name="We'll take care of the rear!" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Units with this special rule must be deployed together as the last units (prior to any character placement) to the rear of the army.</description>
    </rule>
    <rule id="3241-4297-4e88-0366" name="Different Equipment" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Unlike other units, separate Gladiator models may be armed and equipped differently within the unit, including the Toughness option (use a particularly large model). Gladiators may be deployed as a single unit of Light Infantry (at least five models, no Leader, Musician or Standard) or included in other units to a maximum of two per unit; if deployed in other units they are subject to that unit's Leadership and psychology and may not leave. If joined by Spartacus the unit is immune to panic, fear and terror and may use his Leadership even in skirmish order. Victory points are gained for each Gladiator killed.</description>
    </rule>
    <rule id="06df-a9d4-2df7-c18c" name="Skirmishers (Spartacus)" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Skirmishers: see the WAB rulebook (pages 54-56).</description>
    </rule>
    <rule id="ed60-53b0-dfe2-63ce" name="Bolt Thrower (Spartacus)" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Bolt Thrower - see WAB rulebook: range 36", Strength 4/-1 per rank, no save, D3 wounds per hit. Crew of two or three men.</description>
    </rule>
    <rule id="a1d1-33c1-4ece-30c0" name="Fiery Rollers" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>Nominate one formed unit with the rollers at the start of the game and place two rollers or suitable markers along the unit's front facing; while it has the rollers it causes fear in its frontal facing. The unit can only move in open terrain. In its Shooting phase it may 'shoot' one or both rollers at an enemy unit: 3D6" if on higher ground, 2D6" on level ground, over clear ground. A roller reaching the enemy causes D6 Strength 4 hits with no armour save; Drilled units and units in skirmish formation may take a test with -1 to their Ld to avoid each roller. If the unit is charged to its front or charges, each roller causes D6 S4 hits on the enemy unit. Wounds do not count towards combat resolution but may cause a Panic test if 25% casualties are caused. The rollers can only be used once.</description>
    </rule>
    <rule id="e883-1394-227e-6cf9" name="Fasces" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>The Lictor carries the Fasces, which allows the Consul the following options once per Lictor during the game: (1) re-roll any Roman Leadership test once within 12" of the Consul, OR (2) add +1 to any Roman combat resolution once within 12" of the Consul. Lictors may be captured in the same way as a unit standard or killed in hand-to-hand combat; either way each is worth an additional 200 Victory points.</description>
    </rule>
    <rule id="8c3c-e6f2-08bf-0faa" name="Reputation" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>At the start of the game Crassus may remove one legionary in ten (removed equally as possible across all legionary units, rounding to the nearest ten). This allows all Roman Legionary units to re-roll failed Panic tests and, should a legion break and be caught from combat, the slaves cannot loot its equipment. Once a re-rolled Panic test is also failed both benefits are lost. You may re-roll a failed test using the Lictor if it is that desperate.</description>
    </rule>
    <rule id="220b-0a35-497d-055b" name="Wealthy" publicationId="eb14-e889-c793-0fc4" hidden="false">
      <description>At the start of the game Crassus may nominate and upgrade one Legionary unit to become Drilled and Stubborn at no additional points cost.</description>
    </rule>
    <rule id="d81e-b4ce-ed5b-0f8a" name="Superior Byzantine Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of any close combat when charging or counter-charging). Superior Byzantine Cavalry may also choose to retire if they win a round of close combat but fail to force their opponents to flee or fall back: a normal Fall Back in Good Order move, the retiring unit may only be pursued by opponents with Movement equal or greater than its own and may still charge next turn. Not usable by cavalry on barded or half-barded horses.</description>
    </rule>
    <rule id="1d12-bc45-2d33-3c87" name="Superior Germanic Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). The first formed enemy unit successfully charged or counter-charged by Superior Germanic Cavalry will automatically break if it loses the combat, but only if the enemy is outnumbered by the Superior Germanic Cavalry unit.</description>
    </rule>
    <rule id="5cb2-6061-5274-fafb" name="Superior Persian Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). May shoot when they charge or counter-charge and may use massed archery whilst doing so, after enemy charge reactions, counting as short range (the -1 for moving still applies). Enemy units taking 25% casualties or more must pass a Panic test or flee; these casualties do not count towards combat resolution.</description>
    </rule>
    <rule id="b872-96ac-4ea5-adb8" name="Superior Turkish Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). During their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching. May also perform Parthian Shot.</description>
    </rule>
    <rule id="b17a-4b32-79d8-eb7b" name="Superior Arab Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). During their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching.</description>
    </rule>
    <rule id="e3a9-d9d8-2307-2312" name="Shieldwall (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>May form a shieldwall instead of moving. While in a shieldwall all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit. Benefits last while the unit remains stationary and does not lose a round of close combat.</description>
    </rule>
    <rule id="7490-e7d5-847a-a64d" name="Levies (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Levies fear enemies they do not outnumber by at least two to one. Levies do not fear other levies or skirmishers.</description>
    </rule>
    <rule id="cd5e-089d-1006-a3c7" name="Fearsome" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>All enemy units with a base Leadership value of 7 or less fear troops who are Fearsome. If a character or model with a higher Leadership leads the unit they still fear them but may use the leader's higher Leadership for the Fear test. The same applies to warbands.</description>
    </rule>
    <rule id="95d8-6cde-5fe8-2d88" name="Oath of Allegiance" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>If the Army General is killed roll a D6. On a 4+ the troops immediately move towards and charge the nearest enemy and are immune to Panic and Break tests. If they eliminate their opponent they attack the nearest enemy unit again, and so on. They must always pursue a broken enemy.</description>
    </rule>
    <rule id="5f68-9317-adc3-5f98" name="Nomad Cavalry (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Mad Cavalry: tribesmen living most of their lives on horseback count as Nomad Cavalry - they benefit from the Expert Horsemen, Parthian Shot, Feigned Flight and Special Deployment rules. Special Deployment: may make a march (not fast march) or double pace move after deployment but before the battle begins; may not charge or shoot after this move.</description>
    </rule>
    <rule id="ce4b-42b1-6eb6-6e51" name="Skirmishers (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Skirmishers: see the WAB rulebook (pages 54-56).</description>
    </rule>
    <rule id="2280-7c4f-4408-0d5e" name="Combined Formation (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Combined Formation: units may mix two troop types in one unit (for example spearmen with archers in the rear ranks, or cavalry with Hippo-toxotai); the proportions and equipment limits are given in the unit entry. Not enforced.</description>
    </rule>
    <rule id="ae37-af5c-6af4-d2db" name="Blunt-nosed Wedge (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Blunt-nosed Wedge (Kataphraktoi): a unit adopting this formation at deployment pivots instead of turning or wheeling (pivoting more than 90 degrees costs a quarter of the move unless Drilled); when it charges every model may attack and for every two models fighting one extra model in the charged unit may fight too; it flattens out if charged in the flank or rear, loses a round of combat (unless it falls back in good order) or is charged without counter-charging. No rank bonus while in wedge. Needs at least seven models.</description>
    </rule>
    <rule id="e6ca-607d-70ea-60e9" name="Fear Cavalry (Camels)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Camels cause fear in enemy cavalry.</description>
    </rule>
    <rule id="4408-201c-0b5d-35ae" name="Bedouin Cavalry (Phylarch)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Bedouin Cavalry: during their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching. The Phylarch must lead and may not leave a unit of Ghassanid Arab Cavalry.</description>
    </rule>
    <rule id="e6ff-67de-8925-b725" name="Basileus (Emperor)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Emperor: Leadership 10. May only be taken in armies exceeding the points value given in the unit entry.</description>
    </rule>
    <rule id="9fa3-2a4d-66f0-74e5" name="Excubitores" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Excubitores: the Bucellarii are armed with maces and led by the Emperor (Heraclian armies).</description>
    </rule>
    <rule id="c5d9-a0b1-75cc-3f5f" name="Rusticani" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Rusticani: see the Early Byzantines list.</description>
    </rule>
    <rule id="8660-df66-d3fc-41c8" name="Circus Faction Mob" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Green or Blue Circus Faction mob: subject to Warband Psychology Rule 1; cannot Fall Back in Good Order, cannot benefit from the Leadership of characters other than their Faction Leader, nor use the re-roll benefit of the Army Standard.</description>
    </rule>
    <rule id="2e58-7019-1734-cb73" name="Cane Shieldwall" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Spearmen with Cane Shields may form a Cane Shieldwall (as a shieldwall).</description>
    </rule>
    <rule id="8527-75ea-1d4f-09ec" name="Cataphract (Sassanid)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Sassanid Cataphracts: see the Sassanid Persians list.</description>
    </rule>
    <rule id="64e7-ecbd-f9c6-14ae" name="Elephant (Sassanid)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Indian Elephant: see the Sassanid Persians list and the WAB rulebook.</description>
    </rule>
    <rule id="d880-9592-829c-72f3" name="Throne (Sassanid)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>The Shahanshah's throne with guards: see the Sassanid Persians list.</description>
    </rule>
    <rule id="1012-5401-b259-113c" name="Scythed Chariots (Sassanid)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Scythed chariots may be fielded in units of less than three models. They may not have Standards, Leaders or Musicians. A Scythed Chariot counts as three models for the calculation of unit size.</description>
    </rule>
    <rule id="77ac-4e48-8d45-97c0" name="Jan-avaspar" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Jan-avaspar (Shahanshah's guards): Leadership 9; Later Sassanid armies led by the Shahanshah.</description>
    </rule>
    <rule id="7bd2-04f5-bb55-a733" name="Jurz Maces" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Jurz maces count as heavy maces.</description>
    </rule>
    <rule id="41e1-0e30-008f-b975" name="Basque Light Cavalry" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Basque Light Cavalry: see the Germanic Kingdoms list.</description>
    </rule>
    <rule id="bdb4-87f2-020d-9077" name="Priest (Germanic)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Units led by a priest become Stubborn when they fight enemies of a different creed than themselves.</description>
    </rule>
    <rule id="dee3-bedc-300e-b45b" name="Great Khagan" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Great Khagan: Leadership 10.</description>
    </rule>
    <rule id="a75f-576e-fefc-6ca5" name="Companion (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Companions: units led by a Companion may re-roll failed Panic tests. The Companion is not subject to Warband Psychology.</description>
    </rule>
    <rule id="cc22-01bc-7052-d968" name="Marzban (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Marzban: must lead a Khurasan Cavalry unit.</description>
    </rule>
    <rule id="9de5-c470-6aa6-ff1e" name="Naffatun (Byzantium)" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Naffatun must be incorporated in units of City Militia skirmishers (one per unit). Their incendiary projectiles are treated like javelins with Strength 4; no armour save is allowed. A unit that receives a wound from a Naffatun must take an immediate Panic test; if it panics it flees an extra D6".</description>
    </rule>
    <rule id="340b-6fae-dc95-8cdb" name="Heavy Mace" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Heavy Mace: see the WAB rulebook.</description>
    </rule>
    <rule id="0606-6868-54b9-0511" name="Imperial Army Standard" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>Imperial Army Standard: +1 to the Leadership of the standard bearer (Tagmata armies).</description>
    </rule>
    <rule id="3343-f051-f099-9927" name="Byzantium Common Rules" publicationId="15ea-5299-d0f5-5dbb" hidden="false">
      <description>The minimum size of a unit is five models unless stated otherwise. One model in each unit may be upgraded to a Leader, Standard Bearer and Musician as in the WAB rulebook. Stratagem (documented): armies led by an Army General of the relevant kind may use the Stratagem special rule from the Early Byzantine chapter.</description>
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
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">Swords, axes, clubs, hammers and all similar weapons wielded in one hand are comparable in effect: a hand weapon is the basic weapon and no special rules apply. Troops with a weapon in each hand (two swords, or a sword and long dagger) have +1 extra attack in hand-to-hand combat, whatever their Attacks value (p.91). No warrior may ever have a Strength above 5 (p.91).</characteristic>
      </characteristics>
    </profile>
    <profile id="a767-c23a-5b8e-1596" name="Dagger" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">All troops carry daggers or knives as a last resort. Enemy wounded by daggers receive a +1 armour save modifier (one pip better); if they otherwise have no save they save on a 6. E.g. a 5 or 6 save becomes 4, 5 or 6 (p.91). Troops so armed are at a disadvantage compared to those properly prepared for combat.</characteristic>
      </characteristics>
    </profile>
    <profile id="026a-8df7-0a12-0a18" name="Improvised Weapon" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">Bow staves, crossbow butts, javelins, weapons wrested from the enemy, or rocks and rough clubs. Enemy wounded by improvised weapons receive a +1 armour save modifier; if they otherwise have no save they save on a 6 (p.91). Troops so armed are at a disadvantage compared to those properly prepared for combat.</characteristic>
      </characteristics>
    </profile>
    <profile id="bebe-c4da-722c-c475" name="Double-handed Weapon" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">Large axes, swords, hammers and clubs needing two hands. Troops that carry shields cannot use them in hand-to-hand combat (shields are assumed slung or abandoned). Always strike last in hand-to-hand combat regardless of Initiative or charging; if both sides have double-handed weapons normal priorities apply (charger first, otherwise higher Initiative). +2 Strength on all hits (maximum Strength 5); the enemy armour save is reduced by the higher Strength as normal (p.92).</characteristic>
      </characteristics>
    </profile>
    <profile id="635a-1d79-5976-954c" name="Halberd" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">A heavy-bladed weapon on a sturdy shaft. Two hands are needed: troops that carry shields cannot use them in hand-to-hand combat. +1 Strength on all hits (maximum Strength 5); the enemy armour save is reduced by the higher Strength as normal (p.92).</characteristic>
      </characteristics>
    </profile>
    <profile id="5a59-1efb-14ef-017a" name="Thrusting Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">A spear about ten feet long retained and thrust. Infantry fight in two ranks to their front if the unit did not move and the second-rank model's front-rank comrade is fighting exclusively to the front; a unit that charges cannot fight in two ranks. Cavalry add +1 Strength when they charge or countercharge over open ground, in that turn's hand-to-hand combat only (p.93).</characteristic>
      </characteristics>
    </profile>
    <profile id="cc82-90f9-0ade-c0e7" name="Throwing Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">Hand-to-hand weapon, thrown just before combat and used again as a hand weapon. Infantry fight in two ranks in the first round of each combat engagement, both when they charge and when charged; a second-rank model may fight only if the model in front is fighting to its front. Cavalry may re-roll misses in the first round of each combat unless they charged or countercharged through or into difficult terrain. Skirmishing infantry may re-roll misses in the first round (p.92).</characteristic>
      </characteristics>
    </profile>
    <profile id="26ae-ef02-1f24-a490" name="Heavy Throwing Spear" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">A heavier throwing spear (e.g. pilum, saunion, angon, throwing axe) that penetrates shields and armour. Infantry fight in two ranks in the first round of each combat engagement (as throwing spears) and add +1 Strength in the first round. Skirmishing infantry may re-roll misses in the first round (p.93).</characteristic>
      </characteristics>
    </profile>
    <profile id="8acf-e438-93ac-347e" name="Pike" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">An extremely long spear (16 ft or more); two hands are needed but shields or bucklers strapped to the forearm are allowed. Infantry fight in two ranks irrespective of movement and, if fighting exclusively to their front, always strike first regardless of Initiative or charging; if both sides are pike-armed normal priorities apply (p.94).</characteristic>
      </characteristics>
    </profile>
    <profile id="f901-2529-d411-6ed0" name="Kontos" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">A very long cavalry spear needing two hands; riders cannot carry a full-sized shield but may have small shields or bucklers. Cavalry add +1 Strength when they charge or countercharge over open ground (that turn only) and always strike first against troops with shorter weapons if fighting exclusively to their front (not versus pikes; if both have kontos normal priorities apply). Neither bonus applies if charging through or into difficult terrain (p.94).</characteristic>
      </characteristics>
    </profile>
    <profile id="a4b8-1d78-eb6b-c4f2" name="Lance" publicationId="556c-7119-7234-b625" page="91 (summary p.210)" hidden="false" typeId="89ad-db9d-72f5-90d2" typeName="Hand-to-Hand Weapon">
      <characteristics>
        <characteristic name="Effects" typeId="fa7e-7b3b-c328-7b67">The couched lance is the weapon of the charging cavalryman. Cavalry add +2 Strength when they charge or countercharge over open ground (that turn only; maximum Strength 5). Not if charging through or into difficult terrain. After the first charge the rider fights with a hand weapon (p.94).</characteristic>
      </characteristics>
    </profile>
    <profile id="b36d-1525-b0bc-5c0f" name="No Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">None</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">No armour, only a helmet or minimal clothing. Infantry have no save, but a shield turns this into a 6 (it still adds a pip); cavalry save on a 6 for the advantage of riding a horse (p.96). Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="e1d7-1cd3-1431-4862" name="Light Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">5 or 6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">Breastplate or cuirass of metal, cloth or leather reinforced with metal, bone or horn plates, scales or lamellar (p.96). Infantry in light armour alone save on 6, cavalry on 5 or 6. Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="16c5-d2b2-fa96-9cd2" name="Heavy Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">5 or 6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">4, 5 or 6</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">Light armour plus helmet, greaves, manica and further reinforcement (p.96). Infantry in heavy armour alone save on 5 or 6; cavalry on 4, 5 or 6, which becomes 3, 4, 5 or 6 with a shield (a large shield adds nothing more). Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="aa63-8f92-57ef-91e7" name="Cataphract Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">-</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">Armour covering the rider from head to foot (horn, lamellar or overlapping scales); cataphracts have no need of shields (p.96). Cavalry save on 3, 4, 5 or 6 with or without a shield. * Either with or without shield: a shield adds no bonus (p.97). Troops so equipped are also affected by the Cataphracts special rule (p.104). Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="8430-72da-5ac5-d33f" name="Partial Plate Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">4, 5 or 6</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">Mail with plates extending over it (p.97). Infantry save on 4, 5 or 6, or 3, 4, 5 or 6 with a shield (a large shield adds nothing more). Cavalry as cataphract armour: 3, 4, 5 or 6 with or without shield. * Either with or without shield: a shield adds no bonus (p.97). Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="70a8-fcb7-f10e-4737" name="Full Plate Armour" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="96b5-bd5f-9a95-1bd7" typeName="Armour">
      <characteristics>
        <characteristic name="Infantry Save" typeId="80cf-4b2c-fa74-7e4d">3, 4, 5 or 6*</characteristic>
        <characteristic name="Cavalry Save" typeId="227d-844c-2992-a59b">3, 4, 5 or 6*</characteristic>
        <characteristic name="Notes" typeId="85c2-9874-4f90-9229">Articulated metal plates enclosing the wearer from head to foot (p.97). Infantry and cavalry both save on 3, 4, 5 or 6 with or without a shield, so no shield bonus is applied. * Either with or without shield: a shield adds no bonus (p.97). Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ (ignoring barding) -1"; cavalry with metal barding another -1" (p.96).</characteristic>
      </characteristics>
    </profile>
    <profile id="b513-5c2a-34df-6a1d" name="Shield" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Close-combat troops carry shields. Troops with double-handed weapons or halberds cannot use their shields in hand-to-hand combat. No benefit where the armour already gives the maximum save or where marked * (p.97).</characteristic>
      </characteristics>
    </profile>
    <profile id="8367-11b2-7778-977f" name="Large Shield" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+2 pips to the armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">A shield covering a substantial part of the bearer's body, overlapping those of neighbours. Cannot bring a save above the maximums, so there is no benefit over a normal shield in some cases (p.97).</characteristic>
      </characteristics>
    </profile>
    <profile id="f587-5eb5-fc55-6409" name="Pavise" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+2 pips to the armour saving throw (when shot at from the front only)</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">A very large shield for missile troops, hung on the back or propped up. No bonus in other circumstances or in hand-to-hand combat; cannot bring a save above the maximums (p.98).</characteristic>
      </characteristics>
    </profile>
    <profile id="aa05-2e85-a1d8-8d69" name="Buckler" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">A very small shield favoured by lightly equipped troops. Infantry and cavalry in skirmish formation add the pip against all wounds; other troops add it in hand-to-hand combat only, not against shooting (p.98).</characteristic>
      </characteristics>
    </profile>
    <profile id="e556-cf0c-4c05-4d8b" name="Full Metal Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the cavalry armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Metal barding (often just "barding" in army lists) covers the whole mount. Cavalry with metal barding lose a further 1" movement (p.96, 98).</characteristic>
      </characteristics>
    </profile>
    <profile id="b16b-db14-3dfe-1470" name="Half Metal Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the cavalry armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Metal barding covering the front half of the mount: +1 pip only when hit from the front or fighting hand-to-hand to the front, not from the side or rear. Cavalry with metal barding lose a further 1" movement (p.96, 98).</characteristic>
      </characteristics>
    </profile>
    <profile id="967d-06de-de04-9660" name="Full Cloth Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the cavalry armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Padded cloth or felt barding covering the whole mount: +1 pip in hand-to-hand combat only, not against shooting. "Barding" alone in an army list means metal barding (p.98).</characteristic>
      </characteristics>
    </profile>
    <profile id="3902-d49b-5509-fb74" name="Half Cloth Barding" publicationId="556c-7119-7234-b625" page="49 (summary p.205)" hidden="false" typeId="37e2-4bc8-b9e2-0e43" typeName="Shield or Barding">
      <characteristics>
        <characteristic name="Bonus" typeId="8e05-e350-dc3c-2a49">+1 pip to the cavalry armour saving throw</characteristic>
        <characteristic name="Note" typeId="86a0-abae-4649-7d70">Padded cloth barding covering the front half of the mount: +1 pip in hand-to-hand combat when fighting to the front only, not from the side or rear, not against shooting (p.98).</characteristic>
      </characteristics>
    </profile>
  </sharedProfiles>
</gameSystem>
