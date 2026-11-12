# SERIOUSLY APPROVED · FILE 012 · DID IT WORK? — "8 Weird Kitchen Gadgets That Got Real Patents. Did They Work?"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents; "did it work" facts from the web sources listed there).
FMT = "long"
TAIL = 3.0
SAY = {}

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

POP = P("US 506,207", "A STEAM-POWERED|[POPCORN] CART", 1893)
OPEN = P("US 514,200", "THE OPENER|FOR THE [CAP]", 1894)
SCOOP = P("US 576,395", "ONE HAND,|ONE [SCOOP]", 1897)
BREAD = P("US 1,867,377", "THE WHOLE|LOAF, [SLICED]", 1932)
CHEM = P("US 2,241,368", "A LAB FLASK|FOR [COFFEE]", 1941)
GIL = P("US 2,669,142", "THE JAR|[OPENER] · 1954", 1954)
SPIN = P("US 3,885,321", "A CENTRIFUGE|FOR [SALAD]", 1975)
KCUP = P("US 5,840,189", "COFFEE IN|A [CUP] · 1998", 1998)

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

INTRO = dict(hook="8 WEIRD|[KITCHEN] GADGETS", side="FILE 012 · DID IT WORK?")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 012")

Q_ATTN = "for the purpose of attracting the attention of people passing the device."
Q_REGRET = "I feel bad sometimes that I ever did it."

LINES = [
 # ---------- cold open ----------
 ("This is a popcorn machine from eighteen ninety-three. It has a boiler. It has a steam engine. And on top, a little man.", fig(POP, "pop1", "1", calls=[["THE LITTLE MAN", 360, 100, 120, 40]]), "slow"),
 ("He moves. In the patent's own words, for the purpose of attracting the attention of people passing the device.", quote(POP, Q_ATTN, "attracting the attention", "US 506,207 · description"), "slow"),
 ("It was approved.", stamp(POP, "PEANUT-ROASTER OR|CORN-POPPER", "AUG. 10, 1891", "OCT. 10, 1893", at=0.8), "punch"),
 ("Kitchen gadgets always sound weird at first. A flask for coffee. A centrifuge for lettuce. A machine that slices the whole loaf at once. Today: eight weird kitchen gadgets that got real patents. And for each one, the only question that matters. Did it work?", dict(g="title", kicker="DID IT WORK? · FILE 012", title="8 Weird Kitchen|Gadgets", lines=["Real drawings. Real quotes.", "Did they work?"], stamp=True, at=11.0, **INTRO), "calm"),

 # ---------- 1 · popcorn ----------
 ("Number one. Chicago. Back to the little man.", chap(1, POP, "Peanut-Roaster or|Corn-Popper", ["US 506,207", "Filed 1891 · Issued 1893"]), "calm"),
 ("This is the whole machine. On legs, on wheels. A glass case on top. A bin marked peanuts at the front.", fig(POP, "pop1", "1", draw=False, calls=[["GLASS CASE", 220, 420, -60, 60], ["PEANUTS", 560, 900, 60, 70]]), "calm"),
 ("A small steam engine sits in the middle. The patent says it actuates all the rotating parts of the apparatus.", fig(POP, "pop1", "1", draw=False, calls=[["STEAM ENGINE", 380, 670, 120, -60]]), "calm"),
 ("Even the water tank is heated by the exhaust steam from the engine. The exhaust steam is put to work too.", quote(POP, "This tank and the water therein, are heated by the exhaust steam from the engine", "exhaust steam", "US 506,207 · description"), "calm"),
 ("The corn pops in a pan inside the case. A stirrer turns near the bottom of the pan, to prevent the corn from burning.", fig(POP, "pop1", "1", draw=False, vb="80 260 520 420", calls=[["POPPING PAN", 220, 422, 80, 60]]), "calm"),
 ("And the pan has a wire gauze top or band for preventing the popped corn from flying therefrom.", quote(POP, "This pan is made of sheet metal with a wire gauze top or band for preventing the popped corn from flying therefrom", "flying therefrom", "US 506,207 · description"), "calm"),
 ("The front and two sides of the case are glass. You can watch your popcorn being made.", quote(POP, "while the front and two sides thereof are of glass.", "of glass", "US 506,207 · description"), "calm"),
 ("And as the machine runs, a rocking bar works a rod or cord attached to the arm of the little man on top. A popcorn machine with its own show.", fig(POP, "pop1", "1", draw=False, vb="200 0 380 300", calls=[["FIGURE N", 360, 100, 80, 60]]), "slow"),
 ("Approved, eighteen ninety-three.", stamp(POP, "PEANUT-ROASTER OR|CORN-POPPER", "AUG. 10, 1891", "OCT. 10, 1893", at=1.0), "slow"),
 ("Did it work? Yes. That same year, he took his steam-powered machine to the World's Columbian Exposition in Chicago. The company's history tells of a steam-powered clown added to capture attention: the Tosty Rosty Man. And the company is still in business. In two thousand six, Andrew Cretors became the company's fifth president.", verdict(POP, "Yes.|Still Popping", ["1893 World's Columbian Exposition", "source: Wikipedia · cretors.com"]), "calm"),

 # ---------- 2 · bottle opener ----------
 ("Number two. Baltimore. Eighteen ninety-four.", chap(2, OPEN, "Capped-Bottle|Opener", ["US 514,200", "Filed 1893 · Issued 1894"]), "calm"),
 ("A new kind of bottle cap had a problem. It was made of hard metal, and it gripped the bottle. So how do you get it off?", fig(OPEN, "open1", "1–7"), "calm"),
 ("This patent is the answer. It is specially adapted for the removal of hard metal sealing caps from bottles having locking shoulders.", quote(OPEN, "specially adapted for the removal of hard metal sealing caps from bottles having locking shoulders", "hard metal sealing caps", "US 514,200 · description"), "calm"),
 ("The whole idea fits in one sentence. A handle, having at one end a cap centering gage, and also a cap engaging lip.", fig(OPEN, "open1", "1", draw=False, vb="0 0 600 400", calls=[["THE GAGE", 290, 120, 80, -50], ["THE HANDLE", 500, 150, 40, 60]]), "calm"),
 ("Hook the lip under the edge of the cap. The loop rests on top, as a fulcrum.", fig(OPEN, "open1", "4", draw=False, vb="0 480 560 480", calls=[["THE CAP", 120, 560, 60, -60]]), "calm"),
 ("Then lift the handle. In the patent's words: the cap will be pried from the bottle.", quote(OPEN, "so that when the handle is raised as in Fig. 5, the cap will be pried from the bottle", "pried from the bottle", "US 514,200 · description"), "calm"),
 ("Figure seven goes one step further. One of my openers adapted to be mounted on a table or counter. A counter-mounted opener.", fig(OPEN, "open1", "7", draw=False, vb="560 520 430 520", calls=[["ON THE COUNTER", 740, 840, -80, 60]]), "calm"),
 ("Approved, eighteen ninety-four.", stamp(OPEN, "CAPPED-BOTTLE|OPENER", "JUNE 5, 1893", "FEB. 6, 1894", at=1.0), "slow"),
 ("Did it work? Yes. The inventor was William Painter. His company, Crown Cork and Seal, became a large and durable company. And by Gillette's own account, the salesman King Camp Gillette got advice from Painter: invent something used once, thrown away, and bought again. Gillette went on to the disposable razor blade.", verdict(OPEN, "Yes.|Used Once,|Bought Again", ["Crown Cork & Seal", "source: greatpatent.com"]), "calm"),

 # ---------- 3 · ice cream scoop ----------
 ("Number three. Pittsburgh. Eighteen ninety-seven.", chap(3, SCOOP, "Ice-Cream Mold|and Disher", ["US 576,395", "Filed 1896 · Issued 1897"]), "calm"),
 ("A cone-shaped mold. A long handle. And a second handle underneath, like a pair of tongs.", fig(SCOOP, "scoop1", "1 & 2", calls=[["THE MOLD", 210, 180, 60, -60], ["HANDLES", 850, 740, 40, 60]]), "calm"),
 ("The goal of the patent: a disher that may be conveniently operated with one hand.", quote(SCOOP, "has for its object to construct a disher that may be conveniently operated with one hand.", "one hand", "US 576,395 · description"), "calm"),
 ("Inside the cone, blades rest against the wall. Outside, a little toothed rack.", fig(SCOOP, "scoop1", "2", draw=False, vb="0 420 560 540", calls=[["THE RACK", 360, 640, 80, -60]]), "calm"),
 ("Squeeze the handles together, and the rack turns the cone around the blades.", quote(SCOOP, "The operator grasps the handles and by forcing the two together causes the segmental rack h to engage", "forcing the two together", "US 576,395 · description"), "calm"),
 ("The blades loosen the ice cream, and allow the same to fall into the saucer or plate provided therefor.", quote(SCOOP, "and allow the same to fall into the saucer or plate provided therefor.", "fall into the saucer", "US 576,395 · description"), "calm"),
 ("The drawing shows a cone. The patent adds, though this mold may be of any desired shape.", quote(SCOOP, "though this mold may be of any desired shape.", "any desired shape", "US 576,395 · description"), "calm"),
 ("Approved, eighteen ninety-seven.", stamp(SCOOP, "ICE-CREAM MOLD|AND DISHER", "JUNE 10, 1896", "FEB. 2, 1897", at=1.0), "slow"),
 ("Did it work? Yes. The inventor, Alfred Cralle, worked as a hotel porter and at a drugstore in Pittsburgh. Mental Floss says nearly every ice cream scoop on the market today takes inspiration from his original patent. There is no evidence he ever made a fortune from it.", verdict(SCOOP, "Yes.|Nearly Every Scoop", ["One hand, one squeeze", "source: Mental Floss"]), "calm"),

 # ---------- 4 · bread slicer ----------
 ("Number four. Davenport, Iowa. Nineteen thirty-two.", chap(4, BREAD, "Machine for Slicing an Entire|Loaf of Bread at a Single Operation", ["US 1,867,377", "Filed 1928 · Issued 1932"]), "calm"),
 ("That is the actual title. Machine for slicing an entire loaf of bread at a single operation.", fig(BREAD, "bread4", "4"), "slow"),
 ("Every line you see here is a cutting band. A whole row of them, side by side, one for every cut.", fig(BREAD, "bread4", "4", draw=False, calls=[["CUTTING BANDS", 210, 410, -60, -70]]), "calm"),
 ("And the neighbors move against each other. Adjacent bands move in opposite directions to prevent crushing.", quote(BREAD, "adjacent bands move in opposite directions to prevent crushing and displacement of the", "opposite directions", "US 1,867,377 · description"), "calm"),
 ("From above, it is a pair of conveyors. One delivers the bread to the bands. The other receives the sliced bread.", fig(BREAD, "bread1", "1", calls=[["CONVEYOR", 196, 300, 120, 0]]), "calm"),
 ("Belts at the sides hold the slices in substantial loaf form until the wrapping machine places a suitable wrapper around the same.", quote(BREAD, "hold the slices in substantial loaf form until the wrapping machine places a suitable wrapper around the same", "substantial loaf form", "US 1,867,377 · description"), "calm"),
 ("And the promise: the speed of slicing complete loaves of bread will be materially increased.", quote(BREAD, "the speed of slicing complete loaves of bread will be materially increased.", "materially increased", "US 1,867,377 · description"), "calm"),
 ("Approved, nineteen thirty-two.", stamp(BREAD, "MACHINE FOR SLICING|AN ENTIRE LOAF", "NOV. 26, 1928", "JULY 12, 1932", at=1.0), "slow"),
 ("Did it work? Yes. The first commercial use of the machine was by the Chillicothe Baking Company in Missouri. It sold its first slices on July seventh, nineteen twenty-eight, as Kleen Maid Sliced Bread, and it proved to be a success. Wonder Bread took sliced bread nationwide in nineteen thirty. And in nineteen forty-three, the government banned sliced bread. For about seven weeks. The ban was rescinded on March eighth.", verdict(BREAD, "Yes.|The Best Thing", ["First sold July 7, 1928", "source: Wikipedia"]), "calm"),

 # ---------- 5 · Chemex ----------
 ("Number five. New York. Nineteen forty-one.", chap(5, CHEM, "Filtering|Device", ["US 2,241,368", "Filed 1939 · Issued 1941"]), "calm"),
 ("A funnel joined to a flask. The patent calls it a combination of a filter funnel adapted to hold a paper filter and a bottle-like flask.", fig(CHEM, "chem1", "1", calls=[["FILTER", 220, 160, 90, -40], ["FLASK", 220, 620, -60, 50]]), "calm"),
 ("And the flask is no accident. The filtrate flask is preferably constructed in the well known shape of an Erlenmeyer flask.", quote(CHEM, "The filtrate flask … is preferably constructed in the well known shape of an Erlemeyer flask", "Erlemeyer flask", "US 2,241,368 · description"), "calm"),
 ("That is the cone-shaped flask from a chemistry lab. Here, for coffee.", fig(CHEM, "chem4", "4", calls=[["SPOUT", 80, 370, 60, -60], ["HANDLE", 800, 510, -60, 60]]), "calm"),
 ("The patent explains why a funnel joined to a flask needs a way for the air to escape. The air has to get out somewhere. So the design leaves an air passage, a deep groove down the side of the funnel.", fig(CHEM, "chem3", "3"), "calm"),
 ("And that groove does a second job. It conveniently serves as a pouring spout.", quote(CHEM, "the deep groove 6 cooperating with the lip 5 conveniently serves as a pouring spout", "pouring spout", "US 2,241,368 · description"), "calm"),
 ("When you are done, the filter paper which holds the spent coffee grounds is taken out of the funnel.", quote(CHEM, "the filter paper … which holds the spent coffee grounds is taken out of the funnel", "spent coffee grounds", "US 2,241,368 · description"), "calm"),
 ("And a reminder from the inventor. Cleanliness is of primary significance in all filtering operations.", quote(CHEM, "cleanliness is of primary significance in all filtering operations.", "primary significance", "US 2,241,368 · description"), "slow"),
 ("Approved, nineteen forty-one.", stamp(CHEM, "FILTERING|DEVICE", "APR. 13, 1939", "MAY 6, 1941", at=1.0), "slow"),
 ("Did it work? Yes. You know it as the Chemex. It is in the collection of the Museum of Modern Art in New York. In nineteen fifty-eight, it was named one of the best-designed products of modern times. And it turns up at breakfast in the James Bond novel From Russia with Love.", verdict(CHEM, "Yes.|In a Museum", ["Museum of Modern Art collection", "source: Wikipedia"]), "calm"),

 # ---------- 6 · Gilhoolie ----------
 ("Number six. Yonkers, New York. Nineteen fifty-four.", chap(6, GIL, "Cam Operated Sliding|Jaw Closure Remover", ["US 2,669,142", "Filed 1952 · Issued 1954"]), "calm"),
 ("Cam operated sliding jaw closure remover. In plain English, a jar opener.", fig(GIL, "gil1", "1–3"), "calm"),
 ("Two jaws, one fixed and one on a slide along a long handle. Put them around the lid, and swing the lever. The lever locks the jaws on the lid.", fig(GIL, "gil1", "1", draw=False, calls=[["THE JAWS", 160, 110, 90, -40], ["THE LEVER", 80, 510, -50, 60]]), "calm"),
 ("The cam slot that tightens the jaws sits at an angle of approximately fifty-five degrees.", quote(GIL, "said cam slot being disposed at an angle of approximately 55 relative to said axial line", "approximately 55", "US 2,669,142 · claim 1"), "calm"),
 ("And the description adds: This angle, however, is not critical and may be varied to meet necessary conditions.", quote(GIL, "This angle, however, is not critical and may be varied to meet necessary conditions.", "not critical", "US 2,669,142 · description"), "slow"),
 ("Figure thirteen shows it clamped onto a round lid. Now you have a long lever, and the lid turns.", fig(GIL, "gil13", "13", calls=[["THE LID", 230, 360, -60, 50]]), "calm"),
 ("It also does bottle caps. It can pry them off. And it can put them back on. This makes for a superior clamping action for re-sealing such caps on soda and beer bottles.", quote(GIL, "This makes for a superior clamping action for re-sealing such caps on soda and beer bottles and the like.", "re-sealing", "US 2,669,142 · description"), "calm"),
 ("And it punches cans. The patent's review of its own pour: An unusually good pouring spout or opening is thereby provided.", quote(GIL, "An unusually good pouring spout or opening is thereby provided.", "unusually good", "US 2,669,142 · description"), "slow"),
 ("Approved, nineteen fifty-four.", stamp(GIL, "CAM OPERATED SLIDING|JAW CLOSURE REMOVER", "JULY 28, 1952", "FEB. 16, 1954", at=1.0), "slow"),
 ("Did it work? Yes. It was called the Gilhoolie. It debuted in nineteen fifty-three and was sold by mail order for several years. Wikipedia says its inventor was a retired dentist, and this was his only kitchen patent. Today, a Vermont store lists it again. The original Gilhoolie is back.", verdict(GIL, "Yes.|The Gilhoolie", ["Debuted 1953 · mail order", "source: Wikipedia · Vermont Country Store"]), "calm"),

 # ---------- 7 · salad spinner ----------
 ("Number seven. Gray, France. A U.S. patent, nineteen seventy-five.", chap(7, SPIN, "Domestic Appliance for|Drying Vegetables", ["US 3,885,321", "Filed 1973 · Issued 1975"]), "calm"),
 ("A bowl with a lid. A knob on the lid. It looks like a cake tin.", fig(SPIN, "spin1", "1", calls=[["THE KNOB", 240, 170, -60, -60]]), "calm"),
 ("What it actually does: the draining of vegetables and salads under the action of centrifugal force.", quote(SPIN, "the draining of vegetables and salads under the action of centrifugal force", "centrifugal force", "US 3,885,321 · description"), "slow"),
 ("The knob is a crank. Turn it, and a disc in the lid spins the basket inside.", fig(SPIN, "spin2", "2", calls=[["CRANK", 270, 100, 80, -40], ["THE BASKET", 440, 510, 90, 60]]), "calm"),
 ("Earlier salad driers had problems. In one, the basket has a central shaft which rises to its upper opening.", quote(SPIN, "the basket has a central shaft which rises to its upper opening", "central shaft", "US 3,885,321 · description"), "calm"),
 ("In others, the basket cannot be taken out. It is impossible to place the basket on its bottom and to use it alone with its opening turned upwards.", quote(SPIN, "It is impossible to place the basket on its bottom and to use it alone with its opening turned upwards.", "impossible", "US 3,885,321 · description"), "calm"),
 ("This basket sits on a little pivot underneath. No shaft rising up through the middle. Lift it out, and it is easily removable and usable as such, for example as a strainer.", fig(SPIN, "spin2", "2", draw=False, calls=[["THE PIVOT", 440, 630, 90, 50]]), "calm"),
 ("Approved, nineteen seventy-five.", stamp(SPIN, "DOMESTIC APPLIANCE FOR|DRYING VEGETABLES", "OCT. 25, 1973", "MAY 27, 1975", at=1.0), "slow"),
 ("Did it work? Yes. Wikipedia credits the inventor, Gilberte Fouineteau, with the modern salad spinner. A crank-operated spinner came to the American market in nineteen seventy-four. Some skeptics doubted the need for another gourmet gadget. In nineteen seventy-eight alone, an estimated five hundred thousand were sold.", verdict(SPIN, "Yes.|~500,000 in 1978", ["'Another gourmet gadget'", "source: Wikipedia"]), "calm"),

 # ---------- 8 · K-Cup ----------
 ("And number eight. Nineteen ninety-eight.", chap(8, KCUP, "Beverage Filter|Cartridge", ["US 5,840,189", "Filed 1997 · Issued 1998"]), "calm"),
 ("A small cup. A paper filter inside. Coffee in the filter. A lid on top.", fig(KCUP, "kcup1", "1", calls=[["LID", 260, 100, 90, -40], ["COFFEE", 280, 280, -90, 30], ["FILTER", 280, 340, 90, 40], ["CUP", 260, 780, 90, 40]]), "calm"),
 ("The patent complains about older single-cup coffee devices. The coffee is exposed to the air where it can easily get stale.", quote(KCUP, "the coffee is exposed to the air where it can easily get stale or contaminated", "get stale", "US 5,840,189 · description"), "calm"),
 ("This one is hermetically sealed for freshness. And, the patent notes, it is standard practice to replace the oxygen in the package with nitrogen.", quote(KCUP, "it is standard practice to replace the oxygen in the package with nitrogen.", "with nitrogen", "US 5,840,189 · description"), "calm"),
 ("In the machine, a needle comes down through the lid, and hot water goes in. A second needle pierces the bottom, and coffee comes out.", fig(KCUP, "kcup4", "4", calls=[["NEEDLE IN", 340, 130, 100, -50], ["COFFEE OUT", 490, 570, 100, 50]]), "calm"),
 ("And the filter is built not to give up. Even when the filter is wetted, it will not collapse or sag.", quote(KCUP, "Even when the filter 14 is wetted, it will not collapse or sag against the inner wall 12a of the base 12.", "will not collapse or sag", "US 5,840,189 · description"), "calm"),
 ("One cup. One coffee. Then the cup goes in the trash.", fig(KCUP, "kcup1", "1", draw=False), "slow"),
 ("Approved, nineteen ninety-eight.", stamp(KCUP, "BEVERAGE FILTER|CARTRIDGE", "AUG. 20, 1997", "NOV. 24, 1998", at=1.0), "slow"),
 ("Did it work? Too well. You know it as the K-Cup. According to Time, Keurig sold about nine point eight billion pods in twenty fourteen. One of the inventors, John Sylvan, had sold his share in nineteen ninety-seven, for fifty thousand dollars. He told The Atlantic:", verdict(KCUP, "Yes.|9.8 Billion in 2014", ["Share sold in 1997 for $50,000", "source: TIME · The Atlantic"]), "calm"),
 ("I feel bad sometimes that I ever did it.", quote(KCUP, Q_REGRET, "feel bad", "John Sylvan · The Atlantic, via TIME (2015)"), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the popcorn machine. A boiler, a steam engine, a glass case, and a little man on the roof, whose only job is to get your attention. It worked on us.", fig(POP, "pop1", "1", draw=False), "calm"),
 ("Every patent quote in this video is word for word. The sources for every did it work answer are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["506,207 · 514,200 · 576,395", "1,867,377 · 2,241,368 · 2,669,142", "3,885,321 · 5,840,189"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
