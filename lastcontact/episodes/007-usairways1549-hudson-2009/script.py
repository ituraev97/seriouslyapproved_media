# EPISODE 007 — US Airways flight 1549, Airbus A320-214 N106US, loss of thrust in both engines after a bird strike,
# ditching on the Hudson River, January 15, 2009, ~15:30 EST (Weehawken, NJ / New York City).
# Sources: NTSB Aircraft Accident Report NTSB/AAR-10/03 (adopted May 4, 2010): exec summary, 1.1, 1.2, 1.5, 1.6, 1.7,
# 1.12, 1.15, 1.16, 3.1 findings, 3.2 probable cause, 4 recommendations; NTSB docket DCA09MA026: Aircraft Performance
# Group Chairman's Factual Report (radar track, table 1a/2, touchdown parameters), Structures 7C, Powerplants 8A,
# Survival Factors 6E photos, BEA video analysis.
# (id, spoken text, pause_after, speed, visual)
BASH = "FILE FOOTAGE · U.S. AIR FORCE BIRD AIR STRIKE HAZARD TEAM, RAF LAKENHEATH · NOT LGA · DVIDS"
USDA = "FILE FOOTAGE · USDA WILDLIFE SERVICES AT A MILITARY AIRFIELD (BAGRAM, 2016) · NOT LGA · DVIDS"
FEATH = "FILE FOOTAGE · BIRD-STRIKE REMAINS SAMPLED FOR THE SMITHSONIAN FEATHER LAB · U.S. AIR FORCE · NOT FLIGHT 1549 · DVIDS"
RAPCON = "FILE FOOTAGE · U.S. AIR FORCE RADAR APPROACH CONTROL, RAF LAKENHEATH · NOT NEW YORK TRACON · DVIDS"
ICE = "FILE FOOTAGE · U.S. COAST GUARD ICEBREAKING, LOWER HUDSON / NEW YORK HARBOR, JAN. 2026 · NOT 2009 · DVIDS"
CGNY = "FILE FOOTAGE · U.S. COAST GUARD STATION NEW YORK, NEW YORK HARBOR (2020) · NOT THE 2009 RESCUE · DVIDS"
FERRY = "FILE FOOTAGE · NEW YORK HARBOR, FLEET WEEK 2025 · NOT THE 2009 RESCUE · DVIDS"
VEST = "FILE FOOTAGE · U.S. AIR FORCE LIFE PRESERVERS, AIRCREW FLIGHT EQUIPMENT · NOT AN AIRLINE VEST · DVIDS"
DUNK = "FILE FOOTAGE · U.S. ARMY AVIATORS, UNDERWATER ESCAPE / WATER SURVIVAL TRAINING, GDYNIA, POLAND · DVIDS"
F1 = "NTSB AAR-10/03 · FIG. 1 · FLIGHT TRACK OF US AIRWAYS FLIGHT 1549"
F2 = "NTSB AAR-10/03 · FIG. 2 · OCCUPANTS ON THE WINGS AND IN THE SLIDE/RAFTS"
F3 = "NTSB AAR-10/03 · FIG. 3 · A320 AIRSPEED SCALE AND PROTECTION SPEEDS"
F4 = "NTSB AAR-10/03 · FIG. 4 · CUTAWAY OF A TURBOFAN ENGINE"
F5 = "NTSB AAR-10/03 · FIG. 5 · THE TWO AIRFLOW PATHS: FAN (BYPASS) AND CORE"
F9 = "NTSB AAR-10/03 · FIG. 9 · EXITS USED BY THE OCCUPANTS"
F10 = "NTSB AAR-10/03 · FIG. 10 · CANADA GOOSE POPULATION, 1970–2008"
LENG = "NTSB DOCKET DCA09MA026 · POWERPLANTS · LEFT ENGINE RECOVERED FROM THE HUDSON (NTSB)"
INLET = "NTSB DOCKET DCA09MA026 · POWERPLANTS · ENGINE INLET DAMAGE (NTSB)"
RENG = "NTSB DOCKET DCA09MA026 · POWERPLANTS · RIGHT ENGINE, STILL ATTACHED (NTSB)"
TEAR = "NTSB DOCKET DCA09MA026 · POWERPLANTS · ENGINE TEARDOWN (NTSB)"
LIFT = "NTSB DOCKET DCA09MA026 · STRUCTURES · AIRPLANE LIFTED FROM THE RIVER (NTSB)"
BELLY = "NTSB DOCKET DCA09MA026 · STRUCTURES · LOWER FUSELAGE DAMAGE (NTSB)"
AFT = "NTSB DOCKET DCA09MA026 · STRUCTURES · AFT FUSELAGE DAMAGE (NTSB)"
AFT2 = "NTSB DOCKET DCA09MA026 · STRUCTURES · AFT FUSELAGE AFTER RECOVERY (NTSB)"
CABIN = "NTSB DOCKET DCA09MA026 · SURVIVAL FACTORS · CABIN AFTER RECOVERY (NTSB)"
FLOOR = "NTSB DOCKET DCA09MA026 · SURVIVAL FACTORS · AFT CABIN FLOOR DAMAGE (NTSB)"
COCK = "NTSB DOCKET DCA09MA026 · SURVIVAL FACTORS · FLIGHT DECK AFTER RECOVERY (NTSB)"
BEA = "NTSB DOCKET DCA09MA026 · BEA VIDEO ANALYSIS · VIEW FROM THE PIER 88 CAMERA"
LINES = [
 # ---- cold open
 ("o1", "January fifteenth, two thousand nine. Three twenty-seven in the afternoon, just north of LaGuardia, New York.", 0.4, 1.0, ("3d", "open")),
 ("o2", "An Airbus A three twenty, US Airways flight fifteen forty-nine, is climbing out of LaGuardia, bound for Charlotte. One hundred fifty-five people on board.", 0.4, 1.0, ("3d", "open")),
 ("o3", "Two thousand eight hundred eighteen feet above the ground. The captain says one word: birds. One second later, thumps, and a shudder. Both engines lose almost all of their thrust.", 0.5, 0.98, ("3d", "strike")),
 ("o4", "There is no runway they can be sure of reaching. Three and a half minutes later, the airplane is on the Hudson River, between Manhattan and New Jersey.", 0.8, 0.98, ("3d", "strike")),
 ("o5", "Everyone on board survived. Five people were seriously injured, and ninety-five had minor injuries.", 0.5, 1.0, ("card", "toll")),
 ("o6", "In this video: what the N T S B found, second by second. Why the engines could not be brought back. And whether the airplane could have made it back to an airport.", 1.2, 1.0, ("card", "toll")),
 ("t1", "Last contact. Flight fifteen forty-nine. The Hudson River.", 1.4, 0.95, ("card", "title")),
 # ---- how we know
 ("h1", "Everything here comes from the N T S B accident report, number A A R ten, oh three, adopted on May fourth, two thousand ten, and from the investigation's public docket.", 0.4, 1.0, ("card", "how")),
 ("h2", "Both recorders were recovered and read out. Times are eastern standard time. The track comes from Newark radar data in the N T S B docket.", 0.4, 1.0, ("card", "how")),
 ("h3", "The three D scenes are built on those numbers, over today's aerial imagery. Motion in between is interpolated. The model is a generic A three twenty, shown without any airline markings.", 1.0, 1.0, ("3d", "top")),
 # ---- the airplane and the crew
 ("a1", "The airplane was an Airbus A three twenty, two fourteen, registration N one oh six U S. It was delivered new to US Airways in nineteen ninety-nine.", 0.4, 1.0, ("card", "plane")),
 ("a2", "It had two C F M fifty-six turbofan engines. On board, one hundred fifty passengers, including a child held on a lap, three flight attendants and two pilots.", 0.4, 1.0, ("photo", "ph/fig5.png", F5)),
 ("p1", "The captain was fifty-seven, with nineteen thousand six hundred sixty-three flight hours. He had flown F four fighters for the U.S. Air Force.", 0.3, 1.0, ("card", "crew")),
 ("p2", "The first officer was forty-nine, with fifteen thousand six hundred forty-three hours. But only thirty-seven of them were in the A three twenty. He had recently completed his training on the type, and on this leg, he was the pilot flying.", 0.4, 1.0, ("card", "crew")),
 ("p3", "It was the last day of a four-day trip, and the first trip the two had flown together.", 0.8, 1.0, ("card", "crew")),
 # ---- weather and takeoff
 ("w1", "The weather was cold, with good visibility. Ten miles, a light wind, minus six degrees Celsius in Central Park. The Hudson was about forty-one degrees Fahrenheit.", 0.4, 1.0, ("clip", "dv/994186.mp4", 20.5, ICE)),
 ("w2", "At three twenty-four and fifty-four seconds, LaGuardia tower cleared flight fifteen forty-nine for takeoff on runway four.", 0.4, 1.0, ("3d", "climb")),
 ("w3", "The takeoff and the first part of the climb were normal. The departure controller cleared them to fifteen thousand feet.", 0.4, 1.0, ("3d", "climb")),
 ("w4", "At three twenty-seven and five seconds, climbing through about two thousand five hundred feet, the flaps were retracted. The airplane was heading north, at about two hundred nineteen knots.", 0.8, 1.0, ("3d", "climb")),
 # ---- the strike
 ("b1", "Three twenty-seven and ten point four seconds. The captain: birds.", 0.3, 0.97, ("card", "cvr1")),
 ("b2", "At eleven point four, the cockpit voice recorder captures thumps and thuds, then a shuddering sound. In the same second, both engines start to run down. The left one from eighty-two to thirty-five percent fan speed. The right one, to fifteen percent.", 0.4, 0.98, ("card", "cvr1")),
 ("b3", "The first officer: uh oh. The captain: we got one rol, both of 'em rolling back.", 0.3, 0.98, ("card", "cvr1")),
 ("b4", "At three twenty-seven nineteen, the captain calls for engine ignition, and two seconds later, he starts the A P U, the small auxiliary power unit in the tail. At twenty-three seconds, he takes the controls: my aircraft.", 0.4, 1.0, ("card", "cvr1")),
 ("b5", "The N T S B found this early A P U start mattered. It kept primary electrical power on line, so the airplane stayed in normal law, with its flight envelope protections, including protection against a stall.", 0.8, 1.0, ("3d", "strike2")),
 # ---- the birds
 ("g1", "What hit them? Investigators collected feathers, tissue and bone from both engines, the left wing and the fuselage, and sent them to the Smithsonian Institution's Feather Identification Laboratory.", 0.4, 1.0, ("clip", "dv/617155.mp4", 24.5, FEATH)),
 ("g2", "The D N A matched Canada geese. Each engine had ingested at least two large birds, weighing about eight pounds each. One went into the core of each engine.", 0.4, 1.0, ("clip", "dv/617155.mp4", 36.5, FEATH)),
 ("g3", "A chemical analysis of the feathers showed something else. These were not the geese that live around New York all year. They matched migratory geese.", 0.4, 1.0, ("photo", "ph/fig10.png", F10)),
 ("g4", "The strike happened about four and a half miles from LaGuardia, at almost three thousand feet. That, the N T S B found, was beyond the range of the airport's wildlife hazard responsibilities, so the airport's wildlife management would not have mitigated it.", 0.8, 1.0, ("clip", "dv/782357.mp4", 20.5, BASH)),
 # ---- the turn
 ("r1", "The airplane keeps climbing for a few seconds on momentum. At three twenty-seven thirty, it peaks at about three thousand sixty feet, at one hundred eighty-five knots. Then it starts down.", 0.4, 1.0, ("3d", "turn")),
 ("r2", "At three twenty-seven thirty-three, the captain calls New York departure. Cactus fifteen thirty-nine, hit birds, we've lost thrust in both engines, we're turning back towards LaGuardia.", 0.3, 0.98, ("card", "cvr2")),
 ("r3", "Cactus fifteen forty-nine was the flight's radio call sign. He said fifteen thirty-nine; the flight number was fifteen forty-nine. And the words mayday, mayday, mayday never reached the controller. Another pilot was transmitting on the same frequency at the same moment.", 0.4, 1.0, ("clip", "dv/916539.mp4", 20.5, RAPCON)),
 ("r4", "The controller gives them a left turn to heading two two zero, back toward LaGuardia. At three twenty-eight and five seconds, he asks if they want to try runway one three.", 0.3, 1.0, ("card", "cvr2")),
 ("r5", "The captain: we're unable. We may end up in the Hudson.", 0.6, 0.97, ("card", "cvr2")),
 ("r6", "Runway three one? Unable. Runway four is available. The captain: I'm not sure we can make any runway. What's over to our right, anything in New Jersey, maybe Teterboro?", 0.4, 1.0, ("3d", "turn2")),
 ("r7", "Teterboro is off your right side, the controller says. At three twenty-nine and three seconds, the captain says yes, they want to try Teterboro.", 0.4, 1.0, ("3d", "turn2")),
 ("r8", "At three twenty-nine eleven, over the public address: this is the captain, brace for impact.", 0.4, 0.97, ("card", "cvr3")),
 ("r9", "At three twenty-nine twenty-one, the controller offers runway one at Teterboro. The captain: we can't do it. Then: we're gonna be in the Hudson. The airplane is descending through about seven hundred feet, near the west shore of the river.", 0.8, 0.98, ("card", "cvr3")),
 # ---- the checklist
 ("c1", "While the captain flew and talked to A T C, the first officer was working through the quick reference handbook. The engine dual failure checklist.", 0.4, 1.0, ("card", "qrh")),
 ("c2", "Its first steps assume a dual engine failure at high altitude, with time to work. One item is a target speed for a windmill relight: three hundred knots. The first officer read it out: three hundred knots, we don't have that. The highest speed the airplane reached after the strike was two hundred fourteen knots.", 0.4, 1.0, ("card", "qrh")),
 ("c3", "The first officer spent about thirty to forty seconds on the relight steps. The ditching part of the checklist came after them, and the crew never reached it.", 0.4, 1.0, ("card", "qrh")),
 ("c4", "The N T S B found the checklist did not fully apply, but it was the most applicable one the crew had. A checklist for a dual engine failure at low altitude, the board said, would more likely have been completed.", 0.8, 1.0, ("photo", "ph/fig3.png", F3)),
 # ---- why no restart
 ("e1", "Could the pilots have brought the engines back? No.", 0.3, 1.0, ("photo", "ph/fig4.png", F4)),
 ("e2", "The right engine was still on its wing. The left one had separated, and was found in the river eight days later, near the point where the airplane first touched the water.", 0.4, 1.0, ("photo", "ph/e8-001.png", LENG)),
 ("e3", "In both, the N T S B found bird remains in the core and mechanical damage that prevented the engine from producing enough thrust to sustain flight. No evidence of any engine, system or structural problem before the strike.", 0.4, 1.0, ("photo", "ph/e8-004.png", INLET)),
 ("e4", "The left engine kept turning at a reduced level. At three twenty-eight twenty-five, the captain said, the left one's coming back up a little bit. But neither engine could produce enough thrust to sustain flight.", 0.4, 1.0, ("photo", "ph/e8-008.png", RENG)),
 ("e5", "The engines' control system had no way to tell the pilots that thrust could not be restored. If it had, the N T S B said, they would not have spent valuable time trying to relight engines that were too damaged for any pilot action to make operational.", 0.8, 1.0, ("photo", "ph/e8-016.png", TEAR)),
 # ---- certification
 ("k1", "Were these engines tested for birds? Yes, under the rules of the time.", 0.3, 1.0, ("card", "cert")),
 ("k2", "To be certificated, this engine type had to pass two bird tests: a volley of seven medium birds, one and a half pounds each, two of them aimed at the core, and a single large bird of four pounds, fired into the fan, but not into the core.", 0.4, 1.0, ("card", "cert")),
 ("k3", "Flight fifteen forty-nine took in at least two birds of about eight pounds per engine, with one in each core. The N T S B found the size and number of the birds well exceeded the certification standards.", 0.8, 1.0, ("card", "cert")),
 # ---- could they have made an airport
 ("s1", "So, could they have made it back to LaGuardia?", 0.3, 1.0, ("card", "sim")),
 ("s2", "In April two thousand nine, the N T S B ran simulations at the Airbus training center in Toulouse. The pilots were briefed in advance, and turned for an airport immediately after the strike.", 0.4, 1.0, ("card", "sim")),
 ("s3", "Of fifteen valid runs with an immediate turn, eight landed successfully. Five of seven to LaGuardia runway one three. Two of six to runway two two. One of two to Teterboro.", 0.4, 1.0, ("card", "sim")),
 ("s4", "Then they added a thirty-five second delay, to account for recognizing what had happened and deciding what to do. One run, to runway one three. It did not make it.", 0.4, 1.0, ("card", "sim")),
 ("s5", "The N T S B noted the immediate turns did not reflect real world considerations. Its finding was that the captain's decision to ditch on the Hudson, rather than attempt an airport, provided the highest probability that the accident would be survivable.", 0.8, 1.0, ("photo", "ph/fig1.png", F1)),
 # ---- down the river
 ("d1", "Down the river. At three twenty-nine forty-five, the captain says, put the flaps out. The airplane is a few hundred feet above the Hudson, at about one hundred ninety knots, tracking south down the river.", 0.4, 1.0, ("3d", "river")),
 ("d2", "At three twenty-nine fifty-three, the controller tells them radar contact is lost. Radar needs a clear line of sight, and that low, buildings or other obstructions can block it. He keeps transmitting anyway, offering Newark.", 0.4, 1.0, ("3d", "river")),
 ("d4", "The ground proximity warning system sounds fifteen alerts in the last minute and a half. Too low, terrain. Pull up.", 0.4, 1.0, ("3d", "river2")),
 ("d5", "The first officer: two hundred fifty feet in the air. Hundred and seventy knots. Got no power on either one? Try the other one.", 0.3, 0.98, ("card", "cvr4")),
 ("d6", "Got flaps two, you want more? The captain: no, let's stay at two. Got any ideas? The first officer: actually not.", 0.4, 0.98, ("card", "cvr4")),
 # ---- touchdown
 ("x1", "Three thirty and thirty-eight seconds. The captain: we're gonna brace.", 0.4, 0.97, ("3d", "final")),
 ("x2", "From about one hundred feet, he pulls the sidestick back, harder and harder, and below fifty feet, all the way to its stop. But the airplane is slow, and in its alpha protection mode, the flight controls soften the effect of his nose up inputs.", 0.4, 0.98, ("3d", "final")),
 ("x3", "Three thirty and forty-three seconds. The A three twenty touches the Hudson at one hundred twenty-five knots, nose up nine and a half degrees, descending at about seven hundred fifty feet per minute.", 1.0, 0.97, ("3d", "touch")),
 ("x4", "Three minutes and thirty-two seconds after the thumps.", 1.0, 0.97, ("card", "touch")),
 ("x5", "For certification, Airbus's ditching tests assumed a very shallow flight path, about minus half a degree, with engine power available. Flight fifteen forty-nine came in at minus three point four. In the simulator, briefed pilots aiming for minus half a degree came in between minus one and a half and minus three point six degrees in eleven of twelve runs.", 0.4, 1.0, ("card", "touch")),
 ("x6", "The N T S B found it is possible, but unlikely, for pilots to hit all of the ditching parameters with no engine power. And it found the captain's difficulty holding his intended airspeed on final, under high workload, stress and task saturation, contributed to the high descent rate and the fuselage damage.", 0.8, 1.0, ("photo", "ph/s7-014.png", AFT2)),
 # ---- damage
 ("m1", "The impact was hardest at the tail. The lower rear fuselage was torn open, and water began to pour into the back of the cabin.", 0.4, 1.0, ("photo", "ph/s7-013.png", AFT)),
 ("m2", "A vertical beam in the floor structure punched up through the cabin floor right beneath the rear flight attendant's jump seat. She was seriously injured.", 0.4, 1.0, ("photo", "ph/i6-014.png", FLOOR)),
 ("m3", "Because the rear of the airplane was flooding, the two rear slide rafts could not be used.", 0.8, 1.0, ("photo", "ph/s7-008.png", BELLY)),
 # ---- evacuation
 ("v1", "Within seconds of the airplane stopping, people were moving. The N T S B reconstructed the evacuation from videos.", 0.4, 1.0, ("photo", "ph/bea-001.png", BEA)),
 ("v2", "At three thirty fifty-eight, fifteen seconds after touchdown, the left overwing exits open. At three thirty-one oh six, the front left door. Five seconds later, the front right door. Its slide raft is fully deployed five seconds after that.", 0.4, 1.0, ("card", "evac")),
 ("v3", "Passengers stood on both wings. Within two minutes, many of them were in water up to their waists. Forty-one degree water, and a wind chill of two degrees Fahrenheit. About sixty-four people got into the two front slide rafts.", 0.4, 1.0, ("photo", "ph/fig2.png", F2)),
 ("v4", "The flight was not required to carry equipment for an extended flight over water. But this airplane happened to be equipped for it, and so the front slide rafts were there. The N T S B said that contributed to the lack of fatalities.", 0.4, 1.0, ("photo", "ph/fig9.png", F9)),
 ("v5", "Many passengers left without life vests. The board concluded that most passengers will not wait the seven to eight seconds it takes on average to retrieve a vest before giving up. The captain said he and the first officer took vests from under the seats and handed them out, then checked the cabin for anyone left, before leaving themselves.", 0.4, 1.0, ("clip", "dv/872045.mp4", 45.5, VEST)),
 # ---- rescue
 ("y1", "Then the boats came. The airplane was near the New York Waterway ferry terminal at Port Imperial, in Weehawken, New Jersey. Some ferry captains saw it come down.", 0.4, 1.0, ("clip", "dv/965621.mp4", 90.5, FERRY)),
 ("y2", "At three thirty-four and forty seconds, less than four minutes after touchdown, the first vessel arrived. Seven New York Waterway ferries recovered people from the water, the wings and the rafts. A fire department rescue boat and two Coast Guard boats followed.", 0.4, 1.0, ("clip", "dv/994186.mp4", 56.5, ICE)),
 ("y3", "At three fifty-four and forty-three seconds, the last vessel left, carrying the last people rescued from the left wing's slide. Everyone was off the airplane, alive.", 0.4, 1.0, ("card", "rescue")),
 ("y4", "The N T S B called the emergency response timely and efficient, because the responders were close, moved immediately, and had trained before.", 0.8, 1.0, ("clip", "dv/753378.mp4", 24.5, CGNY)),
 # ---- probable cause
 ("q1", "In May two thousand ten, the board adopted its report. The probable cause, in the N T S B's words:", 0.3, 1.0, ("card", "cause")),
 ("q2", "the ingestion of large birds into each engine, which resulted in an almost total loss of thrust in both engines and the subsequent ditching on the Hudson River.", 0.6, 0.97, ("card", "cause")),
 ("q3", "Contributing to the fuselage damage, and to the resulting unavailability of the rear slide rafts: the F A A's approval of ditching certification without determining whether pilots could attain the ditching parameters without engine thrust. The lack of industry flight crew training and guidance on ditching techniques. And the captain's resulting difficulty maintaining his intended airspeed on final approach, due to the task saturation resulting from the emergency situation.", 0.6, 1.0, ("card", "contrib")),
 ("q4", "And contributing to survival: the crew's decision making and crew resource management. The airplane's overwater equipment, though not required. The cabin crew's performance in the evacuation. And the emergency responders' proximity and immediate response.", 0.8, 1.0, ("card", "surv")),
 # ---- what changed
 ("n1", "The N T S B made thirty-four safety recommendations.", 0.3, 1.0, ("card", "recs")),
 ("n2", "Develop technology to tell pilots whether an engine can still run. Test engines against birds at the low fan speeds of a minimum climb, and consider large flocking bird tests, including the core, for smaller engines like this one.", 0.4, 1.0, ("card", "recs")),
 ("n3", "Require a checklist and procedure for a dual engine failure at low altitude. Train pilots on ditching, on the visual illusions of landing on water, and on how alpha protection can limit pitch response.", 0.4, 1.0, ("clip", "dv/865632.mp4", 35.5, DUNK)),
 ("n4", "Life vests and flotation cushions on all flights. Better life vest designs. And a more proactive approach to wildlife hazards around airports.", 0.8, 1.0, ("clip", "dv/465446.mp4", 20.5, USDA)),
 # ---- replay
 ("z1", "Once more. Two thousand eight hundred eighteen feet. Birds. Both engines rolling back. My aircraft. A P U.", 0.4, 0.95, ("3d", "replay")),
 ("z2", "Turning back. Unable. Teterboro. We're gonna be in the Hudson. Brace for impact. Flaps two.", 0.4, 0.95, ("3d", "replay")),
 ("z3", "The river.", 1.2, 0.95, ("3d", "replay")),
 # ---- close
 ("f1", "The N T S B wrote that this was not a typical bird strike. It happened higher and farther from the airport than most, and it took both engines at once. A bird strike, the board said, does not need to be typical to be hazardous.", 0.4, 1.0, ("3d", "orbit")),
 ("f2", "One hundred fifty-five people survived. The N T S B's findings point to many things that went right in a short window: the crew's decisions, an early A P U start, an airplane that happened to carry slide rafts it was not required to have, a cabin crew that moved fast, and rescue boats that were close by.", 0.4, 1.0, ("3d", "orbit")),
 ("f3", "This was LAST CONTACT. Every crash leaves a record. Next file soon.", 1.6, 0.97, ("card", "status")),
]
