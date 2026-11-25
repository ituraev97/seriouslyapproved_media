# EPISODE 008 — Southwest Airlines flight 1380, Boeing 737-7H4 N772SW, left engine failure (fan blade No. 13 fracture),
# loss of engine inlet and fan cowl parts, cabin window departure and rapid depressurization, emergency landing at
# Philadelphia, April 17, 2018. Sources: NTSB Aircraft Accident Report NTSB/AAR-19/03 (adopted Nov. 19, 2019): executive
# summary, 1.1-1.10, 2, 3.1 findings, 3.2 probable cause, 4 recommendations, appendix A/B; NTSB docket DCA18MA142
# (FDR Attachment 1 CSV: latitude/longitude/altitude/airspeed at 1 Hz).
# (id, spoken text, pause_after, speed, visual)
BM = "NTSB BOARD MEETING · NOV. 19, 2019"
NDI = "FILE FOOTAGE · U.S. AIR FORCE NONDESTRUCTIVE INSPECTION SHOP (437TH MXS) · NOT THE ACCIDENT ENGINE · DVIDS"
ARFF = "FILE FOOTAGE · U.S. AIR FORCE AIRFIELD FIREFIGHTERS IN TRAINING · NOT PHILADELPHIA · DVIDS"
F1 = "NTSB AAR-19/03 · FIG. 1 · LOCATIONS OF ENGINE, INLET AND FAN COWL"
F2 = "NTSB AAR-19/03 · FIG. 2 · FAN ASSEMBLY"
F3 = "NTSB AAR-19/03 · FIG. 3 · CROSS-SECTION OF ENGINE AND AIRFRAME COMPONENTS"
F5 = "NTSB AAR-19/03 · FIG. 5 · LEFT ENGINE FAN COWL"
F6 = "NTSB AAR-19/03 · FIG. 6 · LOWER AFT CORNER OF INBOARD FAN COWL ALIGNED WITH WITNESS MARKS ON FUSELAGE"
F7 = "NTSB AAR-19/03 · FIG. 7 · FATIGUE INDICATIONS ON THE FAN BLADE FRACTURE SURFACE"
F10 = "NTSB AAR-19/03 · FIG. 10 · RADIAL RESTRAINT BRACKET DAMAGE"
F12 = "NTSB AAR-19/03 · FIG. 12 · FAN BLADE FRAGMENT EXIT TRAJECTORIES · REPLICA FRAGMENTS FROM TESTS, NOT ACCIDENT PARTS"
F13 = "NTSB AAR-19/03 · FIG. 13 · PREDICTED INLET FAILURE SEQUENCE"
F14 = "NTSB AAR-19/03 · FIG. 14 · PREDICTED FAN COWL FAILURE SEQUENCE"
F15 = "NTSB AAR-19/03 · FIG. 15 · WINDOW BY SEAT 14A AFTER THE ACCIDENT AND WINDOW DIMENSIONS"
F16 = "NTSB AAR-19/03 · FIG. 16 · CRACK ARREST LINES AND RATCHET MARKS IN THE FATIGUE ORIGIN AREA"
F21 = "NTSB AAR-19/03 · FIG. 21 · LOCATION OF THE RADIAL RESTRAINT FITTING ON THE FAN COWL"
LINES = [
 # ---- cold open
 ("o1", "April seventeenth, two thousand eighteen. Eleven oh three in the morning, thirty-two thousand feet over eastern Pennsylvania.", 1.1, 1.0, ("3d", "open")),
 ("o2", "Southwest Airlines flight thirteen eighty, a Boeing seven thirty-seven, is climbing out of New York, bound for Dallas. One hundred forty-nine people on board.", 1.1, 1.0, ("3d", "open")),
 ("o3", "At eleven oh three and thirty-three seconds, the left engine fails. A fan blade has broken off at its root. Pieces of the engine's cover tear away, and one of them strikes the fuselage beside a cabin window.", 1.1, 1.0, ("3d", "fbo")),
 ("o4", "The airplane begins an uncommanded roll to the left, to forty-one degrees. The window is gone, and the cabin loses its pressure.", 3.1, 0.98, ("3d", "fbo")),
 ("o5", "Seventeen minutes later, the airplane lands safely in Philadelphia. One passenger died. Eight others had minor injuries.", 1.2, 1.0, ("card", "toll")),
 ("o6", "In this video: what the N T S B found, second by second. Why one blade broke. And why the engine cover came apart.", 1.9, 1.0, ("card", "toll")),
 ("t1", "Last contact. Southwest flight thirteen eighty.", 2.1, 0.95, ("card", "title")),
 # ---- how we know
 ("h1", "Everything here comes from the N T S B final report, number A A R nineteen, oh three, adopted on November nineteenth, two thousand nineteen, and from the investigation's public docket.", 1.1, 1.0, ("card", "how")),
 ("h2", "Times are eastern daylight time. The track comes from the flight data recorder: latitude, longitude, altitude and speed.", 1.1, 1.0, ("card", "how")),
 ("h3", "The three D scenes are built on those numbers, over today's aerial imagery. Motion in between is interpolated. The model is generic, shown without airline markings.", 1.7, 1.0, ("3d", "top")),
 # ---- the airplane and the crew
 ("a1", "The airplane was a Boeing seven thirty-seven, seven H four, registration N seven seven two S W, delivered new to Southwest in July, two thousand.", 1.1, 1.0, ("card", "plane")),
 ("a2", "It had two C F M fifty-six, seven B engines. The left engine was last overhauled in November, two thousand twelve. Since then, it had flown eighteen thousand eighty-eight hours, in ten thousand seven hundred twelve flights.", 1.1, 1.0, ("photo", "ph/fig3.png", F3)),
 ("p1", "Both pilots were experienced. The captain had about ten thousand five hundred hours in the seven thirty-seven, and had flown for the U.S. Navy. The first officer had almost seven thousand, and had flown for the Air Force.", 1.1, 1.0, ("card", "crew")),
 ("p2", "It was the second day of a four-day trip. On this leg, the first officer was the pilot flying, and the captain was the pilot monitoring. The N T S B found that neither crew qualifications nor medical conditions were factors.", 1.5, 1.0, ("card", "crew")),
 # ---- takeoff and climb
 ("w1", "The airplane took off from LaGuardia at ten forty-three. The takeoff and the climb were uneventful.", 1.1, 1.0, ("3d", "climb")),
 ("w2", "At ten fifty-seven, New York Center cleared them to climb to flight level three eight zero, thirty-eight thousand feet. They did not reach it.", 1.5, 1.0, ("3d", "climb")),
 # ---- the failure
 ("f1", "Eleven oh three and thirty-three seconds. Thirty-two thousand six hundred forty-eight feet. The cockpit voice recorder picks up increased background noise.", 1.0, 1.0, ("3d", "fbo")),
 ("f2", "The recorder shows the left engine's fan speed falling from ninety-nine and a half percent to sixty-one and a half, and its vibration climbing. The crew later described a loud bang, and significant vibration.", 1.1, 1.0, ("3d", "fbo")),
 ("f3", "At the same moment, the airplane begins to roll to the left, on its own. At eleven oh three forty-four, the bank reaches forty-one degrees. The first officer rolls it back, and within about six seconds the airplane is nearly level again.", 1.1, 1.0, ("3d", "fbo")),
 ("f4", "The cabin altitude warning horn sounds about six seconds after the failure. The cabin has lost its pressure. The N T S B found that the window at row fourteen had departed the airplane.", 3.3, 1.0, ("3d", "fbo2")),
 # ---- emergency descent
 ("e1", "At eleven oh three fifty-eight, both engines are brought to idle. The emergency descent begins. Eleven seconds later, the left engine's fuel is cut off, and it windmills for the rest of the flight.", 1.1, 1.0, ("3d", "desc")),
 ("e2", "On the cockpit recording, the next two minutes are mostly unintelligible. At eleven oh four forty-nine, the sound of oxygen masks. The controller: Southwest thirteen eighty, if you're trying to get me, all I hear is static.", 1.1, 1.0, ("card", "cvr1")),
 ("e4", "At eleven oh four fifty-four, the captain: Southwest thirteen eighty has an engine fire, descending. Then: we're single engine, descending, have fire in number one.", 1.1, 0.98, ("card", "cvr1")),
 ("e5", "The airplane is now descending at more than five thousand feet a minute, a peak of five thousand two hundred twenty-eight. The controller suggests Harrisburg. The captain: we're looking at Philly.", 1.1, 1.0, ("3d", "desc")),
 ("e6", "At eleven oh five fifty-two, the controller clears the flight direct to Philadelphia. Two and a half minutes after the failure.", 2.8, 1.0, ("3d", "top2")),
 # ---- why Philadelphia
 ("d1", "Why Philadelphia? When the engine failed, the airplane was twenty-nine nautical miles from Harrisburg, and fifty-seven from Philadelphia.", 1.1, 1.0, ("3d", "top2")),
 ("d2", "But Harrisburg had one runway and a firefighting index of B. Philadelphia had four runways, the longest twelve thousand feet, and the highest index, E. The N T S B found the decision to land in Philadelphia was appropriate.", 1.5, 1.0, ("3d", "top2")),
 # ---- the descent, the captain takes over
 ("c1", "At eleven oh nine thirty, thirteen thousand six hundred feet. The captain: tell you what, I'm gonna take it. She becomes the pilot flying. Southwest's manual says the captain must make the landing if an engine has been shut down.", 1.1, 1.0, ("3d", "desc2")),
 ("c2", "Then the captain slowed down. From two hundred seventy-two knots to two hundred thirty-two in forty seconds.", 1.1, 1.0, ("3d", "desc2")),
 ("c3", "Why? She told investigators she wanted to reduce the airframe vibration. The captain said she was slowing down on purpose. At eleven thirteen twenty-two, she had the controls again.", 1.1, 1.0, ("3d", "desc2")),
 # ---- the cabin
 ("k1", "At eleven fifteen oh four, a flight attendant reaches the first officer on the interphone. She says a window is completely out, and that they are helping an injured passenger.", 1.1, 1.0, ("card", "cvr2")),
 ("k2", "At eleven fifteen fifty-four, the captain changes her plan. She decides to expedite the approach. Let's get it turned in.", 1.1, 1.0, ("card", "cvr2")),
 ("k3", "She also decides to land with five degrees of flaps, because she did not know how controllable the airplane would be. The company's quick reference handbook had no guidance for a single-engine landing with that setting. She takes the speed for fifteen degrees of flaps, one hundred sixty knots, adds twenty, and aims for one hundred eighty.", 1.5, 1.0, ("card", "cvr2")),
 # ---- landing
 ("l1", "At eleven eighteen fifty-nine, the tower clears them to land on runway two seven left. The wind: two eight zero degrees at nineteen knots, gusting to twenty-five.", 1.1, 1.0, ("3d", "final")),
 ("l3", "Eleven twenty and thirty seconds. The approach speed is about one hundred eighty-five knots. For a normal two-engine approach in those conditions, it would have been one hundred forty-nine to one hundred fifty-two. The airplane touches down at about one hundred seventy-one knots, with reverse thrust on the right engine. It is seventeen minutes after the failure.", 1.7, 0.97, ("3d", "land")),
 ("l4", "The airplane leaves the runway by a high-speed taxiway, and stops near a fire truck. The rescue crews report no smoke or fire. Only one passenger needs immediate medical help.", 3.3, 1.0, ("clip", "dv/1012337.mp4", 25.0, ARFF)),
 # ---- the blade
 ("b1", "Now the question that matters most. What broke?", 1.0, 1.0, ("photo", "ph/fig2.png", F2)),
 ("b2", "The fan has twenty-four titanium blades, each weighing a little under eleven pounds.", 1.1, 1.0, ("photo", "ph/fig2.png", F2)),
 ("b3", "Blade number thirteen broke off at its root, just outside the dovetail, the part that slides into the fan disk. The dovetail itself stayed in its slot.", 1.1, 1.0, ("photo", "ph/fig7.png", F7)),
 ("b4", "Under the microscope, the fracture surface told the story. A smooth area, with six curved lines, the marks of a fatigue crack. A crack that grew by about one mark per flight, for about twenty thousand flights.", 1.1, 1.0, ("photo", "ph/fig16.png", F16)),
 ("b5", "The crack started in the dovetail, on the convex side, about point six inch behind the leading edge. It was almost half an inch deep when the blade let go.", 1.1, 1.0, ("photo", "ph/fig16.png", F16)),
 ("b6", "The N T S B found the crack began because the stresses in the dovetail, in normal operation, were higher than expected. And that it likely began before the blades' last overhaul, in October, two thousand twelve.", 1.5, 1.0, ("photo", "ph/fig2.png", F2)),
 # ---- inspections
 ("n1", "At that overhaul, the blades were inspected with a fluorescent penetrant inspection, which detects cracks at the surface. The crack on blade thirteen was not found, for reasons the N T S B could not determine.", 1.1, 1.0, ("clip", "dv/1019710.mp4", 16.0, NDI)),
 ("n2", "The N T S B concluded this crack was most likely not detectable by that test, or by the visual checks done every time the blade roots were relubricated. The blades were not a life-limited part.", 1.1, 1.0, ("clip", "relay/bm04.mp4", 0.0, BM)),
 ("n3", "On August twenty-seventh, two thousand sixteen, another Southwest seven thirty-seven lost a fan blade near Pascagoula, Mississippi, and landed safely in Pensacola. Nobody was hurt.", 1.1, 1.0, ("card", "pns")),
 ("n4", "After that, the engine maker developed two new inspections: an eddy current test at overhaul, and an ultrasonic test of the blade roots, with the blades still on the engine. Eddy current became required at overhaul in November two thousand sixteen.", 1.1, 1.0, ("clip", "relay/bm04.mp4", 14.0, BM)),
 ("n5", "In March, two thousand seventeen, a service bulletin recommended a one-time ultrasonic test of high-time blades. As revised in June, it applied above fifteen thousand flights since the last shop visit. The accident engine had eight thousand four hundred eighty-three, so it was not covered.", 1.1, 1.0, ("card", "sb")),
 ("n6", "In August, two thousand seventeen, the F A A proposed a rule to require the test. The N T S B noted that it would have applied to this engine. The agency was still working on the final rule at the time of the accident.", 1.1, 1.0, ("card", "sb")),
 ("n7", "Three days after the accident, the engine maker issued a new bulletin recommending ultrasonic inspections, and the F A A issued an emergency directive requiring them within twenty days, for engines with thirty thousand flights or more.", 1.1, 1.0, ("card", "sb")),
 # ---- the cover
 ("m1", "Boeing's design intent was that a blade failure would not cause the inlet or the fan cowl to come apart.", 1.0, 1.0, ("photo", "ph/fig1.png", F1)),
 ("m2", "The fan case held, and no blade material passed through it. The inlet and the fan cowl, parts of the nacelle, are what came apart.", 1.1, 1.0, ("photo", "ph/fig1.png", F1)),
 ("m3", "The blade hit the fan case at the six o'clock position, at the very bottom of the engine. Fragments flew forward, at a larger angle than in the certification tests, and into the engine inlet. The inlet came apart.", 1.1, 1.0, ("photo", "ph/fig12.png", F12)),
 ("m4", "The impact also sent a heavy load into the fan cowl, the engine's outer cover, through a fitting at the bottom called the radial restraint. Cracks ran along the cowl, and it tore apart at its three latches.", 1.1, 1.0, ("clip", "relay/bm02.mp4", 20.0, BM)),
 ("m5", "One piece that came off was the aft latch keeper, part of the cowl's own latch. It struck the fuselage just below the window at row fourteen.", 1.1, 1.0, ("clip", "relay/bm02.mp4", 38.0, BM)),
 ("m6", "That window is about ten and a half inches wide and a little over fourteen inches tall. The N T S B found it was the first known complete passenger window loss on the Boeing seven thirty-seven fleet.", 1.1, 1.0, ("photo", "ph/fig15.png", F15)),
 ("m7", "The regulation covering the window's outer pane did not require it to withstand impact. The N T S B found the impact of the latch keeper caused the window to depart, and the cabin to depressurize rapidly.", 1.5, 1.0, ("photo", "ph/fig15.png", F15)),
 # ---- certification
 ("q1", "Were these parts tested for a blade failure? The engine was, in tests that ended in December, nineteen ninety-six. The cowl was not on the engine in those tests. Boeing analyzed it instead, and the airplane was certificated in December, nineteen ninety-seven.", 1.1, 1.0, ("card", "cert")),
 ("q2", "In the engine's certification test, the blade was released at the twelve o'clock position, the top. Boeing's analyses after the accident found that the fan cowl is more sensitive to an impact near the bottom of the engine, close to the radial restraint fitting.", 1.1, 1.0, ("card", "cert")),
 ("q3", "The certification analysis assumed that fitting would fail completely and carry no load to the cowl. The stresses in the cowl were higher than calculated. The board found that, given those results, what happened could not have been predicted.", 1.5, 1.0, ("card", "cert")),
 # ---- the crew's actions
 ("r1", "What about the pilots? The N T S B looked at the checklists. The crew performed most, but not all, of the items on the engine fire or severe damage checklist, and did not start three other checklists the company required.", 1.1, 1.0, ("card", "chk")),
 ("r2", "The board's finding: given the emergency, the crew's performance of most checklist items, and not all, allowed it to appropriately balance procedure with a high workload. Its finding on the diversion: the decision to land in Philadelphia was appropriate.", 1.1, 1.0, ("card", "chk")),
 ("r3", "One more finding. Although it was not a factor in the outcome, the flight attendants should have been secured in their jump seats, in case an evacuation after landing had been needed.", 1.5, 1.0, ("card", "chk")),
 # ---- probable cause
 ("s1", "In November, two thousand nineteen, the board adopted its report. The probable cause, in the N T S B's words:", 1.0, 1.0, ("clip", "relay/bm00.mp4", 5.0, BM)),
 ("s2", "a low-cycle fatigue crack in the dovetail of fan blade number thirteen, which resulted in the fan blade separating in flight and impacting the engine fan case at a location that was critical to the structural integrity and performance of the fan cowl structure.", 1.2, 0.97, ("card", "cause")),
 ("s3", "This impact led to the in-flight separation of fan cowl components, including the inboard fan cowl aft latch keeper, which struck the fuselage near a cabin window and caused the window to depart from the airplane, the cabin to rapidly depressurize, and the passenger fatality.", 3.8, 0.97, ("card", "cause")),
 # ---- recommendations
 ("u1", "The N T S B made seven safety recommendations.", 1.0, 1.0, ("card", "recs")),
 ("u2", "To the F A A: require Boeing to find the critical blade impact locations on this engine, redesign the fan cowl on all seven thirty-seven next generation airplanes, install it on new airplanes, and retrofit the existing ones.", 1.1, 1.0, ("card", "recs")),
 ("u3", "Require engine and airplane makers to analyze every critical blade impact location together, and to account for the results in the design. The European regulator got the same recommendation.", 1.1, 1.0, ("card", "recs")),
 ("u4", "And two more. To the F A A: guidance on helping passengers affected by a loss of seating capacity. To Southwest: training for flight attendants on staying secured in a jump seat during emergency landings.", 1.5, 1.0, ("card", "recs")),
 # ---- replay
 ("z1", "Once more. Thirty-two thousand six hundred forty-eight feet. Blade thirteen. The left engine. The window. Forty-one degrees of bank.", 1.1, 0.95, ("3d", "replay")),
 ("z3", "Seventeen minutes.", 1.9, 0.95, ("3d", "replay")),
 # ---- close
 ("x1", "The N T S B found that this accident demonstrated the fan cowl's susceptibility to a blade impact near the radial restraint fitting. That the crack was most likely not detectable by the inspections of the time. And that the loads that reached the cowl had not been accounted for in its design.", 1.2, 1.0, ("clip", "relay/bm00.mp4", 40.0, BM)),
 ("x2", "One passenger died. The airplane landed safely in Philadelphia, seventeen minutes later.", 3.1, 1.0, ("3d", "orbit")),
 ("x3", "This was LAST CONTACT. Every crash leaves a record. Next file soon.", 20.0, 0.97, ("card", "status")),
]
