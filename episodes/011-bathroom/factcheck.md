# FILE 011 (bathroom): independent fact-check

Checked: episode.py (long video), shorts s1–s3, tiktok t1–t3. Every q quote was checked word for word against the OCR of the scans (pat/<N>/p*.txt). Where the OCR is noisy, the scan reading was used. Quotes were spot-checked on Google Patents for 5,983,411; 3,128,161; 4,790,036; 4,825,779; 5,926,099; 2,528,006; and 428,252. The Google page for 3,732,580 failed to load (server error), so the scan OCR decides for that patent. Its quotes are clean in the OCR apart from line-break artifacts ("hair.and", "in: which", "pro-—…grams").

## Issues

### MUST-FIX

1. **episode.py L152 ("And the claim spells it out: The front of the toilet tank assembly is generally transparent.") and tiktok/t1 L15 (same line)**
   Problem: that sentence is not in claim 1. Claim 1 reads "said front of said toilet tank assembly being generally transparent". The sentence as quoted appears in the Abstract, the Background, the Summary and the Detailed Description (confirmed on Google Patents and in the OCR, p4/p5).
   Fix: spoken "And the patent spells it out: The front of the toilet tank assembly is generally transparent." and `src` "US 5,983,411 · description". Or, to keep the claim, use q = "said front of said toilet tank assembly being generally transparent", spoken "And claim one spells it out: said front of said toilet tank assembly being generally transparent.", with src "US 5,983,411 · claim 1".

2. **episode.py L41 ("This is a toilet. The tank is made of glass…"), shorts/s1 L9 and tiktok/t1 L10 ("…The tank is made of glass, and there are fish in it.")**
   Problem: the patent never says "glass" (checked on Google and in the OCR). It says only that the front is "generally transparent". In the main embodiment only the front is transparent; FIG. 5 adds the front parts of the sides.
   Fix (L41): "This is a toilet. The front of the tank is see-through. And there are fish in it. It is a real United States patent."
   Fix (s1/t1): "This is a real U.S. patent. A toilet. The front of the tank is see-through, and there are fish in it."

3. **episode.py L150 ("…The flush water sits in a box of its own, in the middle of the tank.")** and **L151 ("…The fish swim in the space that wraps around the flush water.")**; **shorts/s1 L12 and tiktok/t1 L14 ("The flush water gets its own box in the middle. The fish swim all the way around it.")**
   Problem: toilet water reservoir 18 is not in the middle. Its mid wall is spaced from the back, and its side walls run to the back 15 of the tank, so the box sits against the back wall. The aquarium reservoir 22 is the space "between the toilet water reservoir 18 and the sides and front 14" (col. 4, claim 1). The fish cannot swim "all the way around" it, because there is nothing behind the box.
   Fix (L150): "Then it adds fish. The flush water sits in a box of its own, against the back of the tank."
   Fix (L151): "From the top, you can see the layout. The fish swim in the space around the front and sides of the flush water."
   Fix (s1/t1): "The flush water gets its own box at the back. The fish swim around its front and sides."

4. **episode.py L126 ("This toilet has motors. Two of them. And the seat is a ring that can turn.")**
   Problem: there are three motors. Electric motor 19 drives the swivel arms (col. 6/7, Stage VII), and "Two electric motors 29 are provided to drive the seat 27." Google Patents confirms three.
   Fix: "This toilet has three motors. Two of them just turn the seat. Because the seat is a ring that can turn."

5. **episode.py L128 ("Here is how. A cleaning unit swings out on arms and clamps over the seat…")**
   Problem: nothing clamps. The slide housing is "moved … into a position above a segment of the ring-shaped seat" and "placed on a segment of the seat". Support rollers 50 touch the inner edge while the seat turns. "Clamp" does not appear in the text (Google + OCR).
   Fix: "Here is how. A cleaning unit swings out on arms and settles over one part of the seat. Water nozzles. Disinfectant nozzles. And a wiper."

6. **episode.py L79 ("…The one the patent describes is three feet long, two feet wide, and about ten inches in height.")**
   Problem: the patent describes a tub "of suitable size to permit a person to conveniently sit therein". The dimensions belong to the inventor's own tub: "the one I use being three feet long…". (The inventor is not named, so referring to "the inventor" is fine.)
   Fix: "In eighteen ninety, this was a portable bathtub. The inventor's own was three feet long, two feet wide, and about ten inches in height." (The quote box stays as it is.)

7. **episode.py L59 ("Not a cheap one, either. A music box known to the trade as a Swiss movement, or music box unit.")**
   Problem: nothing supports "not a cheap one". The patent calls the unit "a standard equipment" and "a spring motored musical unit of a standard type", and it aims at "reasonable cost" (Google + OCR).
   Fix: "Just a standard one. A music box known to the trade as a Swiss movement, or music box unit."

8. **episode.py L69 ("Condition number one. A supply of reading material…")**
   Problem: the patent lists toilet paper first ("A supply of toilet paper needs to be furnished…"). Reading material comes second.
   Fix: "Condition number two. A supply of reading material from which a selection can be made is usually welcome." (or "One of the conditions: …")

### OPTIONAL

9. **episode.py L53 ("And when you are finished, it goes in a cupboard or other convenient place…")**
   Problem: the spoken words are presented as the quote, but the quote box reads "placed in a cupboard…". The line ends at L163, which says "every quote … is word for word".
   Fix: "And when you are done with it, it is placed in a cupboard or other convenient place until it is again desired to use the same."

10. **episode.py L131 ("…The water refilling the tank spins a little turbine, and the turbine makes the electricity.")**
    Problem: the turbine drives "a low-voltage direct-current generator". The generator makes the electricity.
    Fix: "It does not need an outlet, either. The water refilling the tank spins a little turbine, and the turbine drives a generator."

11. **episode.py L132 ("Switches check whether someone is sitting on the seat…")**
    Problem: the narration is true (contact strips 27''/28' and switches 38/39, col. 7). But the figure shown is FIG. 4, the spray section, and its "THE SPRAY" callout has nothing to do with the line. The switches are in FIG. 2, which is not vectorized.
    Fix: show seat1 instead: `fig(SEAT, "seat1", "1", draw=False, calls=[["THE SEAT", 608, 885, -150, 90]])`. Or keep seat3 and move the spray visual to L128/L129.

12. **tiktok/t1 L16 ("The flush handle still works. The lid has a light… And a compartment for aquarium supplies.")**
    Problem: the callouts are THE FLUSH WATER and THE FISH TANK. Neither matches the narration.
    Fix: calls `[["THE FLUSH HANDLE", 469, 512, 120, 80], ["THE SUPPLY COMPARTMENT", 400, 192, 120, -60]]` (points from sources.md).

13. **episode.py L60 (tooth2 callout "THE TRIGGER" at 165,320)**
    Problem: that point is flat spring 29. The trigger is arm 31. The narration on this line talks about the flat spring.
    Fix: rename the label to "THE FLAT SPRING".

14. **episode.py L44 ("…counted down from weird to weirdest.")**
    Problem: the ranking is marked as opinion elsewhere ("on our shelf", "Decided by us"). This first mention reads as a plain statement.
    Fix: "Real drawings, real quotes, counted down, in our opinion, from weird to weirdest."

15. **episode.py L137 ("Number two. The bathtub that rocks.") and L148 ("And number one…")**
    Note: in a bathroom episode, "number two" and "number one" can be heard as toilet puns. They are rank numbers, and the line's content is clean. Leaving them is acceptable. If you would rather avoid any double meaning, use "At number two…" plus a quick cut, or "Second place." Your call.

## Verified OK

- **Dates:** every stamp filed/issued date matches the printed patents. The front pages / headers were checked for 5,983,411, 5,926,099, 4,790,036 and 3,732,580, and the text headers for the pre-1970 patents. All chapter lines "Filed YYYY · Issued YYYY", all side-label years, all HOOK2 years, and every spoken "Approved, <month> <year>" match the issue dates. The pairs are: Nov 1942, Oct 1950, May 1989, May 1890, Apr 1964, May 1973, Jul 1999, Dec 1988, Jul 1913, Nov 1999. The episode span "eighteen ninety to nineteen ninety-nine" is correct.
- **Quotes:** all 44 q quotes in the 7 files appear verbatim in the patent text. The only differences are OCR noise, checked against the scans: "thai he cr she", "ap_ pearance", "purposes.in", "hair.and", "in: which", "eic." = "etc.". The drier quote uses the printed "person's"; Google drops the apostrophe ("persons choice"). Q_THRONE correctly puts the double quotes around "the throne" only.
- **Quote locations:** all "description" labels are correct, including Summary/Objects/Prior Art, which are part of the description. The only wrong location is the "claim 1" label (issue 1).
- **Lid signal:**
  - The pendulum switch works as narrated: a split-shot sinker (weight 60) on a nylon filament (70) bridges contacts 26A/26B by gravity when the device is upright (FIGS. 3A/3B, col. 9).
  - "a size 3/0 split shot sinker…" is verbatim.
  - The device sticks to the underside of the lid. It plays when the lid is raised and stops when it is lowered.
  - The greeting-card module, the bird and "fisherman" models, and "conditioning persons" are all verbatim.
  - No trauma, child or disability material is used.
- **Seat cleaner:**
  - The turbine is driven by water refilling the cistern, and no mains power is needed.
  - The seat cannot rotate while occupied (contact strips / switches 38, 39).
  - "at least 360°", "rotation of 400°", "social hygiene" and "circumferential direction" are verbatim.
  - The arms, the water and disinfectant nozzles and the wiper are correct.
  - No injury or child sentences are used.
- **Drier:**
  - Heads sit on both sides and at the top. Every head swivels (ball joint), and every branch duct has its own damper.
  - There is one push button 18, and the blower and heater sit at the end of the main duct.
  - "Close every damper except the top one" matches "all the branch duct dampers except damper 37 may be closed and heated air will be directed only to the region of the person's head". Damper 37 serves overhead head 23.
- **Hair machine:**
  - The sequence is correct. The heater and thermistor warm the water, pump P3 meters the hair-washing solution, then it washes, drains (P2), refills and rinses with pure water.
  - "Groups switch on and off" matches electrovalves E1–E3 on tubings 6/7/8 opened and closed alternately ("only to some of said showers at a time").
  - The seal and the timer are correct.
- **Toothbrush:**
  - The housing has a "roof portion" and mounts with suction cups on lugs (FIG. 2 shows a wall), so "hangs on the wall like a little house" is fair.
  - A flat spring is depressed by each brush handle.
  - With both brushes home, finger 33 sits in the path of the (spinning) governor 34. "spinning governor" is the patent's own wording.
  - The pull cord 38 has a tassel 39.
- **Portable tub:**
  - Posts fold up and the seat folds.
  - A rocking pedal T works two force-pumps that send water up hose W to nozzle X.
  - The water collects in depression B and is pumped again.
  - A canvas/oil-cloth/rubber cover goes over the frame.
  - Everything folds into the tub, the lid closes, and it has casters.
  - The "any and all parts of his person" sentence is avoided.
- **Towel rack:** suction cups; swing across the tub on pivot sleeve 18; ledge 21 and back rest 20; U-shaped resilient page holder 23 with knob 24. The ash tray is neither mentioned nor shown.
- **Table:** the top slopes toward the user (preferably at least 15°); ledge 34; roll on spindle 36 between the near (front) legs; slatted platform. Smoking content is avoided.
- **Rocking tub:** curved bottom with a back rest at one end; edges beaded for the arms; plate 10 at the lower end; sheet-metal rockers riveted on (two in FIG. 2); water drawn dotted; "plain metal or enamel ware".
- **Aquarium (apart from issues 1–3):**
  - The handle still works the flushing assembly.
  - Light source 30 under the front half of the lid shines into the aquarium reservoir.
  - Compartment 28 is "for storing items such as aquarium supplies".
  - The terrarium line, "more attractive" and the FIG. 6 separate aquarium on top are all correct.
  - "no further discussion…" is verbatim.
- **Callouts:** all coordinates match the figure notes in sources.md, apart from issues 11–13.
- **Content rules:** inventors are never named; no injuries, weapons, sex, medical procedures, children at risk or smoking. Jokes target the inventions ("A dishwasher. For your head.", "A car wash for people").
- **Ranking:** framed as opinion in "WEIRDNESS RANK", "on our shelf" and "Voted by nobody. Decided by us." See optional issue 14.
