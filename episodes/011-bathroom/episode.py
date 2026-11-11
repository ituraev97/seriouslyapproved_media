# SERIOUSLY APPROVED · FILE 011 · THE SHELF — "10 Weird Bathroom Inventions That Got Real Patents"
# Long video, 1920x1080. Countdown 10 -> 1. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, date):
    return dict(num=num, hook=title, side=f"{num} · {date}")

RACK = P("US 2,302,806", "A READING DESK|FOR YOUR [BATH]", "1942")
TOOTH = P("US 2,528,006", "THE MUSICAL|[TOOTHBRUSH] HOLDER", "1950")
TABLE = P("US 4,825,779", "A TABLE FOR|THE [TOILET]", "1989")
PORTA = P("US 428,252", "THE PEDAL|[SHOWER] TENT", "1890")
DRIER = P("US 3,128,161", "GOODBYE,|[TOWELS]", "1964")
HAIR = P("US 3,732,580", "THE HAIR WASHING|[MACHINE]", "1973")
LID = P("US 5,926,099", "THE TOILET LID|THAT [SINGS]", "1999")
SEAT = P("US 4,790,036", "THE SPINNING|[TOILET SEAT]", "1988")
ROCK = P("US 1,067,898", "THE ROCKING|[BATHTUB]", "1913")
AQUA = P("US 5,983,411", "THE TOILET TANK|[AQUARIUM]", "1999")

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"WEIRDNESS RANK · No. {n} OF 10", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="10 WEIRD|[BATHROOM] PATENTS", side="FILE 011 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 011")

Q_PURPOSE = "an apparatus primarily developed for the purpose of housing aquatic creatures"
Q_THRONE = 'The toilet seat can more rightly be called "the throne" if certain conditions are met'

LINES = [
 # ---------- cold open ----------
 ("This is a toilet. The front of the tank is see-through. And there are fish in it. It is a real United States patent.", fig(AQUA, "aquarium1", "1", calls=[["THE FISH TANK", 562, 538, 120, 80]]), "slow"),
 ("Its purpose, in its own words: an apparatus primarily developed for the purpose of housing aquatic creatures.", quote(AQUA, Q_PURPOSE, "housing aquatic creatures", "US 5,983,411 · description"), "calm"),
 ("It was approved. Nineteen ninety-nine.", stamp(AQUA, "TOILET TANK|AQUARIUM", "AUG. 6, 1998", "NOV. 16, 1999"), "punch"),
 ("Today, ten weird bathroom inventions that got real patents. Bathtubs, toilets, towels, toothbrushes, and one machine that washes your hair for you. From eighteen ninety to nineteen ninety-nine. Real drawings, real quotes, counted down, in our opinion, from weird to weirdest.", dict(g="title", kicker="THE SHELF · FILE 011", title="Weird Bathroom|Inventions", lines=["Real patents. Ranked.", "All approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- 10 · towel rack and book holder ----------
 ("Number ten. A towel rack with a second job.", chap(10, RACK, "Bathtub|Book Rack", ["US 2,302,806", "Filed 1941 · Issued 1942"]), "calm"),
 ("This sticks to the inside wall of the bathtub with suction cups. Most of the time, it holds your towel.", fig(RACK, "rack1", "1", calls=[["SUCTION CUPS", 85, 360, 60, 90], ["THE TOWEL", 400, 393, 120, 70]]), "calm"),
 ("But it has a second job. It holds a book in convenient position to permit reading thereof while bathing.", quote(RACK, "in convenient position to permit reading thereof while bathing.", "reading thereof while bathing", "US 2,302,806 · description"), "calm"),
 ("To read, you unstick one end, swing the whole thing across the tub, and stick it to the other side.", fig(RACK, "rack2", "4", calls=[["THE PIVOT", 77, 205, 80, 70], ["SUCTION CUP", 20, 200, 40, -110]]), "calm"),
 ("The book rests on a ledge and leans on the rack. A springy page holder keeps it open, with a little knob for turning pages.", fig(RACK, "rack1", "1", draw=False, calls=[["THE BOOK FRAME", 550, 280, -190, 90], ["PAGE HOLDER", 450, 216, -60, -110]]), "calm"),
 ("All so that he or she can read said book while taking an ablution.", quote(RACK, "so that he or she can read said book while taking an ablution.", "taking an ablution", "US 2,302,806 · description"), "calm"),
 ("And when you are finished, it is placed in a cupboard or other convenient place until it is again desired to use the same.", quote(RACK, "placed in a cupboard or other convenient place until it is again desired to use the same.", "again desired", "US 2,302,806 · description"), "calm"),
 ("A library. Over your bath. Approved, November nineteen forty-two.", stamp(RACK, "TOWEL RACK AND|BOOK HOLDER", "DEC. 16, 1941", "NOV. 24, 1942", at=1.6), "slow"),

 # ---------- 9 · musical toothbrush holder ----------
 ("Number nine. The toothbrush holder that plays music.", chap(9, TOOTH, "Musical|Toothbrush Holder", ["US 2,528,006", "Filed 1949 · Issued 1950"]), "calm"),
 ("It hangs on the wall like a little house. And inside the house is a music box.", fig(TOOTH, "tooth1", "1", calls=[["THE MUSIC BOX", 220, 365, 140, 80], ["THE TOOTHBRUSH", 115, 60, 120, -40]]), "calm"),
 ("A standard one. Known to the trade as a Swiss movement, or music box unit.", quote(TOOTH, "known to the trade as a Swiss movement, or music box unit", "Swiss movement", "US 2,528,006 · description"), "calm"),
 ("Each toothbrush handle presses down a flat spring. While both brushes are home, a little finger blocks the spinning governor of the music box.", fig(TOOTH, "tooth2", "2", calls=[["THE SPRING", 165, 320, 120, 60]]), "calm"),
 ("Pull a toothbrush out, and the music producing unit will operate to produce a musical tune.", quote(TOOTH, "the music producing unit will operate to produce a musical tune.", "a musical tune", "US 2,528,006 · description"), "calm"),
 ("And there is only one way to make it stop. The operation will stop when both tooth brushes are nested in both pockets.", quote(TOOTH, "The operation will stop when both tooth brushes are nested in both pockets.", "both tooth brushes", "US 2,528,006 · description"), "calm"),
 ("You wind it up with a pull cord. The cord has a tassel.", fig(TOOTH, "tooth1", "1", draw=False, calls=[["THE TASSEL", 200, 600, 130, -30]]), "calm"),
 ("Brushing your teeth, with a soundtrack. Approved, October nineteen fifty.", stamp(TOOTH, "MUSICAL|TOOTHBRUSH HOLDER", "DEC. 8, 1949", "OCT. 31, 1950", at=1.8), "slow"),

 # ---------- 8 · table for toilet ----------
 ("Number eight. Furniture for one very specific room.", chap(8, TABLE, "Table for|Toilet", ["US 4,825,779", "Filed 1987 · Issued 1989"]), "calm"),
 ("It opens with a bold idea. The toilet seat can more rightly be called the throne, if certain conditions are met.", quote(TABLE, Q_THRONE, "the throne", "US 4,825,779 · description"), "calm"),
 ("One of the conditions. A supply of reading material from which a selection can be made is usually welcome.", quote(TABLE, "A supply of reading material from which a selection can be made is usually welcome", "usually welcome", "US 4,825,779 · description"), "calm"),
 ("So here is the table. It stands in front of the toilet. The top slopes toward you, at an angle of at least fifteen degrees.", fig(TABLE, "table1", "1", calls=[["READING MATERIAL", 330, 150, 140, -60]]), "calm"),
 ("A ledge along the low edge keeps the magazine from sliding off. And between the front legs, a roll of toilet paper on a spindle.", fig(TABLE, "table1", "1", draw=False, calls=[["THE LEDGE", 470, 208, 120, 40], ["TOILET PAPER", 420, 415, 130, 60]]), "calm"),
 ("Underneath, a slatted platform. The platform structure holds books up the legs, high and dry above the floor.", quote(TABLE, "The platform structure holds books B up the legs, high and dry above the floor.", "high and dry", "US 4,825,779 · description"), "calm"),
 ("It also thought about writing. Some may prefer to prepare notes such as shopping lists.", quote(TABLE, "Some may prefer to prepare notes such as shopping lists", "shopping lists", "US 4,825,779 · description"), "calm"),
 ("And one of its objects: to be handsome in appearance and large enough to be seen and not tripped over.", quote(TABLE, "handsome in appearance and large enough to be seen and not tripped over.", "handsome in appearance", "US 4,825,779 · description"), "calm"),
 ("A desk for the throne. Approved, May nineteen eighty-nine.", stamp(TABLE, "TABLE FOR|TOILET", "NOV. 16, 1987", "MAY 2, 1989", at=1.6), "slow"),

 # ---------- 7 · portable bath-tub ----------
 ("Number seven. The bathroom you can roll away.", chap(7, PORTA, "Portable|Bath-Tub", ["US 428,252", "Filed 1890 · Issued 1890"]), "calm"),
 ("In eighteen ninety, this was a portable bathtub. The inventor's own was three feet long, two feet wide, and about ten inches in height.", quote(PORTA, "three feet long, two feet wide, and about ten inches in height", "about ten inches", "US 428,252 · description"), "calm"),
 ("Posts fold up out of the tub. You sit on a folding seat. And down by your feet, there is a rocking pedal.", fig(PORTA, "porta1", "1", calls=[["THE SEAT", 500, 505, 120, -70], ["THE PEDAL", 308, 725, 130, 70]]), "calm"),
 ("It works two small pumps, oscillated by the feet of the occupant seated on seat N.", quote(PORTA, "oscillated by the feet of the occupant seated on seat N.", "by the feet of the occupant", "US 428,252 · description"), "calm"),
 ("The pumps push the water up a hose to a hand nozzle. It rains down, collects in a dip in the floor, and gets pumped up again.", fig(PORTA, "porta1", "1", draw=False, calls=[["THE HOSE", 350, 450, 140, -40], ["THE NOZZLE", 402, 320, 130, -70]]), "calm"),
 ("By this means only a small amount of water will be necessary.", quote(PORTA, "By this means only a small amount of water will be necessary", "a small amount of water", "US 428,252 · description"), "calm"),
 ("Then a canvas, oil-cloth, or rubber cover goes over the whole frame.", fig(PORTA, "porta2", "2", calls=[["THE COVER", 325, 150, 70, -90]]), "calm"),
 ("The usual splashing is not only prevented from escaping from the tub, but the occupant is wholly secluded from observation.", quote(PORTA, "the usual splashing is not only prevented from escaping from the tub, but the occupant is wholly secluded from observation", "wholly secluded", "US 428,252 · description"), "calm"),
 ("And when you are clean, everything folds into the tub, the lid closes, and the whole bathroom rolls away on casters.", fig(PORTA, "porta3", "3", calls=[["THE LID", 150, 108, 90, -80], ["CASTER", 150, 270, 110, 40]]), "calm"),
 ("A shower you pedal. Inside a tent. Approved, May eighteen ninety.", stamp(PORTA, "PORTABLE|BATH-TUB", "JAN. 13, 1890", "MAY 20, 1890", at=1.6), "slow"),

 # ---------- 6 · after shower body drier ----------
 ("Number six. Goodbye, towels.", chap(6, DRIER, "After Shower|Body Drier", ["US 3,128,161", "Filed 1962 · Issued 1964"]), "calm"),
 ("The problem with earlier hot air driers, according to this patent: it has the major drawback that it is intended only to be used for drying the user's hands or face.", quote(DRIER, "has the major drawback that it is intended only to be used for drying the user's hands or face.", "hands or face", "US 3,128,161 · description"), "calm"),
 ("So here is the fix. A stall. You stand inside. Hot air nozzles point at you from the left, from the right, and from above.", fig(DRIER, "drier1", "1", calls=[["HOT AIR", 205, 235, -150, 70], ["HOT AIR", 420, 235, 140, 70], ["THE TOP HEAD", 313, 123, 130, -60]]), "calm"),
 ("A blower and a heater sit at the end of a long duct. And there is one button.", fig(DRIER, "drier1", "1", draw=False, calls=[["BLOWER + HEATER", 800, 600, -250, -100], ["THE BUTTON", 437, 285, 130, 40]]), "calm"),
 ("The person will then merely press button switch eighteen to start up blower fifteen and air heater sixteen.", quote(DRIER, "The person will then merely press button switch 18 to start up blower 15 and air heater 16.", "merely press", "US 3,128,161 · description"), "calm"),
 ("Every nozzle swivels, and every duct has its own damper. Obviously, any combination of diffusers may be used at will depending on the person's choice, et cetera.", quote(DRIER, "Obviously, any combination of diffusers may be used at will depending on the person's choice, etc.", "the person's choice, etc.", "US 3,128,161 · description"), "calm"),
 ("Close every damper except the top one, and the whole stall becomes a hair dryer.", fig(DRIER, "drier2", "2", calls=[["THE TOP HEAD", 277, 193, 90, 80]]), "calm"),
 ("And it had big plans. A still further object is to provide a drier which eliminates the need for towels for drying purposes in public establishments such as hotels.", quote(DRIER, "A still further object is to provide a drier which eliminates the need for towels for drying purposes in public establishments such as hotels.", "eliminates the need for towels", "US 3,128,161 · description"), "calm"),
 ("A car wash for people. Just the drying part. Approved, April nineteen sixty-four.", stamp(DRIER, "AFTER SHOWER|BODY DRIER", "SEPT. 24, 1962", "APR. 7, 1964", at=1.8), "slow"),

 # ---------- 5 · hair washing machine ----------
 ("Number five. Hands-free shampoo.", chap(5, HAIR, "Hair Washing|Machine", ["US 3,732,580", "Filed 1971 · Issued 1973"]), "calm"),
 ("This is a helmet. Full of shower heads.", fig(HAIR, "hair1", "1", calls=[["THE HELMET", 300, 75, 130, -50], ["THE SHOWERS", 415, 225, 140, 60]]), "punch"),
 ("It has an opening in which the nape of the neck for a person's head can be inserted.", quote(HAIR, "having an opening in which the nape of the neck for a person's head can be inserted", "a person's head", "US 3,732,580 · description"), "calm"),
 ("A seal around the opening keeps your face dry. It prevents the water being injected into the helmet from exiting therefrom and wetting the face of a person.", quote(HAIR, "prevents the water being injected into the helmet from exiting therefrom and wetting the face of a person", "wetting the face", "US 3,732,580 · description"), "calm"),
 ("Then, the starting key is depressed, thereby starting the timer fifteen.", quote(HAIR, "the starting key is depressed, thereby starting the timer 15.", "starting the timer", "US 3,732,580 · description"), "calm"),
 ("The trick is that the showers take turns. Groups switch on and off, causing the hair to continuously move in either direction.", fig(HAIR, "hair2", "2", calls=[["THE SHOWERS", 170, 320, -60, 90], ["WATER IN", 270, 60, 120, -40]]), "calm"),
 ("The patent's promise: the water jets will cause a continuous movement of the hair and a massage of the scalp.", quote(HAIR, "the water jets will cause a continuous movement of the hair and a massage of the scalp.", "a massage of the scalp", "US 3,732,580 · description"), "calm"),
 ("It warms the water, adds the shampoo, washes, drains and rinses. The washing step can be repeated for several times, always under the control of the timer.", quote(HAIR, "The washing step can be repeated for several times, always under the control of the timer 15", "repeated for several times", "US 3,732,580 · description"), "calm"),
 ("And the timer, it says, did great. When suitably programmed, the timer shows an excellent behavior in performing different working programs.", quote(HAIR, "When suitably programmed, the timer shows an excellent behavior in performing different working programs.", "an excellent behavior", "US 3,732,580 · description"), "calm"),
 ("A dishwasher. For your head. Approved, May nineteen seventy-three.", stamp(HAIR, "HAIR WASHING|MACHINE", "JUNE 18, 1971", "MAY 15, 1973", at=1.6), "slow"),

 # ---------- 4 · toilet lid position signal ----------
 ("Number four. The oldest argument in the house.", chap(4, LID, "Electronic Toilet Lid|Position Signal", ["US 5,926,099", "Filed 1997 · Issued 1999"]), "calm"),
 ("The patent states the problem. Toilet lids are often left in the open position through carelessness or inadvertence.", quote(LID, "Toilet lids are often left in the open position through carelessness or inadvertence.", "carelessness or inadvertence", "US 5,926,099 · description"), "calm"),
 ("The fix is a little box you stick under the lid. When the lid goes up, it plays music. When the lid comes down, it stops.", fig(LID, "lid1", "1C", calls=[["THE DEVICE", 204, 400, -60, -120], ["THE MUSIC", 88, 446, 40, 110]]), "calm"),
 ("Where does the music come from? In the preferred embodiment, a greeting card style electronic music, sound, and blinking light module is used.", quote(LID, "In the preferred embodiment, a greeting card style electronic music, sound, and blinking light module is used.", "greeting card style", "US 5,926,099 · description"), "calm"),
 ("Why not a simple buzzer? Prior solutions suggest signal devices that produce unpleasant shrill beeps, buzzes, and flashing lights that discourage their use.", quote(LID, "Prior solutions suggest signal devices that produce unpleasant shrill beeps, buzzes, and flashing lights that discourage their use.", "unpleasant shrill beeps", "US 5,926,099 · description"), "calm"),
 ("So how does the box know the lid is up? Gravity. In one version, a fishing sinker hangs on a nylon line. Tilt the box, and the sinker swings onto the contacts.", fig(LID, "lid3", "3A", calls=[["FISHING SINKER", 204, 223, 140, -40], ["NYLON LINE", 277, 154, 140, -90], ["CONTACTS", 223, 296, 150, 50]]), "calm"),
 ("The patent gets specific. A size three-aught split shot sinker of the common type is utilized as a conductive weight means.", quote(LID, "a size 3/0 split shot sinker of the common type is utilized as a conductive weight means 60.", "split shot sinker", "US 5,926,099 · description"), "calm"),
 ("It even plans other models. A bird-shaped housing with module making bird sounds. And a fisherman model with line and sinker.", quote(LID, 'bird-shaped housing with module making bird sounds, a "fisherman" model with line and sinker', "bird sounds", "US 5,926,099 · description"), "calm"),
 ("And the long-term goal: conditioning persons who use the toilet to lower the toilet seat or cover after use.", quote(LID, "conditioning persons who use the toilet to lower the toilet seat or cover after use", "conditioning persons", "US 5,926,099 · description"), "slow"),
 ("Training humans. With a greeting card. Approved, July nineteen ninety-nine.", stamp(LID, "TOILET LID|POSITION SIGNAL", "DEC. 8, 1997", "JULY 20, 1999", at=1.8), "slow"),

 # ---------- 3 · automatic toilet seat cleaning ----------
 ("Number three. The seat that cleans itself.", chap(3, SEAT, "Automatic Cleaning|of a Toilet Seat", ["US 4,790,036", "Filed 1986 · Issued 1988"]), "calm"),
 ("This toilet has motors. Three of them. And the seat is a ring that can turn.", fig(SEAT, "seat1", "1", calls=[["THE SEAT", 608, 885, -150, 90], ["IT TURNS", 792, 996, 40, 110]]), "calm"),
 ("In its own words, the seat of the toilet, during the cleaning, is moved in a circumferential direction.", quote(SEAT, "the seat of the toilet, during the cleaning, is moved in a circumferential direction", "circumferential direction", "US 4,790,036 · description"), "calm"),
 ("Here is how. A cleaning unit swings out on arms and settles over one part of the seat. Water nozzles. Disinfectant nozzles. And a wiper.", fig(SEAT, "seat2", "3", calls=[["WATER", 500, 331, -120, 90], ["DISINFECTANT", 562, 262, 60, -110], ["THE WIPER", 646, 385, 130, 80]]), "calm"),
 ("Then the seat is rotated by at least three hundred sixty degrees, the upper surface of the seat being dried.", quote(SEAT, "the seat is rotated by at least 360°, the upper surface of the seat being dried.", "at least 360°", "US 4,790,036 · description"), "calm"),
 ("And if one full turn is not enough: One could, for example, use a rotation of four hundred degrees.", quote(SEAT, "One could, for example, use a rotation of 400°", "400°", "US 4,790,036 · description"), "punch"),
 ("It does not need an outlet, either. The water refilling the tank spins a little turbine, and the turbine drives a generator.", fig(SEAT, "seat1", "1", draw=False, calls=[["THE TURBINE", 277, 285, 150, -60]]), "calm"),
 ("The nozzles spray two jets of liquid onto the seat. And switches check whether someone is sitting on it. If someone is, it will not spin.", fig(SEAT, "seat3", "4", calls=[["THE SPRAY", 650, 146, -200, -70], ["THE SEAT", 646, 185, -170, 110]]), "calm"),
 ("And the patent's own verdict: The subject of the invention constitutes an important step forward in social hygiene, without resulting in environmental pollution.", quote(SEAT, "The subject of the invention constitutes an important step forward in social hygiene, without resulting in environmental pollution.", "an important step forward", "US 4,790,036 · description"), "calm"),
 ("A toilet seat on a turntable. Approved, December nineteen eighty-eight.", stamp(SEAT, "AUTOMATIC CLEANING|OF A TOILET SEAT", "OCT. 7, 1986", "DEC. 13, 1988", at=1.8), "slow"),

 # ---------- 2 · rocking bathtub ----------
 ("Number two. The bathtub that rocks.", chap(2, ROCK, "Bath-Tub|(Rocking)", ["US 1,067,898", "Filed 1912 · Issued 1913"]), "calm"),
 ("This is a bathtub. On rockers. Like a rocking chair.", fig(ROCK, "rock1", "1", calls=[["THE ROCKERS", 330, 438, 140, 50]]), "punch"),
 ("The object of my invention is to provide a rocking bath tub having means to prevent the splashing of water during the rocking action.", quote(ROCK, "The object of my invention is to provide a rocking bath tub having means to prevent the splashing of water during the rocking action.", "a rocking bath tub", "US 1,067,898 · description"), "calm"),
 ("One end curves up into a back rest. And the top edges are rounded or beaded, to form smooth rests for the arms.", fig(ROCK, "rock1", "1", draw=False, calls=[["BACK REST", 560, 200, -170, -100], ["ARM REST", 300, 292, -40, -120]]), "calm"),
 ("Underneath, two long rockers of bent sheet metal, riveted on.", fig(ROCK, "rock2", "2", calls=[["THE ROCKERS", 305, 125, 120, -70]]), "calm"),
 ("Which leaves one problem. When you rock forward, the water rocks forward too. So across the low end, there is a plate.", fig(ROCK, "rock1", "1", draw=False, calls=[["SPLASH PLATE", 130, 228, 60, -120]]), "calm"),
 ("When the tub is rocking and the water moving forward the front or portion four of the tub is prevented from overflowing or splashing.", quote(ROCK, "When the tub is rocking and the water moving forward the front or portion 4 of the tub is prevented from overflowing or splashing", "prevented from overflowing", "US 1,067,898 · description"), "calm"),
 ("The drawing even includes the bath. The water within the tub is shown in dotted lines.", quote(ROCK, "The water within the tub is shown in dotted lines.", "dotted lines", "US 1,067,898 · description"), "calm"),
 ("A rocking chair. Full of water. Approved, July nineteen thirteen.", stamp(ROCK, "BATH-|TUB", "AUG. 6, 1912", "JULY 22, 1913", at=1.6), "slow"),

 # ---------- 1 · toilet tank aquarium ----------
 ("And number one. The weirdest bathroom patent on our shelf.", chap(1, AQUA, "Toilet Tank|Aquarium", ["US 5,983,411", "Filed 1998 · Issued 1999"]), "calm"),
 ("It opens with a fact. The use of toilets is known in the prior art.", quote(AQUA, "The use of toilets is known in the prior art.", "known in the prior art", "US 5,983,411 · description"), "calm"),
 ("Then it adds fish. The flush water sits in a box of its own, against the back of the tank.", fig(AQUA, "aquarium1", "1", calls=[["THE FLUSH WATER", 492, 385, -60, -130], ["THE FISH TANK", 562, 538, 120, 80]]), "calm"),
 ("From the top, you can see the layout. The fish swim in the space around its front and sides.", fig(AQUA, "aquarium2", "2", calls=[["FLUSH WATER", 277, 192, 60, -110], ["FISH", 231, 285, -40, 110], ["MORE FISH", 485, 215, 120, 60]]), "calm"),
 ("And the patent spells it out: The front of the toilet tank assembly is generally transparent.", quote(AQUA, "The front of the toilet tank assembly is generally transparent.", "generally transparent", "US 5,983,411 · description"), "calm"),
 ("The flush handle still works. The lid has a light that shines into the aquarium. And a compartment which is designed for storing items such as aquarium supplies therein.", quote(AQUA, "a compartment 28 which is designed for storing items such as aquarium supplies therein.", "aquarium supplies", "US 5,983,411 · description"), "calm"),
 ("The goal: a new toilet tank assembly aquarium that helps make a bathroom more attractive.", quote(AQUA, "a new toilet tank assembly aquarium that helps make a bathroom more attractive.", "more attractive", "US 5,983,411 · description"), "calm"),
 ("No fish? No problem. A new toilet tank assembly aquarium that can also be used as a terrarium.", quote(AQUA, "a new toilet tank assembly aquarium that can also be used as a terrarium.", "a terrarium", "US 5,983,411 · description"), "calm"),
 ("In another version, a separate aquarium sits on top of the tank instead.", fig(AQUA, "aquarium3", "6", calls=[["THE AQUARIUM", 431, 554, 150, -60]]), "calm"),
 ("And how exactly do you use it? The patent keeps that short. Accordingly, no further discussion relating to the manner of usage and operation will be provided.", quote(AQUA, "Accordingly, no further discussion relating to the manner of usage and operation will be provided.", "no further discussion", "US 5,983,411 · description"), "calm"),
 ("A toilet. With fish. Approved, November nineteen ninety-nine.", stamp(AQUA, "TOILET TANK|AQUARIUM", "AUG. 6, 1998", "NOV. 16, 1999", big=True, at=1.6), "slow"),

 # ---------- close ----------
 ("So that is the ranking. But which bathroom patent is the most approved?", dict(g="title", kicker="THIS SHELF'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the toilet table. Because it is the only patent here that gave the toilet seat a promotion.", quote(TABLE, Q_THRONE, "the throne", "US 4,825,779 · description", typed=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["2,302,806 · 2,528,006 · 4,825,779", "428,252 · 3,128,161 · 3,732,580", "5,926,099 · 4,790,036", "1,067,898 · 5,983,411"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
