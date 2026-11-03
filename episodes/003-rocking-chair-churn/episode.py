# SERIOUSLY APPROVED · FILE 003 · ONE PATENT — "The Rocking Chair That Churns Butter (Real 1913 Patent)"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

CHURN = P("US 1,051,684", "THE BUTTER|[ROCKER]", 1913)
WEIGEL = P("US 538,566", "THE [SILENT]|FAN", 1895)
DAVEY = P("US 581,902", "FANS BY|[GRAVITY]", 1897)
KLINE = P("US 1,139,299", "THE [PENDULUM]|FAN", 1915)
NIELSEN = P("US 1,174,436", "THE FAN|[TOWER]", 1916)
SINGER = P("US 1,269,325", "THE [PORCH]|FAN", 1918)

def chap(kicker, d, title, lines, n=""):
    return dict(g="title", kicker=kicker, numeral=n, title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="THE BUTTER|[ROCKER]", side="FILE 003 · ONE PATENT")
FANS = dict(hook="FAN [ATTACHMENT]|FOR ROCKING-CHAIRS", side="FILE 003 · THE RELATIVES")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 003")

Q_IDEA = "so that a churn may be operated by a person seated and rocking in a rocking chair"
Q_ROT = "Hence, the ratchet wheel is rotated in one direction and causes the churn body to correspondingly rotate."
Q_GRAV = "the downward movement of the rod being accomplished by gravity only."
CH_T = "CHURN."
CH_F, CH_I = "JUNE 28, 1912", "JAN. 28, 1913"
FAN_T = "FAN ATTACHMENT FOR|ROCKING-CHAIRS"

LINES = [
 # ---------- cold open ----------
 ("This is a rocking chair.", fig(CHURN, "churn1", "1"), "slow"),
 ("And this, mounted beside it, is a barrel. A butter churn.", fig(CHURN, "churn1", "1", draw=False, ring=[348, 402, 190]), "calm"),
 ("You sit down. You rock. And the barrel turns.", fig(CHURN, "churn2", "2"), "calm"),
 ("It was approved.", stamp(CHURN, CH_T, CH_F, CH_I), "punch"),
 ("This is real. A U.S. patent from nineteen thirteen. Today, one patent: the rocking chair that churns butter. And then, its relatives. Because the rocking chair had other jobs. Mostly one job.", dict(g="title", kicker="ONE PATENT · FILE 003", title="The Rocking Chair|That Churns Butter", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- part 1 · the churn ----------
 ("Part one. Maine, nineteen twelve.", chap("THE ONE PATENT", CHURN, "Churn.", ["US 1,051,684", "Filed 1912 · Issued 1913"], "1"), "calm"),
 ("The official title of this patent is one word. Churn. With a period.", quote(CHURN, "CHURN.", "CHURN.", "US 1,051,684 · title"), "slow"),
 ("The inventor, Alfred Clark, lived in Maine. And his whole idea fits in one sentence.", fig(CHURN, "churn1", "1", draw=False), "calm"),
 ("Here it is.", quote(CHURN, Q_IDEA, "seated and rocking", "US 1,051,684 · description", hide=True), "calm"),
 ("So that a churn may be operated by a person seated and rocking in a rocking chair.", quote(CHURN, Q_IDEA, "seated and rocking", "US 1,051,684 · description", typed=False), "slow"),
 ("Turning cream into butter takes work. Usually, your arms do it. This patent gives the job to your chair.", fig(CHURN, "churn1", "1", draw=False), "calm"),
 ("Start with the chair. It is not just any rocker. The patent calls for a spring rocking chair. The rockers ride on a fixed base frame, held to it by springs.", quote(CHURN, "the base frame 1 of a spring rocking chair 2", "spring rocking chair", "US 1,051,684 · description"), "calm"),
 ("A pair of extra bars runs under that base and sticks out to one side. On their ends stand two posts with bearings. And between the posts, the churn.", fig(CHURN, "churn2", "2", draw=False, calls=[["POSTS", 70, 300, -40, 60], ["BARS", 300, 412, 40, 60]]), "calm"),
 ("The patent describes it plainly.", quote(CHURN, "which churn body is here shown as barrel-shaped and is adapted to be revolved.", "barrel-shaped", "US 1,051,684 · description"), "calm"),
 ("So the barrel does not slosh. It turns over and over, on an axle.", fig(CHURN, "churn2", "2", draw=False, ring=[220, 200, 260]), "calm"),
 ("Figure two shows it from another side. A sectional view, on the line marked A A in figure one.", quote(CHURN, "Fig. 2 is a sectional view of the same on the plane indicated by the line a—a of Fig. 1.", "sectional view", "US 1,051,684 · description"), "calm"),
 ("Now the clever part. On the end of that axle sits a ratchet wheel. A toothed wheel that can be pushed around in one direction.", fig(CHURN, "churn2", "2", draw=False, vb="300 60 260 260", ring=[414, 168, 130]), "calm"),
 ("Two arms hang on the same axle, one on each side of the wheel.", quote(CHURN, "the arm 12 extending upwardly and the arm 13 extending downwardly.", "upwardly", "US 1,051,684 · description"), "calm"),
 ("Each arm carries a pawl, a small hinged catch. The top pawl drops into the teeth by gravity. The bottom pawl is pressed up into them by a spring.", fig(CHURN, "churn1", "1", draw=False, vb="220 260 260 260", ring=[342, 414, 120]), "calm"),
 ("Then two rods connect the chair's rocker to the arms. One from near the front of the rocker. One from near the back.", fig(CHURN, "churn1", "1", draw=False), "calm"),
 ("The front rod goes to the bottom arm. The back rod goes to the top arm.", fig(CHURN, "churn1", "1", draw=False, vb="120 240 400 330"), "calm"),
 ("Rock one way, and both arms swing together. The top pawl pushes the wheel around. The bottom pawl slips.", fig(CHURN, "churn2", "2", draw=False, vb="300 60 260 260", ring=[414, 168, 130]), "calm"),
 ("Rock back, and they trade jobs. The bottom pawl pushes. The top pawl slips.", fig(CHURN, "churn2", "2", draw=False, vb="300 60 260 260"), "calm"),
 ("Hence, the ratchet wheel is rotated in one direction and causes the churn body to correspondingly rotate.", quote(CHURN, Q_ROT, "in one direction", "US 1,051,684 · description"), "slow"),
 ("So you rock back and forth, and the barrel only ever turns one way. Back and forth becomes round and round. While you sit.", fig(CHURN, "churn1", "1", draw=False, ring=[348, 402, 190]), "calm"),
 ("The chair keeps its usual springs. The patent says so.", quote(CHURN, "The usual springs 20 are employed", "The usual springs", "US 1,051,684 · description"), "calm"),
 ("And the inventor left room to grow. The mechanism, he wrote, may be arranged for operating a churn of any kind.", quote(CHURN, "the churn operating mechanism may be arranged for operating a churn of any kind.", "a churn of any kind", "US 1,051,684 · description"), "slow"),
 ("A churn of any kind. One chair. Any churn.", fig(CHURN, "churn1", "1", draw=False), "punch"),
 ("The patent makes exactly one claim. A ratchet, two rocking arms with pawls, and rods. In combination with a chair rocker.", quote(CHURN, "in combination with a chair rocker, a support therefor", "a chair rocker", "US 1,051,684 · claim"), "calm"),
 ("And it ends the old way.", quote(CHURN, "In testimony whereof I affix my signature in presence of two witnesses.", "two witnesses", "US 1,051,684 · end of specification"), "calm"),
 ("Filed June twenty-eighth, nineteen twelve. Approved January twenty-eighth, nineteen thirteen. Seven months, for a chair that makes butter.", stamp(CHURN, CH_T, CH_F, CH_I, at=5.0), "slow"),
 ("Did anyone build one? The patent doesn't say. But here is what the record does show. The rocking chair was already working. Hard.", fig(CHURN, "churn2", "2", draw=False), "calm"),

 # ---------- bridge · the relatives ----------
 ("Look through the patents of that era, and one title keeps coming back. Fan attachment for rocking-chairs.", dict(g="title", kicker="THE RELATIVES", title="Fan Attachment|for Rocking-Chairs", lines=["1893 · 1895 · 1896 · 1896 · 1897 · 1900", "1911 · 1912 · 1913 · 1915 · 1916 · 1981"], **FANS), "calm"),
 ("At least a dozen U.S. patents carry that title. From eighteen ninety-three, all the way to nineteen eighty-one. The years on screen are the years each one was granted.", dict(g="title", kicker="SAME TITLE · AT LEAST 12 PATENTS", title="Fan Attachment|for Rocking-Chairs", lines=["1893 · 1895 · 1896 · 1896 · 1897 · 1900", "1911 · 1912 · 1913 · 1915 · 1916 · 1981"], **FANS), "calm"),
 ("The idea never changes. You rock. A fan blows on you. You are the motor.", fig(KLINE, "kline1", "1"), "slow"),
 ("Here are five rocking-chair fans. Five people. Same problem. Five completely different machines. Four of them carry that title. Some clamp on. Some bolt on. One stays on the porch.", dict(g="title", kicker="THE RELATIVES", title="Five Fans.|One Chair.", lines=["1895 · 1897 · 1915 · 1916 · 1918"], **FANS), "calm"),

 # ---------- 2 · Weigel 1895 ----------
 ("Relative number one. San Francisco, eighteen ninety-four.", chap("RELATIVE No. 1 OF 5", WEIGEL, "Fan Attachment|for Rocking-Chairs", ["US 538,566", "Filed 1894 · Issued 1895"], "1"), "calm"),
 ("Joel Weigel put a tall rod behind the chair. On top, two big fans. The top of the rod is held to the back of the chair.", fig(WEIGEL, "weigel1", "1", calls=[["FANS", 82, 80, 60, 70], ["ROD", 120, 450, -50, 40]]), "calm"),
 ("The bottom of the rod is twisted into a spiral. Like a corkscrew.", fig(WEIGEL, "weigel45", "4 & 5", ring=[64, 140, 150]), "calm"),
 ("The spiral runs through a slotted nut on the base. When the chair rocks, the rod is pushed up and down through the nut. And the spiral makes it spin.", fig(WEIGEL, "weigel45", "4 & 5", draw=False, ring=[94, 228, 120]), "calm"),
 ("And Mr. Weigel had a goal.", quote(WEIGEL, "render their operation noiseless and, generally, more positive and efficient.", "noiseless", "US 538,566 · description", hide=True), "calm"),
 ("To render their operation noiseless.", quote(WEIGEL, "render their operation noiseless and, generally, more positive and efficient.", "noiseless", "US 538,566 · description", typed=False), "slow"),
 ("So the nut is made of leather, or hard rubber. And the holes around the spiral are cut wide, so that there is no contact between these parts.", quote(WEIGEL, "so that there is no contact between these parts", "no contact", "US 538,566 · description"), "calm"),
 ("Up at the chair back, the rod passes between leather washers. And, the patent promises, there is no noise in this connection, nor any jar.", quote(WEIGEL, "and there is no noise in this connection, nor any jar.", "nor any jar", "US 538,566 · description"), "slow"),
 ("He drew it for two kinds of chair. One on a fixed base. And a common rocker, where a lever with a roller rides on the floor.", fig(WEIGEL, "weigel2", "2", ring=[158, 327, 110]), "calm"),
 ("A spring holds that roller constantly upon the floor.", quote(WEIGEL, "a spring l' which holds the bearing roller constantly upon the floor.", "constantly upon the floor", "US 538,566 · description"), "calm"),
 ("And the lever has a spec of its own.", quote(WEIGEL, "This lever is preferably made of three sided angle iron in cross section", "three sided angle iron", "US 538,566 · description"), "calm"),
 ("The fans themselves have handles. The handles are clamped between two plates at the top of the rod, so the fans can be easily placed in position and removed.", fig(WEIGEL, "weigel1", "1", draw=False, vb="40 0 470 240"), "calm"),
 ("The patent makes three claims. The whole third claim is about how to clamp the fans on.", fig(WEIGEL, "weigel1", "1", draw=False, vb="40 0 470 240", ring=[270, 36, 90]), "calm"),
 ("Quiet, positive and efficient. Approved, eighteen ninety-five.", stamp(WEIGEL, FAN_T, "MAY 10, 1894", "APR. 30, 1895", at=2.4), "slow"),

 # ---------- 3 · Davey 1897 ----------
 ("Relative number two. New York, eighteen ninety-six.", chap("RELATIVE No. 2 OF 5", DAVEY, "Fan Attachment|for Rocking-Chairs", ["US 581,902", "Filed 1896 · Issued 1897"], "2"), "calm"),
 ("Edward Davey used one long rod, set at a slant. Three round fans on top.", fig(DAVEY, "davey1", "1", calls=[["FANS", 414, 60, 120, -10]]), "calm"),
 ("The bottom of the rod sits in a socket at the end of a bar. The bar is pinned to the side of the rocker.", fig(DAVEY, "davey1", "1", draw=False, ring=[342, 800, 120]), "calm"),
 ("Halfway up, the rod thickens into a cylinder, cut with a screw thread of great pitch. It passes through a plate fixed under the seat.", quote(DAVEY, "a screw-thread 12 of great pitch", "great pitch", "US 581,902 · description"), "calm"),
 ("Rock the chair, and the rod slides through the plate. And the thread spins it. Rapidly, says the patent.", fig(DAVEY, "davey1", "1", draw=False, vb="330 330 300 300", ring=[480, 474, 140]), "calm"),
 ("The thread also lets the rod lean a little, forward and back, as it passes through. Because the bar at the bottom swings up and down.", quote(DAVEY, "said rod also has a slight forward and back movement as it passes through the plate 13", "slight forward and back movement", "US 581,902 · description"), "calm"),
 ("Going up is the rocker's job. Coming down is handled by something simpler.", quote(DAVEY, Q_GRAV, "gravity only", "US 581,902 · description", hide=True), "calm"),
 ("The downward movement of the rod being accomplished by gravity only.", quote(DAVEY, Q_GRAV, "gravity only", "US 581,902 · description", typed=False), "slow"),
 ("Which is why the lower part of the rod is made of iron, or other metal. To give it weight.", fig(DAVEY, "davey1", "1", draw=False, ring=[360, 720, 130]), "calm"),
 ("And the patent insists on it. The lower end of said rod should possess considerable weight in order that the device may properly operate.", quote(DAVEY, "the lower end of said rod should possess considerable weight in order that the device may properly operate", "considerable weight", "US 581,902 · description"), "slow"),
 ("A fan powered by you. And by gravity. Approved, eighteen ninety-seven.", stamp(DAVEY, FAN_T, "JULY 22, 1896", "MAY 4, 1897", at=2.6), "slow"),

 # ---------- 4 · Kline 1915 ----------
 ("Relative number three. New Jersey, nineteen fourteen.", chap("RELATIVE No. 3 OF 5", KLINE, "Fan Attachment|for Rocking-Chairs", ["US 1,139,299", "Filed 1914 · Issued 1915"], "3"), "calm"),
 ("William Kline moved the fan up, onto the arm of the chair.", fig(KLINE, "kline1", "1", draw=False, ring=[240, 174, 160]), "calm"),
 ("One half of the patent was assigned to Frank J. Kline, also of Rutherford, New Jersey.", fig(KLINE, "kline1", "1", draw=False), "calm"),
 ("It clamps on with a screw. And it can be readily attached to a rocking chair or removed therefrom whenever it is desired to do so.", quote(KLINE, "can be readily attached to a rocking chair or removed therefrom whenever it is desired to do so.", "readily attached", "US 1,139,299 · description"), "calm"),
 ("Below the fan hangs a pendulum, with a weight on the end.", fig(KLINE, "kline1", "1", draw=False, calls=[["PENDULUM", 240, 330, 80, -40], ["WEIGHT", 240, 430, 90, 40]]), "calm"),
 ("Rock the chair, and the pendulum swings. A curved, toothed rack at its top turns a gear. And from there, it gets busy.", fig(KLINE, "kline2", "2", ring=[112, 232, 150]), "calm"),
 ("Two bevel gears. Two ratchet wheels, with their teeth facing opposite ways. Two spring pawls. A bevel pinion between them. All so the fan turns the same way, whichever way you rock.", fig(KLINE, "kline2", "2", draw=False, vb="20 60 220 340"), "calm"),
 ("The fan sits inside a round wire guard. Facing the person in the chair.", fig(KLINE, "kline3", "3"), "calm"),
 ("The patent explains where the air goes.", quote(KLINE, "produces a current of air directed to the head of the occupant of the rocking chair.", "the head of the occupant", "US 1,139,299 · description"), "calm"),
 ("And it doesn't take much. The slightest rocking movement given to the rocking chair causes a swinging of the pendulum.", quote(KLINE, "the slightest rocking movement given to the rocking chair C causes a swinging of the pendulum", "the slightest rocking movement", "US 1,139,299 · description"), "calm"),
 ("The goal, from the first paragraph: a continuous current of air directed onto the occupant as long as the rocking chair or similar article is rocked.", quote(KLINE, "a continuous current of air directed onto the occupant as long as the rocking chair or similar article is rocked.", "as long as", "US 1,139,299 · description"), "slow"),
 ("As long as you rock. Approved, nineteen fifteen.", stamp(KLINE, FAN_T, "JUNE 5, 1914", "MAY 11, 1915", at=2.0), "slow"),

 # ---------- 5 · Nielsen 1916 ----------
 ("Relative number four. Chicago, nineteen fifteen.", chap("RELATIVE No. 4 OF 5", NIELSEN, "Fan Attachment|for Rocking-Chairs", ["US 1,174,436", "Filed 1915 · Issued 1916"], "4"), "calm"),
 ("Hans Peter Martin Nielsen went vertical. A slotted post is fixed to one rocker. It rises behind the arm of the chair. And on top sits a box, with a fan.", fig(NIELSEN, "nielsen1", "1", calls=[["FAN", 302, 124, -120, -40], ["POST", 640, 700, 90, -40]]), "calm"),
 ("Down at the floor, a rod ends in a roller.", quote(NIELSEN, "that carries a roller 33 that rests upon the floor.", "rests upon the floor", "US 1,174,436 · description"), "calm"),
 ("When the chair rocks backward, the post is drawn toward the floor. The rod pulls a lever. The lever pulls a pawl. The pawl turns the gears. And the gears turn the fan.", fig(NIELSEN, "nielsen1", "1", draw=False, ring=[824, 982, 120]), "calm"),
 ("Inside the box: three shafts, a train of gears and cog wheels, and a pawl, mounted with its own little weight.", fig(NIELSEN, "nielsen5", "5", calls=[["WEIGHT", 647, 66, 70, 40], ["GEARS", 347, 276, -150, 230]]), "calm"),
 ("When the chair rocks forward again, a spring resets the pawl.", quote(NIELSEN, "the spring 23 will raise the pawl out of engagement with the wheel", "raise the pawl", "US 1,174,436 · description"), "calm"),
 ("Ready for the next rock.", fig(NIELSEN, "nielsen5", "5", draw=False, ring=[545, 228, 120]), "calm"),
 ("The promise, from the very first paragraph.", quote(NIELSEN, "a simple and inexpensive mechanism which can readily be attached to a rocking chair", "simple and inexpensive", "US 1,174,436 · description"), "calm"),
 ("Simple. Inexpensive. Three sheets of drawings.", fig(NIELSEN, "nielsen1", "1", draw=False), "punch"),
 ("Approved, March seventh, nineteen sixteen.", stamp(NIELSEN, FAN_T, "JAN. 8, 1915", "MAR. 7, 1916", at=1.2), "slow"),

 # ---------- 6 · Singer 1918 ----------
 ("Relative number five. Peekskill, New York. Nineteen sixteen.", chap("RELATIVE No. 5 OF 5", SINGER, "Chair|Attachment", ["US 1,269,325", "Filed 1916 · Issued 1918"], "5"), "calm"),
 ("Alexander Singer took the fan off the chair entirely. His base plate is secured to the floor, behind the chair.", fig(SINGER, "singer1", "1", ring=[413, 604, 110]), "calm"),
 ("Which floor? The patent offers two.", quote(SINGER, "The base 12 may be secured to the floor of a room, or to the floor of a porch at the point desired", "the floor of a porch", "US 1,269,325 · description"), "calm"),
 ("A post rises from the plate. At the top, a fan. Near the bottom, a crank with a large belt wheel. A belt runs up to the fan.", fig(SINGER, "singer1", "1", draw=False, calls=[["FAN", 413, 64, -150, 20], ["BELT WHEEL", 353, 496, -170, -60]]), "calm"),
 ("Then you set the chair in front of it, back toward the post. And hook one rocker into a loop.", fig(SINGER, "singer3", "3", ring=[126, 126, 150]), "calm"),
 ("Rock, and the rocker works a rod. The rod turns the crank. The belt wheel drives the fan.", fig(SINGER, "singer1", "1", draw=False, ring=[353, 496, 130]), "calm"),
 ("The fan arm is adjustable. It can be moved toward and away from the shaft, according to the desire of the occupant.", quote(SINGER, "said arm can be moved toward and away from the shaft according to the desire of the occupant", "the desire of the occupant", "US 1,269,325 · description"), "calm"),
 ("When you're finished, you unhook the chair, and the fan stays where it is.", quote(SINGER, "from which the chair may be readily removed, when the device is not to be used, and without disturbing the fan device.", "without disturbing the fan device", "US 1,269,325 · description"), "calm"),
 ("And the fan has two jobs.", quote(SINGER, "The fan will produce a sufficiently strong current of air to both cool the occupant and keep flies and other insects away.", "keep flies and other insects away", "US 1,269,325 · description", hide=True), "calm"),
 ("A sufficiently strong current of air to both cool the occupant and keep flies and other insects away.", quote(SINGER, "The fan will produce a sufficiently strong current of air to both cool the occupant and keep flies and other insects away.", "keep flies and other insects away", "US 1,269,325 · description", typed=False), "slow"),
 ("Cooling and fly control. On the porch. Approved in nineteen eighteen.", stamp(SINGER, "CHAIR|ATTACHMENT", "APR. 11, 1916", "JUNE 11, 1918", at=3.0), "slow"),
 ("One more detail. Printed at the bottom of this patent, and of others from those years.", quote(SINGER, "Copies of this patent may be obtained for five cents each", "five cents each", "US 1,269,325 · printed notice", hide=True), "calm"),
 ("Copies of this patent may be obtained for five cents each.", quote(SINGER, "Copies of this patent may be obtained for five cents each", "five cents each", "US 1,269,325 · printed notice", typed=False), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the churn. Every other chair in this video makes a breeze. Alfred Clark's chair makes butter. Runner-up: Edward Davey's fan, whose rod comes down by gravity only.", fig(CHURN, "churn1", "1", draw=False, ring=[348, 402, 190]), "calm"),
 ("And the fans never really stopped. In nineteen eighty-one, the United States granted one more patent. Its title: Fan attachment for rocking chairs. Same idea. Eighty-six years after Joel Weigel's.", dict(g="title", kicker="STILL ROCKING", title="Fan Attachment|for Rocking Chairs", lines=["US 4,277,224 · 1981"], **FANS), "slow"),
 ("Every quote in this video is word for word from the patents. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["1,051,684 · 538,566 · 581,902", "1,139,299 · 1,174,436 · 1,269,325"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
