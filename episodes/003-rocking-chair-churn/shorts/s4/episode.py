# SERIOUSLY APPROVED · FILE 003 · Short s4 — US 1,139,299. Facts/quotes: ../../sources.md
FMT = "short"
NUM = 'US 1,139,299'
HOOK = 'GUESS WHAT|THIS [BOX] DOES'
HOOK2 = 'THE PENDULUM|[FAN] · 1915'
HOOK_SWITCH = 1
TAIL = 2.6
LINES = [
 ('This is a real patent from nineteen fifteen. A box with a fan, clamped to the arm of a rocking chair.', dict(g="fig", fig="kline1", figno="1"), 'question'),
 ('Under it hangs a pendulum. Rock the chair, the pendulum swings, and the fan spins.', dict(g="fig", fig="kline1", figno="1", draw=False, calls=[["PENDULUM", 240, 330, 80, -40], ["WEIGHT", 240, 430, 90, 40]]), 'calm'),
 ('Inside: a toothed rack, bevel gears, two ratchet wheels with teeth facing opposite ways, and spring pawls. So the fan turns one way, whichever way you rock.', dict(g="fig", fig="kline2", figno="2", ring=[112, 232, 150]), 'calm'),
 ("And it's sensitive. The slightest rocking movement given to the rocking chair causes a swinging of the pendulum.", dict(g="quote", q="the slightest rocking movement given to the rocking chair C causes a swinging of the pendulum", hit="the slightest rocking movement", src="US 1,139,299 · description"), 'calm'),
 ('The fan faces you, inside a round wire guard.', dict(g="fig", fig="kline3", figno="3"), 'calm'),
 ('It produces a current of air directed to the head of the occupant of the rocking chair.', dict(g="quote", q="produces a current of air directed to the head of the occupant of the rocking chair.", hit="the head of the occupant", src="US 1,139,299 · description"), 'slow'),
 ('A continuous current of air directed onto the occupant as long as the rocking chair or similar article is rocked.', dict(g="quote", q="a continuous current of air directed onto the occupant as long as the rocking chair or similar article is rocked.", hit="as long as", src="US 1,139,299 · description"), 'slow'),
 ('Filed in nineteen fourteen. Approved in nineteen fifteen.', dict(g="stamp", title="FAN ATTACHMENT FOR|ROCKING-CHAIRS", filed="JUNE 5, 1914", date="MAY 11, 1915", big=True, at=2.2), 'slow'),
 ('Stop rocking, and the breeze stops too.', dict(g="fig", fig="kline1", figno="1", draw=False, ring=[240, 174, 160]), 'punch'),
]
