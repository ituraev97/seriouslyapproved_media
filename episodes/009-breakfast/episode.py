# SERIOUSLY APPROVED · FILE 009 · THE SHELF — "10 Weird Breakfast Inventions That Got Real Patents"
# Long video, 1920x1080. Countdown 10 -> 1. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, date):
    return dict(num=num, hook=title, side=f"{num} · {date}")

BACON = P("US 2,513,839", "A PAPERWEIGHT|FOR [BACON]", "1950")
CUP = P("US 510,085", "THE EJECTOR|[EGG CUP]", "1893")
OPEN = P("US 886,266", "THE EGG|[OPENER]", "1908")
BOIL = P("US 546,255", "THE EGG-BOILING|[TOWER]", "1895")
ALARM = P("US 1,513,685", "THE ALARM CLOCK|THAT MAKES [COFFEE]", "1924")
TOAST = P("US 3,670,642", "THE TOAST|[DROP TOWER]", "1972")
PAN = P("US 5,481,963", "THE PANCAKE|[ROBOT]", "1996")
SHIELD = P("US 1,324,659", "A SHIELD FOR|[GRAPEFRUIT]", "1919")
GFB = P("US 1,661,036", "A HAT FOR|[GRAPEFRUIT]", "1928")
CEREAL = P("US 4,986,433", "A SLIDE FOR|[CEREAL]", "1991")
CUBE = P("US 4,092,093", "THE SQUARE|[EGG]", "1978")

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"WEIRDNESS RANK · No. {n} OF 10", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="10 WEIRD|[BREAKFAST] PATENTS", side="FILE 009 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 009")

Q_CUBIC = "changing a whole boiled egg into an aesthetic cubic shape"
Q_SOGGY = "Soggy cereal is so undesirable that many people will not eat it"
Q_SPRAY = "the manipulation of a spoon therein causes the juice to be ejected and sprayed to great disadvantage"
Q_PANOBJ = "automatically cooking, flipping, monogramming and discharging a plurality of pancakes"
Q_ENTRAP = "total entrapment of half-cooked pancakes 37 during all flipping and transfer exercises"
Q_SECOND = "the coffee percolator ceases operation, the light of the lamp goes out, the alarm is sounded a second time"

LINES = [
 # ---------- cold open ----------
 ("This is a hard-boiled egg. It is a cube. And it comes from a real United States patent.", fig(CUBE, "cube10", "10", calls=[["A CUBE", 180, 300, 90, 60]]), "slow"),
 ("The patent's goal, in its own words: changing a whole boiled egg into an aesthetic cubic shape.", quote(CUBE, Q_CUBIC, "aesthetic cubic shape", "US 4,092,093 · description"), "calm"),
 ("It was approved. Nineteen seventy-eight.", stamp(CUBE, "APPARATUS FOR|DEFORMING BOILED EGG", "JUNE 16, 1976", "MAY 30, 1978"), "punch"),
 ("Today, ten weird breakfast inventions that got real patents. Eggs, bacon, toast, pancakes, coffee, cereal, and one grapefruit that needed protection. From eighteen ninety-three to nineteen ninety-six. Real drawings, real quotes, counted down from weird to weirdest.", dict(g="title", kicker="THE SHELF · FILE 009", title="Weird Breakfast|Inventions", lines=["Real patents. Ranked.", "All approved."], stamp=True, at=8.0, **INTRO), "calm"),

 # ---------- 10 · bacon ----------
 ("Number ten. The bacon problem.", chap(10, BACON, "Bacon|Cooking Aid", ["US 2,513,839", "Filed 1945 · Issued 1950"]), "calm"),
 ("Here is a frying pan, some bacon, and a paddle lying on top of it.", fig(BACON, "bacon1", "1", calls=[["THE PADDLE", 560, 250, 120, -90]]), "calm"),
 ("The enemy, according to the patent, is the curling and crimping of bacon strips during the cooking operation.", quote(BACON, "curling and crimping of bacon strips during the cooking operation", "curling and crimping", "US 2,513,839 · description"), "calm"),
 ("So the paddle is a flat metal plate, called a platen, with a weight on it. The bent handle rests on the rim of the pan.", fig(BACON, "bacon1", "1", draw=False, calls=[["THE RIM", 760, 120, -170, 60]]), "calm"),
 ("And then it just sits there, under the action of the weight, so that substantial pressure is supplied to the bacon.", quote(BACON, "under the action of the weight, so that substantial pressure is supplied to the bacon", "substantial pressure", "US 2,513,839 · description"), "calm"),
 ("The payoff, it says, is that it permits cooking from both sides at the same time and with better contact.", quote(BACON, "permits cooking from both sides at the same time and with better contact", "both sides", "US 2,513,839 · description"), "calm"),
 ("A paperweight for bacon. Filed in nineteen forty-five. And approved on the Fourth of July, nineteen fifty.", stamp(BACON, "BACON|COOKING AID", "NOV. 30, 1945", "JULY 4, 1950", at=2.2), "slow"),

 # ---------- 9 · egg cup ----------
 ("Number nine. An egg cup with an exit strategy.", chap(9, CUP, "Egg-Cup", ["US 510,085", "Filed 1893 · Issued 1893"]), "calm"),
 ("It starts like an ordinary egg cup. My invention relates to improvements in egg-cups.", quote(CUP, "My invention relates to improvements in egg-cups", "improvements", "US 510,085 · description"), "calm"),
 ("The top is a little basket of flexible strips. A ring slides up and squeezes them around the egg.", fig(CUP, "egg1", "1", calls=[["THE RING", 70, 130, -40, -60]]), "calm"),
 ("But the real problem came after breakfast. The removal of the egg-shell is often somewhat troublesome.", quote(CUP, "the removal of the egg-shell is often somewhat troublesome", "somewhat troublesome", "US 510,085 · description"), "calm"),
 ("So look down the hollow stem. There is a rod, a spring, and a button at the bottom.", fig(CUP, "egg1", "1", draw=False, calls=[["THE SPRING", 260, 560, 80, 40]]), "calm"),
 ("Press the button, and the egg-shell is afterward ejected by the upward pressure of a plate.", quote(CUP, "The egg-shell is afterward ejected by the upward pressure of a plate", "ejected", "US 510,085 · description"), "calm"),
 ("An ejector seat. For an empty eggshell. Approved, December eighteen ninety-three.", stamp(CUP, "EGG-|CUP", "APR. 29, 1893", "DEC. 5, 1893", at=2.4), "slow"),

 # ---------- 8 · egg opener ----------
 ("Number eight. Opening the egg, the long way.", chap(8, OPEN, "Egg-|Opener", ["US 886,266", "Filed 1907 · Issued 1908"]), "calm"),
 ("The patent opens with a promise. The purpose of the invention is to provide a very simple and economic device for opening eggs.", quote(OPEN, "the purpose of the invention is to provide a very simple and economic device for opening eggs", "very simple", "US 886,266 · description"), "calm"),
 ("Here is the very simple device.", fig(OPEN, "open1", "1", calls=[["THE EGG", 360, 70, 120, -30]]), "punch"),
 ("Two halves on a hinge, like a clam, with two long handles. The egg sits on a little cradle with spurs, adapted to pierce the shell of the egg laid on the cradle.", quote(OPEN, "adapted to pierce the shell of the egg laid on the cradle", "pierce the shell", "US 886,266 · description"), "calm"),
 ("Squeeze the handles, and toothed jaws close in and crack the shell in two.", fig(OPEN, "open3", "3", calls=[["THE JAWS", 470, 330, 140, 80]]), "calm"),
 ("Then open it up. The egg falls out. And the springs do one last thing. They throw off the empty shell.", quote(OPEN, "and in so doing will throw off the empty shell.", "throw off", "US 886,266 · description"), "calm"),
 ("Spurs, jaws, latches and springs. Very simple. Very economic. Approved, nineteen oh eight.", stamp(OPEN, "EGG-|OPENER", "AUG. 19, 1907", "APR. 28, 1908", at=2.6), "slow"),

 # ---------- 7 · egg-boiling tower ----------
 ("Number seven. The egg timer is a bucket.", chap(7, BOIL, "Automatic Egg-|Boiling Apparatus", ["US 546,255", "Filed 1895 · Issued 1895"]), "calm"),
 ("This is one machine. It boils eggs.", fig(BOIL, "boil1", "I", calls=[["THE TANK", 470, 110, 100, -50]]), "punch"),
 ("At the bottom, the eggs sit in a basket in boiling water. The basket hangs from a chain that runs up and over a wheel.", fig(BOIL, "boil1", "I", draw=False, calls=[["THE EGGS", 230, 1250, 120, 40], ["THE WHEEL", 370, 480, -90, -90]]), "calm"),
 ("On the other end of the chain is an empty bucket. And above it, a tank runs a thin stream of water into the bucket.", fig(BOIL, "boil1", "I", draw=False, calls=[["THE BUCKET", 420, 700, 120, 40]]), "calm"),
 ("You choose the cooking time by choosing the nozzle. The patent says the same quantity of water may discharge in two, three, four, and six minutes.", quote(BOIL, "the same quantity of water may discharge in two, three, four, and six minutes", "two, three, four, and six minutes", "US 546,255 · description"), "calm"),
 ("At first the eggs are heavier, and so long as this remains the case the egg-basket will remain lowered.", quote(BOIL, "so long as this remains the case the egg-basket will remain lowered", "remain lowered", "US 546,255 · description"), "calm"),
 ("And when the bucket with its contents becomes heavier than the egg-basket and its contents, the bucket goes down, the eggs come up, and the water shuts itself off.", quote(BOIL, "the bucket with its contents becomes heavier than the egg-basket and its contents", "heavier", "US 546,255 · description"), "calm"),
 ("Each valve even has stops, so the operator always knows to a certainty that the valve is correctly set.", quote(BOIL, "the operator always knows to a certainty that the valve is correctly set into either position", "to a certainty", "US 546,255 · description"), "punch"),
 ("A plumbing tower. To boil an egg. Approved, September eighteen ninety-five.", stamp(BOIL, "AUTOMATIC EGG-|BOILING APPARATUS", "JUNE 29, 1895", "SEPT. 10, 1895", at=2.2), "slow"),

 # ---------- 6 · alarm clock coffee ----------
 ("Number six. The alarm clock that makes coffee.", chap(6, ALARM, "Combined Alarm Clock|and Article Heater", ["US 1,513,685", "Filed 1923 · Issued 1924"]), "calm"),
 ("Clock at the bottom. Coffee pot in the middle. A lamp on top.", fig(ALARM, "alarm1", "1", calls=[["THE CLOCK", 165, 760, 110, 40], ["THE COFFEE", 165, 390, 110, -40]]), "calm"),
 ("The goal: a clock having means adapted to give an alarm at a set hour.", quote(ALARM, "A further object is that of providing a clock having means adapted to give an alarm at a set hour,", "at a set hour", "US 1,513,685 · description"), "calm"),
 ("And at that hour, the lamp is illuminated, and the preparation of the coffee is started and continues.", quote(ALARM, "the lamp is illuminated, and the preparation of the coffee is started and continues", "the coffee is started", "US 1,513,685 · description"), "calm"),
 ("The coffee pours into a cup on a little tray. And the tray sits on a lever, with a counterweight.", fig(ALARM, "alarm2", "2", calls=[["THE CUP", 300, 490, -40, -90]]), "calm"),
 ("When the cup is about full of coffee, its weight tips a lever and cuts the power.", quote(ALARM, "When the cup 65 is about full of coffee,", "about full of coffee", "US 1,513,685 · description"), "calm"),
 ("And then, the coffee percolator ceases operation, the light of the lamp goes out, the alarm is sounded a second time.", quote(ALARM, Q_SECOND, "a second time", "US 1,513,685 · description"), "slow"),
 ("One alarm to wake you up. A second alarm to tell you the coffee is ready. Approved, nineteen twenty-four.", stamp(ALARM, "COMBINED ALARM CLOCK|AND ARTICLE HEATER", "JAN. 4, 1923", "OCT. 28, 1924", at=3.0), "slow"),

 # ---------- 5 · toast tower ----------
 ("Number five. Toast, with a fall.", chap(5, TOAST, "Combination Toasting|and Buttering Apparatus", ["US 3,670,642", "Filed 1970 · Issued 1972"]), "calm"),
 ("Earlier toasters that buttered the toast, the patent says, had a problem. Extra shortening could drip down into the heating compartment, where it may be baked onto the heating elements.", quote(TOAST, "where it may be baked onto the heating elements", "baked onto", "US 3,670,642 · description"), "calm"),
 ("So this is a tower. The bread goes in at the top and toasts on a fork.", fig(TOAST, "toast1", "1", calls=[["THE BREAD", 120, 150, 110, -60]]), "calm"),
 ("Then a timer pulls the fork away. And the toast falls.", fig(TOAST, "toast1", "1", draw=False, calls=[["THE DROP", 140, 640, 110, 40]]), "punch"),
 ("On the way down, a pump sprays it with melted butter. And a blade, driven by a chain, cuts it in half.", fig(TOAST, "toast1", "1", draw=False, calls=[["THE BLADE", 260, 830, 140, 60]]), "calm"),
 ("In the patent's words, the toast slice is buttered and sliced as it falls downwardly through the lower compartment.", quote(TOAST, "so the toast slice 25 is buttered and sliced as it falls downwardly through the lower compartment 15.", "buttered and sliced", "US 3,670,642 · description"), "calm"),
 ("And cleaning the butter sprayer is easy. The apparatus then cycled a couple of times to spray warm soapy water through the nozzle.", quote(TOAST, "the apparatus then cycled a couple of times to spray warm soapy water through the nozzle 63 to clean it.", "warm soapy water", "US 3,670,642 · description"), "calm"),
 ("A drop tower for toast. Approved, June nineteen seventy-two.", stamp(TOAST, "COMBINATION TOASTING|AND BUTTERING APPARATUS", "SEPT. 14, 1970", "JUNE 20, 1972", at=1.8), "slow"),

 # ---------- 4 · pancake maker ----------
 ("Number four. The pancake robot.", chap(4, PAN, "Automated|Pancake Maker", ["US 5,481,963", "Filed 1995 · Issued 1996"]), "calm"),
 ("This is a box. It makes three pancakes at a time.", fig(PAN, "pan1", "1", calls=[["THE PANCAKES", 470, 820, 160, 80]]), "calm"),
 ("Why build it? Because pancakes, the patent explains, need a much hotter grill than other grilled foods. And in many restaurants where the cooking grille surface is zealously guarded, pancakes are not served.", quote(PAN, "In many restaurants where the cooking grille surface is zealously guarded, pancakes are not served.", "zealously guarded", "US 5,481,963 · description"), "calm"),
 ("Its job description: automatically cooking, flipping, monogramming and discharging a plurality of pancakes.", quote(PAN, Q_PANOBJ, "monogramming", "US 5,481,963 · description"), "calm"),
 ("Monogramming. Look closely at the drawings. The pancakes say good morning.", fig(PAN, "pan5", "5", calls=[["GOOD MORNIN", 230, 800, -40, 120]]), "punch"),
 ("A pump squeezes the batter through rubber tubes, to dispense the batter out the exit like toothpaste.", quote(PAN, "to dispense the batter out the exit like toothpaste", "like toothpaste", "US 5,481,963 · description"), "calm"),
 ("Then a second hot plate swings over, helped by a falling weight, and locks on top. The two plates turn over together. The pancakes are flipped.", fig(PAN, "pan4", "4", calls=[["THE FLIP", 420, 330, 120, -70]]), "calm"),
 ("The patent's favorite feature: total entrapment of half-cooked pancakes during all flipping and transfer exercises.", quote(PAN, Q_ENTRAP, "total entrapment", "US 5,481,963 · description"), "slow"),
 ("Then the plate tilts, and the finished pancakes slide out into a tray.", fig(PAN, "pan6", "6", calls=[["BREAKFAST", 600, 1310, 160, 40]]), "calm"),
 ("And, the patent adds, the apparatus can be made to be coin operated.", quote(PAN, "the apparatus can be made to be coin operated", "coin operated", "US 5,481,963 · description"), "punch"),
 ("Pancakes in total entrapment. Approved, January nineteen ninety-six.", stamp(PAN, "AUTOMATED|PANCAKE MAKER", "APR. 24, 1995", "JAN. 9, 1996", at=2.0), "slow"),

 # ---------- 3 · grapefruit shield ----------
 ("Number three. The grapefruit arms race.", chap(3, SHIELD, "Fruit-Eating|Shield", ["US 1,324,659", "Filed 1919 · Issued 1919"]), "calm"),
 ("Nineteen nineteen. A problem everyone knows. The manipulation of a spoon therein causes the juice to be ejected and sprayed to great disadvantage.", quote(SHIELD, Q_SPRAY, "great disadvantage", "US 1,324,659 · description"), "calm"),
 ("The answer is a shield. A disk of glass, clamped onto half a grapefruit.", fig(SHIELD, "shield1", "1", calls=[["THE SHIELD", 300, 150, -80, -80]]), "calm"),
 ("A hood on top makes a pocket, so as to form a pocket under which a spoon is manipulated.", quote(SHIELD, "so as to form a pocket under which a spoon is manipulated", "a spoon is manipulated", "US 1,324,659 · description"), "calm"),
 ("A finger ring lets you hold the shield and the fruit with one hand.", fig(SHIELD, "shield1", "1", draw=False, calls=[["FINGER RING", 90, 270, -60, 80]]), "calm"),
 ("And because it is glass, the eatable or pulp portion of the fruit is visible by reason of the transparency of the shield.", quote(SHIELD, "the eatable or pulp portion of the fruit is visible by reason of the transparency of the shield", "visible", "US 1,324,659 · description"), "calm"),
 ("You eat your grapefruit through a window. Approved, December nineteen nineteen.", stamp(SHIELD, "FRUIT-EATING|SHIELD", "MAY 20, 1919", "DEC. 9, 1919", at=2.0), "slow"),
 ("And nine years later, the grapefruit got a hat. A tall paper hood, pinned into the rind.", fig(GFB, "gfb1", "1", calls=[["THE HOOD", 250, 130, 110, -60]]), "calm"),
 ("Its job: preventing the spattering of the juice when eating the fruit. Same war, new hat.", quote(GFB, "for preventing the spattering of the juice when eating the fruit", "spattering", "US 1,661,036 · description"), "calm"),
 ("This one is disposable. Thrown away after a single use.", quote(GFB, "thrown away after a single use", "single use", "US 1,661,036 · description"), "calm"),
 ("And the hood, the patent notes, may be used to bear advertising matter.", quote(GFB, "may be used to bear advertising matter", "advertising matter", "US 1,661,036 · description"), "punch"),
 ("A grapefruit wearing an ad. Approved, nineteen twenty-eight.", stamp(GFB, "GRAPEFRUIT|SHIELD", "FEB. 15, 1927", "FEB. 28, 1928", at=1.8), "slow"),

 # ---------- 2 · cereal chute ----------
 ("Number two. The cereal slide.", chap(2, CEREAL, "Crispy Cereal|Serving Piece", ["US 4,986,433", "Filed 1990 · Issued 1991"]), "calm"),
 ("This patent takes a strong position. Soggy cereal is so undesirable that many people will not eat it.", quote(CEREAL, Q_SOGGY, "so undesirable", "US 4,986,433 · description"), "calm"),
 ("And cereal that claims to stay crisp? It only slows things down. The cereal eventually becomes soggy anyway.", quote(CEREAL, "the cereal eventually becomes soggy anyway.", "soggy anyway", "US 4,986,433 · description"), "calm"),
 ("It is a particular problem, the patent adds, for those who prefer a leisurely breakfast. And many people simply discard the soggy cereal and its milk, which can be wasteful and costly.", quote(CEREAL, "simply discard the soggy cereal and its milk, which can be wasteful and costly", "wasteful and costly", "US 4,986,433 · description"), "calm"),
 ("So here is the fix. Two bowls. Dry cereal up top. Milk down below. And a chute in between.", fig(CEREAL, "cereal1", "1", calls=[["CEREAL", 570, 60, -170, -10], ["MILK", 170, 300, -60, 80]]), "calm"),
 ("You push two or three bites of cereal into the chute. The slope of the chute then causes the measured portion of cereal to slide under the influence of gravity.", quote(CEREAL, "The slope of the chute then causes the measured portion of cereal to slide under the influence of gravity", "slide", "US 4,986,433 · description"), "calm"),
 ("Down it goes, into the milk. Eat it. Repeat.", fig(CEREAL, "cereal3", "3", calls=[["WHEE", 470, 170, 120, -70]]), "punch"),
 ("The base of the lower bowl can be filled with sand. Because the weighted base helps to counteract the forces generated by the chute.", quote(CEREAL, "the weighted base 13 helps to counteract the forces generated by the chute", "the forces generated by the chute", "US 4,986,433 · description"), "calm"),
 ("The result: fresh crispy cereal, no matter how leisurely a breakfast he enjoys.", quote(CEREAL, "no matter how leisurely a breakfast he enjoys", "leisurely", "US 4,986,433 · description"), "calm"),
 ("A water slide for cereal. Approved, January nineteen ninety-one.", stamp(CEREAL, "CRISPY CEREAL|SERVING PIECE", "JUNE 4, 1990", "JAN. 22, 1991", at=1.8), "slow"),

 # ---------- 1 · square egg ----------
 ("And number one. The weirdest breakfast patent on our shelf.", chap(1, CUBE, "Apparatus for|Deforming Boiled Egg", ["US 4,092,093", "Filed 1976 · Issued 1978"]), "calm"),
 ("The square egg. And it starts with a complaint about knives. It is, however, troublesome and time-consuming to change the original natural shape of the boiled egg into a desired shape by cutting it with a knife.", quote(CUBE, "troublesome and time-consuming to change the original natural shape of the boiled egg into a desired shape by cutting it with a knife", "troublesome", "US 4,092,093 · description"), "calm"),
 ("Here is the machine. A square tube, a piston, and a screw cap.", fig(CUBE, "cube1", "1", calls=[["THE CAP", 230, 40, 110, -20]]), "calm"),
 ("And the tube is not just any size. The patent did the math. The length of each side is required to be equal to a cubic root of the volume of an egg.", quote(CUBE, "is required to be equal to a cubic root of the volume of an egg.", "cubic root", "US 4,092,093 · description"), "calm"),
 ("In the inventor's own experiments, a very good result came at three point nine centimeters per side.", fig(CUBE, "cube1", "1", draw=False, calls=[["3.9 CM", 200, 450, 120, 60]]), "calm"),
 ("You drop in a peeled egg while it is still hot. Then you screw the cap down, and the boiled egg is progressively pressed by the pressing surface of the pressing member.", quote(CUBE, "the boiled egg 20 is progressively pressed by the pressing surface 13 of the pressing member 3", "progressively pressed", "US 4,092,093 · description"), "calm"),
 ("And here is the cross section. Look at the middle. The yolk is square too.", fig(CUBE, "cube7", "7", calls=[["SQUARE YOLK", 187, 466, 100, 90]]), "punch"),
 ("The patent confirms it. The yolk itself will be deformed substantially into a cubic shape.", quote(CUBE, "the yolk 21 itself will be deformed substantially into a cubic shape as shown in FIG. 7", "cubic shape", "US 4,092,093 · description"), "calm"),
 ("The tube can be clear plastic, so you can watch. Then it is desirable to cool the egg-containing apparatus in water or in a refrigerator.", quote(CUBE, "it is desirable to cool the egg-containing apparatus in water or in a refrigerator", "in a refrigerator", "US 4,092,093 · description"), "calm"),
 ("Whereupon, the deformed boiled egg will easily come out from the main body.", quote(CUBE, "Whereupon, the deformed boiled egg will easily come out from the main body 2.", "easily come out", "US 4,092,093 · description"), "calm"),
 ("And the bottom plate can press a pattern into it. Here is the finished cube, with a little swirl on top.", fig(CUBE, "cube10", "10", calls=[["THE PATTERN", 150, 110, 110, -40]]), "calm"),
 ("And a cube is only the start. The patent also lists a triangular, a square, a rectangular, a pentagonal, a hexagonal shape, or a round shape.", quote(CUBE, "a triangular, a square, a rectangular, a pentagonal, a hexagonal shape, or a round shape", "a pentagonal, a hexagonal", "US 4,092,093 · description"), "calm"),
 ("Or desired indented letters or symbols onto the surface of this boiled egg. Your breakfast, with your initials on it.", quote(CUBE, "desired indented letters or symbols onto the surface of this boiled egg", "letters or symbols", "US 4,092,093 · description"), "calm"),
 ("A cube. An egg. Approved, May nineteen seventy-eight.", stamp(CUBE, "APPARATUS FOR|DEFORMING BOILED EGG", "JUNE 16, 1976", "MAY 30, 1978", big=True, at=2.2), "slow"),

 # ---------- close ----------
 ("So that is the ranking. But which breakfast patent is the most approved?", dict(g="title", kicker="THIS SHELF'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the alarm clock. Because it is the only machine here that rings twice. Once for you. Once for the coffee.", quote(ALARM, Q_SECOND, "a second time", "US 1,513,685 · description", typed=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["2,513,839 · 510,085 · 886,266", "546,255 · 1,513,685 · 3,670,642", "5,481,963 · 1,324,659 · 1,661,036", "4,986,433 · 4,092,093"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
