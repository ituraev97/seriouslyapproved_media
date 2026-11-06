# SERIOUSLY APPROVED · FILE 006 · THE SHELF — "8 Real Hat Patents That Do Way Too Much (All Approved)"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

RACK = P("US 4,080,665", "THE RACKET|[WEARS] A CAP", 1978)
UMB = P("US 1,532,310", "THE HAT|[UMBRELLA]", 1925)
FAN = P("US 3,908,199", "A FAN YOU|CAN [WEAR]", 1975)
BANK = P("US 3,748,660", "THE HAT|[PIGGY BANK]", 1973)
NAV = P("US 4,716,599", "THE CAP THAT|[STEERS]", 1988)
CANDY = P("US 3,813,016", "JELLY BEANS|ON [TOP]", 1974)
TACK = P("US 5,070,546", "A TACKLE BOX|ON YOUR [HEAD]", 1991)
GLOVE = P("US 4,628,543", "THE CAP IS|A [GLOVE]", 1986)

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"PATENT No. {n} OF 8", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="HATS THAT DO|TOO [MUCH]", side="FILE 006 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 006")

GL_T, GL_F, GL_I = "COMBINATION CAP AND|BASEBALL GLOVE", "OCT. 25, 1985", "DEC. 16, 1986"
Q_GL_HAND = "the inner liner 25 is shown as being in the shape of a hand, particularly a right hand"
Q_GL_CARRY = "Unfortunately, the baseball glove is just another personal belonging which must be carried to and from the game"
Q_RK_UNIQUE = "is considered to be entirely unique"
Q_RK_SWEAT = "when the cap may be moist with sweat or the like"
Q_UMB = "enables the hat to maintain its character of a hat even in unfolded condition and to keep a surer hold on the head"
Q_FAN_USE = "Use of the fans has been limited to propelling air and to decorations."
Q_BANK = "I have found that such hats may serve the secondary purpose of a coin bank."
Q_NAV_WRONG = "However, many persons who navigate private boats become confused and take buoys on the wrong side."
Q_CANDY = "A child also likes to have his hands free and enjoys wearing ornaments of any kind."
Q_TACK_BIG = "the container may be larger than the head of the wearer and serve as a sun shade as well as storage container"

LINES = [
 # ---------- cold open ----------
 ("This is a baseball cap. Look underneath.", fig(GLOVE, "glove2", "2"), "slow"),
 ("Stitched inside the crown, in the shape of a hand, is a glove.", fig(GLOVE, "glove2", "2", draw=False, calls=[["GLOVE", 366, 240, 70, -70]]), "calm"),
 ("It was approved.", stamp(GLOVE, GL_T, GL_F, GL_I), "punch"),
 ("Somebody invented it. Somebody filed it. And the United States Patent Office said yes. Today, eight real patents for hats that do way too much. A hat is supposed to sit on your head. These ones have other plans.", dict(g="title", kicker="THE SHELF · FILE 006", title="8 Real Hat Patents|That Do Too Much", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=7.0, **INTRO), "calm"),

 # ---------- 1 · tennis racket cover ----------
 ("Number one. The tennis court.", chap(1, RACK, "Combination Tennis Racket|Cover and Cap or Hat", ["US 4,080,665", "Filed 1976 · Issued 1978"]), "calm"),
 ("This is a tennis racket in its cover. Nothing unusual. Yet.", fig(RACK, "rack1", "1"), "calm"),
 ("The patent starts with what everybody already knows. Various types of caps and hats are, of course, also well known.", quote(RACK, "Various types of caps and hats are, of course, also well known.", "of course", "US 4,080,665 · prior art"), "calm"),
 ("But putting the two together, it says, is considered to be entirely unique.", quote(RACK, Q_RK_UNIQUE, "entirely unique", "US 4,080,665 · prior art"), "slow"),
 ("Here is how. The cover comes in two parts. Unzip one side of the cover, and that side is a cap.", fig(RACK, "rack2", "2", calls=[["CAP", 312, 132, 80, -50], ["COVER", 312, 522, 80, 50]]), "calm"),
 ("The bill zips onto the cover. The crown is crushable, so it folds flat over the racket.", fig(RACK, "rack2", "2", draw=False), "calm"),
 ("Take it off, and it goes on your head. Snap fasteners in the back provide an adjustment for head size.", fig(RACK, "rack3", "3", calls=[["SAME CAP", 192, 78, 70, -40]]), "calm"),
 ("In the patent's words, the user need only detach a part of the tennis racket cover from it to be provided with a hat or cap suitable for play.", quote(RACK, "the user need only detach a part of the tennis racket cover from it to be provided with a hat or cap suitable for play", "suitable for play", "US 4,080,665 · summary"), "calm"),
 ("There is also a hat version, with a full brim. A draw string collapses the crown to a flat condition, and the brim zips around the racket.", fig(RACK, "rack9", "9"), "calm"),
 ("One more detail. A flap of fabric keeps the cap away from the springs of the racket.", quote(RACK, Q_RK_SWEAT, "moist with sweat", "US 4,080,665 · col. 3", hide=True), "calm"),
 ("When the cap may be moist with sweat or the like.", quote(RACK, Q_RK_SWEAT, "moist with sweat", "US 4,080,665 · col. 3", typed=False), "slow"),
 ("So after the match, the sweaty cap goes back on the racket. Approved, nineteen seventy-eight.", stamp(RACK, "COMBINATION TENNIS RACKET|COVER AND CAP OR HAT", "OCT. 12, 1976", "MAR. 28, 1978", at=2.4), "slow"),

 # ---------- 2 · umbrella hat ----------
 ("Number two. The weather.", chap(2, UMB, "Hat Convertible|into Umbrella", ["US 1,532,310", "Filed 1920 · Issued 1925"]), "calm"),
 ("This is a lady's hat from nineteen twenty-five. Its brim is not finished. It keeps going.", fig(UMB, "umb1", "1"), "calm"),
 ("The goal, in the patent's words: a hat which can be transformed into an umbrella or parasol by unfolding the same.", quote(UMB, "a hat which can be transformed into an umbrella or parasol by unfolding the same", "umbrella or parasol", "US 1,532,310 · p. 1"), "calm"),
 ("Inside the hat is a frame. Rods, hinged in two parts, like the ribs of an umbrella. And this frame is covered like an umbrella.", fig(UMB, "umb4", "4"), "calm"),
 ("If opened entirely or even only halfway outwards, the hat protects from rain or sunshine.", quote(UMB, "If opened entirely or even only halfway outwards, the hat protects from rain or sunshine", "rain or sunshine", "US 1,532,310 · p. 1"), "calm"),
 ("The idea is speed. This enables the device to be ready for use at any moment and instantaneously.", quote(UMB, "This enables the device to be ready for use at any moment and instantaneously", "instantaneously", "US 1,532,310 · p. 1"), "calm"),
 ("Fold it entirely together, and the patent says you get the form of a toque. Fold in only a few segments, and you get another shape. Stand all the rods straight up, and you get a pointed shape, for instance.", fig(UMB, "umb2", "2"), "calm"),
 ("And unlike other umbrella hats, this one never stops being a hat.", quote(UMB, Q_UMB, "surer hold on the head", "US 1,532,310 · p. 1", hide=True), "calm"),
 ("It enables the hat to maintain its character of a hat even in unfolded condition, and to keep a surer hold on the head.", quote(UMB, Q_UMB, "surer hold on the head", "US 1,532,310 · p. 1", typed=False), "slow"),
 ("Filed in nineteen twenty. Approved almost four and a half years later. Ready for use at any moment.", stamp(UMB, "HAT CONVERTIBLE|INTO UMBRELLA", "NOV. 12, 1920", "APR. 7, 1925", at=3.2), "slow"),

 # ---------- 3 · fan hat ----------
 ("Number three. The heat.", chap(3, FAN, "Fan Hat|Apparatus", ["US 3,908,199", "Filed 1974 · Issued 1975"]), "calm"),
 ("This is a folding hand fan. Closed. The ribs have a strange bend in them.", fig(FAN, "fan1", "1"), "calm"),
 ("The patent opens with a short history. Folding hand fans are well known.", quote(FAN, "Folding hand fans are well known.", "well known", "US 3,908,199 · background"), "calm"),
 ("They are useful for holding in a hand and moving back and forth to propel air currents toward the face. Usually the folding fans are highly decorative.", quote(FAN, "useful for holding in a hand and moving back and forth to propel air currents toward the face", "toward the face", "US 3,908,199 · background"), "calm"),
 ("And then it identifies the problem.", quote(FAN, Q_FAN_USE, "limited", "US 3,908,199 · background", hide=True), "calm"),
 ("Use of the fans has been limited to propelling air and to decorations.", quote(FAN, Q_FAN_USE, "limited", "US 3,908,199 · background", typed=False), "slow"),
 ("Open it partway, and it works as a fan.", fig(FAN, "fan2", "2"), "calm"),
 ("Keep opening, all the way around in a full circle. Snap the last rib to the first one. The bends become a crown and a brim.", fig(FAN, "fan3", "3"), "calm"),
 ("The present invention creates from a hand fan a unique readily collapsible hat.", quote(FAN, "The present invention creates from a hand fan a unique readily collapsible hat.", "collapsible hat", "US 3,908,199 · summary"), "calm"),
 ("There is also a sport model. The middle ribs are longer, producing a beak-like sport hat brim. A sport cap, made of fan.", fig(FAN, "fan7", "7"), "calm"),
 ("And the patent notes that the crown is formed of adjacent flat ribs and is well vented.", quote(FAN, "Crown 72 of the hat is formed of adjacent flat ribs and is well vented.", "well vented", "US 3,908,199 · col. 4"), "slow"),
 ("Fan when you're hot. Hat when you're also hot. Approved, nineteen seventy-five.", stamp(FAN, "FAN HAT|APPARATUS", "AUG. 22, 1974", "SEPT. 30, 1975", at=2.6), "slow"),

 # ---------- 4 · coin bank hats ----------
 ("Number four. The party.", chap(4, BANK, "Miniature|Hats", ["US 3,748,660", "Filed 1971 · Issued 1973"]), "calm"),
 ("This is a man wearing a very small derby hat.", fig(BANK, "bank1", "1", calls=[["HAT", 274, 116, 80, -40]]), "calm"),
 ("The patent explains the business. Certain restaurant chains sell or give away plastic hats for use by customers to provide a carnival atmosphere.", quote(BANK, "certain restaurant chains sell or give away plastic hats for use by customers to provide a carnival atmosphere", "carnival atmosphere", "US 3,748,660 · summary"), "calm"),
 ("The plan is that customers may collect a complete selection of hat styles by regularly patronizing a restaurant.", quote(BANK, "customers may collect a complete selection of hat styles by regularly patronizing a restaurant", "regularly patronizing", "US 3,748,660 · summary"), "calm"),
 ("But a hat that is merely for decorative purposes was not enough. It is also desirable that they have a secondary use.", quote(BANK, Q_BANK, "coin bank", "US 3,748,660 · summary", hide=True), "calm"),
 ("I have found that such hats may serve the secondary purpose of a coin bank.", quote(BANK, Q_BANK, "coin bank", "US 3,748,660 · summary", typed=False), "slow"),
 ("Inside the hat, a paperboard plug with a slot. The slot is preferably long enough to accommodate a coin of fifty cent denomination.", fig(BANK, "bank4", "4", calls=[["COIN SLOT", 225, 210, 80, 60]]), "calm"),
 ("The rubber band that holds the hat on your head also runs across the slot. Push a coin in, and the band flexes. Then it snaps back.", fig(BANK, "bank7", "7", calls=[["PLUG", 282, 180, 90, 60]]), "calm"),
 ("So the coins are kept from being shaken or otherwise removed from the body of the hat. While you wear it.", quote(BANK, "prevents the coins within the hat from being shaken or otherwise removed from the body of the hat", "shaken", "US 3,748,660 · col. 4"), "calm"),
 ("There is a top hat version too. With stars.", fig(BANK, "bank5", "5"), "calm"),
 ("And the hats nest together, for cheap shipping.", fig(BANK, "bank9", "9"), "calm"),
 ("A party hat that saves your money, on your head. Approved, nineteen seventy-three.", stamp(BANK, "MINIATURE|HATS", "MAR. 17, 1971", "JULY 31, 1973", at=2.2), "slow"),

 # ---------- 5 · navigation cap ----------
 ("Number five. The boat.", chap(5, NAV, "Reversible Cap Used|as Navigational Aid", ["US 4,716,599", "Filed 1981 · Issued 1988"]), "calm"),
 ("On the water, buoys are red or black. And you have to pass them on the correct side.", fig(NAV, "nav3", "3"), "calm"),
 ("Many helmsmen refer to the phrase, red, right, return.", quote(NAV, 'Many helmsmen refer to the phrase "red, right, return"', "red, right, return", "US 4,716,599 · background"), "calm"),
 ("But the patent has noticed something.", quote(NAV, Q_NAV_WRONG, "wrong side", "US 4,716,599 · background", hide=True), "calm"),
 ("However, many persons who navigate private boats become confused and take buoys on the wrong side.", quote(NAV, Q_NAV_WRONG, "wrong side", "US 4,716,599 · background", typed=False), "slow"),
 ("What is needed, it says, is a means by which even an unexperienced helmsman may be afforded a rapid reference.", quote(NAV, "even an unexperienced helmsman", "unexperienced", "US 4,716,599 · background"), "calm"),
 ("The solution is a cap. Split down the middle. One half red, one half black. Inside and out.", fig(NAV, "nav12", "1 · 2"), "calm"),
 ("Heading out, you wear it with the tag that says leaving harbor. Coming back, you turn the cap inside out. Now the tag says red right returning.", fig(NAV, "nav12", "1 · 2", draw=False, calls=[["LEAVING HARBOR", 281, 485, -60, 90], ["RED RIGHT RETURNING", 845, 527, -170, 120]]), "calm"),
 ("The visor is long, so you can see the colors under it without looking up. Even through the upper lens portions of a pair of glasses.", quote(NAV, "through the upper lens portions of a pair of glasses worn by the wearer of the hat", "upper lens portions", "US 4,716,599 · col. 3"), "calm"),
 ("And the colors on the outside let other people check whether the helmsman has the hat properly positioned on his head.", quote(NAV, "whether the helmsman of the boat has the hat properly positioned on his head", "properly positioned", "US 4,716,599 · objects"), "calm"),
 ("The patent also hopes it will be substantially automatic in operation. It is a hat.", quote(NAV, "be of simple construction and substantially automatic in operation", "substantially automatic", "US 4,716,599 · objects"), "slow"),
 ("Filed in nineteen eighty-one. Approved in nineteen eighty-eight.", stamp(NAV, "REVERSIBLE CAP USED AS|NAVIGATIONAL AID", "DEC. 28, 1981", "JAN. 5, 1988", at=2.6), "slow"),

 # ---------- 6 · candy cap ----------
 ("Number six. The snack.", chap(6, CANDY, "Candy Container Removably|Connected to a Child's Cap", ["US 3,813,016", "Filed 1973 · Issued 1974"]), "calm"),
 ("The patent begins with a fact. Children like to eat jelly beans.", quote(CANDY, "Children like to eat jelly beans", "jelly beans", "US 3,813,016 · background"), "calm"),
 ("So the container is made in the shape of a greatly enlarged jelly bean. And it goes on top of a cap.", fig(CANDY, "candy1", "1", calls=[["JELLY BEAN", 342, 114, 90, -40]]), "calm"),
 ("Why the cap? Because a child also likes to have his hands free and enjoys wearing ornaments of any kind.", quote(CANDY, Q_CANDY, "ornaments of any kind", "US 3,813,016 · background"), "calm"),
 ("The bean sits on a universal joint. It can be swung into any angular position desired.", fig(CANDY, "candy1", "1", draw=False, calls=[["JOINT", 346, 332, -90, 40]]), "calm"),
 ("To get a snack, you pull the bean off your head. A cord unwinds from a spring-loaded drum inside the cap.", fig(CANDY, "candy2", "2", calls=[["DRUM", 189, 208, 80, 60]]), "calm"),
 ("The cord means the bean is never far away. It will prevent the container from becoming lost.", quote(CANDY, "will prevent the container from becoming lost", "becoming lost", "US 3,813,016 · summary"), "calm"),
 ("Open the lid, eat, close the lid. Put the bean back on top, jerk on the cord, and the drum winds up the extra cord.", fig(CANDY, "candy1", "1", draw=False, calls=[["CORD", 858, 395, 60, 60]]), "calm"),
 ("Even the air vents in the cap may be shaped like a jelly bean, so as to have the same shape as the container, but on a much smaller scale.", quote(CANDY, "may be shaped like a jelly bean so as to have the same shape as the container C, but on a much smaller scale", "much smaller scale", "US 3,813,016 · col. 3"), "calm"),
 ("And one line in the operation section is worth reading slowly.", quote(CANDY, "The jelly bean shaped container C may have jelly beans therein if desired.", "if desired", "US 3,813,016 · operation", hide=True), "calm"),
 ("The jelly bean shaped container may have jelly beans therein. If desired.", quote(CANDY, "The jelly bean shaped container C may have jelly beans therein if desired.", "if desired", "US 3,813,016 · operation", typed=False), "slow"),
 ("Optional jelly beans. Approved, nineteen seventy-four.", stamp(CANDY, "CANDY CONTAINER REMOVABLY|CONNECTED TO A CHILD'S CAP", "FEB. 9, 1973", "MAY 28, 1974", at=1.8), "slow"),

 # ---------- 7 · tackle box hat ----------
 ("Number seven. The lake.", chap(7, TACK, "Container for|Mounting on Headgear", ["US 5,070,546", "Filed 1990 · Issued 1991"]), "calm"),
 ("The patent opens with a census. There are thousands of types of tackle boxes for fishing gear.", quote(TACK, "There are thousands of types of tackle boxes for fishing gear.", "thousands", "US 5,070,546 · related art"), "calm"),
 ("Every type of container from old cigar boxes to the most sophisticated space age construction has been used to store tackle.", quote(TACK, "Every type of container from old cigar boxes to the most sophisticated space age construction has been used to store tackle.", "space age", "US 5,070,546 · related art"), "calm"),
 ("But for the wade fisherman, storage space is at a premium. So here is one more. A small plastic box, with compartments and a lid.", fig(TACK, "tackle1", "1"), "calm"),
 ("Cuts in the bottom snap over the button on top of a baseball cap. At approximately the apogee of the headgear.", fig(TACK, "tackle2", "2", calls=[["BUTTON", 520, 160, 80, 60]]), "calm"),
 ("The lid has a latch. Because the person wearing the cap is going to move about, and look down.", quote(TACK, "the person wearing the cap is going to move about, and look down", "look down", "US 5,070,546 · description"), "calm"),
 ("The box may be about four inches square and be comfortable to wear. Boxes larger than that can be worn, but they become unwieldy. Smaller boxes have less utility.", quote(TACK, "Boxes larger than that can be worn but they become unwieldy.", "unwieldy", "US 5,070,546 · description"), "calm"),
 ("Although, in some cases, the patent allows a bigger one.", quote(TACK, Q_TACK_BIG, "larger than the head", "US 5,070,546 · description", hide=True), "calm"),
 ("The container may be larger than the head of the wearer, and serve as a sun shade as well as storage container.", quote(TACK, Q_TACK_BIG, "larger than the head", "US 5,070,546 · description", typed=False), "slow"),
 ("And it is not only for fishing. The same button holds a tiny baseball cap. On top of your baseball cap. Or a miniature football helmet, for football season.", fig(TACK, "tackle5", "5", calls=[["MINI CAP", 400, 80, 100, 40]]), "calm"),
 ("A box on a hat. Approved, nineteen ninety-one.", stamp(TACK, "CONTAINER FOR MOUNTING|ON HEADGEAR", "JUNE 12, 1990", "DEC. 10, 1991", at=1.6), "slow"),

 # ---------- 8 · cap and glove ----------
 ("Number eight. The ballpark.", chap(8, GLOVE, "Combination Cap|and Baseball Glove", ["US 4,628,543", "Filed 1985 · Issued 1986"]), "calm"),
 ("At a game, the patent observes, balls are hit into spectator seating areas. So fans bring a glove.", quote(GLOVE, "balls are hit into spectator seating areas", "spectator seating", "US 4,628,543 · history"), "calm"),
 ("And that is the problem.", quote(GLOVE, Q_GL_CARRY, "just another personal belonging", "US 4,628,543 · history", hide=True), "calm"),
 ("Unfortunately, the baseball glove is just another personal belonging which must be carried to and from the game.", quote(GLOVE, Q_GL_CARRY, "just another personal belonging", "US 4,628,543 · history", typed=False), "slow"),
 ("An item which is subject to theft or accidental misplacement if left unattended.", quote(GLOVE, "subject to theft or accidental misplacement if left unattended", "accidental misplacement", "US 4,628,543 · history"), "calm"),
 ("The solution looks like any other cap. A person may wear the cap on their head just as they would any other conventional cap.", fig(GLOVE, "glove1", "1"), "calm"),
 ("But inside, the inner liner is shown as being in the shape of a hand. Particularly a right hand. With finger cavities and a thumb cavity.", fig(GLOVE, "glove2", "2", calls=[["HAND", 366, 240, 70, -70], ["OPENING", 534, 258, 60, 60]]), "calm"),
 ("When a ball comes your way, you need only insert your hand through the opening in the back of the cap. Then take it off your head and catch.", quote(GLOVE, "a person need only insert their hand through the opening formed in the back of the cap", "insert their hand", "US 4,628,543 · col. 4"), "calm"),
 ("There is also a mitt version. And pockets inside for extra padding.", fig(GLOVE, "glove3", "3", calls=[["MITT", 264, 222, 80, 60]]), "calm"),
 ("Why not put the fingers on the outside? The patent considered it. The disadvantage is that the cap would not resemble a traditional or conventional cap.", quote(GLOVE, "is that the cap would not resemble a traditional or conventional cap", "would not resemble", "US 4,628,543 · col. 4"), "calm"),
 ("So the glove hides inside the hat. For selective use as a cap for covering a person's head, or a baseball glove.", quote(GLOVE, "for selective use as a cap for covering a person's head or a baseball glove", "or a baseball glove", "US 4,628,543 · claim 1"), "slow"),
 ("Two things, one hat. Approved, nineteen eighty-six.", stamp(GLOVE, GL_T, GL_F, GL_I, at=1.8), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the navigation cap. Because it took just over six years from filing to approval, for a hat that is half red, half black, and goes on inside out when you come home.", fig(NAV, "nav12", "1 · 2", draw=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["4,080,665 · 1,532,310 · 3,908,199", "3,748,660 · 4,716,599 · 3,813,016", "5,070,546 · 4,628,543"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
