# EPISODE 005 — Global Exec Aviation Learjet 60 (N999LJ), runway overrun during rejected takeoff,
# Columbia Metropolitan Airport (CAE), South Carolina, Sept 19, 2008, ~11:53 p.m. EDT.
# Source: NTSB Aircraft Accident Report NTSB/AAR-10/02 (adopted April 6, 2010), incl. CVR transcript (App. B),
# sound spectrum study (1.16.1), performance study + map overlay (1.16.2, fig. 6), findings, probable cause, recs.
# (id, spoken text, pause_after, speed, visual)
C21 = "FILE FOOTAGE · U.S. AIR FORCE C-21A, A MILITARY LEARJET 35A · NOT A LEARJET 60, NOT THE ACCIDENT AIRPLANE · DVIDS"
C21R = "FILE FOOTAGE · C-21A (LEARJET 35A) TAKEOFF ROLL, RAMSTEIN AB · NOT A LEARJET 60 · DVIDS"
C21Q = "FILE FOOTAGE · C-21A (LEARJET 35A), AL UDEID AB · NOT THE ACCIDENT AIRPLANE · DVIDS"
TIRE = "FILE FOOTAGE · AIR FORCE CREW CHIEFS CHANGE A MAIN GEAR TIRE · NOT A LEARJET 60 · DVIDS"
TR17 = "FILE FOOTAGE · C-17 ENGINE + THRUST REVERSER WORK, ROBINS AFB · NOT A LEARJET · DVIDS"
FIRE = "FILE FOOTAGE · U.S. MARINE CORPS AIRCRAFT FIRE TRAINING AT NIGHT · NOT COLUMBIA · DVIDS"
C37 = "FILE FOOTAGE · U.S. AIR FORCE C-37 BUSINESS JET ON THE RUNWAY, RAMSTEIN AB · NOT A LEARJET · DVIDS"
NITE = "FILE FOOTAGE · NIGHT FLIGHT-LINE OPERATIONS · NOT COLUMBIA · DVIDS"
F1 = "NTSB AAR-10/02 · FIG. 1 · LEARJET TECHNICIAN CHECKING MAIN GEAR TIRE PRESSURE"
F2 = "NTSB AAR-10/02 · FIG. 2 · LEARJET 60 THRUST LEVERS + THRUST REVERSER (PIGGYBACK) LEVERS"
F3 = "NTSB AAR-10/02 · FIG. 3 · A LEARJET 60 WITH THRUST REVERSERS DEPLOYED (NTSB PHOTO)"
F4 = "NTSB AAR-10/02 · FIG. 4 · ENGINE N1 FROM THE CVR SOUND SPECTRUM"
F5 = "NTSB AAR-10/02 · FIG. 5 · GROUND SPEED FROM THE CVR SOUND SPECTRUM"
F6 = "NTSB AAR-10/02 · FIG. 6 · CVR COMMENTS, SPEEDS AND TIRE DEBRIS PLOTTED ON RUNWAY 11"
F7 = "NTSB AAR-10/02 · FIG. 7 · RECONSTRUCTED RIGHT OUTBOARD MAIN GEAR TIRE"
F8 = "NTSB AAR-10/02 · FIG. 8 · LEARJET 45 (LEFT) AND LEARJET 60 (RIGHT) WHEEL WELLS"
LINES = [
 # ---- cold open
 ("o1", "September nineteenth, two thousand eight. Just before midnight, at Columbia Metropolitan Airport, in South Carolina.", 0.5, 1.0, ("3d", "open_roll")),
 ("o2", "A Learjet sixty is accelerating down runway one one, on a charter flight to Van Nuys, California. Two pilots, four passengers.", 0.4, 1.0, ("3d", "open_roll")),
 ("o3", "The first officer calls, V one. The speed after which, by their training, the takeoff continues.", 0.4, 0.98, ("3d", "open_roll")),
 ("o4", "About one and a half seconds later, the cockpit voice recorder picks up a loud rumbling sound. A main landing gear tire has come apart.", 0.4, 1.0, ("3d", "tire")),
 ("o5", "The first officer says, go. Then, go, go, go. The captain asks, go? And then the takeoff is rejected.", 0.5, 0.97, ("3d", "tire")),
 ("o6", "The jet goes off the end of the runway, and through the safety area beyond it, at more than one hundred knots.", 0.8, 0.97, ("3d", "open_side")),
 ("o7", "Both pilots and two passengers were killed. Two passengers survived, with serious injuries.", 0.6, 0.97, ("card", "toll")),
 ("o8", "In this video: what the N T S B found, second by second. Four tires. A decision made after V one. And a thrust reverser system that, at the worst moment, pushed the airplane forward.", 1.2, 1.0, ("card", "toll")),
 ("n1", "One note first. The Learjet sixty is in the news again, after the crash near Greenacres, Florida, on November first, two thousand twenty-six.", 0.4, 1.0, ("card", "notthis")),
 ("n2", "This is not that case. That investigation is still open, and the N T S B has not said what caused it. Nothing in this video is an explanation of that crash.", 0.4, 1.0, ("card", "notthis")),
 ("n3", "This is a different accident, from two thousand eight, and the investigation is finished. The N T S B adopted its final report in April two thousand ten.", 1.0, 1.0, ("card", "notthis")),
 ("t1", "Last contact. Learjet sixty, November nine nine nine Lima Juliet. The rejected takeoff at Columbia.", 1.4, 0.95, ("card", "title")),
 # ---- how we know
 ("h1", "Everything in this video comes from the N T S B accident report, number A A R ten, oh two, and its cockpit voice recorder transcript.", 0.4, 1.0, ("card", "how")),
 ("h2", "This airplane had no flight data recorder. It was not required to have one, because it had fewer than ten passenger seats.", 0.4, 1.0, ("card", "how")),
 ("h3", "So the speeds you will see come from a sound spectrum study. The N T S B measured the hum of the tires rolling over the grooves cut into the runway, and the pitch of the engines, and turned those sounds into ground speed and engine speed.", 0.4, 1.0, ("photo", "fig5.png", F5)),
 ("h4", "The three D scenes are built on those numbers, over today's aerial imagery. Motion in between is interpolated. The model is a Learjet fifty-five, the type the Learjet sixty prototype was modified from.", 1.0, 1.0, ("3d", "top")),
 # ---- the airplane
 ("a1", "The Learjet sixty is a twin-engine business jet. This one, serial number sixty, three fourteen, was owned by Inter Travel and Services, and operated by Global Exec Aviation, under Part one thirty-five, the rules for on-demand charter flights.", 0.4, 1.0, ("clip", "c21a.mp4", 0.5, C21)),
 ("a2", "The type was certificated in nineteen ninety-three. But not on a new type certificate. It was approved as a changed product, added to the certificate first issued in nineteen sixty-six for the Learjet twenty-four.", 0.4, 1.0, ("clip", "c21a.mp4", 24.5, C21)),
 ("a4", "The flight that night was the crew's second of the day, a nonscheduled passenger flight from Columbia to Van Nuys.", 0.6, 1.0, ("clip", "c21a.mp4", 120.5, C21)),
 # ---- the crew
 ("p1", "The captain, who was the pilot flying, was thirty-one years old. She held an airline transport pilot certificate and had about three thousand one hundred forty hours in total.", 0.3, 1.0, ("card", "crew")),
 ("p2", "But in the Learjet sixty, she had about thirty-five hours. About eight of them as pilot in command.", 0.4, 1.0, ("card", "crew")),
 ("p3", "The first officer was fifty-two, with about eight thousand two hundred hours in total, and about three hundred in the Learjet sixty.", 0.4, 1.0, ("clip", "c21a.mp4", 56.5, C21)),
 ("p4", "Both were qualified, with no previous accidents, incidents or enforcement actions. They had flown together twice before.", 0.8, 1.0, ("clip", "c21a.mp4", 77.0, C21)),
 # ---- airport / taxi
 ("r1", "Columbia Metropolitan. Runway one one was eight thousand six hundred one feet long and one hundred fifty feet wide. Beyond its far end, a runway safety area, one thousand feet long.", 0.4, 1.0, ("3d", "top")),
 ("r3", "The crew turned the wrong way at first. The controller amended the clearance, and the jet back-taxied on runway one one and turned around on the runway for takeoff.", 0.4, 1.0, ("3d", "backtaxi")),
 ("r4", "The weather was clear. When the captain asked for a wind check, the controller gave, zero seven zero at eight, gusting fourteen.", 0.8, 1.0, ("clip", "nite.mp4", 54.0, NITE)),
 # ---- briefing
 ("b1", "At eleven fifty-one and twenty-two seconds, the captain briefed the rejected takeoff.", 0.3, 1.0, ("card", "brief")),
 ("b2", "She said they would abort for anything below eighty knots. And then, after V one and before V two, for engine failure, fire, malfunction, or loss of directional control.", 0.4, 1.0, ("card", "brief")),
 ("b3", "That is not what she had been trained to do. Her training said: after V one, the takeoff continues, unless the airplane is seriously in doubt as controllable.", 0.4, 1.0, ("card", "brief")),
 ("b4", "The N T S B concluded there was no sign her understanding of the rule was deficient. She most likely misspoke. The N T S B noted that the rejected takeoff criteria rarely change from one takeoff to the next, so a briefing like this can be recited on autopilot.", 0.4, 1.0, ("clip", "nite.mp4", 63.0, NITE)),
 ("b5", "The first officer added that they were, quote, pretty heavy. The N T S B found no evidence that weight and balance contributed.", 1.0, 1.0, ("clip", "c21a.mp4", 88.5, C21)),
 # ---- tires
 ("y1", "Now, the four main landing gear tires. This is the part of the story nobody in the cockpit could see.", 0.4, 1.0, ("clip", "tire.mp4", 8.0, TIRE)),
 ("y2", "Each tire was rated at two hundred twenty pounds per square inch. The certification standard allows an aircraft tire to lose up to five percent of its pressure per day. This model was tested at about two point two percent a day.", 0.4, 1.0, ("card", "tires")),
 ("y3", "The maintenance manual said to measure cold tire pressure before the first flight of every day. Or every ten days, on an airplane that is not flying.", 0.4, 1.0, ("card", "tires")),
 ("y4", "The tires were new in December two thousand seven and had twenty landings. In the twelve days before the accident, the airplane flew on five of them. None of the facilities that handled it serviced the tires, or were asked to.", 0.4, 1.0, ("clip", "c21a.mp4", 8.5, C21)),
 ("y5", "The operator's director of maintenance estimated that the pressures may not have been checked for about three weeks.", 0.4, 1.0, ("clip", "c21a.mp4", 112.0, C21)),
 ("y6", "And checking them is not easy. On the Learjet sixty, someone has to crouch, or lie on the ground, under the wing, to reach the valves. An underinflated tire generally cannot be detected by looking at it.", 0.8, 1.0, ("photo", "fig1.png", F1)),
 ("y7", "An underinflated tire flexes too far with every turn. Heat builds inside, and the nylon cords that give it strength can melt.", 0.8, 1.0, ("clip", "tire.mp4", 20.0, TIRE)),
 # ---- the roll
 ("l1", "The takeoff roll began normally. At eleven fifty-five and zero seconds, the first officer called, eighty knots, crosscheck.", 0.3, 1.0, ("3d", "roll_follow")),
 ("l2", "At ten and a half seconds, V one. For this takeoff, V one was about one hundred thirty-six knots indicated airspeed. Rotation speed, about one forty-five.", 0.3, 1.0, ("3d", "roll_follow")),
 ("l3", "At twelve seconds, the rumbling begins. Ground speed about one hundred thirty-eight knots. The airplane is more than two thousand five hundred feet down the runway, with about six thousand one hundred feet left.", 0.4, 1.0, ("3d", "roll_follow")),
 ("l4", "That matches where the first pieces of the right outboard tire were later found on the runway.", 0.4, 1.0, ("3d", "tire")),
 ("l5", "Skid marks and gouges show the jet veering right, across the centerline, before the captain brought it back in line with the runway.", 0.5, 1.0, ("3d", "veer")),
 ("l6", "Four tenths of a second after the rumbling starts, the first officer says, go. At thirteen seconds: go, go, go.", 0.3, 1.0, ("card", "cvr")),
 ("l7", "At fourteen seconds, the captain asks, go? The ground speed peaks around this moment, at about one hundred forty-four knots.", 0.3, 1.0, ("card", "cvr")),
 ("l8", "The N T S B found that she reduced engine power for about one second, increased it again for about one second, and then reduced it.", 0.3, 1.0, ("card", "cvr")),
 ("l9", "The first officer: no? Alright. Then he asks what that was. At seventeen seconds, the captain: I don't know. We're not goin' though.", 0.5, 1.0, ("card", "cvr")),
 ("l10", "At nineteen and a half seconds, she calls, full out. The thrust reversers deploy, the brakes are applied, and the airplane slows to about one hundred twenty-eight knots.", 0.4, 1.0, ("3d", "decel")),
 ("l11", "By then, debris shows that all four main gear tires had failed. Within about nine seconds of the first one.", 0.8, 1.0, ("photo", "fig6.png", F6)),
 # ---- sound explainer
 ("s2", "Investigators measured the spacing of the grooves in runway one one. Each time a tire crosses a groove, it makes a tiny sound. The faster the airplane, the higher the pitch.", 0.3, 1.0, ("card", "spectrum")),
 ("s4", "The engines did the same. Their fan speed held near ninety-three percent until the noise burst, then wavered, dropped, and later rose again.", 0.8, 1.0, ("photo", "fig4.png", F4)),
 # ---- the trap
 ("f1", "And that rise is the second half of this accident.", 0.4, 1.0, ("card", "trlogic")),
 ("f2", "On the Learjet sixty, the thrust reverser levers sit piggyback on top of the thrust levers. Pilots lift them to command reverse thrust.", 0.4, 1.0, ("photo", "fig2.png", F2)),
 ("f3", "The reversers only stay deployed while the system knows the airplane is on the ground. That signal comes from squat switches on the main landing gear.", 0.4, 1.0, ("photo", "fig3.png", F3)),
 ("f4", "If the system loses that signal, the reversers are designed to stow. That protects against a reverser opening in flight.", 0.4, 1.0, ("clip", "tr17.mp4", 20.5, TR17)),
 ("f5", "But here is the trap. The engine computers then switch to the forward thrust schedule, while the levers in the cockpit are still raised to full reverse. And full reverse lever travel then means high forward thrust.", 0.5, 1.0, ("card", "trlogic")),
 ("f6", "At twenty-one point six seconds, the recorder captured the nosewheel steering disconnect tone. The system had switched to air mode. The shredded tires had damaged the components and wiring in the main gear area.", 0.4, 1.0, ("3d", "fwd")),
 ("f7", "The reversers stowed. There was no warning light telling the crew that their engines were now pushing them forward. The airplane was about two thousand five hundred feet from the end of the runway, at about one hundred twenty-three knots, and it began to accelerate.", 0.4, 1.0, ("3d", "fwd")),
 ("f8", "To stop that thrust, a pilot would have had to push the reverse levers back down to stow. In the middle of a high speed stop, when maximum reverse is exactly what you want, the N T S B called that likely counterintuitive.", 0.8, 1.0, ("3d", "fwd")),
 # ---- had it happened before
 ("e1", "This failure mode was not new.", 0.4, 1.0, ("card", "history")),
 ("e3", "In nineteen ninety-eight, a Learjet sixty rejecting a takeoff at Washington Dulles lost both right main gear tires. The reversers stowed, and it went off the side of the runway, near the end.", 0.4, 1.0, ("clip", "c21r.mp4", 23.5, C37)),
 ("e4", "In two thousand one, at Troy, Alabama, a Learjet sixty hit deer on landing. A squat switch was damaged, the reversers were found stowed, and the sound study showed the engines above any reverse thrust setting.", 0.4, 1.0, ("card", "history")),
 ("e5", "After that, Learjet revised a procedure and offered a modification, which the F A A did not require. The accident airplane already had it, from the factory. The N T S B later found that Learjet's safety analysis, and the F A A's review of it, failed to effectively address uncommanded forward thrust during a rejected takeoff.", 0.8, 1.0, ("photo", "fig8.png", F8)),
 # ---- the end
 ("x1", "Back on runway one one. At twenty-eight point seven seconds, the first officer says, shut 'em off. The engine speed had climbed to about nine thousand one hundred sixty-five r p m.", 0.3, 1.0, ("3d", "overrun_side")),
 ("x2", "At thirty-two point four seconds: they're shut off, they're shut off. At thirty-six seconds, on the tower frequency: roll the equipment, we're goin' off the end.", 0.4, 1.0, ("3d", "overrun_side")),
 ("x3", "The recording ends at forty-one point one seconds.", 0.6, 0.97, ("3d", "overrun_side")),
 ("x4", "The jet crossed the one thousand foot safety area still traveling at more than one hundred knots. It struck approach lights and antennas, went down a steep slope, through the perimeter fence, across a five-lane road, and stopped against an embankment on the far side.", 0.4, 1.0, ("3d", "end_layout")),
 ("x5", "A fire broke out. All three of the airport's firefighting trucks and all four firefighters on duty arrived within five minutes of being alerted. The fire was under control about ten minutes later.", 0.6, 1.0, ("clip", "fire.mp4", 108.0, FIRE)),
 ("x6", "The two passengers who survived had been seated in the rear of the cabin. One of them remembered the captain pointing out the exits. He went straight to the emergency exit behind him, opened it, and both got out through the fire.", 0.4, 1.0, ("clip", "fire.mp4", 150.0, FIRE)),
 ("x7", "The N T S B found that the captain's passenger safety briefing contributed to the survival of those two passengers.", 1.0, 0.97, ("card", "survive")),
 # ---- the tire evidence
 ("w1", "In the lab, investigators rebuilt about eighty percent of the right outboard tire.", 0.3, 1.0, ("photo", "fig7.png", F7)),
 ("w2", "The damage ran around the entire tire, at a generally uniform distance from the rim, on both sidewalls. The nylon fibers had melted and hardened into strands as stiff as broom bristles.", 0.3, 1.0, ("photo", "fig7.png", F7)),
 ("w3", "To bend a sidewall that far, a loaded tire would need to be about thirty-six percent underinflated.", 0.3, 1.0, ("photo", "fig7.png", F7)),
 ("w4", "There was no puncture, no impact damage, and no brake lockup. Tire design and manufacture were not factors.", 0.8, 1.0, ("photo", "fig7.png", F7)),
 # ---- probable cause
 ("c1", "In April two thousand ten, the N T S B adopted its final report. Its probable cause has two parts.", 0.4, 1.0, ("card", "cause")),
 ("c2", "First, the operator's inadequate maintenance of the airplane's tires, which resulted in multiple tire failures during takeoff roll, due to severe underinflation.", 0.4, 0.97, ("card", "cause")),
 ("c3", "Second, the captain's execution of a rejected takeoff after V one, which was inconsistent with her training and standard operating procedures.", 0.6, 0.97, ("card", "cause")),
 ("c4", "Contributing: deficiencies in Learjet's design, and the F A A's certification, of the thrust reverser system, which permitted the failure of critical systems in the wheel well area to result in uncommanded forward thrust that increased the severity of the accident.", 0.3, 1.0, ("card", "contrib")),
 ("c5", "The inadequacy of the safety analysis and its review after the two thousand one accident. Inadequate industry training standards for tire failures. And the flight crew's poor crew resource management.", 0.4, 1.0, ("card", "contrib")),
 ("c6", "The board also found that the uncommanded forward thrust substantially increased the speed at which the airplane left the runway, and made the accident more severe. Whether the jet could have stopped without it, the N T S B said, cannot be determined.", 1.0, 1.0, ("card", "contrib")),
 # ---- V1 explainer
 ("v1", "Why does V one matter so much?", 0.3, 1.0, ("card", "v1")),
 ("v2", "V one is the last moment to begin a stop and still be able to stop on the remaining runway, under the conditions it was calculated for. Past it, crews are trained to fly the problem into the air, where there is time to think, and then come back to a full length runway.", 0.4, 1.0, ("card", "v1")),
 ("v3", "That is why training programs, including hers, emphasized that the pilot flying take a hand off the thrust levers at the V one call. The decision is already made.", 0.4, 1.0, ("clip", "c21a.mp4", 64.5, C21)),
 ("v4", "The N T S B also found that these pilots would have been better prepared if they had practiced tire failures on takeoff in a simulator, with realistic sound and motion. That training did not exist for them.", 0.8, 1.0, ("clip", "c21r.mp4", 9.5, C21R)),
 # ---- what changed
 ("k1", "What changed.", 0.3, 1.0, ("card", "changes")),
 ("k2", "In October two thousand eight, Learjet reminded operators that tire inflation cannot be judged by eye. In February two thousand nine, the F A A issued a safety alert on the dangers of improperly inflated tires.", 0.3, 1.0, ("clip", "c21a.mp4", 180.5, C21)),
 ("k3", "Learjet's revised flight manual made tire pressure checks a limitation: within ninety-six hours before takeoff. And it added a warning in bold: the absence of any thrust reverser lights indicates forward thrust.", 0.3, 1.0, ("card", "changes")),
 ("k4", "The N T S B asked the F A A to make the cockpit reverser levers match what the reversers are actually doing, to require tire pressure checks often enough to stay within limits, and to require tire pressure monitoring systems on all transport category airplanes.", 0.4, 1.0, ("clip", "tr17.mp4", 56.5, TR17)),
 # ---- replay
 ("z2", "Once more, the whole roll. Eighty knots. V one. The first tire. Go, go, go. Go? The reject. Full reverse, brakes, all four tires gone.", 0.4, 0.95, ("3d", "replay")),
 ("z3", "Air mode. The reversers stow. Forward thrust, with two thousand five hundred feet left.", 0.4, 0.95, ("3d", "replay")),
 ("z4", "Shut them off. The end of the runway. And then the safety area, the slope and the road.", 1.0, 0.95, ("3d", "replay")),
 # ---- close
 ("q1", "Two things failed that night, and neither of them was visible from the cockpit. The pressure inside four tires, and the logic inside a thrust reverser system.", 0.4, 1.0, ("3d", "rest_orbit")),
 ("q2", "And less than two seconds after V one came an unknown noise, likely with shaking and vibration. What followed was a rejected takeoff after V one, which the N T S B found was inconsistent with the captain's training and standard operating procedures.", 0.4, 1.0, ("3d", "rest_orbit")),
 ("q4", "This was LAST CONTACT. Every crash leaves a record. Next file soon.", 1.6, 0.97, ("card", "status")),
]
