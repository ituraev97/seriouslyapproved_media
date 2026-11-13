# SERIOUSLY APPROVED · FILE 013 · THE SHELF — "8 Wearable Chairs, Desks and Tents That Got Real Patents"
# Long video, 1920x1080. Countdown 8 -> 1. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, date):
    return dict(num=num, hook=title, side=f"{num} · {date}")

PAD = P("US 3,062,580", "A CUSHION|ON YOUR [BELT]", "1962")
CANE = P("US 159,898", "A CANE THAT|IS A [STOOL]", "1875")
RUG = P("US 536,383", "A RUG YOU|[SLEEP] IN", "1895")
COAT = P("US 1,252,628", "A RUG THAT|IS A [COAT]", "1918")
HARN = P("US 2,656,875", "A STOOL ON|A [HARNESS]", "1953")
TENT = P("US 33,752", "AN OVERCOAT|THAT IS A [TENT]", "1861")
DESK = P("US 4,715,293", "A DESK YOU|[WEAR]", "1987")
STOOL = P("US 5,927,797", "A CHAIR|YOU [WEAR]", "1999")

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"WEARABILITY RANK · No. {n} OF 8", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="8 THINGS YOU|CAN [WEAR]", side="FILE 013 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 013")

Q_HORSE = "If the horse is moving the farrier vertically for more than nine inches, the horse is most likely out of control"
Q_UNNEC = "further description is believed to be unnecessary."

LINES = [
 # ---------- cold open ----------
 ("This is a chair you wear. It is strapped to your waist. It has one leg. And it is a real United States patent.", fig(STOOL, "stool6", "6", calls=[["THE SEAT", 260, 198, 130, -60], ["ONE LEG", 285, 360, 120, 40]]), "slow"),
 ("Inside the leg, a spring keeps the foot on the ground, even when you move.", fig(STOOL, "stool1", "1", calls=[["THE SPRING", 238, 690, 140, 30]]), "calm"),
 ("It was approved. Nineteen ninety-nine.", stamp(STOOL, "PORTABLE|WORK STOOL", "AUG. 6, 1998", "JULY 27, 1999"), "punch"),
 ("Today, eight wearable chairs, desks and tents that got real patents. A cushion on your belt. A desk on your shoulders. A coat that turns into a tent. From eighteen sixty-one to nineteen ninety-nine. Real drawings, real quotes, ranked by how much furniture you are wearing.", dict(g="title", kicker="THE SHELF · FILE 013", title="Furniture|You Can Wear", lines=["Real patents. Ranked.", "All approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- 8 · belt attached seat pad ----------
 ("Number eight. The cushion that follows you.", chap(8, PAD, "Belt Attached|Seat Pad", ["US 3,062,580", "Filed 1960 · Issued 1962"]), "calm"),
 ("This is a foam cushion in a waterproof cover. It clips onto your belt.", fig(PAD, "pad12", "1, 2", calls=[["THE CUSHION", 132, 194, 120, 60], ["THE BELT", 651, 300, 90, -110]]), "calm"),
 ("It was made for people who sit outside for a long time. Hunting, fishing, skiing, or watching a game.", fig(PAD, "pad12", "2", draw=False, calls=[["UNFOLDED", 651, 510, -200, 80]]), "calm"),
 ("The cover is waterproof vinyl, so a wet seat or damp ground stays on the outside of you.", fig(PAD, "pad3", "3", calls=[["WATERPROOF COVER", 485, 254, -230, 90]]), "calm"),
 ("And its main job is not to be forgotten. So that it cannot become lost if a person leaves a seat without thinking of the seat pad.", quote(PAD, "so that it cannot become lost if a person leaves a seat without thinking of the seat pad.", "without thinking of the seat pad", "US 3,062,580 · description"), "calm"),
 ("When you stand up, you fold it in three. An elastic strap snaps around it, and it rides at your waist.", fig(PAD, "pad3", "3", calls=[["THE CLIP", 52, 42, 120, 20], ["THE PAD", 485, 254, -60, 110]]), "calm"),
 ("Folded, it also fits in a suitcase, a bag, a car compartment, or a tackle box.", fig(PAD, "pad3", "3", draw=False, calls=[["SAME PAD", 485, 254, -60, 110]]), "calm"),
 ("For everyone. It is easy to be worn by men, women, or children as desired.", quote(PAD, "easy to be worn by men, women, or children as desired.", "men, women, or children", "US 3,062,580 · description"), "calm"),
 ("The strap can even be elastic, in case the pad becomes entangled. And it comes in any suitable color.", fig(PAD, "pad12", "1", draw=False, calls=[["THE STRAP", 132, 194, 120, 60]]), "calm"),
 ("A pillow with a leash. Approved, November nineteen sixty-two.", stamp(PAD, "BELT ATTACHED|SEAT PAD", "JUNE 9, 1960", "NOV. 6, 1962", at=1.6), "slow"),

 # ---------- 7 · camp-stool and cane ----------
 ("Number seven. The walking stick with a secret.", chap(7, CANE, "Camp-Stool|and Cane", ["US 159,898", "Filed 1874 · Issued 1875"]), "calm"),
 ("Eighteen seventy-five. Here is a folding stool with three legs. One leg is longer than the others, and it becomes the back of the seat.", fig(CANE, "cane1", "1", calls=[["THE SEAT", 130, 250, 120, -80], ["THE BACK", 300, 60, 130, 20]]), "calm"),
 ("The goal, in the patent's own words: to make a campstool the legs of which when folded will form a cane or walking-stick.", quote(CANE, "The object of my invention is to make a campstool the legs of which when folded will form a cane or walking-stick.", "a cane or walking-stick", "US 159,898 · description"), "calm"),
 ("Fold the three legs together, and they make one round stick.", fig(CANE, "cane1", "2, 3", draw=False, calls=[["THE CANE", 560, 600, -150, 60], ["CROSS SECTION", 150, 1035, 130, -40]]), "calm"),
 ("The long leg is shaped like a wedge, so it slides between the other two. Little buttons and pins fit into a groove in the long leg.", fig(CANE, "cane1", "3", draw=False, vb="0 850 400 368", calls=[["THE WEDGE", 150, 1035, 130, -40]]), "calm"),
 ("The seat itself is two leather straps and a stiff piece of wood. You pull it off and roll it up.", fig(CANE, "cane1", "1", draw=False, calls=[["STRAPS AND WOOD", 130, 250, 140, 60]]), "calm"),
 ("And then: The whole seat may thus be conveniently carried in the pocket.", quote(CANE, "The whole seat may thus be conveniently carried in the pocket", "carried in the pocket", "US 159,898 · description"), "calm"),
 ("Does it hold? When used as a chair, the patent says, the stiff front piece will render the device very secure and comfortable.", quote(CANE, "will render the device very secure and comfortable.", "very secure and comfortable", "US 159,898 · description"), "calm"),
 ("A chair. In your pocket. And in your hand. Approved, February eighteen seventy-five.", stamp(CANE, "CAMP-STOOL|AND CANE", "DEC. 19, 1874", "FEB. 16, 1875", at=1.8), "slow"),

 # ---------- 6 · steamer-rug ----------
 ("Number six. The blanket with three careers.", chap(6, RUG, "Steamer-|Rug", ["US 536,383", "Filed 1894 · Issued 1895"]), "calm"),
 ("Eighteen ninety-five. This is a long bag of felted material, woven in one tube, with a slit down the front.", fig(RUG, "rug12", "1, 2", calls=[["THE SLIT", 190, 185, 120, 60]]), "calm"),
 ("Job one. Close the slit and throw it over your lap. It is a steamer rug.", fig(RUG, "rug12", "1", draw=False, calls=[["THE RUG", 190, 450, 130, 40]]), "calm"),
 ("Job two. Climb inside. Button the top, and the fabric folds into little capes over your chest.", quote(RUG, "arranging the fabric to form simulated capes", "simulated capes", "US 536,383 · description"), "calm"),
 ("To get in, you throw back two flaps at the top. A diagonal row of buttons takes it in at the waist, for people of different sizes.", fig(RUG, "rug12", "1", draw=False, calls=[["THE FLAPS", 190, 120, 120, -40]]), "calm"),
 ("Here it is in use as a sleeping-bag by a person in a steamerchair.", fig(RUG, "rug5", "5", calls=[["THE CAPES", 360, 210, 100, -90], ["THE BAG", 40, 287, 110, 110]]), "calm"),
 ("Note the hat. It has a pompom.", fig(RUG, "rug5", "5", draw=False, vb="520 0 281 200", calls=[["THE POMPOM", 657, 30, -120, 60]]), "calm"),
 ("Job three. Put your luggage in the bottom, roll it up, and strap it. Now it is a suitcase.", fig(RUG, "rug4", "4", calls=[["THE STRAP", 150, 60, 110, -30], ["YOUR LUGGAGE", 270, 150, -160, 110]]), "calm"),
 ("The buttons are little disks with a stud. But the patent says ordinary buttons would do just as well.", fig(RUG, "rug12", "2", draw=False, calls=[["THE BUTTONS", 525, 110, -170, 90]]), "calm"),
 ("A rug, a bed and a bag. Approved, March eighteen ninety-five.", stamp(RUG, "STEAMER-|RUG", "MAR. 31, 1894", "MAR. 26, 1895", at=1.6), "slow"),

 # ---------- 5 · coat-rug ----------
 ("Number five. One rectangle. Many outfits.", chap(5, COAT, "Coat-|Rug", ["US 1,252,628", "Filed 1914 · Issued 1918"]), "calm"),
 ("This patent came from an inventor in England. It starts as a single piece of preferably waterproofed material. Flat, it is a traveling rug or a ground sheet.", fig(COAT, "coat1", "1", calls=[["HEAD HOLE", 360, 290, 130, 80], ["SLEEVE SLITS", 225, 110, 120, -60]]), "calm"),
 ("Put your head through the hole in the middle, and button the slits around your arms. Now it has sleeves.", fig(COAT, "coat2", "2", calls=[["THE HOOD", 263, 58, 120, -20], ["A SLEEVE", 63, 240, 60, 90]]), "calm"),
 ("The hood will effectually protect the head neck and throat of the wearer in the most inclement weather.", quote(COAT, "will effectually protect the head neck and throat of the wearer in the most inclement weather.", "the most inclement weather", "US 1,252,628 · description"), "calm"),
 ("Gather the extra cloth at the back, add a belt, and it is a coat for walking.", fig(COAT, "coat3", "3", calls=[["THE BELT", 140, 340, 120, 40]]), "calm"),
 ("Hooks and eyes keep the wind from rearranging the skirt. Leave it loose instead, and it is a cloak for riding, or for cycling.", fig(COAT, "coat3", "3", draw=False, calls=[["THE SKIRT", 170, 560, 120, 40]]), "calm"),
 ("Put two of them together on poles, and it is a tent. With someone inside.", fig(COAT, "coat6", "6", calls=[["THE TENT", 310, 225, -60, -110], ["SOMEONE", 655, 310, 30, 120]]), "calm"),
 ("And Figure seven is a lady's cloak or wrap. It works the same way as the others. So further description is deemed unnecessary.", fig(COAT, "coat7", "7", calls=[["THE CLOAK", 150, 400, 110, 40]]), "calm"),
 ("Its intended customers: troops in the field, travelers, motorists, cyclists or tourists.", fig(COAT, "coat2", "2", draw=False, calls=[["THE COAT-RUG", 263, 400, 130, 40]]), "calm"),
 ("A rug you can wear to dinner. Approved, January nineteen eighteen.", stamp(COAT, "COAT-|RUG", "NOV. 3, 1914", "JAN. 8, 1918", at=1.6), "slow"),

 # ---------- 4 · stool on a harness ----------
 ("Number four. The stool that wears you.", chap(4, HARN, "Stool", ["US 2,656,875", "Filed 1951 · Issued 1953"]), "calm"),
 ("Nineteen fifty-three. Two straps go around your thighs. Two more cross over your back and your chest. And at the bottom, a seat with one leg.", fig(HARN, "harn1", "1", calls=[["CROSSED STRAPS", 343, 380, 140, -60], ["THE STOOL", 98, 1043, 120, -80], ["LEG STRAPS", 327, 1120, 130, 60]]), "calm"),
 ("Its purpose: so that the stool will at all times be carried in such a position that the person may sit upon the same.", quote(HARN, "so that the stool will at all times be carried in such a position that the person may sit upon the same.", "at all times", "US 2,656,875 · description"), "calm"),
 ("Who needs that? It is particularly useful for milkers, auto mechanics, and in the performance of many other tasks.", quote(HARN, "particularly useful for milkers, auto mechanics, and in the performance of many other tasks", "milkers, auto mechanics", "US 2,656,875 · description"), "calm"),
 ("The point is to leave your hands free for other work. The stool simply comes along.", fig(HARN, "harn1", "1", draw=False, calls=[["THE STOOL", 98, 1043, 120, -80]]), "calm"),
 ("The straps cross in front and behind, so they don't slip off your shoulders. No belt needed.", fig(HARN, "harn1", "1", draw=False, calls=[["NO BELT", 343, 640, 140, 40]]), "calm"),
 ("Buckles everywhere. One adjustment fits your height. Another fits the size of your thigh. The straps can be leather, plastics, or fabric.", fig(HARN, "harn1", "1", draw=False, calls=[["THE BUCKLES", 327, 1120, 130, 60]]), "calm"),
 ("So that the wearer has substantially unrestricted freedom of action.", quote(HARN, "so that the wearer has substantially unrestricted freedom of action.", "unrestricted freedom", "US 2,656,875 · description"), "calm"),
 ("And then the patent simply stops explaining. Since, from the foregoing, the construction and advantage of this stool are readily apparent, further description is believed to be unnecessary.", quote(HARN, Q_UNNEC, "believed to be unnecessary", "US 2,656,875 · description"), "calm"),
 ("A stool. With suspenders. Approved, October nineteen fifty-three.", stamp(HARN, "STOOL", "JUNE 6, 1951", "OCT. 27, 1953", at=1.6), "slow"),

 # ---------- 3 · convertible overcoat and tent ----------
 ("Number three. The coat you can sleep under.", chap(3, TENT, "Convertible|Overcoat and Tent", ["US 33,752", "Issued 1861"]), "calm"),
 ("Eighteen sixty-one. A new and useful Combination of a Portable Tent, Overcoat, and Cape.", quote(TENT, "a new and useful Combination of a Portable Tent, Overcoat, and Cape", "Portable Tent, Overcoat, and Cape", "US 33,752 · description"), "calm"),
 ("It was designed for military purposes. A soldier's coat that is also his house.", fig(TENT, "coat33", "3", calls=[["THE COAT", 80, 166, 90, 60]]), "calm"),
 ("First, the overcoat. It is formed of a piece of india-rubber cloth or other waterproof fabric which is light and durable. Straps go over the shoulders.", fig(TENT, "coat33", "3", calls=[["THE STRAPS", 80, 166, 90, 60]]), "calm"),
 ("The coat is nearly a square of cloth. Buttons on one side. Armholes on the other.", fig(TENT, "coat33", "3", draw=False, calls=[["THE ARMHOLES", 40, 200, 100, 40]]), "calm"),
 ("Add the cape on top, buttoned around the neck.", fig(TENT, "cape4", "4", calls=[["THE CAPE", 122, 207, 90, 60]]), "calm"),
 ("Now take it all off. Prop the collar of the coat up on a pole and a cross piece, stretch the straps, and peg them to the ground.", fig(TENT, "tent1", "1", calls=[["THE POLE", 68, 110, 100, -60], ["THE COAT", 340, 40, 100, 70]]), "calm"),
 ("The coat is the roof. The cape buttons on at the top. And a double part the patent calls the blanket or bed buttons to the bottom.", fig(TENT, "tent1", "1", draw=False, calls=[["THE BED", 620, 140, 80, 80]]), "calm"),
 ("Two more straps on the bed are pegged out, each on its own little prop. And the inventor admits: I am aware that portable tents have been constructed to cover a single man or soldier.", quote(TENT, "I am aware that portable tents have been constructed to cover a single man or soldier", "I am aware", "US 33,752 · description"), "calm"),
 ("Then everything folds up. It may be compactly folded and packed in or on the knapsack. The weight of the invention, about six pounds.", quote(TENT, "may be compactly folded and packed in or on the knapsack", "packed in or on the knapsack", "US 33,752 · description"), "calm"),
 ("A house you can button. Approved, November eighteen sixty-one.", stamp(TENT, "OVERCOAT|AND TENT", "NOT LISTED", "NOV. 19, 1861", at=1.6), "slow"),

 # ---------- 2 · body-supported instrument desk ----------
 ("Number two. The office you carry on your shoulders.", chap(2, DESK, "Body-Supported|Instrument Desk", ["US 4,715,293", "Filed 1986 · Issued 1987"]), "calm"),
 ("Nineteen eighty-seven. A tube frame hangs from padded straps on your shoulders. In front of you, a table. On the table, a computer.", fig(DESK, "desk1", "1", calls=[["THE STRAPS", 155, 225, -120, -40], ["THE COMPUTER", 155, 560, 140, 40]]), "calm"),
 ("The patent calls it a hand operated instrument platform retained over the shoulders of ones body.", quote(DESK, "a hand operated instrument platform retained over the shoulders of ones body", "over the shoulders", "US 4,715,293 · description"), "calm"),
 ("The shoulder straps are padded, and the hard frame does not touch your shoulders at all.", fig(DESK, "desk1", "1", draw=False, calls=[["PADDED STRAPS", 155, 225, -120, -40]]), "calm"),
 ("It is for places where conventional tables, desks and fixed workplaces are unavailable.", quote(DESK, "where conventional tables, desks and fixed workplaces are unavailable.", "unavailable", "US 4,715,293 · description"), "calm"),
 ("It lists what earlier body-worn platforms carried. Cameras, tree boring drills, food, writing materials and the like.", quote(DESK, "cameras, tree boring drills, food, writing materials and the like.", "tree boring drills", "US 4,715,293 · description"), "calm"),
 ("This one was for portable computers, inventory scanners, calculators and field surveying instruments.", fig(DESK, "desk1", "1", draw=False, calls=[["THE INSTRUMENT", 155, 560, 140, 40]]), "calm"),
 ("Because putting a computer down outside is risky. Attempting to place the instrument on a stationary surface while in the field creates a potentially hazardous situation.", quote(DESK, "Attempting to place the instrument on a stationary surface while in the field creates a potentially hazardous situation.", "potentially hazardous situation", "US 4,715,293 · description"), "calm"),
 ("Here is the frame on its own. The table top can be solid, or soft woven fabric stretched across the frame. It tilts, and folds up when you are done.", fig(DESK, "desk2", "2", calls=[["THE TABLE TOP", 456, 565, 110, 70], ["SHOULDER LOOPS", 316, 113, 130, -40]]), "calm"),
 ("A fabric top lets the computer nest itself in the middle. In one version, spring-loaded buttons fit the frame to your height and shoulder width. The tube is preferably aluminum.", fig(DESK, "desk3", "3", draw=False, calls=[["ADJUSTABLE FRAME", 300, 300, 140, -40]]), "calm"),
 ("And one of its objects was comfort. An important object of the invention is the comfort in which the table may be worn.", quote(DESK, "An important object of the invention is the comfort in which the table may be worn.", "the table may be worn", "US 4,715,293 · description"), "calm"),
 ("Note the hard hat. This desk goes to work.", fig(DESK, "desk3", "3", calls=[["THE HARD HAT", 240, 52, 140, 20]]), "calm"),
 ("A laptop, before laptops sat on laps. Approved, December nineteen eighty-seven.", stamp(DESK, "INSTRUMENT|DESK", "DEC. 9, 1986", "DEC. 29, 1987", at=1.8), "slow"),

 # ---------- 1 · portable work stool ----------
 ("And number one. The chair you wear, all day.", chap(1, STOOL, "Portable|Work Stool", ["US 5,927,797", "Filed 1998 · Issued 1999"]), "calm"),
 ("It was made for farriers, the people who put shoes on horses. Shoeing a horse typically takes about one hour. Crouching. Holding a hoof.", quote(STOOL, "Shoeing a horse typically takes about one hour", "about one hour", "US 5,927,797 · description"), "calm"),
 ("Normally, the farrier crouches with no support and grips the horse's leg between his own legs. The patent says it could also help with field work, milking, working on vehicles.", quote(STOOL, "field work, milking, working on vehicles", "milking", "US 5,927,797 · description"), "calm"),
 ("So the seat is strapped to your waist. When you want to sit, you pull a front strap, and the seat comes between your legs.", fig(STOOL, "stool5", "5", calls=[["THE BELT", 279, 95, 110, -50], ["THE SEAT", 279, 317, 120, 60], ["FRONT STRAP", 51, 673, 130, 20]]), "calm"),
 ("The one leg telescopes. Pins set the height. And a coil spring in the middle keeps the foot down on the ground.", fig(STOOL, "stool1", "1", calls=[["HEIGHT PINS", 230, 440, 140, -40], ["THE SPRING", 238, 690, 140, 30], ["THE FOOT", 211, 1123, 140, -20]]), "calm"),
 ("When you stand back up, the spring pushes the leg back out, so the stool stays right under you.", fig(STOOL, "stool6", "6", draw=False, calls=[["STAYS UNDER YOU", 285, 360, 120, 40]]), "calm"),
 ("For horse shoeing, the whole stool is about twenty-nine to thirty-six inches long. The height changes about one inch at a time.", fig(STOOL, "stool1", "1", draw=False, calls=[["29 TO 36 INCHES", 230, 440, 140, -40]]), "calm"),
 ("The spring was chosen for a person weighing between about one hundred five and two hundred forty-five pounds.", quote(STOOL, "a person weighing between about 105 and 245 pounds", "105 and 245 pounds", "US 5,927,797 · description"), "calm"),
 ("Because the horse moves. And the spring lets the leg follow the farrier up and down, several inches either way.", fig(STOOL, "stool6", "6", calls=[["UP AND DOWN", 285, 360, 120, 30]]), "calm"),
 ("Beyond that, the patent has advice. If the horse is moving the farrier vertically for more than nine inches, the horse is most likely out of control.", quote(STOOL, Q_HORSE, "most likely out of control", "US 5,927,797 · description"), "calm"),
 ("And the farrier had better move away from the horse.", quote(STOOL, "and the farrier had better move away from the horse.", "had better move away", "US 5,927,797 · description"), "slow"),
 ("A chair with one leg and a seat belt. Approved, July nineteen ninety-nine.", stamp(STOOL, "PORTABLE|WORK STOOL", "AUG. 6, 1998", "JULY 27, 1999", big=True, at=1.6), "slow"),

 # ---------- close ----------
 ("So that is the ranking. But which wearable patent is the most approved?", dict(g="title", kicker="THIS SHELF'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the stool on a harness. Because it is the patent that most politely decided it had explained enough.", quote(HARN, Q_UNNEC, "believed to be unnecessary", "US 2,656,875 · description", typed=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["3,062,580 · 159,898 · 536,383", "1,252,628 · 2,656,875 · 33,752", "4,715,293 · 5,927,797"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
