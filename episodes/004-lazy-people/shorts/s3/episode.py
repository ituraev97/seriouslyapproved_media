# SERIOUSLY APPROVED · FILE 004 · Short s3 — US 4,091,805. Facts/quotes: ../../sources.md
FMT = "short"
NUM = 'US 4,091,805'
HOOK = 'WHAT IS|THIS [HAND] FOR?'
HOOK2 = 'A HAND ON A|[STICK] · 1978'
HOOK_SWITCH = 2
TAIL = 2.6
LINES = [
 ('This is a real invention. A plastic hand. On a stick.', dict(g='fig', fig='scr2', figno='2'), 'question'),
 ('The patent describes the hand. It has a plurality of fingers bent in scratching position. And a wrist.', dict(g='quote', q='has a plurality of fingers bent in scratching position and a wrist', hit='bent in scratching position', src='US 4,091,805 · description'), 'calm'),
 ("It's called a vibrating back scratcher. And it was approved.", dict(g='stamp', title='VIBRATING|BACK SCRATCHER', filed='MAR. 18, 1977', date='MAY 30, 1978', at=3.0), 'punch'),
 ('Over the shoulder it goes. The hand lands on the back.', dict(g='fig', fig='scr1', figno='1', calls=[['HAND', 120, 312, -80, 40]]), 'calm'),
 ('Inside the handle: an electric vibrator and a rechargeable battery. Press the switch, and the hand vibrates back and forth along the rod.', dict(g='quote', q='for vibrating the rod in axial directions', hit='axial directions', src='US 4,091,805 · description'), 'calm'),
 ('To recharge it, a cord comes out of the handle. So that it is readily extended to an electric wall outlet.', dict(g='quote', q='so that it is readily extended to an electric wall outlet for the recharging power', hit='electric wall outlet', src='US 4,091,805 · description'), 'calm'),
 ("The goal, in the patent's words:", dict(g='quote', q='functions efficiently, effectively and reliably to scratch the back of a user', hit='scratch the back of a user', src='US 4,091,805 · background', hide=True), 'calm'),
 ('It functions efficiently, effectively and reliably to scratch the back of a user.', dict(g='quote', q='functions efficiently, effectively and reliably to scratch the back of a user', hit='scratch the back of a user', src='US 4,091,805 · background', typed=False), 'slow'),
 ('Filed in nineteen seventy-seven. Approved in nineteen seventy-eight.', dict(g='stamp', title='VIBRATING|BACK SCRATCHER', filed='MAR. 18, 1977', date='MAY 30, 1978', big=True, at=2.4), 'slow'),
 ('A plastic hand that shakes.', dict(g='fig', fig='scr2', figno='2', draw=False), 'punch'),
]
