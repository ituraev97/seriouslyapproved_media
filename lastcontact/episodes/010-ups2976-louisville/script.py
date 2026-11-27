# EPISODE 010 — UPS flight 2976, McDonnell Douglas MD-11F N259UP, left engine and pylon separation on takeoff, Louisville (SDF), Nov 4, 2025, ~17:14 EST.
# NTSB DCA26MA024 — investigation ONGOING (no probable cause yet). Sources: NTSB preliminary report; NTSB investigative update (Jan 14, 2026);
# IIC opening presentation + docket exhibits of the May 19–20, 2026 investigative hearing (Structures 7A/7F/7H/7K/7U, FDR 10A + CSV, Materials 15A,
# Maintenance 11A, Hazmat 17A, Video Group 19A, exemplar photos 7AA); NTSB animation (YouTube NTSBgov, May 19, 2026); NTSB media briefings Nov 5–7, 2025;
# NTSB closing remarks (May 20, 2026). Cause/blame: NEVER stated; findings are attributed to the NTSB as "so far".
# (id, spoken text, pause_after, speed, visual)  visual = ("3d", shot) | ("card", name) | ("photo", file, credit) | ("clip", file, start_s, label)
ANIM = "NTSB ANIMATION · PYLON FAILURE SEQUENCE · MAY 19, 2026"
SURV = "AIRPORT SURVEILLANCE VIDEO (SOURCE: UPS) · PLAYED AT HALF SPEED · FROM THE NTSB ANIMATION, MAY 19, 2026"
BRO2 = "NTSB B-ROLL · INVESTIGATORS MAP THE SCENE · NOV. 6, 2025"
BRO = "NTSB B-ROLL · AERIAL VIEW OF THE SCENE, LOUISVILLE · NOV. 7, 2025"
M1 = "NTSB MEDIA BRIEFING 1 · NOV. 5, 2025"
M2 = "NTSB MEDIA BRIEFING 2 · NOV. 6, 2025"
M3 = "NTSB MEDIA BRIEFING 3 · NOV. 7, 2025"
H1 = "NTSB INVESTIGATIVE HEARING · DAY 1 · MAY 19, 2026"
H2 = "NTSB INVESTIGATIVE HEARING · DAY 2 · MAY 20, 2026"
P1 = "NTSB PRELIMINARY REPORT · FIG. 1 · AIRPORT SURVEILLANCE VIDEO STILLS (SOURCE: UPS)"
P2 = "NTSB PRELIMINARY REPORT · AIRPORT SURVEILLANCE VIDEO (SOURCE: UPS)"
P3 = "NTSB PRELIMINARY REPORT · FIG. 3 · FLIGHT TRACK FROM ADS-B DATA"
P4 = "NTSB PRELIMINARY REPORT · FIG. 5 · PYLON-TO-WING CONNECTION (BOEING DIAGRAM, EDITED BY NTSB)"
P5 = "NTSB PRELIMINARY REPORT · FIG. 8 · LEFT WING CLEVIS AND THE FRACTURED BEARING"
P6 = "NTSB PRELIMINARY REPORT · FIG. 7 · LEFT PYLON AFT MOUNT, FRACTURED LUGS"
P7 = "NTSB PRELIMINARY REPORT · FIG. 9 · PARTS RETAINED FOR THE MATERIALS LABORATORY"
P8 = "NTSB PRELIMINARY REPORT · FIG. 10 · BEARING AND HARDWARE AFTER REMOVAL"
U1 = "NTSB INVESTIGATIVE UPDATE · JAN. 14, 2026 · FIG. 2 · THE FRACTURED BEARING RACE"
U2 = "NTSB INVESTIGATIVE UPDATE · JAN. 14, 2026 · FIG. 3 · FATIGUE AND OVERSTRESS AREAS"
U3 = "NTSB INVESTIGATIVE UPDATE · JAN. 14, 2026 · FIG. 4 · CUTAWAY OF THE ASSEMBLY"
U4 = "NTSB INVESTIGATIVE UPDATE · JAN. 14, 2026 · FIG. 5 · FDR DATA, LAST 30 SECONDS (PRELIMINARY)"
M15A = "NTSB DOCKET · MATERIALS GROUP · LEFT AFT MOUNT AND WING CLEVIS"
M15B = "NTSB DOCKET · MATERIALS GROUP · THE BEARING RACE UNDER THE MICROSCOPE"
M15C = "NTSB DOCKET · MATERIALS GROUP · FRACTURE SURFACE OF THE BEARING RACE"
M15D = "NTSB DOCKET · MATERIALS GROUP · ELECTRON MICROSCOPE IMAGE OF THE FRACTURE"
EXE = "NTSB DOCKET · EXHIBIT 7AA · EXEMPLAR MD-11 PYLON AFT MOUNT BULKHEAD (NOT THE ACCIDENT PART)"
EXE2 = "NTSB DOCKET · EXHIBIT 7AA · EXEMPLAR AFT MOUNT, SIDE VIEW (NOT THE ACCIDENT PART)"
S7A1 = "NTSB DOCKET · STRUCTURES GROUP · PYLON STRUCTURE DIAGRAM"
S7A2 = "NTSB DOCKET · STRUCTURES GROUP · PYLON-TO-WING ATTACHMENTS"
BOE1 = "NTSB DOCKET · EXHIBIT 7U · BOEING HEARING SLIDE · PYLON-TO-WING ATTACHMENT"
LINES = [
 # ---- cold open (3D from FDR)
 ("o1", "November fourth, two thousand twenty-five. Twelve minutes past five in the afternoon, Louisville, Kentucky.", 1.1, 1.0, ("3d", "open")),
 ("o2", "UPS flight twenty-nine seventy-six, a Boeing M D eleven freighter, starts its takeoff roll on runway one seven right. Next stop, Honolulu. Three pilots on board.", 1.1, 1.0, ("3d", "open")),
 ("o3", "At five thirteen and five seconds, the airplane lifts off, at one hundred seventy-four knots. Four seconds later, five feet above the runway, the data from the left engine stops being reliable.", 1.1, 1.0, ("3d", "climb")),
 ("o4", "Two seconds after that, the fire indication for the left engine. The airplane will never climb higher than twenty-nine feet. The recording ends twenty-five seconds after liftoff.", 0.7, 1.0, ("3d", "climb")),
 ("o5", "Three crew members and eleven people on the ground were killed. Twenty-three more people on the ground were injured, and one of them died of injuries fifty-one days later.", 0.5, 1.0, ("clip", "relay/broll1.mp4", 73.0, BRO)),
 ("o6", "In this video: what the N T S B has found so far. A crack in a bearing ring. A Boeing service letter from two thousand eight. And what a public hearing asked about it.", 1.1, 1.0, ("clip", "relay/anim4.mp4", 37.0, SURV)),
 ("t1", "Last contact. UPS flight twenty-nine seventy-six.", 1.4, 0.95, ("card", "title")),
 # ---- how we know
 ("h1", "The investigation is not finished. The N T S B has not determined a probable cause, and neither will we. Its final report is still to come.", 1.1, 1.0, ("clip", "relay/m2b.mp4", 20.0, M2)),
 ("h2", "Everything here comes from the board's own publications: its preliminary report, an investigative update from January, its media briefings, and the public docket opened at the investigative hearing in May. That docket includes material from the parties, such as Boeing and UPS, and we say when something is theirs. Where we describe findings, they are findings so far, and we say who made them.", 1.1, 1.0, ("card", "how")),
 ("h3", "The three D scenes are built on the airplane's own flight data recorder, over today's aerial imagery. Motion between data points is interpolated. The model is a generic M D eleven, without markings.", 1.1, 1.0, ("3d", "top")),
 # ---- the airplane and the flight
 ("a1", "The airplane was a McDonnell Douglas M D eleven F, registration N two five nine U P. Built in nineteen ninety-one. It joined UPS in two thousand six.", 1.1, 1.0, ("photo", "ph/exe1.jpg", EXE)),
 ("a2", "The M D eleven is a three-engine widebody. One engine hangs under each wing. The third sits at the base of the tail. On this airplane, they were General Electric C F six engines.", 1.1, 1.0, ("photo", "ph/diag.png", P4)),
 ("a3", "On board that afternoon, about one hundred ninety-three thousand pounds of jet fuel, and one hundred sixteen thousand pounds of cargo, packed in thirty-nine containers. Thirty-two of them were loaded by the Postal Service, and the cargo was bound for Hawaii.", 1.1, 1.0, ("card", "load")),
 ("a4", "The captain had about eighty-six hundred flight hours, almost five thousand of them in the M D eleven. The first officer, who was flying, had about ninety-two hundred hours, about one thousand in type. A relief officer, the third pilot, had more than fifteen thousand hours, nearly nine thousand in type.", 1.4, 1.0, ("card", "crew")),
 ("w1", "Conditions at the airport: visual, ten miles of visibility, a light wind, six knots from the east-southeast, in the airport's last observation before takeoff.", 1.1, 1.0, ("card", "wx")),
 ("w2", "About five eleven, the tower cleared the flight for takeoff. At five twelve sixteen, the throttles move forward on all three engines.", 1.1, 1.0, ("3d", "open")),
 ("w3", "At five thirteen and five seconds, with computed airspeed one hundred seventy-four knots, the nose gear leaves the ground.", 1.4, 1.0, ("3d", "climb")),
 # ---- the event
 ("e1", "An airport surveillance camera recorded the next seconds. Shortly after rotation, the left engine and its pylon, the structure that holds the engine to the wing, separate from the airplane, as one unit.", 1.1, 1.0, ("photo", "ph/surv6.png", P1)),
 ("e2", "A fire ignites on the left engine, and near the place where the pylon was attached to the wing. According to the preliminary report, the engine travels above the fuselage and hits the ground. The fire near the wing keeps burning until the end.", 1.1, 1.0, ("photo", "ph/surv1.png", P2)),
 ("e3", "In the data: at five thirteen eleven, the left engine fire indication, and the stick shaker activates, and stays active, apart from two data points. One second later, pressure in hydraulic system one falls from about three thousand pounds per square inch to sixteen.", 1.1, 1.0, ("photo", "ph/fdrplot.png", U4)),
 ("e4", "The throttle angles for engines two and three increase at five thirteen twelve, and again at twenty-two. The rudder pedal input stays in the nose-right direction, and the control wheel mostly right wing down, to the end of the recording.", 1.1, 1.0, ("3d", "side")),
 ("e5", "At five thirteen twenty-one, the radio altitude reaches its maximum: twenty-nine feet. Four seconds later, an increasing left roll begins. The recording ends at five thirteen thirty.", 0.5, 1.0, ("3d", "side")),
 ("e6", "The airplane cleared the blast fence past the end of the runway. Then its left main landing gear hit the roof of a warehouse at the southern edge of the airport. It struck a storage yard and two more buildings, and was mostly consumed by fire.", 1.1, 1.0, ("photo", "ph/track.png", P3)),
 ("e7", "The wreckage area ran about three thousand feet south-southeast from that first roof. The N T S B's aerial view of the scene, from November seventh.", 0.5, 1.0, ("clip", "relay/broll1.mp4", 61.0, BRO)),
 ("e8", "A witness in the tower reported that the takeoff speed looked normal for that type of airplane, but the climb did not. Another reported that the airplane stopped climbing and began to lose altitude before rolling slightly to the left.", 1.4, 1.0, ("clip", "relay/m1b.mp4", 5.0, M1)),
 # ---- why no climb: open question
 ("c1", "Why did the airplane not climb? The N T S B says its airplane performance study is not finished. It will look at why the altitude did not substantially increase after the pylon and engine separated, and at how the separation affected handling.", 1.1, 1.0, ("clip", "relay/m3c.mp4", 15.0, M3)),
 ("c2", "One detail the board has pointed out. After the pylon separated, the leading edge slats on the left wing stayed extended, and a fire burned on the left wing.", 1.1, 1.0, ("clip", "relay/h1b.mp4", 20.0, H1)),
 ("c3", "The board's hearing slides raised an older accident. In nineteen seventy-nine, a DC ten, the M D eleven's ancestor, lost its left engine and pylon on takeoff at Chicago O'Hare. The N T S B found the slats on that wing had retracted, after hydraulic lines were severed. The airplane rolled left and crashed. Two hundred seventy-three people died.", 1.1, 1.0, ("clip", "relay/h1e.mp4", 8.0, H1)),
 ("c4", "The M D eleven carries changes made after that accident. A Boeing hearing slide says the M D eleven's slats stay extended after a hydraulic failure. What the slats did in Louisville, and what it meant, is still the N T S B's to say.", 1.4, 1.0, ("photo", "ph/boe_dc10.png", "NTSB DOCKET · EXHIBIT 7U · BOEING HEARING SLIDE · DC-10 IMPROVEMENTS INCORPORATED ON THE MD-11")),
 # ---- the response
 ("r1", "The N T S B launched investigators to Louisville, and was on scene on November fifth. Parties to the investigation: the F A A, UPS, Boeing, G E Aerospace, a pilots' association, a Teamsters union division, and Collins Aerospace.", 1.1, 1.0, ("clip", "relay/m1a.mp4", 8.0, M1)),
 ("r2", "At its briefings, the board said what it knew, and what it didn't. Investigators documented the site and collected the recorders. Both were recovered, and both were read out.", 1.1, 1.0, ("clip", "relay/broll1.mp4", 25.0, BRO2)),
 ("r3", "The cockpit voice recorder held two hours and four minutes, including the whole flight. The flight data recorder, sixty-three hours, across twenty-four flights, about four hundred fifty parameters. The docket also holds the cockpit recording's report. We have chosen not to use it.", 1.4, 1.0, ("clip", "relay/m3a.mp4", 10.0, M3)),
 # ---- what was found
 ("f1", "On and beside runway one seven right, investigators found the left engine, the left pylon, and pieces of fan blades. The left wing's attachment fitting, the clevis, was found at the accident site, with the bolt, the bearing and the hardware still on it.", 1.1, 1.0, ("photo", "ph/clevis.png", P5)),
 ("f2", "How is an engine held on a wing? A pylon, and three attachments. A forward mount. A thrust link behind it. And an aft mount, a triangular bulkhead with two lugs at the top. Between those lugs sits one spherical bearing, a ball inside a ring called the race, and a bolt runs through it into the wing.", 1.1, 1.0, ("photo", "ph/exe2.jpg", EXE)),
 ("f3", "The aft mount of the left pylon was found with both of its lugs fractured. The bearing's race was broken all the way around, in two pieces.", 1.1, 1.0, ("photo", "ph/lugs.png", P6)),
 ("f4", "The pieces went to the N T S B Materials Laboratory in Washington. There, investigators found fatigue cracking in the bearing race. Fatigue is damage from repeated loads. A crack starts small and grows under repeated loading, until what is left can no longer hold.", 1.1, 1.0, ("photo", "ph/parts.png", P7)),
 ("f5", "In this race, the fatigue cracks began around the entire circumference, at the edge of a groove cut into the inside of the ring, to help spread grease. About seventy-five percent of the fracture surface was fatigue. The rest was overstress, the final break.", 1.1, 1.0, ("photo", "ph/upd_fat.png", U2)),
 ("f6", "Under the electron microscope, the fracture surfaces. Some grease-like material was still inside the bearing.", 1.1, 1.0, ("photo", "ph/sem.png", M15D)),
 ("f7", "The lugs had fatigue cracks too, along the bores. But the fracture on the outboard side of the forward lug was mostly overstress, with only two small fatigue cracks at the edge of the bore.", 1.4, 1.0, ("photo", "ph/lugs2.png", M15A)),
 # ---- NTSB animation
 ("n1", "At the hearing, the N T S B showed an animation of how it says the cracks led to the separation, so far. A crack grows outward from the corners of the groove, in the bearing race.", 1.1, 1.0, ("clip", "relay/anim3.mp4", 17.0, ANIM)),
 ("n2", "The race splits in two, and the pieces can migrate, forward and aft, inside the lugs. The abnormal loading that follows, the animation shows, starts new fatigue cracks in the bores of the lugs.", 1.1, 1.0, ("clip", "relay/anim3.mp4", 46.0, ANIM)),
 ("n3", "In the animation, the cracks grow outward. The inboard side of the lugs fractures completely. Then the lugs bend, and the outboard side fractures.", 1.1, 1.0, ("clip", "relay/anim3.mp4", 71.0, ANIM)),
 ("n4", "In the animation, the engine rotates up around its forward mount, the forward mount fails, and the engine departs the airplane. The last part shows the airport surveillance video at half speed: the left pylon and engine leave the wing, as one unit, shortly after rotation.", 1.4, 1.0, ("clip", "relay/anim4.mp4", 23.0, ANIM)),
 # ---- what Boeing wrote
 ("s1", "This bearing has a history in the records. In May two thousand eight, Boeing sent operators a service letter about the bearing at the aft end of the M D eleven pylon.", 1.1, 1.0, ("card", "sl")),
 ("s2", "A revised version, in two thousand eleven, described four earlier failures of this part number, on three airplanes. In each, the failure had started at the groove cut into the inside of the race.", 1.1, 1.0, ("card", "sl")),
 ("s3", "A broken race can be seen. Its two halves slide out, beyond the surface of the lugs. So the letter pointed to a visual check: is the bearing still flush? Boeing's review, the letter says, found the failure would not result in a safety of flight condition.", 1.1, 1.0, ("photo", "ph/upd_section.png", U3)),
 ("s4", "The revised letter also described a newer bearing, with no groove. It recommended installing it if a bearing was found unserviceable. The N T S B's update notes that it did not prohibit fitting the old type as a replacement.", 1.1, 1.0, ("card", "sl")),
 ("s5", "In the N T S B docket, a Boeing document lists every operator report it knew of, before the accident, of a crack in this bearing that required replacing it. Seven. The first in two thousand two. The last in two thousand twenty. As of April, two thousand twenty-six.", 1.4, 1.0, ("card", "seven")),
 # ---- this airplane
 ("m1", "And this airplane. At the time of the accident it had about ninety-three thousand flight hours, and twenty-one thousand cycles. A cycle is one takeoff and landing.", 1.1, 1.0, ("card", "mx")),
 ("m2", "UPS's program called for a general visual inspection and a detailed visual inspection of the left pylon aft mount every seventy-two months. The last, on October twenty-eighth, two thousand twenty-one. The bearings were lubricated on October eighteenth, two thousand twenty-five. Seventeen days before the accident.", 1.1, 1.0, ("card", "mx")),
 ("m3", "A special detailed inspection of the lugs, with non-destructive testing, would have come due at twenty-nine thousand two hundred cycles. This airplane had twenty-one thousand and forty-three. It had not reached it.", 1.4, 1.0, ("card", "mx")),
 # ---- fleet actions
 ("x1", "Three days after the crash, UPS grounded its M D elevens, as a precaution, at Boeing's recommendation. The next day, the F A A issued an emergency airworthiness directive, prohibiting further flight of every M D eleven until it was inspected. On November fourteenth, the order grew to include the DC ten.", 1.1, 1.0, ("clip", "relay/m1d.mp4", 10.0, M1)),
 ("x2", "The inspections that followed found three M D elevens with a migrated bearing race, all of them UPS airplanes with G E engines. And one DC ten or M D ten. In one UPS finding, the lugs showed a gap, and cracks on the inboard and outboard sides.", 1.1, 1.0, ("photo", "ph/uh_lug.png", "NTSB DOCKET · EXHIBIT 7K · UPS INSPECTION RESULTS · MIGRATED BEARING RACE (UPS)")),
 ("x3", "None of that tells us why. These are inspection findings. What they mean is for the N T S B to say.", 1.4, 1.0, ("card", "ad")),
 # ---- the hearing
 ("g1", "In May, the N T S B held a two-day investigative hearing in Washington. A hearing is not where a cause is decided. Its purpose is to gather facts, in public, from witnesses.", 1.1, 1.0, ("clip", "relay/h2a.mp4", 13.0, H2)),
 ("g2", "Panel one was about fleet safety processes. How an anomaly found in maintenance is reported, to the airline's quality assurance, to Boeing, to the F A A. How the F A A and Boeing decide whether a problem is an unsafe condition. And what operators are told afterwards.", 1.1, 1.0, ("clip", "relay/h1c.mp4", 10.0, H1)),
 ("g3", "The board described the system like this. Data comes in: service difficulty reports, reports from operators. It is analyzed, to decide whether an unsafe condition exists. Then a corrective action is chosen. A service letter, or an airworthiness directive.", 1.1, 1.0, ("clip", "relay/h2b.mp4", 10.0, H2)),
 ("g4", "The difference matters. A service letter is the manufacturer's advice to operators. An airworthiness directive is an F A A rule, and is mandatory.", 1.1, 1.0, ("clip", "relay/h2d.mp4", 10.0, H2)),
 ("g5", "Panel two was about design requirements. What F A A rules require when a pylon fails. And how fuel lines, hydraulic lines and other systems are routed near the attachment points.", 1.1, 1.0, ("clip", "relay/h2c.mp4", 10.0, H2)),
 ("g6", "Witnesses came from UPS, a maintenance provider, a labor union, the F A A and Boeing. Their testimony is public. The board's analysis of it is not, yet.", 1.4, 1.0, ("clip", "relay/h1d.mp4", 10.0, H1)),
 # ---- what is next
 ("z1", "At the close, the Chairwoman said the hearing had shed light on facts and circumstances, all of which the board will consider in its final report.", 1.1, 1.0, ("clip", "relay/h2e.mp4", 10.0, H2)),
 ("z2", "That report, she said, will be much broader than the hearing. It will contain the board's analysis, the probable cause, and its safety recommendations.", 1.1, 1.0, ("clip", "relay/h2e.mp4", 40.0, H2)),
 ("z3", "The investigation began during a federal government shutdown. The N T S B went anyway, and worked nights and weekends afterwards to stay on schedule. The aim: a final report within twelve to eighteen months of the accident. In the Chairwoman's words, quote, we hope to have answers no later than next May. That is May, twenty twenty-seven.", 1.4, 1.0, ("clip", "relay/h2f.mp4", 10.0, H2)),
 # ---- open questions
 ("q1", "Four questions this video cannot answer. One. Why the airplane did not climb after the engine left. The performance study is not finished.", 1.1, 1.0, ("card", "open")),
 ("q2", "Two. How a cracked bearing race, and fractured lugs, came to be in that condition on this airplane, and when. The board has described the fatigue. Its analysis of the rest is still to come.", 1.1, 1.0, ("card", "open")),
 ("q3", "Three. What reached operators over the years, and what was done with it. The whole first panel of the hearing was about that. There are no findings yet.", 1.1, 1.0, ("card", "open")),
 ("q4", "And four. What the F A A's design rules require when a pylon fails, and how systems are routed near the attachment points. That was the second panel's subject. The board has announced no findings on it.", 1.4, 1.0, ("card", "open")),
 ("y1", "Replay. Five twelve sixteen, throttles forward. Five thirteen oh five, liftoff. Five thirteen eleven, fire. Five thirteen twenty-one, twenty-nine feet. Five thirteen thirty, the recording ends.", 0.8, 0.97, ("3d", "replay")),
 ("y2", "The N T S B has not determined the cause of this accident. When it does, we will cover it. Every crash leaves a record.", 1.0, 0.97, ("card", "status")),
]
