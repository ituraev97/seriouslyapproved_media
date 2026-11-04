# SERIOUSLY APPROVED · FILE 004 · THE SHELF — "8 Real Patents for Very Lazy People (All Approved)"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

SCR = P("US 4,091,805", "A HAND|ON A [STICK]", 1978)
ICE = P("US 4,850,843", "THE [POWER]|SCOOP", 1989)
GOLF = P("US 2,943,856", "NEVER [BEND]|OVER AGAIN", 1960)
LAWN = P("US 2,941,346", "THE [REMOTE]|LAWN MOWER", 1960)
GROOM = P("US 5,540,186", "THE PET|[BRUSHES ITSELF]", 1996)
BED = P("US 2,930,053", "THE BED THAT|[MAKES ITSELF]", 1960)
FORK = P("US 5,062,211", "THE [MOTORIZED]|PASTA FORK", 1991)
CHAIR = P("US 4,719,764", "A FRIDGE|IN THE [CHAIR]", 1988)

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"PATENT No. {n} OF 8", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="FOR VERY|[LAZY] PEOPLE", side="FILE 004 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 004")

CH_T, CH_F, CH_I = "CHAIR WITH REFRIGERATOR AND|ARMREST BEVERAGE COOLER", "AUG. 18, 1986", "JAN. 19, 1988"
Q_TV = "to enjoy television or merely relax and consume beverages and related products without getting out of the chair"
Q_ICE = "The user must struggle to dislodge a scoop or just wait until the ice cream warms sufficiently to soften."
Q_GOLF = "while the player remains in a straight, upstanding position"
Q_HUMAN = "Most animals will remain appreciative for extended periods of time, when brushes are moved against their bodies by the human hand."
Q_KICK = "kicked-out covers may be automatically re-tucked into place by the bed occupant merely by flipping a switch"
Q_EMB = "causing embarrassment to the user"
Q_CIRCLE = "When the entire area has been cut the mower will merely propel itself in a tight circle"

LINES = [
 # ---------- cold open ----------
 ("This is an armchair. With a refrigerator in it.", fig(CHAIR, "chair1", "1"), "slow"),
 ("A cold can sits in the armrest. More cans wait behind a little door in the side. You never have to stand up.", fig(CHAIR, "chair1", "1", draw=False, calls=[["CAN HOLDER", 363, 328, 60, -60], ["FRIDGE", 258, 450, -60, 60]]), "calm"),
 ("It was approved.", stamp(CHAIR, CH_T, CH_F, CH_I), "punch"),
 ("Somebody invented it. Somebody filed it. And the United States Patent Office said yes. Today, eight real patents for very lazy people. Every one of them took more effort than the thing it saves.", dict(g="title", kicker="THE SHELF · FILE 004", title="8 Real Patents for|Very Lazy People", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=7.0, **INTRO), "calm"),

 # ---------- 1 · back scratcher ----------
 ("Number one. The itch.", chap(1, SCR, "Vibrating|Back Scratcher", ["US 4,091,805", "Filed 1977 · Issued 1978"]), "calm"),
 ("This is a man with an itch. And this is his solution.", fig(SCR, "scr1", "1"), "calm"),
 ("The drawing shows it in use. Over the shoulder. The hand lands on the back.", fig(SCR, "scr1", "1", draw=False, calls=[["HAND", 120, 312, -80, 40]]), "calm"),
 ("A rod. On one end, a handle. On the other end, a hand.", fig(SCR, "scr2", "2", calls=[["HAND", 186, 66, 0, 70], ["HANDLE", 906, 66, 0, 70]]), "calm"),
 ("Not a real one. An artificial hand, made of any suitable material such as, for example, plastic.", quote(SCR, "of any suitable material such as, for example, plastic", "plastic", "US 4,091,805 · description"), "calm"),
 ("And the patent is specific about the fingers.", quote(SCR, "has a plurality of fingers bent in scratching position and a wrist", "bent in scratching position", "US 4,091,805 · description", hide=True), "calm"),
 ("It has a plurality of fingers bent in scratching position. And a wrist.", quote(SCR, "has a plurality of fingers bent in scratching position and a wrist", "bent in scratching position", "US 4,091,805 · description", typed=False), "slow"),
 ("Inside the handle, an electric vibrator and a rechargeable battery. Press the switch, and the hand vibrates back and forth along the rod.", quote(SCR, "for vibrating the rod in axial directions", "axial directions", "US 4,091,805 · description"), "calm"),
 ("To recharge it, a cord comes out of the end of the handle. So that it is readily extended to an electric wall outlet.", quote(SCR, "so that it is readily extended to an electric wall outlet for the recharging power", "electric wall outlet", "US 4,091,805 · description"), "calm"),
 ("The objects of the invention: a back scratcher of simple structure, which is inexpensive in manufacture, used with facility, convenience and safety.", quote(SCR, "used with facility, convenience and safety", "with facility", "US 4,091,805 · background"), "calm"),
 ("The goal, in the patent's words: it functions efficiently, effectively and reliably to scratch the back of a user.", quote(SCR, "functions efficiently, effectively and reliably to scratch the back of a user", "scratch the back of a user", "US 4,091,805 · background"), "slow"),
 ("A plastic hand that shakes. Approved, nineteen seventy-eight.", stamp(SCR, "VIBRATING|BACK SCRATCHER", "MAR. 18, 1977", "MAY 30, 1978", at=1.8), "slow"),

 # ---------- 2 · ice cream server ----------
 ("Number two. Dessert.", chap(2, ICE, "Ice Cream|Server", ["US 4,850,843", "Filed 1988 · Issued 1989"]), "calm"),
 ("The patent begins with a hardship.", quote(ICE, Q_ICE, "just wait", "US 4,850,843 · background", hide=True), "calm"),
 ("The user must struggle to dislodge a scoop. Or just wait until the ice cream warms sufficiently to soften.", quote(ICE, Q_ICE, "just wait", "US 4,850,843 · background", typed=False), "slow"),
 ("Waiting is not an option. So: a motorized ice cream scoop.", fig(ICE, "ice1", "1"), "calm"),
 ("A handle with batteries. A motor. And a bowl that spins, with saw teeth around the edge.", fig(ICE, "ice1", "1", draw=False, calls=[["MOTOR", 294, 354, -80, -40], ["SAW TEETH", 337, 630, 90, 30]]), "calm"),
 ("The teeth cut into the ice cream at the push of a button.", quote(ICE, "cut into the ice cream at the push of a button", "push of a button", "US 4,850,843 · summary"), "calm"),
 ("Where does the motor come from? A reversible motor, such as the type utilized in commercially available battery-powered screwdrivers.", quote(ICE, "such as the type utilized in commercially available battery-powered screwdrivers", "battery-powered screwdrivers", "US 4,850,843 · description"), "slow"),
 ("The motor head tilts. Straight down for deep containers. Sideways when there is plenty left.", fig(ICE, "ice23", "2 & 3"), "calm"),
 ("The handle is about twenty centimeters long. Of course, the patent adds, these dimensions are not critical.", quote(ICE, "Of course, these dimensions are not critical", "not critical", "US 4,850,843 · description"), "calm"),
 ("It sits on a charging stand. The contacts attract each other magnetically. And the switch seals against moisture and water when washed.", quote(ICE, "seals against moisture/water when washed", "when washed", "US 4,850,843 · description"), "calm"),
 ("The verdict, from the patent: the ice cream server makes the scooping of hard ice cream far more convenient.", quote(ICE, "Thus, the ice cream server makes the scooping of hard ice cream far more convenient.", "far more convenient", "US 4,850,843 · summary"), "calm"),
 ("Especially, it adds, if the ice cream is hard and the container nearly empty.", quote(ICE, "especially if the ice cream is hard and the container nearly empty", "nearly empty", "US 4,850,843 · description"), "slow"),
 ("A power tool for dessert. Approved, nineteen eighty-nine.", stamp(ICE, "ICE CREAM|SERVER", "AUG. 9, 1988", "JUL. 25, 1989", at=1.8), "slow"),

 # ---------- 3 · golf tee ----------
 ("Number three. The golf course.", chap(3, GOLF, "Golf Ball and Tee|Handling Devices", ["US 2,943,856", "Filed 1958 · Issued 1960"]), "calm"),
 ("Golf has one move that nobody talks about. You have to bend down to put the ball on the tee.", fig(GOLF, "golf12", "1 & 2"), "calm"),
 ("This patent has one goal. You never bend down. In its words: without stooping or bending over, the player may then press downwardly upon the handle.", quote(GOLF, "Without stooping or bending over, the player may then press downwardly upon the handle", "Without stooping or bending over", "US 2,943,856 · description"), "calm"),
 ("The device fits onto the handle end of a conventional golf club. A cup holds the ball. Two little arms grip the tee underneath.", fig(GOLF, "golf12", "1 & 2", draw=False, calls=[["BALL", 606, 252, 80, -40], ["TEE", 232, 470, -70, 50]]), "calm"),
 ("You push the club into the ground. The tee goes in. A plunger hits the grass, and the arms open.", fig(GOLF, "golf4", "4"), "calm"),
 ("And there it is. The tee in the ground, the ball on top, in readiness for use.", quote(GOLF, "in readiness for use", "in readiness for use", "US 2,943,856 · description"), "calm"),
 ("All this, the patent says, while the player remains in a straight, upstanding position.", quote(GOLF, Q_GOLF, "straight, upstanding position", "US 2,943,856 · description"), "slow"),
 ("There is also a hook for pulling the tee back out. Also without the necessity of stooping or bending over for that purpose.", quote(GOLF, "also without the necessity of stooping or bending over for that purpose", "for that purpose", "US 2,943,856 · description"), "calm"),
 ("And when you're done, it clips to your golf bag. Or to wearing apparel of the player.", quote(GOLF, "the device may be attached to a golf bag or to wearing apparel of the player", "wearing apparel", "US 2,943,856 · description"), "calm"),
 ("Its other advantages, according to the patent: small size, easy portability, and its adaptability to economical manufacture.", quote(GOLF, "in its adaptability to economical manufacture", "economical manufacture", "US 2,943,856 · description"), "calm"),
 ("Standing straight. Approved, nineteen sixty.", stamp(GOLF, "GOLF BALL AND TEE|HANDLING DEVICES", "MAR. 20, 1958", "JUL. 5, 1960", at=1.6), "slow"),

 # ---------- 4 · remote lawn mower ----------
 ("Number four. The lawn. Nineteen fifty-three.", chap(4, LAWN, "Remote Control|of a Lawn Mower", ["US 2,941,346", "Filed 1953 · Issued 1960"]), "calm"),
 ("An electric lawn mower. A long cable. And at the other end of the cable, a little box with a knob.", fig(LAWN, "lawn2", "2", calls=[["CONTROL BOX", 828, 612, -60, -80]]), "calm"),
 ("You stay at the box. The mower goes out on the lawn.", fig(LAWN, "lawn2", "2", draw=False), "calm"),
 ("The patent knows this is hard. Remote control, requiring positive and certain action, in general involves complex instrumentation.", quote(LAWN, "Remote control, requiring positive and certain action, in general involves complex instrumentation.", "complex instrumentation", "US 2,941,346 · col. 1"), "calm"),
 ("No radio. The signal travels down the power cable itself. The mower steers by stopping one wheel or the other.", quote(LAWN, "does not require complex instrumentation, separate control circuits, or the use of radio", "the use of radio", "US 2,941,346 · col. 1"), "calm"),
 ("Why a knob? Moving a control to the left or right, the patent explains, may be confusing. Depending on where the mower is.", quote(LAWN, "may be confusing", "may be confusing", "US 2,941,346 · col. 4"), "calm"),
 ("And steering is simple. Mere rotation of control knob thirteen c will cause corresponding rotation of the mower.", quote(LAWN, "Mere rotation of control knob 13c will cause corresponding “rotation” of the mower.", "corresponding “rotation”", "US 2,941,346 · col. 7"), "calm"),
 ("A reel on top winds the cable back in. Preventing entanglement of the mower in the cable strands.", fig(LAWN, "lawn3", "3", calls=[["CABLE REEL", 444, 66, 90, 30]]), "calm"),
 ("And then there is the optional extra. Feeler arms that sense uncut grass. The patent calls it an automatic grass hunting system.", quote(LAWN, "automatic grass hunting system", "grass hunting", "US 2,941,346 · col. 7"), "slow"),
 ("The mower will thus guide itself around a given plot. One swath at a time. And at the end?", fig(LAWN, "lawn4", "4", calls=[["FEELER ARMS", 258, 474, 60, -80]]), "calm"),
 ("When the entire area has been cut the mower will merely propel itself in a tight circle.", quote(LAWN, Q_CIRCLE, "a tight circle", "US 2,941,346 · col. 7"), "slow"),
 ("Filed in nineteen fifty-three. The lawn waited almost seven years. Approved, nineteen sixty.", stamp(LAWN, "METHOD AND APPARATUS FOR THE|REMOTE CONTROL OF A LAWN MOWER", "NOV. 2, 1953", "JUN. 21, 1960", at=2.8), "slow"),

 # ---------- 5 · self grooming ----------
 ("Number five. The pets.", chap(5, GROOM, "Mechanically Assisted Animal|Self Grooming Device", ["US 5,540,186", "Filed 1994 · Issued 1996"]), "calm"),
 ("The patent opens with a problem. Every grooming device so far needs a person. All of these devices require human assistance to be useful.", quote(GROOM, "all of these devices require human assistance to be useful", "human assistance", "US 5,540,186 · prior art"), "calm"),
 ("And it admits why people bother.", quote(GROOM, Q_HUMAN, "appreciative for extended periods", "US 5,540,186 · summary", hide=True), "calm"),
 ("Most animals will remain appreciative for extended periods of time, when brushes are moved against their bodies by the human hand.", quote(GROOM, Q_HUMAN, "appreciative for extended periods", "US 5,540,186 · summary", typed=False), "slow"),
 ("So the human hand is replaced. A round base. A motor. And a tall brush that turns by itself.", fig(GROOM, "groom1a", "1a", calls=[["BRUSH", 474, 372, 100, 0], ["MOTOR", 522, 612, 100, 20]]), "calm"),
 ("Ten to fifteen revolutions per minute. To simulate the brushing movements of the human hand.", quote(GROOM, "to simulate the brushing movements of the human hand", "the human hand", "US 5,540,186 · summary"), "calm"),
 ("It runs on low voltage. Harmless to an animal upon chewing into the line cord. And a sensor can start it automatically. Motion, heat, or optical.", quote(GROOM, "harmless to an animal upon chewing into the line cord", "chewing into the line cord", "US 5,540,186 · description"), "calm"),
 ("On top, a lure on a spring, constantly moving in circles. In the drawing, the lure is a mouse.", fig(GROOM, "groom1a", "1a", draw=False, ring=[486, 48, 170]), "calm"),
 ("One version even has a speaker. With prerecorded sounds of a mouse, or a human talking to an animal.", quote(GROOM, "sounds of a mouse, or a human talking to an animal", "a human talking to an animal", "US 5,540,186 · description"), "slow"),
 ("As an incentive for an animal to frequent the device more often.", quote(GROOM, "as an incentive for an animal to frequent the device more often", "more often", "US 5,540,186 · description"), "calm"),
 ("The floor has slots that catch the loose hair. Protecting the living environment from unnecessary animal hair.", fig(GROOM, "groom1b", "1b"), "calm"),
 ("And one more object, listed on its own. Yet another object is that the present invention produces a synergistic effect.", quote(GROOM, "Yet another object is that the present invention produces a synergistic effect.", "synergistic effect", "US 5,540,186 · summary"), "slow"),
 ("It does not say which effect. Approved, nineteen ninety-six.", stamp(GROOM, "MECHANICALLY ASSISTED ANIMAL|SELF GROOMING DEVICE", "DEC. 2, 1994", "JUL. 30, 1996", at=1.8), "slow"),

 # ---------- 6 · bedmaking ----------
 ("Number six. The bedroom.", chap(6, BED, "Bedmaking|Device", ["US 2,930,053", "Filed 1959 · Issued 1960"]), "calm"),
 ("The patent has done the math on making a bed. It takes a great deal of walking about the bed, and also a considerable amount of bending over.", quote(BED, "a great deal of walking about the bed, and also a considerable amount of bending over", "bending over", "US 2,930,053 · col. 1"), "calm"),
 ("And worse. The work is routine, and does not result in the creation of new economic wealth.", quote(BED, "since the work is routine and does not result in the creation of new economic wealth", "new economic wealth", "US 2,930,053 · col. 1"), "slow"),
 ("So: an inexpensive mechanical bed-making device. Under the mattress, cords run out from the center like the spokes of a wheel.", fig(BED, "bed2", "2", calls=[["PULL CORDS", 402, 306, 120, -60]]), "calm"),
 ("Clamps grab the edges of the sheet. A motor under the bed winds the cords in, and the sheet is pulled tight from every side.", fig(BED, "bed1", "1"), "calm"),
 ("In the morning, the occupant gets up, flips the switch, and the motor draws the bed coverings to their desired tight, tucked-in, neat and unwrinkled position.", quote(BED, "draws the bed coverings to their desired tight, tucked-in, neat and unwrinkled position", "neat and unwrinkled", "US 2,930,053 · col. 3"), "calm"),
 ("The promise: no more countless hours of unproductive labor.", quote(BED, "countless hours of unproductive labor", "countless hours", "US 2,930,053 · col. 1"), "slow"),
 ("And it works with you still in it. The patent lists that as an object.", quote(BED, Q_KICK, "flipping a switch", "US 2,930,053 · col. 1", hide=True), "calm"),
 ("Kicked-out covers may be automatically re-tucked into place by the bed occupant merely by flipping a switch.", quote(BED, Q_KICK, "flipping a switch", "US 2,930,053 · col. 1", typed=False), "slow"),
 ("And if you hold the switch down too long? The pulleys merely slip, and no harm is done.", quote(BED, "merely slip on the stub shafts 38 and no harm is done", "no harm is done", "US 2,930,053 · col. 3"), "calm"),
 ("The bed makes itself. Approved, nineteen sixty.", stamp(BED, "BEDMAKING|DEVICE", "JAN. 22, 1959", "MAR. 29, 1960", at=1.6), "slow"),

 # ---------- 7 · pasta fork ----------
 ("Number seven. Dinner.", chap(7, FORK, "Motorized Twisting|Pasta Fork", ["US 5,062,211", "Filed 1991 · Issued 1991"]), "calm"),
 ("The patent describes the old way. The user's hand is turned and twisted to gather spaghetti onto the tines of the fork.", quote(FORK, "the user's hand is turned and twisted so as to gather food, such as spaghetti, pasta or the like onto the tines of the fork", "turned and twisted", "US 5,062,211 · prior art"), "calm"),
 ("The problem, as stated: the only twisting motion is done by the wrist and hand of the user.", quote(FORK, "the only twisting motion is done by the wrist and hand of the user", "wrist and hand of the user", "US 5,062,211 · prior art"), "slow"),
 ("And if the food slips off on the way up, the patent warns of consequences.", quote(FORK, Q_EMB, "embarrassment", "US 5,062,211 · prior art", hide=True), "calm"),
 ("Causing embarrassment to the user.", quote(FORK, Q_EMB, "embarrassment", "US 5,062,211 · prior art", typed=False), "punch"),
 ("Earlier twisting forks had to be pushed down into the plate. Which, the patent notes, requires a visual coordination to follow collection of the food product on the forked end.", quote(FORK, "This procedure requires a visual coordination to follow collection of the food product on the forked end.", "visual coordination", "US 5,062,211 · prior art"), "calm"),
 ("So: a long-standing need, finally met. A fork with batteries, a motor, and gears. The fork end turns under push-button control.", fig(FORK, "fork12", "1 & 2", calls=[["BATTERY", 204, 372, -90, -30], ["MOTOR", 204, 600, -90, 30], ["BUTTON", 600, 804, 90, 0]]), "calm"),
 ("The middle tine is longer than the others, so the fork spins around it. The pasta wraps itself.", quote(FORK, "the central tine 34 is longer than the tines on its opposite sides so as to form a pivoting point", "pivoting point", "US 5,062,211 · description"), "calm"),
 ("Then it holds still. To retain the food in place while the implement is being raised to the user's mouth.", quote(FORK, "retain the food in place while the implement is being raised to the user's mouth", "raised to the user's mouth", "US 5,062,211 · summary"), "calm"),
 ("The whole patent has one claim and one sheet of drawings. Filed in March. Approved in November.", fig(FORK, "fork12", "1 & 2", draw=False), "calm"),
 ("No more wrist. Approved, nineteen ninety-one.", stamp(FORK, "MOTORIZED TWISTING|PASTA FORK", "MAR. 4, 1991", "NOV. 5, 1991", at=1.6), "slow"),

 # ---------- 8 · chair ----------
 ("And number eight. Back to the chair.", chap(8, CHAIR, "Chair with Refrigerator and|Armrest Beverage Cooler", ["US 4,719,764", "Filed 1986 · Issued 1988"]), "calm"),
 ("The patent starts with a survey. Chairs have been constructed with various features ancillary to the usual function of a chair.", quote(CHAIR, "Chairs have been constructed with various features ancillary to the usual function of a chair", "ancillary", "US 4,719,764 · col. 1"), "calm"),
 ("But none of the above patents utilizes a chair with a refrigeration system incorporated therein. Until now.", quote(CHAIR, "none of the above patents utilizes a chair with a refrigeration system incorporated therein", "refrigeration system", "US 4,719,764 · col. 1"), "calm"),
 ("Here is the inside. A compressor, a condenser coil and an air grill, all built into a recliner. If desired, a small fan.", fig(CHAIR, "chair4", "4", calls=[["COMPRESSOR", 318, 828, -40, 70], ["FRIDGE", 690, 540, 60, -60]]), "calm"),
 ("The cold runs through a coil around the can holder in the armrest. The can sits low, with just enough sticking out to enable easy gripping thereof.", fig(CHAIR, "chair3", "3"), "calm"),
 ("The fridge door is hinged at the bottom, so it opens downward. A magnet keeps it shut. A rack on the door holds the cans.", fig(CHAIR, "chair1", "1", draw=False, calls=[["DOOR", 258, 450, -60, 60]]), "calm"),
 ("And when there is no can in the armrest, a plug closes the hole. For a relatively smooth upper surface to the armrest.", fig(CHAIR, "chair4", "4", draw=False, calls=[["PLUG", 774, 387, 60, -60]]), "calm"),
 ("All of it, so the occupant can get a drink without changing position in the chair or getting out of the chair.", quote(CHAIR, "without the occupant changing position in the chair or getting out of the chair", "changing position", "US 4,719,764 · summary"), "calm"),
 ("The can holder may be provided either on the left- or right-hand armrest. Or on both.", quote(CHAIR, "may be provided either on the left- or right-hand armrest or on both", "or on both", "US 4,719,764 · description"), "slow"),
 ("And the patent says what it's all for.", quote(CHAIR, Q_TV, "without getting out of the chair", "US 4,719,764 · description", hide=True), "calm"),
 ("To enjoy television or merely relax and consume beverages and related products without getting out of the chair.", quote(CHAIR, Q_TV, "without getting out of the chair", "US 4,719,764 · description", typed=False), "slow"),
 ("Or on both. Approved, nineteen eighty-eight.", stamp(CHAIR, CH_T, CH_F, CH_I, at=1.2), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the lawn mower. Because it took almost seven years to approve a machine that, when the work is done, just spins in a tight circle on the grass. Until someone steers it somewhere else.", fig(LAWN, "lawn2", "2", draw=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["4,091,805 · 4,850,843 · 2,943,856", "2,941,346 · 5,540,186 · 2,930,053", "5,062,211 · 4,719,764"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
