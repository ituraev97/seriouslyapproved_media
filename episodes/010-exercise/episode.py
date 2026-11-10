# SERIOUSLY APPROVED · FILE 010 · ONE PATENT — "6 Weird Exercise Machines That Got Real Patents"
# Long video, 1920x1080. One deep patent (US 5,926,857 armor with rollers) + 5 relatives. Facts and quotes: sources.md.
FMT = "long"
TAIL = 3.0
SAY = {"gyral": "jyral", "Gyral": "Jyral", "Jean-Yves Blondeau": "Zhon Eve Blon-doe", "snow-plough": "snow-plow", "Atari": "uh-tar-ee"}

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

ARMOR = P("US 5,926,857", "FULL-BODY|[ROLLERBLADES]", "1999")
WHEEL = P("US 2,953,394", "THE HUMAN|[HAMSTER WHEEL]", "1960")
HELMET = P("US 3,128,095", "THE WEIGHT|[HELMET]", "1964")
SHOES = P("US 4,457,084", "DISCO|[SPRING SHOES]", "1984")
BIKE = P("US 4,512,567", "THE [ATARI]|EXERCISE BIKE", "1985")
BED = P("US 5,989,168", "THE EXERCISE|[BED]", "1999")

def chap(kicker, d, title, lines, n=""):
    return dict(g="title", kicker=kicker, numeral=n, title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="6 WEIRD|[EXERCISE] PATENTS", side="FILE 010 · ONE PATENT")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 010")

AR_T, AR_F, AR_I = "ARMOR WITH|ROLLERS", "MAY 31, 1996", "JULY 27, 1999"
Q_OBJ = "The object of the present invention is to propose a new sport involving skill and speed"
Q_POS = "sitting, standing, lying on his stomach or on his back, kneeling and on all fours, and to move from one position to another without stopping"
Q_PLOUGH = 'he can move his arms to the "snow-plough position"'
Q_AXIS = "the occupant becomes in effect an axis"
Q_PISTON = "moving both arms and legs in piston like fashion in various degrees of synchronization"
Q_DISCO = "The hopping and dancing shoe 91 is suitable to accompany music such as rock n' roll, a flamenco or disco"

LINES = [
 # ---------- cold open ----------
 ("This is a man wearing roller skates. On his feet. And his knees. And his elbows. And wheels on his hands.", fig(ARMOR, "armor1", "1", calls=[["FEET", 396, 1578, 160, 20], ["KNEES", 288, 1062, -200, 40], ["ELBOWS", 612, 498, 120, 80], ["HANDS", 168, 894, -130, 60]]), "slow"),
 ("And on his chest. And on his back. And two on his behind.", fig(ARMOR, "armor1", "1", draw=False, calls=[["CHEST", 204, 366, -160, -40], ["BACK", 504, 294, 160, -60], ["BEHIND", 528, 726, 170, 60]]), "calm"),
 ("So he can roll in every position. Even lying down.", fig(ARMOR, "armorde", "2d, 2e"), "calm"),
 ("It was approved.", stamp(ARMOR, AR_T, AR_F, AR_I), "punch"),
 ("This is real. A U.S. patent from nineteen ninety-nine. Today, one patent, up close: full-body rollerblades. And then, five more exercise machines that got real patents. A wheel you stand inside. A helmet full of weights. Disco spring shoes. An exercise bike that plays video games. And a bed that bends you.", dict(g="title", kicker="ONE PATENT · FILE 010", title="Weird Exercise|Machines", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- part 1 · the armor ----------
 ("Part one. The one patent.", chap("THE ONE PATENT", ARMOR, "Armor with|Rollers", ["US 5,926,857", "Filed 1996 · Issued 1999"], "1"), "calm"),
 ("The official title is three words. Armor with rollers.", quote(ARMOR, "ARMOR WITH ROLLERS", "ROLLERS", "US 5,926,857 · title"), "slow"),
 ("The inventor, Jean-Yves Blondeau, lived in France. And the patent opens like a trend report. Snow surfing, skateboarding and windsurfing are booming, it says. Notably with a young audience eager for thrills.", quote(ARMOR, "notably with a young audience eager for thrills", "eager for thrills", "US 5,926,857 · description"), "calm"),
 ("But it spots one flaw in all of those sports. You are, in most cases, being able to use your feet only for support.", quote(ARMOR, "being able to use his feet only for support", "feet only", "US 5,926,857 · description"), "calm"),
 ("So, the goal.", quote(ARMOR, Q_OBJ, "a new sport", "US 5,926,857 · description", hide=True), "calm"),
 ("The object of the present invention is to propose a new sport involving skill and speed.", quote(ARMOR, Q_OBJ, "a new sport", "US 5,926,857 · description", typed=False), "slow"),
 ("A sport where you roll at high speed, on any hard, smooth surface. In all positions while constantly varying his bearing points.", quote(ARMOR, "in all positions while constantly varying his bearing points", "in all positions", "US 5,926,857 · description"), "calm"),
 ("Here is the equipment. Start at the top. A helmet of conventional type also forms an integral part of this armor.", fig(ARMOR, "armor1", "1", draw=False, ring=[252, 150, 190], calls=[["CONVENTIONAL", 252, 90, 160, -40]]), "calm"),
 ("Your arms go into long, rigid gauntlets, hinged at the elbow. A pair of rollers at the elbow. And past the hand, one bigger roller.", fig(ARMOR, "armor1", "1", draw=False, calls=[["2 ROLLERS", 612, 498, 120, 80], ["1 BIG ROLLER", 168, 894, -60, 120]]), "calm"),
 ("Each gauntlet has a hole, so you can still hold things. A gripping opening is also provided enabling the user to have the use of his hands.", quote(ARMOR, "A gripping opening 13 is also provided enabling the user to have the use of his hands.", "the use of his hands", "US 5,926,857 · description"), "calm"),
 ("Your legs go into rigid leg-pads, with two rollers at each knee. And your shoes are roller skates, with two extra rollers up front, at the toes.", fig(ARMOR, "armor1", "1", draw=False, calls=[["KNEE", 288, 1062, -200, 40], ["TOES", 180, 1434, -150, 60]]), "calm"),
 ("Then the jacket. On the front, a frame with three rollers. Two at the shoulders, one at the pelvis.", fig(ARMOR, "armor1", "1", draw=False, calls=[["SHOULDERS", 204, 366, -170, -40], ["PELVIS", 252, 714, -170, 30]]), "calm"),
 ("On the back, another frame. And the patent did the testing. Experience has shown that it is preferable to equip this back part with four rollers.", quote(ARMOR, "Experience has shown that it is preferable to equip this back part with four rollers", "Experience has shown", "US 5,926,857 · description"), "calm"),
 ("Below those, two more. The buttock support rollers. They are there in order to enable the user to raise himself into the seated position.", quote(ARMOR, "in order to enable the user to raise himself into the seated position", "the seated position", "US 5,926,857 · description"), "calm"),
 ("And on the chest, two rails, enabling the user to slide on steps or on a balustrade.", quote(ARMOR, "enabling the user to slide on steps or on a balustrade", "on a balustrade", "US 5,926,857 · description"), "calm"),
 ("All the parts open and close, enabling the user to get into them, and fix them to his body. The quotation marks are in the patent.", quote(ARMOR, 'enabling the user to "get into them" and fix them to his body', '"get into them"', "US 5,926,857 · description"), "calm"),
 ("Then, sheet two. Eleven tiny drawings of what you can do in it. Figures two A to two K.", fig(ARMOR, "armorabc", "2a–2c"), "calm"),
 ("You start off standing, as if on roller skates. Then one knee goes down. Then the hands, and both knees.", fig(ARMOR, "armorabc", "2a–2c", draw=False, calls=[["STANDING", 70, 40, 60, -20], ["ONE KNEE", 470, 70, 40, -40], ["HANDS", 840, 90, 40, -50]]), "calm"),
 ("Then all fours. And then, flat out. Lying down. Still rolling.", fig(ARMOR, "armorde", "2d, 2e"), "calm"),
 ("Which raises a question. How do you brake, lying flat on wheels? The patent has an answer.", fig(ARMOR, "armorde", "2d, 2e", draw=False, ring=[750, 70, 180]), "question"),
 ("To slow down in this position, he can move his arms to the snow-plough position.", quote(ARMOR, Q_PLOUGH, "snow-plough position", "US 5,926,857 · description"), "slow"),
 ("It is a move from skiing. You open your elbows out, press down on them, and bring your hands together.", fig(ARMOR, "armorfg", "2f, 2g"), "calm"),
 ("From kneeling, you can also roll back, rock onto your feet, sit down, and lie on your back. Still rolling. Then do it all in reverse to get up.", fig(ARMOR, "armorhk", "2h–2k"), "calm"),
 ("And the floor is just the start. Also inclined planes or vertical surfaces, for example in corridors, on which he can lean.", quote(ARMOR, "also inclined planes or vertical surfaces (for example in corridors) on which he can lean", "for example in corridors", "US 5,926,857 · description"), "calm"),
 ("The full list. Sitting, standing, lying on his stomach or on his back, kneeling and on all fours. And to move from one position to another without stopping.", quote(ARMOR, Q_POS, "without stopping", "US 5,926,857 · description"), "calm"),
 ("And that is why it belongs on this shelf. The suit, says the patent, enables him to train the whole of his muscular system, in homogeneous manner.", quote(ARMOR, "enables him to train the whole of his muscular system, in homogeneous manner", "the whole of his muscular system", "US 5,926,857 · description"), "calm"),
 ("Even the word roller is open-minded. It can also designate simple ball-bearings held captive in a cage.", quote(ARMOR, "can also designate simple ball-bearings held captive in a cage", "held captive", "US 5,926,857 · description"), "calm"),
 ("A suit of armor, covered in wheels. A gym you wear. Approved, July nineteen ninety-nine.", stamp(ARMOR, AR_T, AR_F, AR_I, big=True, at=2.4), "slow"),

 # ---------- part 2 · the relatives ----------
 ("Part two. The relatives. Five more exercise machines, and every one of them got a real patent.", dict(g="title", kicker="ONE PATENT · FILE 010", title="The|Relatives", lines=["Five more exercise patents.", "1960 to 1999."], **INTRO), "calm"),

 # wheel
 ("First, Iowa, nineteen fifty-eight.", chap("THE RELATIVES · 1 OF 5", WHEEL, "Occupant Propelled|Gyral Wheel", ["US 2,953,394", "Filed 1958 · Issued 1960"], "2"), "calm"),
 ("A man stands inside a giant wheel.", fig(WHEEL, "gyral1", "1", calls=[["A MAN", 270, 102, 150, -40], ["A WHEEL", 486, 234, 20, 120]]), "punch"),
 ("The inventor's own name for it: my invention relates to what I refer to as a gyral wheel, designed for use as entertainment and for exercise.", quote(WHEEL, "My invention relates to what I refer to as a gyral wheel", "gyral wheel", "US 2,953,394 · description"), "calm"),
 ("One wheel, with a tire like a bicycle's. On each side, an oval frame on spokes. Inside each frame, a hand grip up top and a foot saddle at the bottom, riding on little rollers.", fig(WHEEL, "gyral34", "3, 4", calls=[["FOOT SADDLE", 66, 534, 40, 130], ["HAND GRIP", 300, 530, -60, -110]]), "calm"),
 ("To start, you put one foot in a saddle and push off the ground with the other. Like a scooter. Then that foot goes in too.", fig(WHEEL, "gyral1", "1", draw=False, calls=[["FEET IN", 222, 450, 140, 40]]), "calm"),
 ("Seen from the front, in figure two, it is narrow. Just the tire, and the two frames, one on each side.", fig(WHEEL, "gyral2", "2"), "calm"),
 ("And then, the motion. Shifting your weight from leg to leg, and moving both arms and legs in piston like fashion in various degrees of synchronization.", quote(WHEEL, Q_PISTON, "piston like fashion", "US 2,953,394 · description"), "calm"),
 ("As the wheel turns, the patent explains, the occupant becomes in effect an axis.", quote(WHEEL, Q_AXIS, "an axis", "US 2,953,394 · description"), "slow"),
 ("It takes some practice. But by suitable practice, he will be able to propel the vehicle for his enjoyment, sport and exercise.", quote(WHEEL, "by suitable practice will be able to propel the vehicle for his enjoyment, sport and exercise", "suitable practice", "US 2,953,394 · description"), "calm"),
 ("A hamster wheel. For a person. Approved, September nineteen sixty.", stamp(WHEEL, "OCCUPANT PROPELLED|GYRAL WHEEL", "FEB. 6, 1958", "SEPT. 20, 1960", at=1.8), "slow"),

 # helmet
 ("Next, New Jersey, nineteen sixty-one. This one is about your neck.", chap("THE RELATIVES · 2 OF 5", HELMET, "Metallic Weight|Exercising Helmet", ["US 3,128,095", "Filed 1961 · Issued 1964"], "3"), "calm"),
 ("The patent gets right to it. A device for exercising the neck and neck muscles.", quote(HELMET, "a device for exercising the neck and neck muscles", "neck and neck muscles", "US 3,128,095 · description"), "calm"),
 ("It starts as an ordinary helmet, of the type used for athletic purposes. A shell is bonded on top.", fig(HELMET, "helmet1", "1", calls=[["THE HELMET", 276, 288, 120, 40]]), "calm"),
 ("And on that shell, you stack weights. Hollow metal domes, like bowls.", fig(HELMET, "helmet67", "6, 7", calls=[["A WEIGHT", 204, 342, 120, 10]]), "calm"),
 ("These weights may be nested with each other, and each is of a different size, thus being of a different weight.", quote(HELMET, "these weights may be nested with each other, and each is of a different size, thus being of a different weight", "nested", "US 3,128,095 · description"), "calm"),
 ("Here are three of them, stacked. A strap goes over the top and hooks into holes in the helmet's ear pieces, to hold them down.", fig(HELMET, "helmet2", "2", calls=[["3 WEIGHTS", 300, 60, 150, -10]]), "calm"),
 ("Claim four makes it official. The weight is comprised of a plurality of nested metal hemispherical shells.", quote(HELMET, "wherein said weight is comprised of a plurality of nested metal hemispherical shells.", "nested metal hemispherical shells", "US 3,128,095 · claim 4"), "calm"),
 ("The point, in the patent's words: to vary the amount of weight placed upon the helmet, to thus vary the stress placed upon the neck during exercises.", quote(HELMET, "to vary the amount of weight placed upon the helmet, to thus vary the stress placed upon the neck during exercises", "stress placed upon the neck", "US 3,128,095 · description"), "calm"),
 ("And when you are done, take the weights off. It is just a helmet again. A conventional athletic helmet.", quote(HELMET, "to facilitate the use of the head piece as a conventional athletic helmet", "conventional athletic helmet", "US 3,128,095 · description"), "calm"),
 ("A set of dumbbells, worn as a hat. Approved, April nineteen sixty-four.", stamp(HELMET, "METALLIC WEIGHT|EXERCISING HELMET", "MAR. 30, 1961", "APR. 7, 1964", at=2.0), "slow"),

 # shoes
 ("Next, nineteen eighty-one. Shoes.", chap("THE RELATIVES · 3 OF 5", SHOES, "Hopping and|Dancing Shoes", ["US 4,457,084", "Filed 1981 · Issued 1984"], "4"), "calm"),
 ("A lace-up shoe, sitting on two big coil springs, on top of a flat base.", fig(SHOES, "shoes1", "1", calls=[["SPRINGS", 420, 264, 150, 60], ["BASE", 396, 324, -60, 90]]), "calm"),
 ("You put your foot in, and the patent says the player laces up the shoe firmly to hop and, or, dance.", quote(SHOES, "laces up the shoe firmly to hop and/or dance", "hop and/or dance", "US 4,457,084 · description"), "calm"),
 ("Then figure nine. Big cone-shaped springs. And on the side, something else.", fig(SHOES, "shoes9", "9", calls=[["SPRINGS", 492, 264, 120, 50]]), "calm"),
 ("Bells can be attached to the sides of the shoe, or on its shoe lace.", fig(SHOES, "shoes9", "9", draw=False, ring=[684, 132, 150], calls=[["BELLS", 684, 132, -130, -90]]), "punch"),
 ("Or castanets. They attach to the sole, the shoe, or the laces, to create a desired rhythm energized by the vibration or rhythmical movement of the player's foot.", quote(SHOES, "to create a desired rhythm energized by the vibration or rhythmical movement of the player's foot", "a desired rhythm", "US 4,457,084 · description"), "calm"),
 ("Because, the patent explains, the shoe is suitable to accompany music such as rock n' roll, a flamenco or disco.", quote(SHOES, Q_DISCO, "a flamenco or disco", "US 4,457,084 · description"), "calm"),
 ("The cone springs even fix the noise problem. They can deaden metallic noises caused by the contact of the spring coils during the repeated hopping and dancing.", quote(SHOES, "It can also deaden metallic noises caused by the contact of the spring coils during the repeated hopping and dancing.", "metallic noises", "US 4,457,084 · description"), "calm"),
 ("And the patent has one very specific suggestion. They may be used by middle aged men for weight control exercise.", quote(SHOES, "The present hopping and dancing shoes may be used by middle aged men for weight control exercise", "middle aged men", "US 4,457,084 · description"), "calm"),
 ("Two pogo sticks. With bells. For the dance floor. Approved, July nineteen eighty-four.", stamp(SHOES, "HOPPING AND|DANCING SHOES", "APR. 8, 1981", "JULY 3, 1984", at=2.4), "slow"),

 # bike
 ("Next, nineteen eighty-three. The exercise bike meets the arcade.", chap("THE RELATIVES · 4 OF 5", BIKE, "Exercise Bicycle|for Video Games", ["US 4,512,567", "Filed 1983 · Issued 1985"], "5"), "calm"),
 ("The patent opens with the news. Video games have become extremely popular and are played by many people, particularly those in their teenage years.", quote(BIKE, "video games have become extremely popular and are played by many people, particularly those in their teenage years", "extremely popular", "US 4,512,567 · description"), "calm"),
 ("So, the plan. An exercise bicycle to enable one to fully control and play any type of video game while performing worthwhile exercise.", quote(BIKE, "to enable one to fully control and play any type of video game while performing worthwhile exercise", "worthwhile exercise", "US 4,512,567 · description"), "calm"),
 ("It was not the first bike to make demands. The patent lists an earlier one that powered a television. And if one does not do so, one will not be able to view the television.", quote(BIKE, "and if one does not do so, one will not be able to view the television", "will not be able to view the television", "US 4,512,567 · description"), "calm"),
 ("Here it is. A normal exercise bike, plus a box of electronics and one cable. The label says: to video game.", fig(BIKE, "bike2", "2", calls=[["THE CABLE", 762, 623, 60, 120]]), "calm"),
 ("And the patent names the console. A typical video game apparatus is designated as the Atari four hundred or the Atari eight hundred.", quote(BIKE, "designated as the Atari 400 or the Atari 800", "Atari 400", "US 4,512,567 · description"), "calm"),
 ("Move the handlebars left and right, or up and down, and you steer the action on the screen. Pedal, and you set how much it moves.", fig(BIKE, "bike2", "2", draw=False, calls=[["STEER", 356, 300, -150, -40], ["PEDAL", 277, 647, -150, 60]]), "calm"),
 ("In one version, the handlebars do nothing at all, unless you pedal fast enough. If, however, the operator pedals the bicycle rapidly enough, the game responds.", quote(BIKE, "If, however, the operator pedals the bicycle rapidly enough", "rapidly enough", "US 4,512,567 · description"), "calm"),
 ("The goal, in the patent's words: making video game playing a more healthful event.", quote(BIKE, "making video game playing a more healthful event", "a more healthful event", "US 4,512,567 · description"), "calm"),
 ("Pedal to play. Approved, April nineteen eighty-five.", stamp(BIKE, "EXERCISE BICYCLE|APPARATUS", "MAR. 28, 1983", "APR. 23, 1985", at=1.4), "slow"),

 # bed
 ("And finally, nineteen ninety-eight. The bed.", chap("THE RELATIVES · 5 OF 5", BED, "Exercise|Bed", ["US 5,989,168", "Filed 1998 · Issued 1999"], "6"), "calm"),
 ("The patent spots a gap in the market. The conventional exercise machines can not be used as a bed for sleeping or resting on.", quote(BED, "The conventional exercise machines can not be used as a bed for sleeping or resting on.", "can not be used as a bed", "US 5,989,168 · description"), "calm"),
 ("And the reverse is also true. The conventional beds can not be used as an exercise device.", quote(BED, "The conventional beds can not be used as an exercise device for relaxing or training the muscles of a person.", "can not be used as an exercise device", "US 5,989,168 · description"), "calm"),
 ("So here is the solution, in use. A person lies down. Their feet go between soft rollers at the end, raised or lowered with a hand wheel.", fig(BED, "bed3", "3", calls=[["FEET", 1382, 344, -60, -140]]), "calm"),
 ("Under the bed, a motor pushes a rod. The rod moves a frame, which pulls an elastic cord. The cord drags the front half of the bed toward the back.", fig(BED, "bed3", "3", draw=False, calls=[["MOTOR", 1229, 603, 60, 130]]), "calm"),
 ("The rear support can even be adjusted in length, so as to tilt the exercise bed.", fig(BED, "bed3", "3", draw=False, calls=[["TILT", 1206, 748, 60, 120]]), "calm"),
 ("And the middle of the bed rises up under you. Both frames are displaced upwards to push the back muscles of a person resting on the exercise bed.", quote(BED, "both front bed frame and the rear bed frame are displaced upwards to push the back muscles of a person resting on the exercise bed", "displaced upwards", "US 5,989,168 · description"), "calm"),
 ("The result, in the patent's words: the backbone of the user is therefore braced and extended.", quote(BED, "The backbone A2 of the user A of the exercise bed of the present invention is therefore braced and extended.", "braced and extended", "US 5,989,168 · description"), "calm"),
 ("A bed that does the stretching for you. Approved, November nineteen ninety-nine.", stamp(BED, "EXERCISE|BED", "DEC. 30, 1998", "NOV. 23, 1999", big=True, at=1.8), "slow"),

 # ---------- close ----------
 ("Six machines. But which one is the most approved?", dict(g="title", kicker="THIS FILE'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going back to the armor. Because somebody had to work out how to brake while lying flat on wheels. And then they wrote it down, and it got approved.", quote(ARMOR, Q_PLOUGH, "snow-plough position", "US 5,926,857 · description", typed=False), "calm"),
 ("Every quote in this video is word for word from the patent. The patent numbers are in the video description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["5,926,857 · 2,953,394", "3,128,095 · 4,457,084", "4,512,567 · 5,989,168"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
