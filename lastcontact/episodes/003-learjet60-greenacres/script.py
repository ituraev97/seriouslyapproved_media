# EPISODE 003 — Learjet 60 in-flight breakup and crash near Greenacres, Florida, Nov 1, 2026 (NTSB ERA27MA026)
# Sources: NTSB investigation page ERA27MA026 (updates Nov 5, 8, 9), NTSB media briefings Nov 2 and Nov 3
# (Member Tom Chapman, IIC) as quoted by AP/PBS, ABC, WPTV, CBS12, AIN, Bloomberg; FAA statement Nov 1; FAA AIM.
# (id, spoken text, pause_after, speed, visual)
# visual: ("3d", shot) | ("card", name) | ("photo", file, credit) | ("clip", file, start_s, label)
C21 = "FILE FOOTAGE · C-21A, A LEARJET 35-BASED U.S. AIR FORCE JET · NOT THE ACCIDENT AIRCRAFT · DVIDS"
WX = "FILE FOOTAGE · AIR FORCE RESERVE WEATHER RECONNAISSANCE FLIGHT · NOT THIS FLIGHT · DVIDS"
TOPS = "FILE FOOTAGE · STORM CLOUD TOPS FROM A WC-130J · NOT THIS STORM · DVIDS"
RAD = "FILE FOOTAGE · U.S. AIR FORCE RADAR CONTROLLERS · NOT MIAMI CENTER · DVIDS"
WXR = "FILE FOOTAGE · AIRBORNE WEATHER RADAR DISPLAY, WC-130J · NOT THIS FLIGHT · DVIDS"
FCST = "FILE FOOTAGE · U.S. AIR FORCE WEATHER FORECASTERS · NOT CONNECTED TO THIS FLIGHT · DVIDS"
NTSBPH = "NTSB PHOTO · AN INVESTIGATOR SEARCHES THE IMPACT SITE FOR WRECKAGE"
LINES = [
 # ---- cold open
 ("o1", "Sunday, November first, two thousand twenty-six. Twelve forty-seven in the afternoon, eastern time. A Learjet sixty is flying at thirty-five thousand feet, on its way to the Bahamas.", 0.5, 1.0, ("3d", "cruise")),
 ("o2", "The crew tells air traffic control they have light ice on the airplane, and moderate turbulence, causing altitude deviations of about seven hundred feet.", 0.45, 1.0, ("3d", "cruise")),
 ("o3", "They ask to climb to thirty-seven thousand feet. The controller approves.", 0.5, 1.0, ("3d", "cruise")),
 ("o4", "According to the N T S B, less than thirty seconds later, a transmission from the airplane announces a descent. Then a mayday.", 0.7, 0.97, ("3d", "cruise_dive")),
 ("o5", "At about twelve fifty-one, the jet hits the ground in Palm Beach County, next to a mobile home community. All nine people on board are killed.", 1.1, 0.95, ("card", "toll")),
 ("o6", "In this video, we go through only what the N T S B and the F A A have said so far: the radio calls as investigators described them, the weather questions, and the pieces of the tail found miles from the crash site.", 0.5, 1.02, ("card", "toll")),
 ("o7", "None of this is a finding of cause. The investigation is in its early stage, and the N T S B has not determined one.", 1.3, 0.96, ("card", "title")),

 # ---- what we use
 ("r1", "A quick note first. A lot of numbers about this crash are circulating online: descent rates, flight tracks, and recordings of the radio calls.", 0.4, 1.0, ("card", "rules")),
 ("r2", "Most of them come from flight-tracking websites and from unofficial recordings of air traffic control. Some may turn out to be accurate. But they are not what the N T S B has published.", 0.4, 1.0, ("card", "rules")),
 ("r3", "So in this video, the facts about the flight come from the N T S B's investigation page, from what N T S B officials said at their briefings, or from the F A A. Where a detail comes from local officials or news reporting, we say so.", 1.0, 1.0, ("card", "rules")),
 ("r4", "We also do not play recordings of the radio calls. Out of respect for the people on board, we describe them only in the words the N T S B used.", 1.0, 1.0, ("card", "rules")),

 # ---- investigation
 ("p1", "The N T S B launched a go team the same day. Board member Tom Chapman led the briefings on scene, alongside the investigator in charge.", 0.4, 1.0, ("photo", "ph/ntsb1.jpg", NTSBPH)),
 ("p2", "On the first evening, about twenty N T S B investigators began arriving, with more the next day. Their specialties included aircraft systems, structures, recorders, weather, and air traffic control.", 0.4, 1.0, ("photo", "ph/ntsb1.jpg", NTSBPH)),
 ("p3", "The F A A and the airplane's manufacturer are parties to the investigation. The case number is E R A twenty-seven M A zero two six.", 1.0, 1.0, ("card", "parties")),
 ("p4", "The F A A's statement that day said the Learjet sixty crashed in a residential area near Cresthaven, Florida, around twelve fifty p m local time, with nine people on board. It said the N T S B would be in charge of the investigation, and would provide all updates.", 1.0, 1.0, ("card", "parties")),

 # ---- airplane / flight
 ("a1", "The airplane was a Learjet sixty: a midsize business jet, with two engines mounted at the back of the fuselage, and a T-tail. The horizontal tail sits on top of the vertical fin.", 0.4, 1.02, ("clip", "dv/987371.mp4", 0.5, C21)),
 ("a2", "The footage you are seeing is not the accident airplane. It is a C-21, the Air Force version of an older Learjet, the thirty-five. The layout is similar: rear engines, and a T-tail.", 0.4, 1.0, ("clip", "dv/987371.mp4", 24.0, C21)),
 ("a3", "The N T S B identifies the operator as Aurora Aviation, doing business as Upper Jet. According to Member Chapman, the flight was operating under Part one thirty-five of the federal aviation regulations: the rules for charter flights.", 0.4, 1.0, ("card", "airframe")),
 ("a4", "News reports identified the airplane's registration as November seven two two Bravo Delta. The F A A's registry lists that registration as a Learjet sixty. The N T S B has not published the registration on its investigation page.", 0.5, 1.0, ("card", "airframe")),
 ("a5", "On board were two pilots and seven passengers. We will not name anyone who was on the airplane.", 1.0, 0.97, ("clip", "dv/987371.mp4", 64.0, C21)),

 ("f1", "The flight departed Austin-Bergstrom International Airport in Texas at about ten thirty-seven in the morning, eastern time.", 0.4, 1.0, ("card", "route")),
 ("f2", "Its destination was North Eleuthera, an island airport in the Bahamas.", 0.4, 1.0, ("card", "route")),
 ("f3", "One detail about time: daylight saving time ended early that Sunday morning. So every time in this video is eastern standard time.", 0.6, 1.0, ("card", "route")),
 ("f4", "The N T S B has not published the flight's route or its altitudes before twelve forty-seven. Flight-tracking sites show more, but that data is not part of the official record yet.", 1.0, 1.0, ("clip", "dv/987371.mp4", 120.0, C21)),

 # ---- the radio calls
 ("t1", "By twelve forty-seven, the Learjet was at thirty-five thousand feet, talking to the Miami Air Route Traffic Control Center. That is the facility that handles high-altitude traffic over South Florida.", 0.4, 1.0, ("clip", "dv/916539.mp4", 12.0, RAD)),
 ("t2", "According to Member Chapman, at about twelve forty-seven the crew reported light clear ice, which they described as manageable.", 0.4, 1.0, ("card", "calls")),
 ("t3", "They reported moderate turbulence, causing altitude deviations of about seven hundred feet.", 0.4, 1.0, ("card", "calls")),
 ("t4", "They reported an outside air temperature of minus forty-seven degrees Celsius. And they reported precipitation.", 0.4, 1.0, ("card", "calls")),
 ("t5", "Then the crew asked to climb to thirty-seven thousand feet. Air traffic control approved it.", 0.6, 1.0, ("card", "calls")),
 ("t6", "In Chapman's words: less than thirty seconds later, a transmission from the airplane announced the descent, followed by a mayday call.", 0.5, 0.97, ("card", "calls")),
 ("t7", "At about twelve forty-eight, a transmission said, in part: we are in an overspeed condition, descending. The rest of that call was unintelligible.", 0.5, 0.96, ("card", "calls")),
 ("t8", "According to the N T S B, later transmissions described a rapid descent, and gave altitude callouts. The impact was at about twelve fifty-one.", 1.2, 0.96, ("card", "calls")),
 ("t9", "That is roughly four minutes, from the report of ice and turbulence at about twelve forty-seven, to the impact. The N T S B has not published the airplane's altitude, speed or flight path during the descent.", 1.2, 0.98, ("clip", "dv/916535.mp4", 36.0, RAD)),

 # ---- explainers: ice, turbulence, overspeed
 ("e1", "Let's slow down and look at those words, because each one has a specific meaning in aviation.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 80.0, WX)),
 ("e2", "First, ice. Clear ice, as the F A A's Aeronautical Information Manual describes it, is a glossy, clear, or translucent ice, formed by the relatively slow freezing of large supercooled water droplets.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 80.0, WX)),
 ("e3", "Light icing, in the F A A's reporting terms, means ice is building up at a rate that requires occasional cycling of the de-icing systems. The F A A's reference rate is about a quarter of an inch to one inch per hour on unprotected parts of the wing, and its guidance says the pilot should consider leaving the icing conditions.", 0.4, 1.0, ("card", "terms")),
 ("e4", "The crew called the ice manageable. The N T S B has not said whether ice played any role.", 0.8, 0.98, ("card", "terms")),
 ("e5", "Second, moderate turbulence. In the F A A's definitions, moderate turbulence causes changes in altitude or attitude, but the airplane remains in positive control at all times. People on board feel definite strain against their seat belts.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 200.0, WX)),
 ("e6", "For context: between twenty-nine thousand and forty-one thousand feet, air traffic control can separate airplanes vertically by as little as one thousand feet.", 0.4, 1.0, ("card", "terms")),
 ("e7", "Member Chapman said the reported turbulence will be examined closely by investigators. That is not a finding of cause.", 0.8, 1.0, ("card", "terms")),
 ("e8", "Third, overspeed. Every jet has a maximum operating speed, and at high altitude a maximum operating Mach number: a limit expressed as a fraction of the speed of sound.", 0.4, 1.0, ("3d", "overspeed")),
 ("e9", "Go past that limit, and the airplane's overspeed warning sounds. The limit exists to protect the structure and the airplane's handling.", 0.4, 1.0, ("3d", "overspeed")),
 ("e10", "When the crew said they were in an overspeed condition, they were telling the controller that the airplane was above its maximum operating speed. The N T S B has not said how fast it was going, or why.", 1.2, 0.98, ("3d", "overspeed")),

 # ---- the weather
 ("w1", "Now, the weather. Member Chapman called the weather a major focus of the investigation.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 460.0, WX)),
 ("w2", "At the second briefing, investigators said they could not yet say whether the airplane flew through an active thunderstorm. The conditions at its cruise altitude had not been determined.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 460.0, WX)),
 ("w3", "Thunderstorms matter to pilots for more than rain. In and around them, there can be strong up and down drafts, turbulence and icing. The F A A notes that these often extend far beyond the visible storm cloud.", 0.4, 1.0, ("clip", "dv/986834.mp4", 6.0, TOPS)),
 ("w4", "The F A A's guidance to pilots says: never regard any thunderstorm lightly, even when radar echoes are of light intensity. And it says to avoid by at least twenty miles any thunderstorm identified as severe, or giving an intense radar echo.", 0.4, 1.0, ("clip", "dv/986834.mp4", 6.0, TOPS)),
 ("w5", "The airplane had weather radar. In the F A A's words, weather radar normally shows areas of moderate to heavy precipitation, and radar does not detect turbulence.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 780.0, WXR)),
 ("w6", "According to the Associated Press, investigators will try to determine whether the crew knew about the storm cell, what the airplane's weather radar showed, and whether the pilots checked any other weather services.", 0.4, 1.0, ("clip", "dv/1022425.mp4", 880.0, WXR)),
 ("w7", "Those questions are open. The N T S B has not said what the crew saw on their radar, or whether they were inside a storm cell when the emergency began.", 1.2, 0.98, ("clip", "dv/906065.mp4", 60.0, FCST)),

 # ---- the ground
 ("g1", "The airplane came down near South Military Trail, between Cresthaven Boulevard and Tenth Avenue North, in the Greenacres area of Palm Beach County.", 0.4, 1.0, ("3d", "site_wide")),
 ("g2", "The main wreckage was in an impact crater, in the roadway, and the crater filled with water. The investigator in charge said the biggest obstacle would be recovering the major wreckage from that crater.", 0.4, 1.0, ("3d", "site_wide")),
 ("g3", "The debris field was about half a mile by four tenths of a mile, across ball fields, businesses and homes. Debris was also found on the roofs of nearby buildings.", 0.4, 1.0, ("3d", "site_field")),
 ("g4", "On the ground, one man in a vehicle leaving the area next to the site suffered a leg injury, according to the N T S B. Palm Beach County officials said hundreds of residents of the mobile home community had to leave their homes.", 0.5, 1.0, ("3d", "site_field")),
 ("g5", "The N T S B later listed the areas it had cleared: the Green Acres Mobile Home Community, a truck business, a shopping plaza, a self-storage site, and John I. Leonard High School.", 1.0, 1.0, ("3d", "site_field")),

 # ---- breakup / elevator
 ("b1", "At the first briefing, Member Chapman described early evidence about what happened to the airplane before it reached the ground.", 0.4, 1.0, ("card", "quote")),
 ("b2", "Quote: We do have some evidence that there was some breakup of the aircraft before impact.", 0.9, 0.95, ("card", "quote")),
 ("b3", "The next day, the N T S B said most of the airplane's left elevator had been found, in three pieces, about one point three to three point eight miles from the crash site.", 0.4, 1.0, ("3d", "site_rings")),
 ("b4", "The N T S B has not published where exactly those pieces were found, only the distances. So on this map, the rings show distance only, not direction.", 0.6, 1.0, ("3d", "site_rings")),
 ("b5", "What is an elevator? On a T-tail jet like this one, the elevators are the movable surfaces at the back of the horizontal tail, high on top of the fin. They control the airplane's pitch: nose up, and nose down.", 0.4, 1.0, ("3d", "tail")),
 ("b6", "In Chapman's words: the function of the elevator is to control the pitch, up and down. And knowing that it was lost is a very important piece of evidence, in terms of pointing us towards other things to investigate.", 0.4, 1.0, ("3d", "tail")),
 ("b7", "He also said at least some important pieces of the aircraft separated before impact.", 0.6, 1.0, ("3d", "tail")),
 ("b8", "Here is what the N T S B has not said. It has not said whether the elevator separated at the start of the emergency, or as a result of the forces during the descent. That is one of the central questions.", 1.2, 0.97, ("clip", "dv/1022425.mp4", 520.0, WX)),

 # ---- recovery
 ("x1", "The recovery work at the site lasted more than a week.", 0.4, 1.0, ("card", "recovery")),
 ("x2", "On November fourth, excavation began at the crash site. The next day, the N T S B said it had found a portion of one engine.", 0.4, 1.0, ("card", "recovery")),
 ("x3", "By November eighth, investigators had recovered and identified components from both wings, both engines, the flight deck, the vertical stabilizer, the horizontal stabilizer, the left elevator, aileron sections, and multiple flap track assemblies.", 0.4, 1.0, ("card", "recovery")),
 ("x4", "Some of those parts were sent to the N T S B's laboratories in Washington, D C, for closer inspection. The N T S B said all recovered wreckage will go to a secure location for further examination.", 0.4, 1.0, ("card", "recovery")),
 ("x5", "The N T S B also asked the public for help. Anyone who found debris was asked not to keep it, move it, or throw it away, and to email the N T S B instead. Even small pieces, the agency said, may contain important evidence.", 1.0, 1.0, ("card", "recovery")),

 # ---- recorders
 ("c1", "Then, on November ninth, the N T S B announced that it had recovered the cockpit voice recorder.", 0.4, 1.0, ("card", "cvr")),
 ("c2", "It was found at the site of the initial impact, after the excavation there was completed. It went to the N T S B's Vehicle Recorders Laboratory in Washington for evaluation.", 0.4, 1.0, ("card", "cvr")),
 ("c3", "Earlier, Member Chapman had said maintenance records indicated a recorder was installed, but investigators did not yet know whether it was on board.", 0.4, 1.0, ("card", "cvr")),
 ("c4", "A cockpit voice recorder captures the pilots' voices, radio calls, and sounds in the cockpit, such as warnings and alerts. Investigators typically turn it into a written transcript, and the audio itself is not released to the public.", 0.4, 1.0, ("clip", "dv/987371.mp4", 68.0, C21)),
 ("c5", "As of this video, the N T S B has not said what is on the recording, or how much of it is usable. It has also not said whether this airplane carried a flight data recorder.", 1.2, 0.98, ("card", "cvr")),

 # ---- other statements
 ("s1", "Two more things the N T S B said on scene.", 0.4, 1.0, ("card", "briefing")),
 ("s2", "First, news reports noted that the crash site is less than ten miles from Mar-a-Lago, and the question came up at a briefing. Chapman's answer: there is no evidence of a connection. Purely coincidence.", 0.4, 1.0, ("card", "briefing")),
 ("s3", "Second, Chapman said the N T S B was not aware of prior accidents of this type involving the Learjet sixty, but that investigators will look at trends.", 0.4, 1.0, ("card", "briefing")),
 ("s4", "He also said the N T S B does not determine probable cause on scene, and he declined to speculate about the cause, or about the actions of the crew.", 1.0, 1.0, ("card", "briefing")),
 ("s5", "Member Chapman also said investigators had received dashcam footage and multiple eyewitness accounts. And investigators said they will examine what the crew and the controllers knew, when they knew it, and what actions they took.", 1.0, 1.0, ("clip", "dv/916535.mp4", 36.0, RAD)),

 # ---- open questions
 # ---- recap
 ("k1", "Let's put the timeline the N T S B has described in one place.", 0.4, 1.0, ("card", "calls")),
 ("k2", "About ten thirty-seven: departure from Austin. About twelve forty-seven: at thirty-five thousand feet, the crew reports light clear ice, moderate turbulence with altitude deviations of about seven hundred feet, and precipitation, and asks to climb to thirty-seven thousand feet.", 0.4, 1.0, ("card", "calls")),
 ("k3", "Less than thirty seconds later, a transmission announces the descent, then a mayday. At about twelve forty-eight, a transmission says the airplane is in an overspeed condition, descending. About twelve fifty-one, the impact.", 0.4, 1.0, ("card", "calls")),
 ("k4", "On the ground: a debris field of about half a mile by four tenths of a mile, and pieces of the left elevator found one point three to three point eight miles away.", 0.6, 1.0, ("3d", "site_rings")),
 ("k5", "Everything beyond that, for now, is a question.", 1.0, 0.97, ("3d", "site_rings")),
 ("q1", "So, here is where the facts end, and the questions begin.", 0.5, 0.98, ("card", "open")),
 ("q2", "What weather was the airplane in, at thirty-five thousand feet, at twelve forty-seven?", 0.5, 1.0, ("card", "open")),
 ("q3", "What happened in the seconds after the climb to thirty-seven thousand feet was approved?", 0.5, 1.0, ("card", "open")),
 ("q4", "Why was the airplane in an overspeed condition?", 0.5, 1.0, ("card", "open")),
 ("q5", "When, and why, did the left elevator separate?", 0.5, 1.0, ("card", "open")),
 ("q6", "And did ice play any role?", 0.5, 1.0, ("card", "open")),
 ("q7", "Each of these is a question, not an answer. The cockpit voice recorder, the wreckage, radar data and weather records should help the N T S B answer them.", 1.2, 0.98, ("card", "open")),

 # ---- what's next
 ("n1", "What happens next? The N T S B typically publishes a preliminary report within about thirty days of an accident. It will lay out facts, without analysis, and without a cause.", 0.4, 1.0, ("clip", "dv/986834.mp4", 60.0, TOPS)),
 ("n2", "The final report, with the probable cause, typically comes twelve to twenty-four months after the accident.", 0.4, 1.0, ("card", "status")),
 ("n3", "When the preliminary report comes out, we will go through it here, line by line, and update what you have seen in this video.", 0.5, 1.0, ("card", "status")),
 ("n4", "Nine people lost their lives on this flight. The goal of the investigation is to understand what happened, so that it does not happen again.", 0.6, 0.95, ("card", "status")),
 ("n5", "This is Last Contact. Every crash leaves a record.", 1.5, 0.95, ("card", "status")),
]
