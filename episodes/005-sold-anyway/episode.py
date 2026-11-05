# SERIOUSLY APPROVED · FILE 005 · DID IT WORK? — "8 Real Patents That Sounded Weird and Sold Anyway"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents; "did it work" facts from the web sources listed there).
FMT = "long"
TAIL = 3.0
SAY = {"paraffine": "paraffin"}

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

PIN = P("US 6,281", "ONE PIECE|OF [WIRE]", 1849)
EAR = P("US 188,292", "PADS FOR|YOUR [EARS]", 1877)
STRAW = P("US 375,962", "THE [FAKE]|STRAW", 1888)
CANDY = P("US 618,428", "THE [SUGAR]|MACHINE", 1899)
VAC = P("US 889,823", "A FAN|AND A [SACK]", 1908)
BED = P("US 1,185,124", "THE BED THAT|[DISAPPEARS]", 1916)
POP = P("US 1,505,592", "ICE IN A|[TEST TUBE]", 1924)
CORN = P("US 1,706,491", "ANYTHING|ON A [STICK]", 1929)

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"PATENT No. {n} OF 8", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

def verdict(d, title, lines):
    return dict(g="title", kicker="DID IT WORK?", title=title, lines=lines, **d)

INTRO = dict(hook="WEIRD.|THEN [SOLD]", side="FILE 005 · DID IT WORK?")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 005")

Q_LIST = "wieners, boiled ham, hard boiled eggs, cheese, sliced peaches, pineapples, bananas and like fruit, and cherries, dates, figs, strawberries"
Q_CRULLER = "the general appearance of the food product is that of a cruller on a stick"
Q_SNOW = "leaving a white and colorless mass of ice or snow"
Q_STRAW = "an imitation straw requiring close examination in order to distinguish it from the natural straw"
Q_LAMP = "which in use may be connected to a common incandescent lamp socket in the usual manner"
Q_OBV = "in a manner which will be readily obvious to all conversant with such matters"

LINES = [
 # ---------- cold open ----------
 ("This is a pot of hot oil. And this is a list, from a patent filed in nineteen twenty-seven.", fig(CORN, "corn9", "9"), "slow"),
 ("Wieners. Boiled ham. Hard boiled eggs. Cheese. Sliced peaches. Pineapples. Bananas. Cherries, dates, figs, strawberries.", quote(CORN, Q_LIST, "hard boiled eggs", "US 1,706,491 · description"), "slow"),
 ("All of it, on a stick, dipped in batter, and fried. It was approved.", stamp(CORN, "COMBINED DIPPING, COOKING, AND|ARTICLE-HOLDING APPARATUS", "JUL. 5, 1927", "MAR. 26, 1929", at=2.6), "punch"),
 ("Some patents sound ridiculous, and then they end up in every kitchen, every closet, every county fair. Today: eight real patents that sounded weird. And sold anyway. For each one, we ask the only question that matters. Did it work?", dict(g="title", kicker="DID IT WORK? · FILE 005", title="8 Real Patents That|Sounded Weird", lines=["Real drawings. Real quotes.", "Then they sold."], stamp=True, at=9.0, **INTRO), "calm"),

 # ---------- 1 · dress-pin ----------
 ("Number one. Eighteen forty-nine.", chap(1, PIN, "Dress-|Pin", ["US 6,281", "Issued April 10, 1849"]), "calm"),
 ("This is the whole invention. A piece of wire, bent.", fig(PIN, "pin12", "1 & 2"), "calm"),
 ("The patent calls itself a faithful and accurate description. And it describes a pin made of one piece of wire or metal combining a spring, and clasp or catch.", quote(PIN, "a pin made of one piece of wire or metal combining a spring, and clasp or catch", "one piece of wire", "US 6,281 · description"), "calm"),
 ("One end is the point. In the middle, a coil, the spring. At the far end, a little hook to catch the point.", fig(PIN, "pin12", "1 & 2", draw=False, calls=[["COIL SPRING", 216, 99, 60, 60], ["CATCH", 45, 135, 40, 30]]), "calm"),
 ("Open it, and the spring throws the point out. Close it, and the point is held by its own spring.", fig(PIN, "pin12", "1 & 2", draw=False, calls=[["OPEN", 540, 135, -40, 30]]), "calm"),
 ("They may be made of common pin wire, the patent says. Or of the precious metals.", quote(PIN, "They may be made of common pin wire, or of the precious metals.", "precious metals", "US 6,281 · description"), "calm"),
 ("And the main selling point: there being no joint to break or pivot to wear or get loose as in other plans.", quote(PIN, "there being no joint to break or pivot to wear or get loose as in other plans", "no joint to break", "US 6,281 · description"), "calm"),
 ("The last figures add decoration. Any ornamental design may be attached to the bar.", fig(PIN, "pin", "1–8", calls=[["ORNAMENT", 540, 657, -60, -60]]), "calm"),
 ("You know it as the safety pin. Approved, eighteen forty-nine.", stamp(PIN, "DRESS-|PIN", "—", "APR. 10, 1849", at=2.0), "slow"),
 ("Did it work? The pin did. The story goes that its inventor, Walter Hunt, owed someone fifteen dollars, and invented it to pay the debt. And then sold the rights for four hundred dollars.", verdict(PIN, "The Pin, Yes.", ["$15 debt · rights sold for $400", "source: History.com"]), "calm"),

 # ---------- 2 · ear-mufflers ----------
 ("Number two. Maine. Winter.", chap(2, EAR, "Improvement in|Ear-Mufflers", ["US 188,292", "Filed & issued 1877"]), "calm"),
 ("Two pads, on a metal spring band. The patent promises a simpler and more effective device of this character than is now in ordinary use.", quote(EAR, "by which a simpler and more effective device of this character may be produced than is now in ordinary use", "simpler and more effective", "US 188,292 · description"), "calm"),
 ("The band is a flattened metallic spring, semicircular in shape. Each pad hangs from it on a loop of wire.", fig(EAR, "ear1", "1", calls=[["SPRING BAND", 216, 27, 70, 50], ["PAD", 108, 297, -40, 60]]), "calm"),
 ("The wire frame can swing, but only so far. Little bends act as a stop, to keep the pad from swinging outwardly too far.", fig(EAR, "ear1", "1", draw=False, calls=[["WIRE FRAME", 324, 324, 40, 60]]), "calm"),
 ("The pads are covered with cloth. And may be lined with fur, wool, skin, or any other fibrous non-conductor of heat.", quote(EAR, "may be also lined or covered with fur, wool, skin, or any other fibrous non-conductor of heat", "non-conductor of heat", "US 188,292 · description"), "calm"),
 ("Figure two shows the muffler in use. A gentleman with a fur collar and a very calm expression.", fig(EAR, "ear2", "2"), "slow"),
 ("The band goes over the top of the head. Its contractile action pushes the pads firmly against the ears, and protects them from cold.", fig(EAR, "ear2", "2", draw=False, calls=[["PAD", 255, 205, 60, -40]]), "calm"),
 ("How exactly? In a manner which will be readily obvious to all conversant with such matters.", quote(EAR, Q_OBV, "readily obvious", "US 188,292 · description"), "slow"),
 ("Earmuffs. Approved, eighteen seventy-seven.", stamp(EAR, "IMPROVEMENT IN|EAR-MUFFLERS", "FEB. 8, 1877", "MAR. 13, 1877", at=1.4), "slow"),
 ("Did it work? Chester Greenwood built a factory near his hometown. In its best year, nineteen thirty-six, it made over four hundred thousand pairs. His town still celebrates Chester Greenwood Day every December.", verdict(EAR, "Yes.|400,000 Pairs", ["Best year: 1936", "source: Smithsonian Magazine"]), "calm"),

 # ---------- 3 · artificial straw ----------
 ("Number three. Washington, D.C. Eighteen eighty-seven.", chap(3, STRAW, "Artificial|Straw", ["US 375,962", "Filed 1887 · Issued 1888"]), "calm"),
 ("Before this patent, a drinking straw was a straw. An actual stalk of grass. It made drinks taste grassy.", fig(STRAW, "straw", "1–4"), "calm"),
 ("The patent's goal: a cheap, durable, and unobjectionable substitute for the natural straws.", quote(STRAW, "to provide a cheap, durable, and unobjectionable substitute for the natural straws", "unobjectionable", "US 375,962 · description"), "calm"),
 ("The method. A strip of paper. A spinning rod. The corner of the strip goes into a slit in the rod.", fig(STRAW, "straw4", "4", calls=[["PAPER STRIP", 279, 324, 60, 60], ["SPINDLE", 315, 205, 0, -70]]), "calm"),
 ("The rod turns, the paper winds around it in a spiral, and a dab of paste holds the end.", fig(STRAW, "straw4", "4", draw=False), "calm"),
 ("Then the tube is dipped into a vat of molten paraffine. That makes it waterproof.", fig(STRAW, "straw", "1–4", draw=False, calls=[["FINISHED STRAW", 117, 540, 80, 0]]), "calm"),
 ("And the paper is colored in imitation of the natural straw. Because the goal was not a new thing. The goal was a better fake.", quote(STRAW, "colored in imitation of the natural straw", "in imitation", "US 375,962 · description"), "calm"),
 ("The patent is proud of the result.", quote(STRAW, Q_STRAW, "close examination", "US 375,962 · description", hide=True), "calm"),
 ("An imitation straw requiring close examination in order to distinguish it from the natural straw.", quote(STRAW, Q_STRAW, "close examination", "US 375,962 · description", typed=False), "slow"),
 ("The paper straw. Approved, eighteen eighty-eight.", stamp(STRAW, "ARTIFICIAL|STRAW", "MAY 11, 1887", "JAN. 3, 1888", at=1.6), "slow"),
 ("Did it work? Marvin Stone's factory had been making cigarette holders. By eighteen ninety, it was making more drinking straws than cigarette holders.", verdict(STRAW, "Yes.|Straws Won", ["By 1890: more straws than", "cigarette holders · source: Wikipedia"]), "calm"),

 # ---------- 4 · candy machine ----------
 ("Number four. Nashville. A dentist and a confectioner.", chap(4, CANDY, "Candy-|Machine", ["US 618,428", "Filed 1897 · Issued 1899"]), "calm"),
 ("Yes. A dentist. William Morrison, working with confectioner John C. Wharton, invented a machine to turn sugar into thread.", fig(CANDY, "candy1", "1"), "calm"),
 ("The object, in their words: to obtain an edible product consisting of the said filaments of melted and spun sugar or candy.", quote(CANDY, "to obtain an edible product consisting of the said filaments of melted and spun sugar or candy", "spun sugar", "US 618,428 · description"), "calm"),
 ("A bowl on a spinning shaft. A flame underneath to melt the sugar. The bowl spins, and the melted sugar flies out through tiny gaps at the edge.", fig(CANDY, "candy2", "2", calls=[["SUGAR", 486, 54, 80, -10], ["BURNER", 334, 152, -60, 60]]), "calm"),
 ("A ring around the outside catches it. Thus forming into silk-like filaments and small beads of candy.", quote(CANDY, "thus forming into silk-like filaments and small beads of candy", "silk-like filaments", "US 618,428 · description"), "calm"),
 ("Now the whole machine. The flame is fed from a gasoline tank, with an air pump. And everything runs on a pedal.", fig(CANDY, "candy3", "3", calls=[["PEDAL", 621, 900, -70, -50], ["GAS TANK", 207, 792, -40, -70]]), "calm"),
 ("Propelled by foot-power, in the manner of a lathe.", quote(CANDY, "propelled by foot-power in the manner of a lathe", "foot-power", "US 618,428 · description"), "slow"),
 ("Turn the heat up or down, and you get different forms of filaments, beads, or solid bands of candy.", quote(CANDY, "several different forms or proportions of filaments, beads, or solid bands of candy", "solid bands of candy", "US 618,428 · description"), "calm"),
 ("Cotton candy. Approved, eighteen ninety-nine.", stamp(CANDY, "CANDY-|MACHINE", "DEC. 23, 1897", "JAN. 31, 1899", at=1.4), "slow"),
 ("Did it work? At the nineteen-oh-four World's Fair, it was sold as Fairy Floss. By one account, sixty-eight thousand, six hundred fifty-five boxes, at twenty-five cents each.", verdict(CANDY, "Yes.|Fairy Floss", ["68,655 boxes · 25¢ · 1904 World's Fair", "source: Wikipedia"]), "calm"),

 # ---------- 5 · carpet sweeper ----------
 ("Number five. Canton, Ohio.", chap(5, VAC, "Carpet Sweeper|and Cleaner", ["US 889,823", "Filed 1907 · Issued 1908"]), "calm"),
 ("James Spangler worked as a janitor at a dry goods store. He built a machine to suck up the dust.", fig(VAC, "vac2", "2"), "calm"),
 ("A box on wheels. An electric motor on top. Inside, a fan that turns fast enough to make suction.", fig(VAC, "vac2", "2", draw=False, calls=[["MOTOR", 459, 324, -60, -70], ["FAN", 414, 486, 60, 40]]), "calm"),
 ("At the front, a spinning brush. Right behind it, the fan pulls the dust and dirt in.", fig(VAC, "vac2", "2", draw=False, calls=[["BRUSH", 801, 630, -40, -80]]), "calm"),
 ("And the dirt goes into a sack, hung from the handle.", fig(VAC, "vac1", "1", calls=[["SACK", 54, 162, 70, -50], ["MOTOR", 468, 315, 70, 60]]), "calm"),
 ("According to his biography, his early version used a pillowcase borrowed from the store as the dirt bag. And a broom stick for the handle.", fig(VAC, "vac2", "2", draw=False, calls=[["SACK", 72, 360, 60, -60]]), "calm"),
 ("There is even a spring reel on the handle. The wires will be automatically wound upon the reel when it becomes slack.", quote(VAC, "the wires 24 will be automatically wound upon the reel when it becomes slack", "automatically wound", "US 889,823 · description"), "calm"),
 ("And where do you plug it in? Nineteen-oh-seven had an answer. Into a light bulb socket.", quote(VAC, Q_LAMP, "incandescent lamp socket", "US 889,823 · description"), "slow"),
 ("The vacuum cleaner. Approved, nineteen-oh-eight.", stamp(VAC, "CARPET SWEEPER|AND CLEANER", "SEPT. 14, 1907", "JUNE 2, 1908", at=1.8), "slow"),
 ("Did it work? Spangler showed it to his cousin Susan Hoover. Her husband, William Henry Hoover, bought the patent in nineteen-oh-eight. Today, most people associate the vacuum cleaner with him.", verdict(VAC, "Yes.|Just Not His Name", ["Patent bought by W. H. Hoover, 1908", "source: Wikipedia"]), "calm"),

 # ---------- 6 · disappearing bed ----------
 ("Number six. San Francisco.", chap(6, BED, "Disappearing|Bed", ["US 1,185,124", "Filed 1913 · Issued 1916"]), "calm"),
 ("The invention relates to beds which are adapted to be moved into a closet or recess when not in use.", quote(BED, "beds which are adapted to be moved into a closet or recess when not in use", "into a closet", "US 1,185,124 · description"), "calm"),
 ("But this one does more than fold. It goes through the wall. So that it may be used in either chamber, on opposite sides of the wall.", quote(BED, "so that they may be used in either chamber on opposite sides of the wall", "opposite sides of the wall", "US 1,185,124 · description"), "calm"),
 ("Here it is from above. The wall. An opening. The bed, attached to the door.", fig(BED, "bed1", "1", calls=[["WALL", 72, 144, 0, -80], ["BED", 576, 72, 60, 60], ["DOOR", 650, 238, 0, 70]]), "calm"),
 ("Swing the door, and the bed swings with it. To this room. Or, in dotted lines, to the other one.", fig(BED, "bed1", "1", draw=False, calls=[["THE OTHER ROOM", 414, 360, 80, -40]]), "calm"),
 ("A spring and a sliding arm keep it close. Thereby preventing rattling as the door is moved.", quote(BED, "thereby preventing rattling as the door is moved", "preventing rattling", "US 1,185,124 · description"), "calm"),
 ("Folded up, it stands on end behind the door. Like a closet that is secretly a bedroom.", fig(BED, "bed2", "2", calls=[["THE BED", 450, 396, 70, 40]]), "calm"),
 ("One detail the patent is careful to mention. As the door opens, the bed is swung quicker than the door.", quote(BED, "the bed is swung quicker than the door", "quicker than the door", "US 1,185,124 · description"), "slow"),
 ("A Murphy bed, by Mister Murphy. Approved, nineteen sixteen.", stamp(BED, "DISAPPEARING|BED", "JAN. 20, 1913", "MAY 30, 1916", at=1.6), "slow"),
 ("Did it work? So well that in nineteen eighty-nine, a federal appeals court ruled that Murphy bed had become a generic name. And the inventor? According to legend, he lived in a one-room apartment in San Francisco.", verdict(BED, "Yes.|Too Well", ["\"Murphy bed\" ruled generic, 1989", "source: Wikipedia"]), "calm"),

 # ---------- 7 · popsicle ----------
 ("Number seven. Oakland, California.", chap(7, POP, "Frozen|Confectionery", ["US 1,505,592", "Filed 1924 · Issued 1924"]), "calm"),
 ("The goal: a frozen confection that can be eaten without contamination by contact with the hand. And without the need for a plate, spoon, fork or other implement.", quote(POP, "which can be conveniently consumed without contamination by contact with the hand", "contact with the hand", "US 1,505,592 · description"), "calm"),
 ("The mold? Small containers which may be ordinary test tubes.", quote(POP, "small containers which may be ordinary test tubes are charged with the liquid syrup", "ordinary test tubes", "US 1,505,592 · description"), "calm"),
 ("Fill the tube with syrup. Put a stick in it. A board on top holds the sticks down, so they don't float up.", fig(POP, "pop2", "2", calls=[["BOARD", 261, 45, 60, -40], ["TEST TUBES", 135, 144, -60, 60]]), "calm"),
 ("Freeze it. Warm the tube a little. And pull.", fig(POP, "pop", "1, 3 & 4", calls=[["TEST TUBE", 150, 342, 40, 60], ["STICK", 108, 36, 60, 30]]), "calm"),
 ("It will be noted that a substantial tensile force is required to withdraw the confection. Because the ice comes out like a piston, against a vacuum.", quote(POP, "It will be noted that a substantial tensile force is required to withdraw the confection", "substantial tensile force", "US 1,505,592 · description"), "calm"),
 ("The wood matters too. Bass, birch and poplar, being sapless and tasteless. And the wooden handle is an insulator of heat.", fig(POP, "pop", "1, 3 & 4", draw=False, calls=[["FINISHED", 531, 342, -60, 70]]), "calm"),
 ("Then the patent explains how you eat it. You can suck the flavor out first. As a refreshing drink derived from the solid on the stick.", quote(POP, "as a refreshing drink derived from the solid on the stick", "refreshing drink", "US 1,505,592 · description"), "calm"),
 ("And what is left behind?", quote(POP, Q_SNOW, "colorless", "US 1,505,592 · description", hide=True), "question"),
 ("Leaving a white and colorless mass of ice or snow.", quote(POP, Q_SNOW, "colorless", "US 1,505,592 · description", typed=False), "slow"),
 ("The Popsicle. Approved, nineteen twenty-four.", stamp(POP, "FROZEN|CONFECTIONERY", "JUL. 19, 1924", "AUG. 19, 1924", at=1.6), "slow"),
 ("Did it work? Frank Epperson sold the rights in the nineteen twenties, and later said he regretted it. According to NPR, some two billion Popsicles are sold each year.", verdict(POP, "Yes.|2 Billion a Year", ["Rights sold in the 1920s", "source: NPR"]), "calm"),

 # ---------- 8 · corn dog ----------
 ("And number eight. Back to the hot oil. Buffalo, New York.", chap(8, CORN, "Combined Dipping, Cooking, and|Article-Holding Apparatus", ["US 1,706,491", "Filed 1927 · Issued 1929"]), "calm"),
 ("The patent describes a new and novel edible food product. Food on a stick, coated with batter, and deep fried.", quote(CORN, "a new and novel edible food product", "new and novel", "US 1,706,491 · description"), "calm"),
 ("The result, according to the inventor, is a clean, wholesome and tasty refreshment.", quote(CORN, "a clean, wholesome and tasty refreshment", "tasty refreshment", "US 1,706,491 · description"), "calm"),
 ("The machine is a pot of oil with clips around the rim. Each clip holds one stick, upright, with the food under the oil.", fig(CORN, "corn4", "4", calls=[["CLIP", 234, 144, -60, -40], ["BATTER", 375, 500, 70, 40]]), "calm"),
 ("Done? Lift the stick and lay it sideways across the clip. The food hangs just above the oil, to be kept warm until served.", fig(CORN, "corn9", "9", calls=[["COOKING", 360, 288, 40, 70], ["KEPT WARM", 648, 333, 0, -80]]), "calm"),
 ("A lid keeps it tidy. For the purposes of retaining heat, confining odors, preventing oil from spattering.", fig(CORN, "corn8", "8", calls=[["COVER", 198, 27, 70, 30]]), "calm"),
 ("It cooks in about one and a half minutes. The crust is crispy and well browned. And the amount of oil absorbed by the batter is practically nil.", quote(CORN, "that the amount of oil absorbed by the batter is practically nil", "practically nil", "US 1,706,491 · description"), "calm"),
 ("If you chose fruit, there is good news. The flavor is not destroyed, but rather the juice of the fruit flavors the surrounding pastry.", quote(CORN, "if the article is fruit the flavor is not destroyed but rather the juice of the fruit flavors the surrounding pastry", "surrounding pastry", "US 1,706,491 · description"), "calm"),
 ("And the patent's own description of how it looks.", quote(CORN, Q_CRULLER, "a cruller on a stick", "US 1,706,491 · description", hide=True), "calm"),
 ("The general appearance of the food product is that of a cruller on a stick.", quote(CORN, Q_CRULLER, "a cruller on a stick", "US 1,706,491 · description", typed=False), "slow"),
 ("A cruller on a stick. Approved, nineteen twenty-nine.", stamp(CORN, "COMBINED DIPPING, COOKING, AND|ARTICLE-HOLDING APPARATUS", "JUL. 5, 1927", "MAR. 26, 1929", at=2.0), "slow"),
 ("Did it work? Wikipedia cites this patent in the history of the corn dog. About a decade later, the Fletcher family says, they brought their Corny Dogs to the State Fair of Texas.", verdict(CORN, "Yes.|The Corn Dog", ["Corny Dogs · State Fair of Texas", "1938–1942 · source: Wikipedia"]), "calm"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the frozen confectionery. A patent that tells you, step by step, how to suck the flavor out of your dessert, until only a white and colorless mass of ice remains. Two billion a year.", fig(POP, "pop", "1, 3 & 4", draw=False), "calm"),
 ("Every patent quote in this video is word for word. The numbers and the sources for the sales are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["6,281 · 188,292 · 375,962 · 618,428", "889,823 · 1,185,124", "1,505,592 · 1,706,491"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
