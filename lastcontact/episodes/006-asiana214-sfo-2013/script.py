# EPISODE 006 — Asiana Airlines flight 214, Boeing 777-200ER HL7742, descent below visual glidepath and impact
# with seawall, San Francisco International Airport (SFO), runway 28L, July 6, 2013, ~11:28 PDT.
# Source: NTSB Aircraft Accident Report NTSB/AAR-14/01 (adopted June 24, 2014): sec. 1.1 (history of flight, table 1),
# 1.2, 1.5, 1.7, 1.10, 1.12, 1.15, figures 4, 5, 8, 9, 11, 14; executive summary; findings; probable cause (3.2); recs (4).
# (id, spoken text, pause_after, speed, visual)
KC46 = "FILE FOOTAGE · U.S. AIR FORCE KC-46A (BOEING 767-BASED), ALTUS AFB · NOT A 777, NOT THE ACCIDENT AIRPLANE · DVIDS"
SIM = "FILE FOOTAGE · FLIGHT SIMULATORS, U.S. NAVAL TEST PILOT SCHOOL · NOT ASIANA TRAINING · DVIDS"
TWR = "FILE FOOTAGE · AIR TRAFFIC CONTROL TOWER, CREECH AFB · NOT SFO · DVIDS"
ARFF = "FILE FOOTAGE · USMC FIREFIGHTERS, BURN TRAINING ON A MOCK MV-22, MCAS NEW RIVER · NOT SFO · DVIDS"
ARFF2 = "FILE FOOTAGE · USMC AIRCRAFT RESCUE AND FIREFIGHTING DEMO (MAWTS-1, WTI 1-27) · NOT SFO · DVIDS"
F4 = "NTSB AAR-14/01 · FIG. 4 · PROFILE VIEW OF THE LAST 40 SECONDS OF FLIGHT 214"
F5 = "NTSB AAR-14/01 · FIG. 5 · AERIAL VIEW OF THE FLIGHT 214 WRECKAGE (NTSB)"
F8 = "NTSB AAR-14/01 · FIG. 8 · BOEING 777 MODE CONTROL PANEL"
F9 = "NTSB AAR-14/01 · FIG. 9 · 777 FLIGHT MODE ANNUNCIATOR"
F11 = "NTSB AAR-14/01 · FIG. 11 · FIRE DAMAGE TO THE FLIGHT 214 AIRPLANE (NTSB)"
F14 = "NTSB AAR-14/01 · FIG. 14 · AUTOMATION SEQUENCE FROM 1,850 TO 1,330 FT"
LINES = [
 # ---- cold open
 ("o1", "July sixth, two thousand thirteen. Late morning, clear skies over San Francisco Bay.", 0.5, 1.0, ("3d", "open")),
 ("o2", "A Boeing seven seven seven, Asiana Airlines flight two fourteen from Seoul, is on a visual approach to runway two eight left. Three hundred seven people on board.", 0.4, 1.0, ("3d", "open")),
 ("o3", "The weather is good. The runway is in sight. The airplane is not broken. And yet, about a minute from the runway, the autothrottle has stopped controlling the airspeed, and none of the three pilots will notice the change.", 0.4, 1.0, ("3d", "open")),
 ("o4", "Just below two hundred feet, the instructor says, it's low. At ninety feet, he says, speed. The thrust levers go forward.", 0.4, 0.98, ("3d", "open_low")),
 ("o5", "Seven seconds later, the main landing gear and the rear fuselage hit the seawall, short of the runway.", 0.8, 0.97, ("3d", "open_low")),
 ("o6", "Three passengers were killed. One hundred eighty-seven people were injured, forty-nine of them seriously.", 0.6, 0.97, ("card", "toll")),
 ("o7", "In this video: what the N T S B found, second by second. A visual approach without a glideslope. An autothrottle that, without the crew realizing it, was no longer controlling speed. And a go-around that came too late.", 1.2, 1.0, ("card", "toll")),
 ("t1", "Last contact. Asiana flight two fourteen. The approach to San Francisco.", 1.4, 0.95, ("card", "title")),
 # ---- how we know
 ("h1", "Everything here comes from the N T S B accident report, number A A R fourteen, oh one, adopted in June two thousand fourteen.", 0.4, 1.0, ("card", "how")),
 ("h2", "The airplane had a flight data recorder and a cockpit voice recorder, and both were read out. The times you will see are Pacific daylight time, to a tenth of a second where the report gives it.", 0.4, 1.0, ("card", "how")),
 ("h3", "The three D scenes are built on those numbers, over today's aerial imagery. Motion in between is interpolated. The model is a generic Boeing seven seven seven, shown without any airline markings.", 1.0, 1.0, ("3d", "top")),
 # ---- the flight and the crew
 ("a1", "The airplane was a Boeing seven seven seven, two hundred E R, Korean registration H L seven seven four two. A twin engine wide body.", 0.4, 1.0, ("clip", "dv/755613.mp4", 189.0, KC46)),
 ("a2", "Flight two fourteen left Incheon, near Seoul, for a scheduled flight of about ten and a half hours. On board, two hundred ninety-one passengers, twelve flight attendants and four pilots.", 0.4, 1.0, ("clip", "dv/755613.mp4", 28.0, KC46)),
 ("a3", "Two of the pilots were relief crew. The two who flew the approach were a training pair. This was an operating experience flight: a captain in training, flying under the supervision of an instructor.", 0.6, 1.0, ("clip", "dv/755613.mp4", 0.5, KC46)),
 ("p1", "In the left seat, the pilot flying. Forty-five years old, nine thousand six hundred eighty-four hours in total. He had flown the Airbus A three twenty and the Boeing seven thirty-seven as a captain.", 0.3, 1.0, ("card", "crew")),
 ("p2", "But in the seven seven seven, he had thirty-three hours. He was about halfway through his operating experience, and this was the first time he flew a visual approach without a glideslope in the seven seven seven outside a simulator.", 0.4, 1.0, ("card", "crew")),
 ("p3", "In the right seat, the pilot monitoring. An experienced seven seven seven captain with three thousand two hundred eight hours in the type. And this was his first flight as an instructor pilot.", 0.4, 1.0, ("card", "crew")),
 ("p4", "A relief first officer sat in the jump seat behind them, as an observer.", 0.8, 1.0, ("clip", "dv/1026385.mp4", 14.0, SIM)),
 # ---- SFO, no glideslope
 ("r1", "San Francisco International. Runway two eight left points west, and its approach end sits right at the edge of the bay, behind a seawall.", 0.4, 1.0, ("3d", "top")),
 ("r2", "That summer, the airport was in the middle of a project to enlarge its runway safety areas, and the threshold of two eight left had been moved. Because of that work, the electronic glideslope for the runway was out of service. The F A A had published that in a notice to airmen.", 0.4, 1.0, ("card", "nogs")),
 ("r3", "A glideslope is a radio beam that gives pilots, and the autopilot, a precise vertical path down to the runway. Without it, the crew had to manage the descent themselves, using the airplane's automation and their own judgment.", 0.4, 1.0, ("card", "nogs")),
 ("r4", "They still had a lateral guide, the localizer, and a row of four lights next to the runway, called the P A P I. Two white and two red means on the path. All white means high. All red means low.", 0.4, 1.0, ("card", "papi")),
 ("r4b", "The P A P I lights for two eight left had been relocated in that same project. On July second, four days before the accident, an F A A flight check certified them at a glidepath of two point nine eight degrees.", 0.4, 1.0, ("card", "papi")),
 ("r5", "The weather was suitable for a visual approach. Wind from two one zero at about six or seven knots, ten miles visibility, a few clouds at one thousand six hundred feet.", 0.8, 1.0, ("clip", "dv/1001638.mp4", 0.5, TWR)),
 # ---- the approach
 ("e1", "At eleven twenty-one and forty-nine seconds, the approach controller asked if they had the airport in sight. The instructor replied, okay, runway in sight. They were cleared for the visual approach.", 0.4, 1.0, ("clip", "dv/1001638.mp4", 56.0, TWR)),
 ("e1b", "At eleven twenty-two and fifty-two seconds, the autopilot captured the localizer, about fifteen point four miles from the runway. The airplane was descending through about five thousand three hundred feet, at about two hundred ten knots.", 0.4, 1.0, ("clip", "dv/755613.mp4", 126.5, KC46)),
 ("e2", "At eleven twenty-three seventeen, about fourteen miles out, the controller asked them to slow to one hundred eighty knots, and hold that speed until five miles from the airport.", 0.4, 1.0, ("3d", "far")),
 ("e3", "The N T S B found the speed restriction was standard, and there was ample distance to get onto the right path. But the descent was not managed well, and the airplane drifted well above the desired three degree glidepath.", 0.4, 1.0, ("3d", "far")),
 ("e4", "At eleven twenty-four and fifty-three seconds, as the landing gear came down, the instructor said, this seems a little high. The pilot flying asked, do you mean it's too high? Then: I will descend more. These words were spoken in Korean; this is the N T S B's translation.", 0.4, 1.0, ("card", "cvr1")),
 ("e5", "He set a descent rate of one thousand five hundred feet per minute on the autopilot.", 0.4, 1.0, ("card", "cvr1")),
 ("e6", "At five miles from the runway, the airplane was still about four hundred feet above the three degree path. Speed about one hundred seventy-four knots.", 0.4, 1.0, ("3d", "far")),
 ("e7", "At eleven twenty-six and twelve seconds, the pilot flying called for flaps thirty. The airspeed, one hundred seventy-four knots, was above the flaps thirty limit of one hundred seventy.", 0.6, 1.0, ("3d", "far")),
 # ---- the automation trap
 ("m1", "And now, the moment the N T S B spent much of its report on. Eleven twenty-six and twenty-five point seven seconds.", 0.4, 1.0, ("card", "modes")),
 ("m2", "The autopilot pitch mode changed to flight level change speed. F L C H. Nobody called it out. In a post accident interview, the pilot flying said he had considered pressing that button to get a higher descent rate, but could not recall whether he did. The N T S B concluded it is likely that he selected it.", 0.4, 1.0, ("card", "modes")),
 ("m3", "Here is the problem. The altitude selected on the mode control panel was three thousand feet, the missed approach altitude. The airplane was below it. So in that mode, the automation started to climb.", 0.4, 1.0, ("photo", "fig8.png", F8)),
 ("m4", "Three seconds later, the pilot flying disconnected the autopilot. He pulled the thrust levers back to idle, overriding the autothrottle.", 0.4, 1.0, ("card", "modes")),
 ("m5", "And when the thrust levers reached idle, the autothrottle went into a mode called HOLD. In HOLD, the autothrottle does not move the thrust levers, and it does not control airspeed. The thrust stayed at idle.", 0.4, 1.0, ("photo", "fig14.png", F14)),
 ("m6", "The change was shown on the flight mode annunciator, the row of mode labels at the top of each pilot's primary flight display. None of the three pilots recalled seeing it.", 0.4, 1.0, ("photo", "fig9.png", F9)),
 ("m7", "The N T S B found that, because of complexities in the seven seven seven's automatic flight control system and gaps in the related training and documentation, the pilot flying had an inaccurate understanding of how the autopilot and autothrottle interacted to control airspeed. He believed the autothrottle would keep controlling his speed. In HOLD, it would not.", 0.8, 1.0, ("card", "modes")),
 # ---- the last 1,000 feet
 ("l1", "Eleven twenty-six and fifty-five seconds. One thousand feet above the ground, two point one miles out. Airspeed about one hundred fifty-one knots, and falling. Descent rate one thousand five hundred feet per minute. The P A P I shows four white lights. Still high.", 0.4, 1.0, ("3d", "profile")),
 ("l2", "The observer in the jump seat says, sink rate, sir. A few seconds later, again: sink rate, sir.", 0.4, 1.0, ("3d", "profile")),
 ("l3", "Eleven twenty-seven fifteen. Five hundred feet. This is the point where, under Asiana's procedures, the approach had to be stabilized. Otherwise, a go-around.", 0.4, 1.0, ("card", "gate")),
 ("l4", "The airspeed has just reached the target, one hundred thirty-seven knots. The lights show three white and one red, slightly high. But the thrust levers are at idle, and the airplane is descending at about one thousand two hundred feet per minute, when about seven hundred was needed to stay on the path.", 0.4, 1.0, ("card", "gate")),
 ("l5", "Two signs, the N T S B said, that the approach was not stabilized. The crew should have gone around. There was no five hundred foot callout, and they continued. The N T S B noted that this is not unusual: industry statistics show about ninety-seven percent of unstable approaches are continued to landing.", 0.6, 1.0, ("card", "gate")),
 ("l6", "Eleven twenty-seven and twenty seconds. The instructor says, on glide path, sir. Two white, two red. For a moment, the picture out the window looks right.", 0.4, 1.0, ("3d", "papi")),
 ("l7", "But the engines are at idle, and nothing is holding the speed. Three seconds later, the airspeed drops below the reference speed of one hundred thirty-two knots. One white, three red.", 0.4, 1.0, ("3d", "papi")),
 ("l8", "Eleven twenty-seven thirty-one. Four red lights. Two hundred nineteen feet, one hundred twenty-two knots.", 0.4, 1.0, ("3d", "papi")),
 ("l9", "The nose keeps rising as the pilot flying pulls back to stay up. The airplane keeps slowing.", 0.6, 1.0, ("photo", "fig4.png", F4)),
 # ---- the end
 ("x1", "At about one hundred eighty feet, the instructor says, it's low. The pilot flying answers, yeah.", 0.4, 0.98, ("card", "cvr2")),
 ("x2", "At one hundred twenty-four feet, a master caution chime sounds. Airspeed about one hundred fourteen knots.", 0.4, 0.98, ("card", "cvr2")),
 ("x3", "At ninety feet, the instructor says, speed. Less than a second later, he pushes both thrust levers forward.", 0.4, 0.98, ("card", "cvr2")),
 ("x4", "The engines respond within their design specification, but from idle they need six to seven seconds to approach full power. The stick shaker starts. The lowest airspeed of the approach, about one hundred three knots.", 0.4, 0.98, ("3d", "final")),
 ("x5", "At eleven twenty-seven and forty-seven point eight seconds, the instructor calls, go around. Two and a half seconds before impact. Once the airplane was below one hundred feet, the N T S B found, it no longer had the performance to complete a go-around.", 0.4, 0.98, ("3d", "final")),
 ("x6", "Eleven twenty-seven and fifty seconds. The main landing gear, then the underside of the rear fuselage, strike the seawall. Engine fan speed is passing about ninety-two percent. Airspeed about one hundred six knots.", 1.0, 0.97, ("3d", "final")),
 # ---- impact sequence and survival
 ("s1", "The tail broke off at the aft pressure bulkhead. The airplane slid along the runway, its rear lifted, and it spun about three hundred thirty degrees before coming down a final time, off the left side of the runway.", 0.4, 1.0, ("3d", "rest")),
 ("s2", "It stopped about two thousand four hundred feet from the seawall, at about eleven twenty-eight and six seconds.", 0.4, 1.0, ("3d", "rest")),
 ("s3", "The impact forces exceeded certification limits. Inside the cabin, two slide rafts inflated, injuring and temporarily trapping two flight attendants. Four flight attendants seated in the aft galley were ejected when that part of the airplane was destroyed. They had been wearing their restraints.", 0.4, 1.0, ("photo", "fig5.png", F5)),
 ("s4", "Two of the three passengers who died were ejected. They were not wearing their seatbelts. The N T S B said they would likely have remained in the cabin and survived if they had been.", 0.6, 1.0, ("photo", "fig5.png", F5)),
 ("s5", "Then, fire. It started inside the separated right engine, which had come to rest against the right side of the fuselage.", 0.4, 1.0, ("photo", "fig11.png", F11)),
 ("s6", "When a flight attendant saw it, he started the evacuation. Ninety-eight percent of the passengers got out on their own.", 0.4, 1.0, ("clip", "dv/1023470.mp4", 14.5, ARFF2)),
 ("s7", "As the fire spread into the fuselage, firefighters entered the airplane and brought out five passengers who were injured and unable to leave.", 0.4, 1.0, ("clip", "dv/1021914.mp4", 182.5, ARFF)),
 ("s8", "In the end, ninety-nine percent of the people on board survived.", 0.8, 1.0, ("clip", "dv/1023470.mp4", 49.5, ARFF2)),
 # ---- why
 ("w1", "So why did three experienced pilots not see the airspeed fall for so long?", 0.4, 1.0, ("card", "why")),
 ("w2", "The N T S B said their insufficient monitoring of airspeed likely resulted from four things. Expectancy: they believed the autothrottle was controlling speed, and what they saw seemed to confirm it. Increased workload, from the high approach and the tasks squeezed into its final minute.", 0.4, 1.0, ("card", "why")),
 ("w3", "Fatigue: they had crossed eight time zones, and the approach came at a time when they would normally have been asleep. The N T S B found all three were likely fatigued. And automation reliance.", 0.4, 1.0, ("card", "why")),
 ("w4", "The report also looked at the crew dynamic. The instructor was on his first flight supervising a trainee in line operations. The N T S B said he had not had the chance, during his own training, to practice that under an experienced instructor's eye.", 0.4, 1.0, ("clip", "dv/1026385.mp4", 42.5, SIM)),
 ("w5", "And the pilot flying told investigators that at five hundred feet he worried that letting the lights go to four red would mean failing his flight, and being embarrassed. It was not a check flight. The N T S B found he had not received enough training on planning and flying visual approaches.", 0.8, 1.0, ("clip", "dv/1026385.mp4", 7.5, SIM)),
 # ---- probable cause
 ("c1", "In June two thousand fourteen, the board adopted its findings. The probable cause, in the N T S B's words:", 0.3, 1.0, ("card", "cause")),
 ("c2", "the flight crew's mismanagement of the airplane's descent during the visual approach, the pilot flying's unintended deactivation of automatic airspeed control,", 0.2, 0.97, ("card", "cause")),
 ("c3", "the flight crew's inadequate monitoring of airspeed, and the flight crew's delayed execution of a go-around after they became aware that the airplane was below acceptable glidepath and airspeed tolerances.", 0.6, 0.97, ("card", "cause")),
 ("c4", "Contributing, the N T S B listed five factors. The first: the complexities of the autothrottle and autopilot flight director systems, which were inadequately described in Boeing's documentation and Asiana's pilot training, increasing the likelihood of mode error.", 0.4, 1.0, ("card", "contrib")),
 ("c5", "Then, the crew's nonstandard communication and coordination about the automation. The pilot flying's inadequate training on visual approaches. The instructor's inadequate supervision. And flight crew fatigue, which likely degraded their performance.", 0.8, 1.0, ("card", "contrib")),
 # ---- what changed
 ("k1", "The N T S B made twenty-seven new safety recommendations.", 0.3, 1.0, ("card", "recs")),
 ("k2", "To the F A A: require better seven seven seven training on autothrottle modes, and a demonstration of the situations in which the autothrottle does not protect against low speed. And a special design review of how the seven seven seven controls airspeed.", 0.4, 1.0, ("card", "recs")),
 ("k3", "Also, design requirements for low energy alerting systems, a warning when an airplane is getting too slow or too low. And to Boeing: develop and evaluate a change to its wide body autoflight systems, to help keep the airplane above its minimum energy state.", 0.4, 1.0, ("clip", "dv/755613.mp4", 154.5, KC46)),
 ("k4", "To Asiana: reinforce, in training, the standard procedures for mode control panel inputs and the callouts that go with them. Have new instructors supervised by a more experienced instructor until they are proficient. And allow more manual flying, in training and on the line.", 0.4, 1.0, ("card", "recs")),
 ("k5", "And for airport firefighters: a minimum staffing level that allows crews to fight a fire inside an airplane and rescue the people in it, and minimum training for every officer placed in command at an accident scene.", 0.8, 1.0, ("clip", "dv/1023470.mp4", 84.5, ARFF2)),
 # ---- replay
 ("z1", "Once more, the last minute. One thousand feet: four white, sink rate. Five hundred feet, target speed, but idle thrust.", 0.4, 0.95, ("3d", "replay")),
 ("z2", "On glide path. Below reference speed. Four red. It's low. Chime. Speed. Thrust levers forward. Stick shaker. Go around.", 0.4, 0.95, ("3d", "replay")),
 ("z3", "The seawall.", 1.2, 0.95, ("3d", "replay")),
 # ---- close
 ("q1", "There was no mechanical failure on flight two fourteen. The N T S B found no evidence of any structural, engine, or system failure before impact, and no problem with the autoflight system. The automation behaved as it was designed to.", 0.4, 1.0, ("3d", "orbit")),
 ("q2", "What failed was the link between the people and the machine: what the pilots expected the autothrottle was doing, and what it was actually doing. Two pilots watching the runway, a third watching the descent rate, and no one watching the speed.", 0.4, 1.0, ("3d", "orbit")),
 ("q3", "This was LAST CONTACT. Every crash leaves a record. Next file soon.", 1.6, 0.97, ("card", "status")),
]
