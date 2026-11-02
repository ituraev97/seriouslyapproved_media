# SERIOUSLY APPROVED · FILE 002 · THE SHELF — "8 Real Patents for Your Cat (All Approved)"
# Long video, 1920x1080. Facts and quotes: sources.md (scan OCR, checked against Google Patents).
FMT = "long"
TAIL = 3.0

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

POOL = P("US 5,188,059", "A POOL TABLE|FOR [CATS]", 1993)
TUBE = P("US 2,540,309", "THE ROLLING|[CAT] TUBE", 1951)
BRIDGE = P("US 5,002,012", "ROPE [BRIDGES]|FOR CATS", 1991)
MOUSE = P("US 1,534,964", "A [MOUSE]|IN A BALL", 1925)
REMOTE = P("US 5,675,225", "THE [REMOTE]|CAT TOY", 1997)
LITTER = P("US 5,738,040", "A LITTER BOX|WITH A [FAN]", 1998)
PEND = P("US 5,881,679", "THE MAGNETIC|[PENDULUM]", 1999)
TREAD = P("US 5,913,750", "A [TREADMILL]|FOR CATS", 1999)

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"PATENT No. {n} OF 8", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="FOR YOUR|[CAT]", side="FILE 002 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 002")
TQ = "As cats are adept at minimizing exertion, the treadmill 48 should be covered with a plastic cover 62"

LINES = [
 # ---------- cold open ----------
 ("This is a treadmill. For a cat.", fig(TREAD, "tread1", "1"), "slow"),
 ("The cat walks up a moving belt. At the top, there's a perch. And the patent suggests putting the food and water up there. Dinner now comes with cardio.", fig(TREAD, "tread1", "1", draw=False), "calm"),
 ("It was approved.", stamp(TREAD, "FELINE EXERCISE AND|ENTERTAINMENT CENTER", "NOV. 20, 1997", "JUN. 22, 1999"), "punch"),
 ("Somebody invented it. Somebody filed it. And the United States Patent Office said yes. Today, eight real patents. All of them for your cat. None of them requested by your cat.", dict(g="title", kicker="THE SHELF · FILE 002", title="8 Real Patents|for Your Cat", lines=["Real drawings. Real quotes.", "Really approved."], stamp=True, at=7.0, **INTRO), "calm"),

 # ---------- 1 · pool table bed ----------
 ("Number one. The living room.", chap(1, POOL, "Amusement Device|and Bed for Cats", ["US 5,188,059", "Filed 1989 · Issued 1993"]), "calm"),
 ("This is a wooden box, about fourteen by twenty-four inches. Leather is stretched across the top. There are holes in the corners. And a slit in the middle.", fig(POOL, "pool1", "1"), "calm"),
 ("Under the leather, there is a ball. The patent explains why.", quote(POOL, "Cats love ping-pong balls.", "ping-pong balls", "US 5,188,059 · description", hide=True), "calm"),
 ("Cats love ping-pong balls.", quote(POOL, "Cats love ping-pong balls.", "ping-pong balls", "US 5,188,059 · description", typed=False), "punch"),
 ("The cat pokes a paw through a hole. The ball moves. The cat cannot see why.", fig(POOL, "pool2", "2"), "calm"),
 ("Then the inventor offers a theory. Carefully.", quote(POOL, "While not wishing to be bound by any theory to explain why cats are entertained by the present invention", "not wishing to be bound by any theory", "US 5,188,059 · description"), "slow"),
 ("The theory: the ball responds to the cat. But the cat cannot figure that out and believes the ball is moving of its own accord.", quote(POOL, "the cat cannot figure that out and believes the ball is moving of its own accord", "of its own accord", "US 5,188,059 · description"), "calm"),
 ("The leather is fixed to the box with brass upholstery studs. Such as those used in fine leather furniture.", quote(POOL, "with brass upholstery studs, such as those used in fine leather furniture", "fine leather furniture", "US 5,188,059 · description"), "calm"),
 ("Cheaper versions are allowed. The box could be plywood, fiber board, or cardboard. Although, the patent adds, this is not preferred.", quote(POOL, "cardboard (although this is not preferred)", "not preferred", "US 5,188,059 · description"), "calm"),
 ("It is also a bed. And it comes in colors. To match your decor.", fig(POOL, "pool1", "1", draw=False), "calm"),
 ("The patent's example: powder blue decor? Blonde wood and powder blue leather. Antique decor? Dark walnut and burgundy leather.", quote(POOL, "a consumer with a powder blue decor might prefer an embodiment of the invention in a blonde wood stain with powder blue leather", "powder blue leather", "US 5,188,059 · description"), "slow"),
 ("The holes are compared to the pockets of a billiard table. And the patent suggests an upgrade. Six holes. So the end product would look even more like a real pool table with six pockets.", quote(POOL, "the end product would look even more like a real pool table with six pockets", "a real pool table", "US 5,188,059 · description"), "calm"),
 ("And it is a multiplayer game. The game gets even more lively when more than one cat plays.", quote(POOL, "The game gets even more lively when more than one cat plays.", "more than one cat", "US 5,188,059 · description"), "calm"),
 ("Cats play with the present invention for hours, says the patent. Approved, nineteen ninety-three.", stamp(POOL, "AMUSEMENT DEVICE|AND BED FOR CATS", "MAY 22, 1989", "FEB. 23, 1993", at=3.0), "slow"),

 # ---------- 2 · rolling tube ----------
 ("Number two. Nineteen forty-nine.", chap(2, TUBE, "Plaything|for Cats", ["US 2,540,309", "Filed 1949 · Issued 1951"]), "calm"),
 ("A clear plastic tube. Open at both ends. Big enough for a cat to walk inside.", fig(TUBE, "tube12", "1 & 2"), "calm"),
 ("Inside, toys hang on strings. The cat goes in to grab them.", fig(TUBE, "tube6", "6"), "calm"),
 ("The tube starts as a flat sheet with holes along the edges. You roll it up and lace it shut with string.", fig(TUBE, "tube12", "1 & 2", draw=False), "calm"),
 ("And when the cat grabs, the tube rolls. The patent claims a tube free to roll on a floor in response to movements of a cat.", quote(TUBE, "free to roll on a floor in response to movements of a cat", "free to roll", "US 2,540,309 · claims"), "calm"),
 ("So the cat is inside a rolling tube, chasing toys that roll with it.", fig(TUBE, "tube12", "1 & 2", draw=False), "slow"),
 ("The patent is honest about who this is really for.", quote(TUBE, "induces the cats to perform numerous antics quite amusing to the observers", "quite amusing to the observers", "US 2,540,309 · description", hide=True), "calm"),
 ("It induces the cats to perform numerous antics quite amusing to the observers.", quote(TUBE, "induces the cats to perform numerous antics quite amusing to the observers", "quite amusing to the observers", "US 2,540,309 · description", typed=False), "slow"),
 ("It ships flat. Plastic sheets, string and toys, to be assembled by the purchaser.", quote(TUBE, "to be assembled by the purchaser", "assembled by the purchaser", "US 2,540,309 · description"), "calm"),
 ("And everything can be made of waterproof plastic. For sanitary cleansing.", quote(TUBE, "For sanitary cleansing, the flat sheets, toy elements, and also the string, can be made of waterproof plastic material.", "sanitary cleansing", "US 2,540,309 · description"), "calm"),
 ("Some assembly required. Approved, nineteen fifty-one.", stamp(TUBE, "PLAYTHING|FOR CATS", "MAY 6, 1949", "FEB. 6, 1951", at=1.6), "slow"),

 # ---------- 3 · rope bridges ----------
 ("Number three. Look up.", chap(3, BRIDGE, "Overhead Wall Mounted Cat|Platform System with|Multiple Access", ["US 5,002,012", "Filed 1989 · Issued 1991"]), "calm"),
 ("This is a platform, high on the wall. For the cat.", fig(BRIDGE, "bridge1", "1"), "calm"),
 ("The cat can climb a carpeted pole to get there. Or it can take the bridge.", fig(BRIDGE, "bridge1", "1", draw=False), "calm"),
 ("Each suspension bridge is made up of a plurality of small platforms or steps attached to ropes.", quote(BRIDGE, "Each suspension bridge is made up of a plurality of small platforms or steps attached to ropes.", "suspension bridge", "US 5,002,012 · summary"), "calm"),
 ("Rope bridges. Indoors. Held up by what the claims call undulating connector ropes.", quote(BRIDGE, "undulating connector ropes", "undulating", "US 5,002,012 · claims 1, 2"), "slow"),
 ("The steps can be inclined. Or horizontal. Or carpeted. The claims cover all of it.", fig(BRIDGE, "bridge1", "1", draw=False), "calm"),
 ("The goal, in the patent's words: a device which more fully exploits a cat's superior climbing abilities and sense of balance.", quote(BRIDGE, "a device which more fully exploits a cat's superior climbing abilities and sense of balance", "superior climbing abilities", "US 5,002,012 · summary"), "calm"),
 ("To the greater enjoyment of the cat. And entertainment of its owner.", quote(BRIDGE, "to the greater enjoyment of the cat and entertainment of its owner", "entertainment of its owner", "US 5,002,012 · summary"), "slow"),
 ("And there is a bonus. It is mounted on the wall, so it occupies little human space.", quote(BRIDGE, "which occupies little human space", "little human space", "US 5,002,012 · summary"), "calm"),
 ("It is also designed to blend with the furnishings. A rope bridge on the living room wall. Blending in.", quote(BRIDGE, "to provide a platform which can be made to blend with the furnishings and environment", "blend with the furnishings", "US 5,002,012 · summary"), "slow"),
 ("Little human space. Approved, nineteen ninety-one.", stamp(BRIDGE, "OVERHEAD WALL MOUNTED|CAT PLATFORM SYSTEM|WITH MULTIPLE ACCESS", "MAR. 27, 1989", "MAR. 26, 1991", at=1.6), "slow"),

 # ---------- 4 · mouse in a ball ----------
 ("Number four. We go back to nineteen twenty-three.", chap(4, MOUSE, "Animal|Toy", ["US 1,534,964", "Filed 1923 · Issued 1925"]), "calm"),
 ("A hollow rubber ball with oval slots. And inside the ball, a mouse.", fig(MOUSE, "mouse1", "1"), "calm"),
 ("Not a real one. The claim calls it a catnip-scented figure of a mouse. Made of cloth, stuffed with catnip.", quote(MOUSE, "a catnip-scented figure of a mouse", "catnip-scented", "US 1,534,964 · claim 1"), "calm"),
 ("So that, quote, an odor will be produced that is pleasing to a cat.", quote(MOUSE, "an odor will be produced that is pleasing to a cat", "pleasing to a cat", "US 1,534,964 · description"), "slow"),
 ("And here is the plan, written in nineteen twenty-three.", quote(MOUSE, "the cat may see the mouse but cannot remove the same from the ball", "cannot remove the same", "US 1,534,964 · objects", hide=True), "calm"),
 ("The cat may see the mouse but cannot remove the same from the ball.", quote(MOUSE, "the cat may see the mouse but cannot remove the same from the ball", "cannot remove the same", "US 1,534,964 · objects", typed=False), "slow"),
 ("Not by the cat, anyway. How do you get the mouse in? You stretch the rubber ball until one slot is big enough.", fig(MOUSE, "mouse2", "2"), "calm"),
 ("And the mouse is too light to push its way out. Even when the ball is upside down.", quote(MOUSE, "the mouse which is not of sufficient weight to force its way through when the ball is inverted", "not of sufficient weight", "US 1,534,964 · description"), "calm"),
 ("And the inventor promises peace in the house. The ball will not injure the furniture nor hurt the cat.", quote(MOUSE, "will not injure the furniture nor hurt the cat", "nor hurt the cat", "US 1,534,964 · description"), "calm"),
 ("The furniture is mentioned first. Approved, nineteen twenty-five.", stamp(MOUSE, "ANIMAL|TOY", "JAN. 18, 1923", "APR. 21, 1925", at=2.0), "slow"),

 # ---------- 5 · remote toy ----------
 ("Number five. Remote control.", chap(5, REMOTE, "Interactive|Pet Toy", ["US 5,675,225", "Filed 1995 · Issued 1997"]), "calm"),
 ("A low base. A rotating arm. A string. And on the end of the string, a toy.", fig(REMOTE, "remote1", "1"), "calm"),
 ("A battery motor swings the toy around. A switch reverses it. The switch can sit at the end of a cable. So you can play with your cat from across the room.", fig(REMOTE, "remote1", "1", draw=False), "calm"),
 ("The patent goes further. It lets the owner directly or remotely play with his pet from virtually anywhere.", quote(REMOTE, "lets the owner directly or remotely play with his pet from virtually anywhere", "from virtually anywhere", "US 5,675,225 · background"), "calm"),
 ("It also has a view of cats. And of us.", quote(REMOTE, "House cats, like people, are creatures of habit.", "creatures of habit", "US 5,675,225 · background"), "slow"),
 ("And a mission. To help cats that have grown over fearful, aggressive, or have become poor hunters.", quote(REMOTE, "a novel pet toy to help cats that have grown over fearful, aggressive or have become poor hunters", "poor hunters", "US 5,675,225 · summary"), "calm"),
 ("It calls itself a theater of learning.", quote(REMOTE, "a theater of learning", "theater of learning", "US 5,675,225 · background"), "slow"),
 ("And the motor is belt driven, because, quote, the motor belt drive mechanism produces less noise which is more pleasing to operators and pets.", quote(REMOTE, "The motor belt drive mechanism produces less noise which is more pleasing to operators and pets.", "more pleasing", "US 5,675,225 · background"), "calm"),
 ("And it knows its audience. Cats have shown a tendency to chew on exposed cords. So the remote cord carries only one and a half volts. A wireless remote, the patent adds, could also be used.", quote(REMOTE, "the remote cord has only 1.5 volts direct current", "1.5 volts", "US 5,675,225 · summary"), "calm"),
 ("It can be mounted upright, upside down, on a wall, or hung on a door knob. Some parts are held on with screws. However, gluing or other fasteners could also be used.", quote(REMOTE, "however, gluing or other fasteners could also be used", "gluing or other fasteners", "US 5,675,225 · description"), "calm"),
 ("The patent says that a lot. Approved, nineteen ninety-seven.", stamp(REMOTE, "INTERACTIVE|PET TOY", "AUG. 23, 1995", "OCT. 7, 1997", at=1.6), "slow"),

 # ---------- 6 · litter box ----------
 ("Number six. The litter box.", chap(6, LITTER, "Ventilated Cat|Litter Box", ["US 5,738,040", "Filed 1996 · Issued 1998"]), "calm"),
 ("This is not a box. This is a cabinet. With a doorway for the cat, and a drawer for the litter.", fig(LITTER, "litter1", "1"), "calm"),
 ("The patent's opinion of itself is high. It has all the advantages of the prior art and none of the disadvantages.", quote(LITTER, "which has all the advantages of the prior art and none of the disadvantages", "none of the disadvantages", "US 5,738,040 · summary"), "calm"),
 ("Inside, the floor has carpet. The synthetic carpeting serves to clean cat litter residue off of the cat's paws.", quote(LITTER, "The synthetic carpeting 24 serves to clean cat litter residue off of the cat's paws.", "off of the cat's paws", "US 5,738,040 · description"), "calm"),
 ("There's a shelf, too. A sitting area for the cat if it chooses to remain within the housing.", quote(LITTER, "The L-shaped shelf provides a sitting area for the cat if it chooses to remain within the housing 12.", "if it chooses to remain", "US 5,738,040 · description"), "slow"),
 ("And there is a round window on the side. The patent explains who the window is for.", quote(LITTER, "The circular window 34 is elevated for viewing of the interior of the housing 12 by the cat's owners.", "by the cat's owners", "US 5,738,040 · description", hide=True), "calm"),
 ("The circular window is elevated for viewing of the interior of the housing by the cat's owners.", quote(LITTER, "The circular window 34 is elevated for viewing of the interior of the housing 12 by the cat's owners.", "by the cat's owners", "US 5,738,040 · description", typed=False), "slow"),
 ("The drawer has a window too. So the owner can visualize the litter box without having to open the drawer.", quote(LITTER, "The window 44 allows for the cat owner to visualize the litter box without having to open the drawer 38.", "visualize the litter box", "US 5,738,040 · description"), "calm"),
 ("Then the technology. A motion detector senses the cat coming in, and switches on an exhaust fan in the roof.", quote(LITTER, "The motion detector 52 will detect the entrance of the cat into the housing 12.", "detect the entrance of the cat", "US 5,738,040 · description"), "calm"),
 ("The fan has a hose. The hose connects to an outlet of the house. The fan keeps running for a while after the cat leaves.", fig(LITTER, "litter4", "4"), "calm"),
 ("Plus a deodorizer. Which, the patent says, serves to offset the unpleasant odor produced from the litter box.", quote(LITTER, "The deodorizer 48 serves to offset the unpleasant odor produced from the litter box.", "unpleasant odor", "US 5,738,040 · description"), "calm"),
 ("How do you use it? The patent is brief. Accordingly, no further discussion relating to the manner of usage and operation will be provided.", quote(LITTER, "Accordingly, no further discussion relating to the manner of usage and operation will be provided.", "no further discussion", "US 5,738,040 · description"), "slow"),
 ("No further discussion. Approved, nineteen ninety-eight.", stamp(LITTER, "VENTILATED CAT|LITTER BOX", "OCT. 18, 1996", "APR. 14, 1998", at=1.6), "slow"),

 # ---------- 7 · magnetic pendulum ----------
 ("Number seven. Physics.", chap(7, PEND, "Magnetic Pendulum Device|for Feline Amusement|and Exercise", ["US 5,881,679", "Filed 1997 · Issued 1999"]), "calm"),
 ("The patent opens with respect. Cats are predatory creatures with precision tuned hunting skills.", quote(PEND, "Cats are predatory creatures with precision tuned hunting skills.", "precision tuned", "US 5,881,679 · prior art"), "calm"),
 ("Then it admits a problem with humans. There may be times when the owner does not have time or energy to play with their pets.", quote(PEND, "There may be times when the owner does not have time or energy to play with their pets", "time or energy", "US 5,881,679 · prior art"), "calm"),
 ("And a problem with other toys. Their repetitious motion can become very predictable to the cat.", quote(PEND, "their repetitious motion can become very predictable to the cat", "very predictable", "US 5,881,679 · prior art"), "calm"),
 ("So: a pendulum. A toy hangs on a rod over the base. One magnet under the toy, magnets in the base. They push against each other.", fig(PEND, "pend1", "1"), "calm"),
 ("Bat the toy, and it darts and bounces in a way the cat cannot predict.", fig(PEND, "pend2", "2", ring=[950, 440, 170]), "calm"),
 ("The toy on the end can be swapped. The drawings show a mouse, a bird, even a flower. Different colors and forms.", fig(PEND, "pend4", "4a, 4b, 4d"), "calm"),
 ("And the patent reports what happens when the cat wins.", quote(PEND, "When seized, the toy has been found to continue to twitch and jump in a most lifelike manner.", "in a most lifelike manner", "US 5,881,679 · summary", hide=True), "calm"),
 ("When seized, the toy has been found to continue to twitch and jump in a most lifelike manner.", quote(PEND, "When seized, the toy has been found to continue to twitch and jump in a most lifelike manner.", "in a most lifelike manner", "US 5,881,679 · summary", typed=False), "slow"),
 ("And according to the patent, cats tend to return to this device for repeated play more frequently than with other less engaging designs.", quote(PEND, "the cats tend to return to this device for repeated play more frequently than with other less engaging designs", "repeated play", "US 5,881,679 · summary"), "calm"),
 ("It even has a setting for older cats. Adjustable to match the cat's dexterity as it ages and its responsiveness diminishes.", quote(PEND, "adjustable to match the cat's dexterity as it ages and its responsiveness diminishes", "as it ages", "US 5,881,679 · objects"), "calm"),
 ("A senior mode. Approved, nineteen ninety-nine.", stamp(PEND, "MAGNETIC PENDULUM|DEVICE FOR FELINE|AMUSEMENT AND EXERCISE", "JUL. 29, 1997", "MAR. 16, 1999", at=1.4), "slow"),

 # ---------- 8 · treadmill ----------
 ("And number eight. Back to the treadmill.", chap(8, TREAD, "Feline Exercise and|Entertainment Center", ["US 5,913,750", "Filed 1997 · Issued 1999"]), "calm"),
 ("The patent begins with humans. Regular exercise has been recognized as an important component of general health for humans.", quote(TREAD, "Regular exercise has been recognized as an important component of general health for humans.", "for humans", "US 5,913,750 · background"), "calm"),
 ("Cats, it notes, have everything handed to them. So here is the solution. A wooden frame. Pine boards, for example. A perch on top. And a motorless treadmill leading up to it.", fig(TREAD, "tread3", "3"), "calm"),
 ("The belt rolls back as the cat climbs. So the cat walks farther than the ramp is long.", fig(TREAD, "tread3", "3", draw=False), "calm"),
 ("The belt is, for example, eight inches wide and seventy-two inches long. With small wooden bars across it, to aid in cat traction.", quote(TREAD, "spaced wooden bars 61 to aid in cat traction and serve as steps", "to aid in cat traction", "US 5,913,750 · description"), "calm"),
 ("And the patent anticipated one problem.", quote(TREAD, TQ, "adept at minimizing exertion", "US 5,913,750 · description", hide=True), "calm"),
 ("As cats are adept at minimizing exertion, the treadmill should be covered. To prevent the cat from simply jumping from the floor to the perch.", quote(TREAD, TQ, "adept at minimizing exertion", "US 5,913,750 · description", typed=False), "slow"),
 ("The angle is adjustable. Less steep for heavier feline use, and more steep for lighter feline use.", quote(TREAD, "less steep for heavier feline use, and more steep for lighter feline use", "heavier feline use", "US 5,913,750 · claim 4"), "calm"),
 ("The bottom end can even rest on a bookcase or a chair. Or connect to another piece of cat furniture.", fig(TREAD, "tread1", "1", draw=False), "calm"),
 ("The goal, in the patent's words: to obtain the desired treadmill time for a particular perch entry.", quote(TREAD, "to obtain the desired treadmill time for a particular perch entry", "treadmill time", "US 5,913,750 · summary"), "slow"),
 ("Food and water can go on the perch. And so, the patent adds, can a cat hygiene pan. Everything a cat needs. At the top of a treadmill.", quote(TREAD, "a cat hygiene pan may be positioned between the horizontal members or on the perch", "on the perch", "US 5,913,750 · description"), "calm"),
 ("And the perch has a door. It can be closed to keep the cat inside for short periods of time, for example when non-cat-appreciative guests are in the house.", quote(TREAD, "for example when non-cat-appreciative guests are in the house", "non-cat-appreciative guests", "US 5,913,750 · description"), "slow"),
 ("Treadmill time. Approved, nineteen ninety-nine.", stamp(TREAD, "FELINE EXERCISE AND|ENTERTAINMENT CENTER", "NOV. 20, 1997", "JUN. 22, 1999", at=1.6), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the cat treadmill. Because somewhere, a cat is walking uphill to dinner. And the belt is rolling back.", fig(TREAD, "tread1", "1", draw=False), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["5,188,059 · 2,540,309 · 5,002,012", "1,534,964 · 5,675,225 · 5,738,040", "5,881,679 · 5,913,750"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
