# SERIOUSLY APPROVED · FILE 003 · Short s5 — US 1,174,436. Facts/quotes: ../../sources.md
FMT = "short"
NUM = 'US 1,174,436'
HOOK = "GUESS WHAT|THIS [POST] DOES"
HOOK2 = 'THE FAN|[TOWER] · 1916'
HOOK_SWITCH = 1
TAIL = 2.6
LINES = [
 ('This is a real patent from nineteen sixteen. A post fixed to a rocking chair. A roller on the floor. And a box on top.', dict(g="fig", fig="nielsen1", figno="1"), 'question'),
 ('The box has a fan in it.', dict(g="fig", fig="nielsen1", figno="1", draw=False, calls=[["FAN", 302, 124, -120, -40]]), 'punch'),
 ('Rock backward, and the post is drawn toward the floor. A rod pulls a lever, a pawl turns the gears, and the gears spin the fan.', dict(g="fig", fig="nielsen1", figno="1", draw=False, ring=[824, 982, 120]), 'calm'),
 ('Rock forward again, and a spring resets the pawl.', dict(g="quote", q="the spring 23 will raise the pawl out of engagement with the wheel", hit="raise the pawl", src="US 1,174,436 · description"), 'calm'),
 ('Inside the box: three shafts, a train of gears and cog wheels, and a pawl, mounted with its own little weight.', dict(g="fig", fig="nielsen5", figno="5", calls=[["WEIGHT", 647, 66, 70, 40], ["GEARS", 347, 276, -150, 230]]), 'calm'),
 ("The patent's promise:", dict(g="quote", q="a simple and inexpensive mechanism which can readily be attached to a rocking chair", hit="simple and inexpensive", src="US 1,174,436 · description", hide=True), 'calm'),
 ('A simple and inexpensive mechanism which can readily be attached to a rocking chair.', dict(g="quote", q="a simple and inexpensive mechanism which can readily be attached to a rocking chair", hit="simple and inexpensive", src="US 1,174,436 · description", typed=False), 'slow'),
 ('It came with three sheets of drawings.', dict(g="fig", fig="nielsen5", figno="5", draw=False), 'calm'),
 ('Filed in nineteen fifteen. Approved in nineteen sixteen.', dict(g="stamp", title="FAN ATTACHMENT FOR|ROCKING-CHAIRS", filed="JAN. 8, 1915", date="MAR. 7, 1916", big=True, at=2.2), 'slow'),
 ('Simple. Inexpensive. Three sheets.', dict(g="fig", fig="nielsen1", figno="1", draw=False), 'punch'),
]
