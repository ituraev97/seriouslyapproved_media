# EPISODE 004 — UPS Flight 358 (B767-300F, N336UP) and Copa Airlines Flight 427 (B737-800, HP-1826CMP)
# taxiway collision, Miami International Airport, Saturday Nov 14, 2026, ~9:00-9:15 p.m. EST.
# Sources: FAA statement Nov 14 (faa.gov accident/incident statements); NTSB statements Nov 15 as quoted by
# Global News / AP (PBS); Copa and UPS statements; Miami-Dade Aviation Dept (Greg Chin) via Fox News / CNN;
# FAA registry N336UP; FAA airport diagram MIA (AL-257, SE-3 29 OCT-26 NOV 2026); FAA AIM 4-3-18;
# 49 CFR 830.2; NTSB Safety Recommendation letter A-12-48/-49 (Sept 4, 2012); FAA ASDE-X page;
# FAA "Nationwide Ground Stop: Questions and Answers" (Nov 15, 2026).
# (id, spoken text, pause_after, speed, visual)
# visual: ("3d", shot) | ("card", name) | ("photo", file, credit) | ("clip", file, start_s, label)
K46 = "FILE FOOTAGE · U.S. AIR FORCE KC-46A, BUILT ON THE BOEING 767 · NOT THE UPS AIRPLANE · DVIDS"
P8 = "FILE FOOTAGE · U.S. NAVY P-8A, BASED ON THE BOEING 737-800 · NOT THE COPA AIRPLANE · DVIDS"
TWR = "FILE FOOTAGE · U.S. AIR FORCE CONTROL TOWER · NOT MIAMI TOWER · DVIDS"
TWRN = "FILE FOOTAGE · AIR TRAFFIC CONTROLLERS AT NIGHT, OSAN AIR BASE · NOT MIAMI · DVIDS"
TWR2 = "FILE FOOTAGE · AIR TRAFFIC CONTROL TOWER, OSAN AIR BASE · NOT MIAMI TOWER · DVIDS"
NITE = "FILE FOOTAGE · NIGHT OPERATIONS ON A MILITARY FLIGHT LINE · NOT MIAMI · DVIDS"
DIAG = "FAA AIRPORT DIAGRAM · MIAMI INTL (AL-257) · THE INTERSECTION HAS NOT BEEN IDENTIFIED BY THE NTSB OR FAA"
LINES = [
 # ---- cold open
 ("o1", "Saturday, November fourteenth, two thousand twenty-six. A little after nine at night, at Miami International Airport.", 0.5, 1.0, ("3d", "open_wide")),
 ("o2", "Two jets are moving on the taxiways. A Copa Airlines Boeing seven thirty-seven has just landed from Panama City, and is taxiing to its gate, with one hundred seventy-two people on board.", 0.4, 1.0, ("3d", "open_wide")),
 ("o3", "A U P S Boeing seven sixty-seven freighter is taxiing out, for a departure to Bogota, Colombia.", 0.4, 1.0, ("3d", "open_wide")),
 ("o4", "According to the F A A, air traffic controllers told the U P S crew to give way to the Copa flight.", 0.5, 1.0, ("3d", "approach")),
 ("o5", "According to the N T S B, the U P S airplane did not stop. The left winglet of the Copa seven thirty-seven struck the nose of the seven sixty-seven.", 0.8, 0.97, ("3d", "contact")),
 ("o6", "Two passengers on the Copa flight had minor injuries. No one was seriously hurt. But the N T S B says the U P S airplane was substantially damaged, and it has opened an investigation.", 1.0, 1.0, ("card", "toll")),
 ("o7", "In this video: what the F A A and the N T S B have said so far, what the words in their statements mean, and why a collision between two taxiing airplanes is taken so seriously.", 0.5, 1.02, ("card", "toll")),
 ("o8", "None of this is a finding of cause. The investigation has just started, and the N T S B has not determined why the airplanes collided.", 1.3, 0.96, ("card", "title")),

 # ---- what we use
 ("r1", "A quick note on how we built this video.", 0.3, 1.0, ("card", "rules")),
  ("r3", "Recordings of the radio calls from that night are circulating online. We do not play those recordings, and we do not use them as evidence. The facts here come from the F A A's statement, from what the N T S B has said, and from the airlines and the airport.", 0.4, 1.0, ("card", "rules")),
 ("r4", "And the three-D scenes you see are illustrations. The N T S B has not published which intersection it was, or where exactly each airplane was. So the layout and positions on screen are not a reconstruction.", 1.0, 1.0, ("card", "rules")),

 # ---- the two flights
 ("f1", "Let's start with the two flights.", 0.3, 1.0, ("card", "flights")),
 ("f2", "Copa Airlines flight four twenty-seven, a Boeing seven thirty-seven eight hundred, had arrived from Panama City, Panama. Copa says there were one hundred sixty-six passengers and six crew members on board.", 0.4, 1.0, ("card", "flights")),
 ("f3", "The N T S B gives its registration as H P one eight two six C M P. That is a Panamanian registration, which means this was a foreign airline operating into the United States.", 0.4, 1.0, ("clip", "dv/910649.mp4", 37.0, P8)),
 ("f4", "The footage you are seeing is not the Copa airplane. It is a U S Navy P eight, a military airplane based on the same seven thirty-seven eight hundred design. Note the shape of the wing. On the Copa airplane, the wing ends in a winglet: a tip that turns upward.", 0.5, 1.0, ("clip", "dv/910649.mp4", 55.0, P8)),
 ("f5", "U P S flight three fifty-eight was a Boeing seven sixty-seven three hundred freighter, registration November three three six Uniform Papa. It was taxiing out for a departure to Bogota.", 0.4, 1.0, ("clip", "dv/755613.mp4", 1.0, K46)),
 ("f6", "The F A A registry lists that airplane as a Boeing seven sixty-seven, manufactured in two thousand nine, with General Electric C F six engines.", 0.4, 1.0, ("clip", "dv/755613.mp4", 19.0, K46)),
 ("f7", "Again, this is not the U P S airplane: it is a K C forty-six, an Air Force tanker built on the seven sixty-seven. U P S has not said how many crew members were on board. It said its crew was safe.", 0.6, 1.0, ("clip", "dv/755613.mp4", 186.0, K46)),

 # ---- sizes
 ("z1", "These are two very different airplanes in size.", 0.3, 1.0, ("3d", "sizes")),
 ("z2", "Boeing's published figures put the seven sixty-seven three hundred at about one hundred eighty feet long, with a wingspan of about one hundred fifty-six feet.", 0.4, 1.0, ("3d", "sizes")),
 ("z3", "The seven thirty-seven eight hundred is about one hundred thirty feet long, with a wingspan of about one hundred seventeen feet, including the winglets.", 0.4, 1.0, ("3d", "sizes")),
 ("z4", "So in this event, the outer tip of the smaller airplane's wing met the very front of the larger one. The N T S B has not published the height of the contact point, or the angle between the two airplanes.", 1.0, 1.0, ("3d", "sizes")),

 # ---- the airport
 ("a1", "Miami International is a major gateway for both passengers and cargo. According to the Miami-Dade Aviation Department, it handled more than fifty-five million passengers and nearly three and a half million tons of cargo in two thousand twenty-five.", 0.4, 1.0, ("photo", "ph/mia_diagram.png", DIAG)),
 ("a2", "This is the F A A's official airport diagram. It has four runways, and a dense network of taxiways, with many intersections between the terminal, the cargo areas and the runways.", 0.4, 1.0, ("photo", "ph/mia_diagram.png", DIAG)),
 ("a3", "The airport says the collision happened at the intersection of two taxiways. Neither the F A A nor the N T S B has said which two, so we are not marking any spot on this map.", 0.4, 1.0, ("photo", "ph/mia_diagram.png", DIAG)),
 ("a4", "One detail printed on the diagram itself: A S D E X in use. That is the F A A's Airport Surface Detection Equipment, Model X.", 0.4, 1.0, ("photo", "ph/mia_diagram_asde.png", DIAG)),
 ("a5", "The F A A describes it as a surveillance system that uses radar, multilateration and satellite technology, so controllers can track aircraft and vehicles on the airport surface. The F A A says it is particularly useful at night, or in poor weather. It was developed to help reduce runway incursions.", 0.4, 1.0, ("clip", "dv/1001638.mp4", 31.0, TWR)),
 ("a6", "The N T S B has not said what the controllers' surface displays showed that night. That will be part of what investigators look at.", 1.0, 1.0, ("clip", "dv/1011126.mp4", 280.0, TWRN)),

 # ---- context
 ("c1", "One more piece of context. The collision came one day after a very unusual day for American aviation.", 0.4, 1.0, ("card", "context")),
 ("c2", "On Friday, November thirteenth, after a technical problem at about three thirty p m eastern time, the F A A issued a nationwide ground stop.", 0.4, 1.0, ("card", "context")),
 ("c3", "According to the F A A, legacy equipment became unstable when data began flooding its telecommunications network, disrupting aircraft communications and radar feeds. Air traffic resumed at about eight fifteen that evening. The F A A says it has no indication of a cyberattack.", 0.4, 1.0, ("card", "context")),
  ("c5", "Neither the F A A nor the N T S B has linked the ground stop to what happened in Miami the next night. We mention it only because it was the backdrop to that weekend.", 1.0, 1.0, ("clip", "dv/998856.mp4", 65.0, NITE)),

 # ---- what the agencies said
 ("s1", "Now, the official statements, word by word.", 0.4, 1.0, ("card", "faa")),
 ("s2", "The F A A's statement says: the wingtip of a Copa Airlines Boeing seven thirty-seven struck the nose of a U P S Boeing seven sixty-seven while the airplanes were taxiing at Miami International Airport.", 0.4, 1.0, ("card", "faa")),
 ("s3", "Air traffic controllers had told the U P S crew to give way to the Copa flight. The Copa flight was taxiing to the gate, and the U P S flight was taxiing for departure to Bogota.", 0.4, 1.0, ("card", "faa")),
 ("s4", "The F A A gave the time as around nine p m local time. The airport later put the contact at about nine fifteen.", 0.6, 1.0, ("clip", "dv/1011126.mp4", 127.0, TWR2)),
 ("s5", "Then the N T S B. As quoted by Global News, the N T S B said U P S three fifty-eight was taxiing to the runway, and was instructed to give way to the Copa seven thirty-seven, which was taxiing to the gate.", 0.4, 1.0, ("card", "ntsb")),
 ("s6", "And then this sentence. Quote: U P S three fifty-eight did not stop, and the left winglet of C M P four twenty-seven impacted the nose of U P S three fifty-eight.", 0.6, 0.95, ("card", "ntsb")),
 ("s7", "The N T S B said there was substantial damage to the U P S airplane, and that the damage assessment of the Copa airplane had not yet been completed.", 0.4, 1.0, ("card", "ntsb")),
 ("s8", "Notice what that statement does and does not say. It describes what happened in sequence. It does not say why the U P S airplane did not stop, and it does not assign responsibility to anyone.", 1.2, 0.98, ("card", "ntsb")),

 # ---- on the ground after
 ("g1", "What happened right after the contact?", 0.3, 1.0, ("card", "after")),
 ("g2", "Copa said the contact involved the left wingtip of its seven thirty-seven, and called it a minor collision. Two passengers were treated at the scene for apparent minor injuries. All passengers got off the airplane at the terminal.", 0.4, 1.0, ("card", "after")),
 ("g3", "Miami-Dade Fire Rescue treated two people on scene, and neither needed to be taken to a hospital, according to the airport's communications director, Greg Chin.", 0.4, 1.0, ("card", "after")),
 ("g4", "He said flights were redirected to other taxiways, and airport operations were not affected.", 0.4, 1.0, ("card", "after")),
 ("g5", "U P S said its crew was safe, that it was working with the authorities, and that it could not speculate on the details. It also said the N T S B is responsible for investigating incidents like this.", 1.0, 1.0, ("clip", "dv/755613.mp4", 7.0, K46)),

 # ---- give way / taxi rules
 ("t1", "So what does it mean, when a controller tells a crew to give way?", 0.4, 1.0, ("clip", "dv/1001638.mp4", 1.0, TWR)),
 ("t2", "On a big airport at night, ground controllers sequence airplanes the way a traffic officer runs an intersection. One airplane continues. The other one waits, and lets it pass first.", 0.4, 1.0, ("clip", "dv/1001638.mp4", 16.0, TWR)),
 ("t3", "In plain terms, give way means exactly that: let the other airplane go first. The F A A has not released the exact wording of the instructions that night, or when they were given.", 0.4, 1.0, ("clip", "dv/1001638.mp4", 46.0, TWR)),
 ("t4", "There is a principle in the F A A's Aeronautical Information Manual that applies to every pilot on the airport, in both airplanes. The manual says that taxi instructions are based on known traffic and known physical airport conditions.", 0.4, 1.0, ("card", "aim")),
 ("t5", "And it says: although an A T C clearance is issued for taxiing purposes, when operating in accordance with the regulations, it is the responsibility of the pilot to avoid collision with other aircraft.", 0.5, 0.97, ("card", "aim")),
 ("t7", "On the ground, safety has layers: the controller's instructions, each crew's own lookout, and the airport's lights, signs and markings. Investigators will look at all of them, for both airplanes and for the tower. That is standard practice, and it is not a finding about anyone.", 1.0, 1.0, ("clip", "dv/1011126.mp4", 300.0, TWRN)),

 # ---- why the NTSB: accident vs incident
 ("d1", "Why is the N T S B investigating a collision at taxi speed, where no one was seriously hurt? The answer is in two definitions in federal law.", 0.4, 1.0, ("clip", "dv/971144.mp4", 1.0, K46)),
 ("d2", "Under the N T S B's rules, an aircraft accident is an occurrence, from boarding to deplaning, in which a person is killed or seriously injured, or in which the aircraft receives substantial damage.", 0.4, 1.0, ("card", "terms")),
 ("d3", "Substantial damage means damage or failure that adversely affects the structural strength, performance, or flight characteristics of the aircraft, and that would normally require major repair or replacement of the affected component.", 0.4, 1.0, ("card", "terms")),
 ("d4", "One interesting detail. The same rule lists damage that is not considered substantial, and that list includes damage to wingtips.", 0.4, 1.0, ("card", "terms")),
 ("d5", "So when the N T S B says the U P S airplane was substantially damaged, it is using a defined, legal term. Under those rules, substantial damage is one of the things that makes an event an accident, not just an incident, even though the airplanes were taxiing and no one was seriously injured.", 1.0, 1.0, ("card", "terms")),

 # ---- the wingtip problem
 ("w1", "This is not the first time a wingtip and another airplane have met on a taxiway. The N T S B has written about wingtip collisions during taxi before.", 0.4, 1.0, ("clip", "dv/755613.mp4", 25.0, K46)),
 ("w2", "In September two thousand twelve, it sent a safety recommendation letter to the F A A. It said it had investigated twelve accidents since nineteen ninety-three in which a large airplane's wingtip collided with another airplane, or an object, during taxi.", 0.4, 1.0, ("card", "letter")),
 ("w4", "The letter described three recent cases. One of them: on July fourteenth, two thousand eleven, at Boston Logan, the left winglet of a Delta seven sixty-seven three hundred struck the horizontal stabilizer of a regional jet that was waiting on a perpendicular taxiway.", 0.4, 1.0, ("card", "cases")),
 ("w5", "In April two thousand eleven, at New York's Kennedy airport, the wingtip of an Air France A three eighty struck the tail of a regional jet. And in May two thousand twelve, at Chicago O'Hare, a seven forty-seven's wingtip hit the tail of a regional jet.", 0.4, 1.0, ("card", "cases")),
 ("w6", "The N T S B's point was about visibility. On large airplanes like the seven forty-seven, seven fifty-seven, seven sixty-seven and seven seventy-seven, it wrote, the pilot cannot see the airplane's wingtips from the cockpit, unless the pilot opens the cockpit window and leans out.", 0.4, 1.0, ("3d", "wingview")),
 ("w7", "So judging the clearance of a wingtip, it said, is difficult, and relies mainly on the pilot's judgment.", 0.4, 1.0, ("3d", "wingview")),
 ("w8", "The N T S B recommended that the F A A require an anti-collision aid, such as a camera system, to help pilots judge wingtip clearance and path during taxi: on newly built large airplanes, and as a retrofit on existing ones.", 0.4, 1.0, ("card", "recs")),
 ("w9", "According to Aviation Week, in two thousand thirteen the F A A rejected the recommendation to mandate those aids.", 0.5, 1.0, ("clip", "dv/1011126.mp4", 154.0, TWR2)),
 ("w10", "An important caution. In Miami, it was the seven thirty-seven's winglet that touched the seven sixty-seven's nose. The N T S B has not said what either crew could see, or whether visibility from the cockpit played any role. The letter is background, not an explanation of this event.", 1.2, 0.97, ("3d", "winglet")),

 # ---- replay
 ("x1", "Let's put the sequence the agencies have described in one place.", 0.4, 1.0, ("card", "timeline")),
 ("x2", "Copa four twenty-seven lands after a flight from Panama City, and taxis toward its gate. U P S three fifty-eight taxis toward the runway for a departure to Bogota.", 0.4, 1.0, ("card", "timeline")),
 ("x3", "Air traffic control instructs U P S three fifty-eight to give way to the Copa flight.", 0.4, 1.0, ("card", "timeline")),
 ("x4", "According to the N T S B, the U P S airplane does not stop, and the Copa airplane's left winglet strikes the U P S airplane's nose. The F A A puts the time at around nine p m. The airport says it happened at the intersection of two taxiways, at about nine fifteen.", 0.4, 1.0, ("card", "timeline")),
 ("x5", "Two people treated for minor injuries. Substantial damage to the U P S airplane. The Copa airplane's damage still being assessed.", 0.6, 1.0, ("3d", "replay")),
 ("x6", "Everything else, for now, is a question.", 1.0, 0.97, ("3d", "replay")),

 # ---- what investigators will look at
 ("i1", "What will investigators look at? The N T S B has not published a plan for this case, but in ground collisions the record usually includes a few standard pieces.", 0.4, 1.0, ("clip", "dv/998856.mp4", 105.0, NITE)),
 ("i2", "The recorded radio communications between the tower and both crews. The airport's surface surveillance data, showing where each airplane was, second by second. The cockpit voice recorders and flight data recorders, if their data from that period was preserved.", 0.4, 1.0, ("clip", "dv/998856.mp4", 121.0, NITE)),
 ("i3", "Interviews with both crews and the controllers. The lighting, signs and markings at the intersection. And the damage marks themselves, which can show the angle of contact.", 0.4, 1.0, ("clip", "dv/998856.mp4", 137.0, NITE)),
 ("i4", "As of this video, the N T S B has not said which of these it has collected, or what any of them show.", 1.0, 1.0, ("card", "status_mid")),

 # ---- Miami context
 ("m1", "This is also not the first time this year that Miami International has been at the center of an N T S B investigation.", 0.4, 1.0, ("clip", "dv/755613.mp4", 199.0, K46)),
 ("m2", "On September sixth, a Boeing seven sixty-seven freighter operated as twenty-one Air flight seventy-five ninety-eight overran a runway at Miami, crossed a public road and struck two vehicles. Five people on the ground were killed.", 0.4, 1.0, ("card", "miami")),
 ("m3", "That is a separate event, with its own ongoing investigation. We covered it in an earlier video. The two events share only the airport, and the type of one of the jets.", 1.0, 1.0, ("card", "miami")),

 # ---- open questions
 ("q1", "So, here is where the facts end, and the questions begin.", 0.5, 0.98, ("card", "open")),
 ("q2", "When exactly was the give way instruction issued, and what was said in reply?", 0.5, 1.0, ("card", "open")),
 ("q3", "Why did the U P S airplane not stop before the Copa airplane passed?", 0.5, 1.0, ("card", "open")),
 ("q4", "How fast was each airplane moving at the moment of contact?", 0.5, 1.0, ("card", "open")),
 ("q5", "What did the tower's surface surveillance show, and was there any alert?", 0.5, 1.0, ("card", "open")),
 ("q6", "And how badly was the Copa airplane's wing damaged?", 0.5, 1.0, ("card", "open")),
 ("q7", "Each of these is a question, not an answer. The N T S B's preliminary report should begin to fill in some of the facts.", 1.2, 0.98, ("card", "open")),

 # ---- what's next
 ("n1", "What happens next? The N T S B said it expects to release a preliminary report within thirty days. It will lay out facts, without analysis, and without a cause.", 0.4, 1.0, ("clip", "dv/1011126.mp4", 316.0, TWRN)),
 ("n2", "The final report, with a probable cause, typically comes twelve to twenty-four months after an accident.", 0.4, 1.0, ("card", "status")),
 ("n3", "When the preliminary report comes out, we will go through it here, line by line, and correct anything in this video that turns out to be different.", 0.5, 1.0, ("card", "status")),
 ("n4", "One hundred seventy-two people were on the Copa flight that night, and the U P S crew. Everyone walked away. The goal of the investigation is to understand why two airliners ended up in the same place at the same time, so that it does not happen again.", 0.6, 0.97, ("card", "status")),
 ("n5", "This is Last Contact. Every crash leaves a record.", 1.5, 0.95, ("card", "status")),
]
