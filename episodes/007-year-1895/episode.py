# SERIOUSLY APPROVED · FILE 007 · THE YEAR FILE — "9 Weird Victorian Inventions That Got Real Patents (1895)"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, date):
    return dict(num=num, hook=title, side=f"{num} · {date}")

CANE = P("US 531,878", "THE CANE|[UMBRELLA]", "JAN. 1, 1895")
SWING = P("US 533,149", "A FAN FOR|YOUR [SWING]", "JAN. 29, 1895")
RAIL = P("US 535,674", "A BICYCLE|FOR [RAILS]", "MAR. 12, 1895")
HORSE = P("US 543,874", "THE HORSE|WITH [WHEELS]", "AUG. 6, 1895")
HAT = P("US 544,419", "A HAT WITH|A [LIGHT]", "AUG. 13, 1895")
MONK = P("US 546,021", "THE MONKEY|[DRUMMER]", "SEPT. 10, 1895")
SPID = P("US 545,958", "THE SPIDER|AND THE [FLY]", "SEPT. 10, 1895")
BOAT = P("US 546,105", "A BICYCLE|ON [WATER]", "SEPT. 10, 1895")
CAN = P("US 546,104", "A ROOF FOR|YOUR [BICYCLE]", "SEPT. 10, 1895")

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"1895 · PATENT No. {n} OF 9", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="THE YEAR|[1895]", side="FILE 007 · THE YEAR FILE")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 007")

Q_HAT_WORN = "The hat or cap will otherwise be worn just the same as any ordinary hat or cap"
Q_RAIL_CAR = "the machine will follow the rails like an ordinary car"
Q_CAN_SAIL = "may be arranged at an angle, to operate as a sail for accelerating the speed of the bicycle to assist the rider"
Q_SWING_FAN = "and, as is obvious, will fan him"
Q_SPID = "so that the spider will seem to be trying to catch it"

LINES = [
 # ---------- cold open ----------
 ("These are real Victorian-era inventions. This one is a policeman's hat.", fig(HAT, "hat1", "1"), "slow"),
 ("Look at the band. That is an electric lamp, in its own reflector. The wires run down to a battery in your pocket. Or something else.", fig(HAT, "hat1", "1", draw=False, calls=[["LAMP", 46, 330, 70, 60]]), "calm"),
 ("It was approved. In eighteen ninety-five.", stamp(HAT, "ELECTRIC-WIRE-CONTAINING|HAT OR CAP BAND", "JUNE 10, 1895", "AUG. 13, 1895"), "punch"),
 ("Welcome to the year file. One year, nine real patents, all approved. The year is eighteen ninety-five. America is in a bicycle craze, the electric light is still new, and the United States Patent Office is very, very busy.", dict(g="title", kicker="THE YEAR FILE · FILE 007", title="The Weirdest|Patents of 1895", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- 1 · cane umbrella ----------
 ("Number one. New Year's Day.", chap(1, CANE, "Cane-|Umbrella", ["US 531,878", "Filed 1894 · Issued Jan. 1, 1895"]), "calm"),
 ("The very first patent on our list was issued on January first, eighteen ninety-five. It is a walking cane. With an umbrella inside.", fig(CANE, "cu2", "2"), "calm"),
 ("And the patent does not claim to be the first. Its object, it says, is to simplify the construction and operation of cane umbrellas.", quote(CANE, "The object of this invention is to simplify the construction and operation of cane umbrellas", "cane umbrellas", "US 531,878 · description"), "calm"),
 ("So by eighteen ninety-five, cane umbrellas already needed simplifying.", quote(CANE, "The object of this invention is to simplify the construction and operation of cane umbrellas", "simplify", "US 531,878 · description", typed=False), "slow"),
 ("Here is the trick. Pull the umbrella out of the cane, turn it around, and push it back in the other way.", fig(CANE, "cu1", "1 · 2", calls=[["CANE", 244, 685, -90, 40], ["UMBRELLA", 487, 122, 60, -40]]), "calm"),
 ("Now the knob at the end of the cane is the handle of the umbrella. In the patent's words, it forms its top when the cane is used for walking, and its bottom when the umbrella is open.", fig(CANE, "cu1", "1", draw=False, calls=[["KNOB", 472, 921, 80, 20]]), "calm"),
 ("Closed, the umbrella slides into the hollow cane until a rim stops it, and a catch holds it in place. From the outside, it is just a cane.", fig(CANE, "cu2", "2", draw=False, calls=[["CATCH", 52, 762, 60, 30]]), "calm"),
 ("And because the umbrella only ever goes in from one end, the other end of the cane can remain permanently closed.", quote(CANE, "the other end of the cane can remain permanently closed", "permanently closed", "US 531,878 · description"), "calm"),
 ("No cap to lose. Approved on the first day of the year.", stamp(CANE, "CANE-|UMBRELLA", "SEPT. 20, 1894", "JAN. 1, 1895", at=1.6), "slow"),

 # ---------- 2 · fan for swings ----------
 ("Number two. The porch.", chap(2, SWING, "Fan Attachment|for Swings", ["US 533,149", "Filed 1894 · Issued 1895"]), "calm"),
 ("Four weeks later, the Patent Office approved this. A frame, a swing, and a big flat board on two long arms.", fig(SWING, "fan1", "1"), "calm"),
 ("The board is a fan. The patent wants a simple and cheap attachment adapted to fan the occupant of a swing during the oscillation of the swing.", quote(SWING, "a simple and cheap attachment adapted to fan the occupant of a swing during the oscillation of the swing", "fan the occupant", "US 533,149 · description"), "calm"),
 ("It works like this. When you swing forward, the fan swings back. When you swing back, the fan swings forward.", fig(SWING, "fan1", "1", draw=False, calls=[["FAN", 483, 495, 60, 50]]), "calm"),
 ("The fan will swing in the direction contrary to that the occupant of the swing moves.", quote(SWING, "the fan 8 will swing in the direction contrary to that the occupant of the swing moves", "contrary", "US 533,149 · description", hide=True), "calm"),
 ("And, as is obvious, will fan him.", quote(SWING, "the fan 8 will swing in the direction contrary to that the occupant of the swing moves, and, as is obvious, will fan him", "will fan him", "US 533,149 · description", typed=False), "slow"),
 ("Why not let the fan fly in a big circle? Because, the patent explains, the occupant of the swing would derive no benefit from air thrown off from the fan in other than a downward direction.", quote(SWING, "the occupant of the swing would derive no benefit from air thrown off from the fan in other than a downward direction", "no benefit", "US 533,149 · description"), "calm"),
 ("You can build the frame anywhere, or hang it by ropes from trees or the roofs of porches.", fig(SWING, "fan2", "2"), "calm"),
 ("The patent also worries about effort. A needless amount of motion on the part of the fan makes a swing needlessly hard to operate.", quote(SWING, "a needless amount of motion on the part of the fan makes a swing needlessly hard to operate", "needlessly hard", "US 533,149 · description"), "calm"),
 ("And swing is meant broadly. Whether it be an ordinary seat, a cradle, a hammock, or so on.", quote(SWING, "whether it be an ordinary seat, a cradle, a hammock, or so on", "or so on", "US 533,149 · description"), "calm"),
 ("You swing. The fan swings back. Approved, January eighteen ninety-five.", stamp(SWING, "FAN ATTACHMENT|FOR SWINGS", "MAR. 23, 1894", "JAN. 29, 1895", at=2.4), "slow"),

 # ---------- 3 · railroad bicycle ----------
 ("Number three. The railroad.", chap(3, RAIL, "Attachment|for Bicycles", ["US 535,674", "Filed 1894 · Issued 1895"]), "calm"),
 ("This is an ordinary bicycle. Look at what it is standing on.", fig(RAIL, "rail1", "1"), "calm"),
 ("Those are railroad tracks. A small third wheel runs on the opposite rail, held by three braces.", fig(RAIL, "rail1", "1", draw=False, calls=[["THIRD WHEEL", 158, 592, 80, -60]]), "calm"),
 ("The goal, in the patent's words: a bicycle run upon the rails of an ordinary railway track.", quote(RAIL, "upon the rails of an ordinary railway track", "railway track", "US 535,674 · description"), "calm"),
 ("And it is not for one special machine. It is a device of great simplicity and cheapness, which may be applied to any safety bicycle.", quote(RAIL, "a device of great simplicity and cheapness, which may be applied to any safety bicycle", "any safety bicycle", "US 535,674 · description"), "calm"),
 ("The third wheel has a concave rim, so it hugs the rail.", fig(RAIL, "rail2", "2", calls=[["CONCAVE RIM", 300, 400, 100, 40]]), "calm"),
 ("And because the braces hold the steering fork, the patent says no steering is necessary. It enables the machine to be practically self-steering.", quote(RAIL, "enables the machine to be practically self-steering", "self-steering", "US 535,674 · description"), "calm"),
 ("All the rider need do is to simply use his strength to propel the machine.", quote(RAIL, Q_RAIL_CAR, "like an ordinary car", "US 535,674 · description", hide=True), "calm"),
 ("And the machine will follow the rails like an ordinary car.", quote(RAIL, Q_RAIL_CAR, "like an ordinary car", "US 535,674 · description", typed=False), "slow"),
 ("When you are done, the whole attachment folds into a very small compass.", quote(RAIL, "may be folded into a very small compass", "very small compass", "US 535,674 · description"), "calm"),
 ("A bicycle that thinks it is a train. Approved, March eighteen ninety-five.", stamp(RAIL, "ATTACHMENT|FOR BICYCLES", "AUG. 4, 1894", "MAR. 12, 1895", at=2.6), "slow"),

 # ---------- 4 · velocipede hobby-horse ----------
 ("Number four. The stable.", chap(4, HORSE, "Velocipede|Hobby-Horse", ["US 543,874", "Filed 1894 · Issued 1895"]), "calm"),
 ("In eighteen ninety-five, you could have a rocking horse, or you could have a velocipede. This patent refused to choose.", fig(HORSE, "hh1", "1"), "calm"),
 ("My invention relates to a hobby-horse velocipede.", quote(HORSE, "My invention relates to a hobby-horse velocipede", "hobby-horse velocipede", "US 543,874 · description"), "slow"),
 ("The horse sits on a frame with three wheels. Under the saddle are two curved toothed racks.", fig(HORSE, "hh1", "1", draw=False, calls=[["RACKS", 460, 342, 90, 40]]), "calm"),
 ("Rock the horse, and the racks turn the gears, the gears turn a chain, and the chain turns the back wheels.", fig(HORSE, "hh1", "1", draw=False, vb="300 200 500 400"), "calm"),
 ("And it works both ways. When the hobby-horse is rocked forward the sprocket-wheel is rotated, and also when the horse is rocked rearward said wheel is rotated.", quote(HORSE, "when the hobby-horse is rocked forward the sprocket-wheel 13 is rotated", "rocked forward", "US 543,874 · description"), "calm"),
 ("Each gear only turns the shaft one way. A ratchet lets it slip on the return. So one rack drives on the forward rock, and the other on the backward rock.", fig(HORSE, "hh1", "1", draw=False, vb="300 200 500 400", calls=[["GEARS", 460, 342, 80, -60]]), "calm"),
 ("So every rock, forward or back, moves you forward.", fig(HORSE, "hh1", "1", draw=False, calls=[["BACK WHEELS", 738, 481, 60, -70]]), "calm"),
 ("To steer, there is a handle on top of the horse. And the front of the horse may be moved up and down while you steer.", quote(HORSE, "the forward portion of the hobby-horse may be moved up and down", "up and down", "US 543,874 · description"), "calm"),
 ("A horse that rocks its way down the street. Approved, August eighteen ninety-five.", stamp(HORSE, "VELOCIPEDE|HOBBY-HORSE", "OCT. 22, 1894", "AUG. 6, 1895", at=2.6), "slow"),

 # ---------- 5 · light-up hat ----------
 ("Number five. The night shift.", chap(5, HAT, "Electric-Wire-Containing|Hat or Cap Band", ["US 544,419", "Filed June 1895 · Issued Aug. 1895"]), "calm"),
 ("Back to the hat from the beginning. Figure one, according to the patent, is a perspective view of a policeman's hat.", fig(HAT, "hat1", "1"), "calm"),
 ("The invention is not the hat. It is the band around it. A removable band adapted to have an incandescent light attached to it.", quote(HAT, "adapted to have an incandescent light attached to it", "incandescent light", "US 544,419 · description"), "calm"),
 ("Inside the band run wires. At the front is a little tab with two buttons. The lamp, in its own reflector, snaps onto them.", fig(HAT, "hat7", "7", calls=[["LAMP", 90, 130, 60, -60]]), "calm"),
 ("Under this construction, the lamp may be attached to and removed from the band with perfect convenience.", quote(HAT, "Under this construction the lamp may be attached to and removed from the band with perfect convenience.", "perfect convenience", "US 544,419 · description"), "calm"),
 ("The band itself is made, by preference, of enameled leather, so as to be waterproof. Useful, for a hat with electricity in it.", quote(HAT, "composed of enameled leather, or otherwise constructed, so as to be waterproof", "waterproof", "US 544,419 · description"), "calm"),
 ("Then the body wires. They are called that, the patent explains, because they lead down from the hat or cap over the body to some source of electrical energy.", quote(HAT, "lead down from the hat or cap over the body to some source of electrical energy", "over the body", "US 544,419 · description"), "calm"),
 ("Whether that be a battery carried in the pocket, or a dynamo carried upon a bicycle.", quote(HAT, "a dynamo carried upon a bicycle, or what not", "or what not", "US 544,419 · description", hide=True), "calm"),
 ("Or what not.", quote(HAT, "a dynamo carried upon a bicycle, or what not", "or what not", "US 544,419 · description", typed=False), "punch"),
 ("The band even adjusts to fit any particular hat. And otherwise, the patent promises, nothing changes.", fig(HAT, "band", "2a"), "calm"),
 ("The hat or cap will otherwise be worn just the same as any ordinary hat or cap.", quote(HAT, Q_HAT_WORN, "any ordinary hat", "US 544,419 · description"), "slow"),
 ("Filed in June. Approved in August. Just over two months, for a hat that plugs in.", stamp(HAT, "ELECTRIC-WIRE-CONTAINING|HAT OR CAP BAND", "JUNE 10, 1895", "AUG. 13, 1895", at=1.8), "slow"),

 # ---------- 6 · monkey drummer ----------
 ("Number six. September tenth, eighteen ninety-five. A busy day. The last four patents on our list were all issued on the same Tuesday.", chap(6, MONK, "Toy|(Drum-Beater)", ["US 546,021", "Filed 1895 · Issued Sept. 10, 1895"]), "calm"),
 ("The first is a toy. A toy drum-beater, consisting of a figure, preferably that of a monkey.", quote(MONK, "a toy drum-beater, consisting of a figure, preferably that of a monkey", "preferably that of a monkey", "US 546,021 · description"), "calm"),
 ("The patent was assigned to the Waterbury Button Company, of Waterbury, Connecticut. A button company. With a drumming monkey.", fig(MONK, "mk1", "1"), "calm"),
 ("Here he is. A coat with buttons, a hat with a plume, a stick in each hand, and a drum.", fig(MONK, "mk1", "1", draw=False, calls=[["DRUM", 248, 611, 80, 40]]), "calm"),
 ("Inside his body is a toothed bar. Hold the handle in one hand, and slide the bar with the other.", fig(MONK, "mk2", "2"), "calm"),
 ("Each drum-stick striking the drum at each movement of the bar. The result, the patent says, is the regular time or marching-beat of the drum.", quote(MONK, "the regular time or marching-beat of the drum", "marching-beat", "US 546,021 · description"), "calm"),
 ("Speed is up to you. The bar may be slid back and forth slowly or quickly, as desired.", quote(MONK, "a moderate movement being preferable", "moderate movement", "US 546,021 · description", hide=True), "calm"),
 ("A moderate movement being preferable.", quote(MONK, "a moderate movement being preferable", "moderate movement", "US 546,021 · description", typed=False), "slow"),
 ("And the patent ends with a promise: a device which will readily attract the attention, and which is comparatively inexpensive and not easily injured.", quote(MONK, "not easily injured", "not easily injured", "US 546,021 · description"), "calm"),
 ("A monkey with a marching beat. Approved.", stamp(MONK, "TOY", "MAR. 2, 1895", "SEPT. 10, 1895", at=1.8), "slow"),

 # ---------- 7 · spider toy ----------
 ("Number seven. Same day. Another toy.", chap(7, SPID, "Toy|(Climbing Spider)", ["US 545,958", "Filed 1895 · Issued Sept. 10, 1895"]), "calm"),
 ("This is a spider on a thread. And near the top of the thread is a fly.", fig(SPID, "sp1", "1", calls=[["FLY", 204, 170, 60, 30]]), "calm"),
 ("Inside the spider is a spring, like the spring of a watch. Pull the thread out, let go, and the spring winds it back up.", fig(SPID, "sp2", "2"), "calm"),
 ("Which makes the spider climb, taking up the string as a spider does his web.", quote(SPID, "taking up the string as a spider does his web", "as a spider does his web", "US 545,958 · description"), "calm"),
 ("And while it climbs, a crank vibrates the legs, so they move in a rapid and natural manner.", fig(SPID, "sp2", "2", draw=False, calls=[["LEGS", 51, 420, 60, -60]]), "calm"),
 ("The fly is there for one reason.", quote(SPID, Q_SPID, "trying to catch it", "US 545,958 · description", hide=True), "calm"),
 ("So that the spider will seem to be trying to catch it.", quote(SPID, Q_SPID, "trying to catch it", "US 545,958 · description", typed=False), "slow"),
 ("There is even a deluxe model. Two slotted plates, three legs on each. The patent says it imparts, probably, a more life-like appearance to the movements of the legs. But it is more complex and expensive.", quote(SPID, "imparts, probably, a more life-like appearance to the movements of the legs", "probably", "US 545,958 · description"), "calm"),
 ("One small note. Again and again, the patent calls the spider an insect. We will allow it.", fig(SPID, "sp1", "1", draw=False, calls=[["NOT AN INSECT", 178, 713, 80, 60]]), "calm"),
 ("A spider forever chasing a fly up a string. Approved.", stamp(SPID, "TOY", "APR. 4, 1895", "SEPT. 10, 1895", at=2.0), "slow"),

 # ---------- 8 · marine velocipede ----------
 ("Number eight. Same day. The lake.", chap(8, BOAT, "Marine|Velocipede", ["US 546,105", "Filed 1893 · Issued Sept. 10, 1895"]), "calm"),
 ("If you can ride a velocipede on a road, why not on water. This is a marine velocipede. From above.", fig(BOAT, "mv2", "2"), "calm"),
 ("Two cigar-shaped cylinders or floats, arranged parallel to each other. A seat between them.", quote(BOAT, "two cigar-shaped cylinders or floats arranged parallel to each other", "cigar-shaped", "US 546,105 · description"), "calm"),
 ("From the side, you can see what drives it. A big propelling wheel at the back.", fig(BOAT, "mv1", "1", calls=[["PROPELLING WHEEL", 157, 435, 80, -40]]), "calm"),
 ("Between the floats, above the water, sits the body. It rests on beams at the back, and on a spring at the front. A suspension, for a boat.", fig(BOAT, "mv1", "1", draw=False), "calm"),
 ("The rider steers with handles on a post, which pull cables, which turn two rudders at once.", fig(BOAT, "mv2", "2", draw=False, calls=[["SEAT", 191, 760, 80, 30]]), "calm"),
 ("And there is a second post, upon the upper end of which may be fixed an umbrella, flag, or other convenient device, at pleasure.", quote(BOAT, "may be fixed an umbrella, flag, or other convenient device, at pleasure", "at pleasure", "US 546,105 · description"), "calm"),
 ("The patent is proud of its cables. They run close along the floats, so there are no obstructions to become clogged with vegetable or other floating matter.", quote(BOAT, "there are no obstructions to become clogged with vegetable or other floating matter", "vegetable", "US 546,105 · description"), "calm"),
 ("Filed in May eighteen ninety-three. Approved more than two years later. A bicycle that floats.", stamp(BOAT, "MARINE|VELOCIPEDE", "MAY 6, 1893", "SEPT. 10, 1895", at=2.6), "slow"),

 # ---------- 9 · bicycle canopy ----------
 ("Number nine. Same day. One last bicycle.", chap(9, CAN, "Canopy|for Bicycles", ["US 546,104", "Filed 1894 · Issued Sept. 10, 1895"]), "calm"),
 ("A tall stem clamps onto the frame. On top, the frame of a canopy. A roof for your bicycle.", fig(CAN, "can1", "1", calls=[["CANOPY FRAME", 220, 70, 80, 40]]), "calm"),
 ("It exists for protecting the rider from the rays of the sun, and to shelter him from rain.", quote(CAN, "for protecting the rider from the rays of the sun and to shelter him from rain", "rays of the sun", "US 546,104 · description"), "calm"),
 ("Held flat, the patent says, it offers no obstruction in riding against the wind.", quote(CAN, "it offers no obstruction in riding against the wind", "no obstruction", "US 546,104 · description"), "calm"),
 ("But tilt it.", fig(CAN, "can3", "3"), "slow"),
 ("And it may be arranged at an angle, to operate as a sail.", quote(CAN, Q_CAN_SAIL, "as a sail", "US 546,104 · description", hide=True), "calm"),
 ("For accelerating the speed of the bicycle to assist the rider.", quote(CAN, Q_CAN_SAIL, "as a sail", "US 546,104 · description", typed=False), "slow"),
 ("There is also a second version. Here the canopy sits on a square frame of bars, mounted on top of the stem.", fig(CAN, "can7", "7"), "calm"),
 ("It folds up when not in use. And for a lady's bicycle, the clamps are attached to the steering-bar instead.", fig(CAN, "can1", "1", draw=False), "calm"),
 ("A roof, a sunshade, and a sail. On a bicycle. Approved, September tenth, eighteen ninety-five.", stamp(CAN, "CANOPY|FOR BICYCLES", "SEPT. 27, 1894", "SEPT. 10, 1895", at=3.4), "slow"),

 # ---------- close ----------
 ("So which patent of eighteen ninety-five is the most approved?", dict(g="title", kicker="1895'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the hat. Two months from filing to approval, for a policeman's hat with a lamp on its band, wired to a battery in the pocket. Or a dynamo on a bicycle. Or what not.", fig(HAT, "hat1", "1", draw=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["531,878 · 533,149 · 535,674", "543,874 · 544,419 · 546,021", "545,958 · 546,105 · 546,104"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
