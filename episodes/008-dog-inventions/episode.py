# SERIOUSLY APPROVED · FILE 008 · THE SHELF — "Ranking the Weirdest Dog Inventions (All Real Patents)"
# Long video, 1920x1080. Countdown 9 -> 1. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, date):
    return dict(num=num, hook=title, side=f"{num} · {date}")

FLEA = P("US 5,003,756", "A COAT FOR|[FLEAS]", "1991")
LEASH = P("US 887,072", "THE SELF-WINDING|[LEASH]", "1908")
FOUN = P("US 3,272,181", "THE DOG'S|[WATER COOLER]", "1966")
TRIKE = P("US 4,134,364", "WALK THE DOG|BY [TRICYCLE]", "1979")
BATH = P("US 2,438,979", "BATH TIME,|[STRAPPED IN]", "1948")
FETCH = P("US 4,995,374", "THE FETCH|[MACHINE]", "1991")
WHEEL = P("US 528,066", "THE DOG|[POWER PLANT]", "1894")
UMB = P("US 5,918,611", "A DOG WITH|AN [UMBRELLA]", "1999")
GOG = P("US 5,732,415", "GOGGLES|FOR [DOGS]", "1998")
GOG79 = P("US 4,178,742", "GOGGLES|FOR [DOGS]", "1979")

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"WEIRDNESS RANK · No. {n} OF 9", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="RANKING THE|[WEIRDEST]", side="FILE 008 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 008")

Q_FLEA = "if a flea survives by migrating to a distant point of the dog, the dog can reach him by scratching or biting."
Q_WORLD = "The world may never know."
Q_OWNER = "the human owner usually wears out long before the dog is ready to call it enough for the day."
Q_MACH = "a milk or cream separator, a churn, a pump, a sewing machine, a washing machine, a printing press"
Q_LATTER = "to wash the dog without any interference on the part of the latter"

LINES = [
 # ---------- cold open ----------
 ("This dog is wearing goggles. Real ones. From a real United States patent.", fig(GOG, "gog3", "3", calls=[["GOGGLES", 138, 282, 80, -60]]), "slow"),
 ("And the patent stops to ask why dogs hang their heads out of car windows. Its answer: the world may never know.", quote(GOG, Q_WORLD, "never know", "US 5,732,415 · description"), "calm"),
 ("It was approved. Nineteen ninety-eight.", stamp(GOG, "ADJUSTABLE|PET EYEWEAR", "FEB. 24, 1997", "MAR. 31, 1998"), "punch"),
 ("Today we are ranking the weirdest dog inventions that got real patents. Coats, leashes, fountains, bathtubs, umbrellas, and one very large wheel. Nine of them, from eighteen ninety-four to nineteen ninety-nine. Real drawings, real quotes, counted down from weird to weirdest.", dict(g="title", kicker="THE SHELF · FILE 008", title="The Weirdest|Dog Inventions", lines=["Real patents. Ranked.", "All approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- 9 · flea coat ----------
 ("Number nine. The flea war.", chap(9, FLEA, "Dog Garment|with Flea Repelling Means", ["US 5,003,756", "Filed 1990 · Issued 1991"]), "calm"),
 ("This is a dog in a coat. The coat is not for the cold. It is for the fleas.", fig(FLEA, "flea1", "1", calls=[["THE COAT", 420, 330, 80, -60]]), "calm"),
 ("The patent begins with flea collars. These collars, it admits, appear to be successful in keeping the fleas off the dog's back and head.", quote(FLEA, "These collars appear to be successful in keeping the fleas off the dog's back and head", "appear to be successful", "US 5,003,756 · description"), "calm"),
 ("But the fleas have a plan. The fleas merely migrate to other portions of the dog.", quote(FLEA, "the fleas merely migrate to other portions of the dog", "migrate", "US 5,003,756 · description"), "calm"),
 ("Particularly to those portions where the dog has difficulty in scratching or biting.", quote(FLEA, "particularly to those portions where the dog has difficulty in scratching or biting.", "difficulty", "US 5,003,756 · description"), "calm"),
 ("So the coat covers the chest, the neck, the sides and the back. And inside, rows of little loops hold ordinary flea strips.", fig(FLEA, "flea2", "2", calls=[["FLEA STRIPS", 300, 200, 80, -60]]), "calm"),
 ("The fleas have nowhere left to go. And if one makes a run for it, the patent has thought of that too.", quote(FLEA, Q_FLEA, "scratching or biting", "US 5,003,756 · description", hide=True), "calm"),
 ("If a flea survives by migrating to a distant point of the dog, the dog can reach him by scratching or biting.", quote(FLEA, Q_FLEA, "scratching or biting", "US 5,003,756 · description", typed=False), "slow"),
 ("A coat with a battle plan. Approved, nineteen ninety-one.", stamp(FLEA, "DOG GARMENT WITH|FLEA REPELLING MEANS", "MAR. 8, 1990", "APR. 2, 1991", at=1.8), "slow"),

 # ---------- 8 · leading device ----------
 ("Number eight. Nineteen-oh-eight.", chap(8, LEASH, "Leading|Device", ["US 887,072", "Filed 1907 · Issued 1908"]), "calm"),
 ("This is a dog collar. And this little box on it is the invention.", fig(LEASH, "lead1", "1", calls=[["THE BOX", 214, 390, -60, 60]]), "calm"),
 ("It is a device for leading pet dogs or other pet animals when they are taken out to accompany a person in his or her walks.", quote(LEASH, "a device for leading pet dogs or other pet animals when they are taken out to accompany a person in his or her walks", "pet dogs", "US 887,072 · description"), "calm"),
 ("In the language of nineteen-oh-seven, the invention is particularly adapted for ladies.", quote(LEASH, "The invention is particularly adapted for ladies", "for ladies", "US 887,072 · description"), "calm"),
 ("The problem is an old one. A dog on a leash keeps running on the wrong side of lamp posts or pedestrians.", quote(LEASH, "running on the wrong side of lamp posts or pedestrians", "lamp posts", "US 887,072 · description"), "calm"),
 ("Thus causing much annoyance to the owner.", quote(LEASH, "thus causing much annoyance to the owner", "much annoyance", "US 887,072 · description"), "slow"),
 ("The usual fix is to wrap the chain around your hand, and unwrap it again after the object has passed. Which, the patent says, is an awkward performance when obliged to be done frequently.", quote(LEASH, "which is an awkward performance when obliged to be done frequently.", "awkward performance", "US 887,072 · description"), "calm"),
 ("And sometimes it goes worse. Frequently the leash is dropped and the dog permitted to run away.", quote(LEASH, "frequently the leash is dropped and the dog permitted to run away.", "run away", "US 887,072 · description"), "calm"),
 ("The objects of the present invention, the patent says, are to obviate and overcome all these difficulties and annoyances due to the usual form of leash.", quote(LEASH, "The objects of the present invention are to obviate and overcome all these difficulties and annoyances due to the usual form of leash", "obviate and overcome", "US 887,072 · description"), "calm"),
 ("So the box on the collar holds a drum with a spring. The chain winds out when the dog runs, and winds back in by itself.", fig(LEASH, "lead1", "1", draw=False, calls=[["THE CHAIN", 120, 470, 80, -40]]), "calm"),
 ("A leash that reels itself in. In nineteen-oh-eight. Approved.", stamp(LEASH, "LEADING|DEVICE", "JAN. 12, 1907", "MAY 12, 1908", at=2.0), "slow"),

 # ---------- 7 · drinking fountain ----------
 ("Number seven. The water cooler.", chap(7, FOUN, "Animal Actuated|Drinking Fountain", ["US 3,272,181", "Filed 1965 · Issued 1966"]), "calm"),
 ("A bowl. A tall pipe. And a little plate on the side.", fig(FOUN, "foun1", "1", calls=[["THE PIPE", 482, 85, 80, 40]]), "calm"),
 ("The invention is specially designed for use by dogs, both as a means to obtain water and as a training device.", quote(FOUN, "The invention is specially designed for use by dogs, both as a means to obtain water and as a training device.", "training device", "US 3,272,181 · description"), "calm"),
 ("Here is how it works. The dog steps on the plate. A valve opens. And water comes up out of the pipe, right where the dog is waiting.", fig(FOUN, "foun2", "2", calls=[["THE PEDAL", 207, 341, 80, -40], ["THE WATER", 257, 229, 120, -80]]), "calm"),
 ("The patent describes it more formally. It lets animals operate the drinking fountain by a conscious applying of weight thereto.", quote(FOUN, "for allowing animals to operate the drinking fountain by a conscious applying of weight thereto.", "conscious applying of weight", "US 3,272,181 · description"), "calm"),
 ("A conscious applying of weight. The dog has to mean it.", quote(FOUN, "for allowing animals to operate the drinking fountain by a conscious applying of weight thereto.", "conscious", "US 3,272,181 · description", typed=False), "slow"),
 ("And it doubles as school. A further object is a drinking fountain which may be used as a training means for dogs. The lesson being: press here for water.", quote(FOUN, "A further object of the present invention is to provide a drinking fountain which may be used as a training means for dogs.", "training means", "US 3,272,181 · description"), "calm"),
 ("One more detail, from the very top of the patent. The inventor assigned five percent of it to someone else. Five percent of a dog water cooler.", fig(FOUN, "foun2", "2", draw=False), "calm"),
 ("Step, drink, repeat. Approved, nineteen sixty-six.", stamp(FOUN, "ANIMAL ACTUATED|DRINKING FOUNTAIN", "APR. 22, 1965", "SEPT. 13, 1966", at=1.6), "slow"),

 # ---------- 6 · tricycle ----------
 ("Number six. The tricycle.", chap(6, TRIKE, "Dog Exercising|Device", ["US 4,134,364", "Filed 1976 · Issued 1979"]), "calm"),
 ("Look closely. Next to the front wheel, there is a dog. On a leash.", fig(TRIKE, "trike1", "1", calls=[["THE DOG", 424, 409, -80, 60]]), "calm"),
 ("And the vehicle, in the patent's words, is preferably an adult tricycle.", quote(TRIKE, "which is preferably an adult tricycle", "adult tricycle", "US 4,134,364 · description"), "slow"),
 ("A bar clamps onto the frame and sticks out to the side. The leash hangs from the end. It positions the dog alongside the bicycle.", quote(TRIKE, "which positions the dog alongside the bicycle", "alongside", "US 4,134,364 · description"), "calm"),
 ("Far enough out that it prevents the dog from running into the vehicle or running off sidewise.", quote(TRIKE, "prevents the dog from running into the vehicle or running off sidewise", "sidewise", "US 4,134,364 · description"), "calm"),
 ("The latch is clever. It yieldably resists normal tugging by the dog.", quote(TRIKE, "which yieldably resists normal tugging by the dog", "normal tugging", "US 4,134,364 · description"), "calm"),
 ("But it releases if the dog should suddenly lurch with great force. Say, at a squirrel.", quote(TRIKE, "releases if the dog should suddenly lurch with great force", "great force", "US 4,134,364 · description"), "calm"),
 ("The whole attachment is meant to be easy to apply and remove, and the tether adjusts for different size animals. Small dog, big dog, same tricycle.", fig(TRIKE, "trike1", "1", draw=False, calls=[["THE CLAMP", 388, 235, 80, -60]]), "calm"),
 ("And if one dog is not enough, figure five shows a version for two.", fig(TRIKE, "trike1", "1", draw=False), "calm"),
 ("A dog, a bar, and an adult tricycle. Approved, nineteen seventy-nine.", stamp(TRIKE, "DOG EXERCISING|DEVICE", "AUG. 26, 1976", "JAN. 16, 1979", at=2.2), "slow"),

 # ---------- 5 · bath harness ----------
 ("Number five. Bath night.", chap(5, BATH, "Frame and Harness|for Dog Baths", ["US 2,438,979", "Filed 1946 · Issued 1948"]), "calm"),
 ("This is a bathtub. In the bathtub, a frame. And in the frame, a dog.", fig(BATH, "bath1", "1", calls=[["THE DOG", 333, 183, -80, -40]]), "calm"),
 ("The patent's goal is a device for holding an animal such as a dog in a fixed position in a bath tub.", quote(BATH, "a device for holding an animal such as a dog in a fixed position in a bath tub", "fixed position", "US 2,438,979 · description"), "calm"),
 ("Anyone who has washed a dog knows why. The patent puts it politely.", quote(BATH, Q_LATTER, "the latter", "US 2,438,979 · description", hide=True), "calm"),
 ("To wash the dog without any interference on the part of the latter.", quote(BATH, Q_LATTER, "the latter", "US 2,438,979 · description", typed=False), "slow"),
 ("The latter being the dog.", quote(BATH, Q_LATTER, "without any interference", "US 2,438,979 · description", typed=False), "punch"),
 ("The frame is four bars. Screws with rubber caps press against the walls of the tub, so it fits tubs of different width.", fig(BATH, "bath2", "2", calls=[["RUBBER CAPS", 186, 72, 80, 40]]), "calm"),
 ("Then three straps. One around the neck, one around the chest near the front legs, and one by the hind legs.", fig(BATH, "bath2", "2", draw=False, calls=[["STRAPS", 450, 260, 80, -60]]), "calm"),
 ("All, the patent promises, without causing any particular discomfort to the animal.", quote(BATH, "without causing any particular discomfort to the animal", "particular discomfort", "US 2,438,979 · description"), "calm"),
 ("And when bath night is over, it comes apart for storing in a small space.", fig(BATH, "bath1", "1", draw=False), "calm"),
 ("No shaking. No escaping. Approved, nineteen forty-eight.", stamp(BATH, "FRAME AND HARNESS|FOR DOG BATHS", "JAN. 23, 1946", "APR. 6, 1948", at=1.8), "slow"),

 # ---------- 4 · fetch machine ----------
 ("Number four. The machine that plays fetch.", chap(4, FETCH, "Throw and Fetch|Doggie Toy", ["US 4,995,374", "Filed 1990 · Issued 1991"]), "calm"),
 ("The patent opens with history. Throw and fetch, it says, is an activity which is probably as old as the man-dog relationship.", quote(FETCH, "is an activity which is probably as old as the man-dog relationship.", "man-dog relationship", "US 4,995,374 · description"), "calm"),
 ("Then it states the problem. The human owner usually wears out long before the dog is ready to call it enough for the day.", quote(FETCH, Q_OWNER, "wears out", "US 4,995,374 · description"), "calm"),
 ("And it notes, with some respect, that at least some dogs never seem to get enough of this throw and fetch game.", quote(FETCH, "at least some dogs never seem to get enough of this throw and fetch game", "never seem to get enough", "US 4,995,374 · description"), "calm"),
 ("So here is the answer. Figure one. A box on the lawn fires the ball. The dog runs.", fig(FETCH, "fetch1", "1", calls=[["THE BALL", 821, 41, -80, 40], ["THE BOX", 60, 215, 60, -60]]), "calm"),
 ("Figure two. The dog brings the ball back.", fig(FETCH, "fetch2", "2"), "calm"),
 ("Figure three. The dog drops the ball into the top of the box. It rolls into a tube, and a solenoid fires it out again.", fig(FETCH, "fetch3", "3", calls=[["THE BALL", 163, 105, 80, -40]]), "calm"),
 ("And again. And again. For as long as the dog keeps bringing it back.", fig(FETCH, "fetch1", "1", draw=False), "calm"),
 ("Its stated object: a doggie toy which automatically exercises a dog.", quote(FETCH, "It is yet a further object of this invention to provide a doggie toy which automatically exercises a dog.", "automatically", "US 4,995,374 · description"), "calm"),
 ("The human finally gets to sit down. Approved, nineteen ninety-one.", stamp(FETCH, "THROW AND FETCH|DOGGIE TOY", "FEB. 23, 1990", "FEB. 26, 1991", at=2.0), "slow"),

 # ---------- 3 · tread wheel ----------
 ("Number three. The oldest one on the list.", chap(3, WHEEL, "Tread-|Wheel", ["US 528,066", "Filed 1894 · Issued 1894"]), "calm"),
 ("Eighteen ninety-four. This is a big spoked wheel, with a wide track on the inside of the rim.", fig(WHEEL, "wheel1", "1", calls=[["THE TRACK", 60, 330, 80, -60]]), "calm"),
 ("You may recognize the shape. It is a hamster wheel. It is not for a hamster.", fig(WHEEL, "wheel1", "1", draw=False), "slow"),
 ("It is a tread wheel to be operated by the gravity or weight of an animal, as a dog, goat or sheep.", quote(WHEEL, "to be operated by the gravity or weight of an animal, as a dog, goat or sheep", "a dog, goat or sheep", "US 528,066 · description"), "calm"),
 ("The object, in its own words, is a wheel that is strong, light of weight and easily operated. Easily operated by whom, it does not need to say.", quote(WHEEL, "a wheel that is strong, light of weight and easily operated", "easily operated", "US 528,066 · description"), "calm"),
 ("The dog walks on the inside of the rim, the wheel turns, and a belt around the outside carries the power away.", fig(WHEEL, "wheel2", "2"), "calm"),
 ("To run what? The patent has a list. A milk or cream separator, a churn, a pump.", quote(WHEEL, Q_MACH, "a churn, a pump", "US 528,066 · description"), "calm"),
 ("A sewing machine, a washing machine.", quote(WHEEL, Q_MACH, "a washing machine", "US 528,066 · description", typed=False), "calm"),
 ("A printing press.", quote(WHEEL, Q_MACH, "a printing press", "US 528,066 · description", typed=False), "punch"),
 ("The patent makes sure there is room in there. The wheel provides sufficient space for the convenient travel therein of the dog or other animal that runs the wheel.", quote(WHEEL, "provides sufficient space for the convenient travel therein of the dog or other animal that runs the wheel.", "convenient travel", "US 528,066 · description"), "calm"),
 ("There is even a speed governor. A little weighted lever that keeps the wheel from running too fast.", fig(WHEEL, "wheel3", "3"), "calm"),
 ("A dog-powered laundry room. Approved, October eighteen ninety-four.", stamp(WHEEL, "TREAD-|WHEEL", "JUNE 28, 1894", "OCT. 23, 1894", at=2.2), "slow"),

 # ---------- 2 · umbrella ----------
 ("Number two. Rain.", chap(2, UMB, "Animal|Umbrella", ["US 5,918,611", "Filed 1997 · Issued 1999"]), "calm"),
 ("This dog is carrying its own umbrella.", fig(UMB, "umb1", "1", calls=[["THE UMBRELLA", 300, 110, 60, -40]]), "slow"),
 ("The patent explains. Animals as well as humans require protection from the rain when they are being walked.", quote(UMB, "Animals as well as humans require protection from the rain when they are being walked.", "as well as humans", "US 5,918,611 · description"), "calm"),
 ("And it is not a simple task to have the walker hold an umbrella both over himself and the animal he is walking.", quote(UMB, "It is not a simple task to have the walker hold an umbrella both over himself and the animal he is walking.", "not a simple task", "US 5,918,611 · description"), "calm"),
 ("So a saddle clips onto the dog's harness and collar. A pole rises from the saddle. And on top, a folding canopy, with a drape around the edge.", fig(UMB, "umb1", "1", draw=False, calls=[["THE SADDLE", 250, 370, 80, 60]]), "calm"),
 ("From behind, it looks like this.", fig(UMB, "umb2", "2"), "slow"),
 ("The patent lists its objects with growing excitement. Still yet another object of the present invention is to provide an animal umbrella that is self-supporting.", quote(UMB, "STILL YET ANOTHER OBJECT of the present invention is to provide an animal umbrella that is self-supporting.", "STILL YET ANOTHER", "US 5,918,611 · description"), "calm"),
 ("Even its list of earlier patents builds up to this, in capital letters: finally, still yet another example.", quote(UMB, "FINALLY, STILL YET ANOTHER EXAMPLE", "FINALLY", "US 5,918,611 · description"), "slow"),
 ("And it was not the first. Among the earlier patents it lists is an animal umbrella in the form of a cap with pointed ears extending outwardly therefrom.", quote(UMB, "an animal umbrella that is in the form of a cap with pointed ears extending outwardly therefrom", "pointed ears", "US 5,918,611 · description"), "calm"),
 ("Here is the canopy on its own. It folds, like any umbrella.", fig(UMB, "umb4", "4"), "calm"),
 ("A dog that brings its own umbrella. Approved, July nineteen ninety-nine.", stamp(UMB, "ANIMAL|UMBRELLA", "APR. 2, 1997", "JULY 6, 1999", at=2.0), "slow"),

 # ---------- 1 · goggles ----------
 ("And number one. The weirdest dog patent on our shelf.", chap(1, GOG, "Adjustable|Pet Eyewear", ["US 5,732,415", "Filed 1997 · Issued 1998"]), "calm"),
 ("Goggles for dogs. It is, therefore, an object of the invention to protect the eyes of animals, and particularly canines.", quote(GOG, "It is, therefore, an object of the invention to protect the eyes of animals, and particularly canines.", "particularly canines", "US 5,732,415 · description"), "calm"),
 ("It is for pets, and primarily dogs, who enjoy hanging their heads out of the windows of moving cars.", quote(GOG, "pets, and primarily dogs, who enjoy hanging their heads out of the windows of moving cars.", "out of the windows", "US 5,732,415 · description"), "calm"),
 ("And then, the patent wonders why. Perhaps this is because they enjoy the feel of the wind against their skin.", quote(GOG, "Perhaps this is because they enjoy the feel of the wind against their skin.", "the wind", "US 5,732,415 · description"), "calm"),
 ("Perhaps it is simply that they like to look outward at the passing countryside.", quote(GOG, "Perhaps it is simply that they like to look outward at the passing countryside.", "passing countryside", "US 5,732,415 · description"), "calm"),
 ("The world may never know.", quote(GOG, Q_WORLD, "never know", "US 5,732,415 · description"), "punch"),
 ("Whatever the reason, the dog gets a clear goggle, with straps that run back to a collar.", fig(GOG, "gog3", "3", draw=False, calls=[["STRAP", 312, 300, 80, 60]]), "calm"),
 ("And when the car stops, they flip up onto the head. Like aviator goggles.", fig(GOG, "gog5", "5", calls=[["FLIPPED UP", 536, 109, 100, -40]]), "calm"),
 ("The patent also promises that pug nosed dogs will be fitted just as easily as long-nosed dogs, such as the one shown in the figures.", quote(GOG, "pug nosed dogs will be fitted just as easily as long-nosed dogs, such as the one shown in the figures.", "pug nosed", "US 5,732,415 · description"), "calm"),
 ("And these were not the first dog goggles either. Back in nineteen seventy-nine, another patent drew a schnauzer-looking dog in goggles.", fig(GOG79, "gog79", "2"), "calm"),
 ("That one explained it with more confidence. As instinct commands, the animal desires to extend his head out an open window and into the onrushing wind.", quote(GOG79, "As instinct commands, the animal desires to extend his head out an open window and into the onrushing wind.", "As instinct commands", "US 4,178,742 · description"), "calm"),
 ("Two patents. Two theories. One window.", fig(GOG, "gog5", "5", draw=False), "slow"),
 ("Goggles for the dog with its head out the window. Approved, nineteen ninety-eight.", stamp(GOG, "ADJUSTABLE|PET EYEWEAR", "FEB. 24, 1997", "MAR. 31, 1998", big=True, at=2.4), "slow"),

 # ---------- close ----------
 ("So that is the ranking. But which dog patent is the most approved?", dict(g="title", kicker="THIS SHELF'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the fetch machine. Because it is the only patent here that admits the truth. The human gets tired first.", quote(FETCH, Q_OWNER, "wears out", "US 4,995,374 · description", typed=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["5,003,756 · 887,072 · 3,272,181", "4,134,364 · 2,438,979 · 4,995,374", "528,066 · 5,918,611 · 5,732,415", "4,178,742"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
