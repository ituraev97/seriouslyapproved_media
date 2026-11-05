# SERIOUSLY APPROVED · FILE 005 · Short s4 — US 889,823. Facts/quotes: ../../sources.md
FMT = "short"
NUM = 'US 889,823'
HOOK = 'WHERE DO YOU|PLUG [THIS] IN?'
HOOK2 = 'THE [VACUUM]|CLEANER · 1908'
HOOK_SWITCH = 2
TAIL = 2.6
SAY = {"paraffine": "paraffin"}
LINES = [
 ('This is a real invention from nineteen-oh-seven. A box on wheels, with a motor on top.', {'g': 'fig', 'fig': 'vac2', 'figno': '2', 'calls': [['MOTOR', 459, 324, -60, -70]]}, 'question'),
 ('Inside, a fan makes suction. A spinning brush at the front. And the dust goes into a sack on the handle.', {'g': 'fig', 'fig': 'vac2', 'figno': '2', 'draw': False, 'calls': [['FAN', 414, 486, 60, 40], ['BRUSH', 801, 630, -40, -80]]}, 'calm'),
 ("It's called a carpet sweeper and cleaner. And it was approved.", {'g': 'stamp', 'title': 'CARPET SWEEPER|AND CLEANER', 'filed': 'SEPT. 14, 1907', 'date': 'JUNE 2, 1908', 'at': 2.6}, 'punch'),
 ('A spring reel on the handle winds up the cord. The wires will be automatically wound upon the reel when it becomes slack.', {'g': 'quote', 'q': 'the wires 24 will be automatically wound upon the reel when it becomes slack', 'hit': 'automatically wound', 'src': 'US 889,823 · description'}, 'calm'),
 ('And where do you plug it in?', {'g': 'quote', 'q': 'which in use may be connected to a common incandescent lamp socket in the usual manner', 'hit': 'incandescent lamp socket', 'src': 'US 889,823 · description', 'hide': True}, 'question'),
 ('It may be connected to a common incandescent lamp socket in the usual manner. A light bulb socket.', {'g': 'quote', 'q': 'which in use may be connected to a common incandescent lamp socket in the usual manner', 'hit': 'incandescent lamp socket', 'src': 'US 889,823 · description', 'typed': False}, 'slow'),
 ("The sack hangs from the handle. According to the inventor's biography, the first version used a pillowcase.", {'g': 'fig', 'fig': 'vac1', 'figno': '1', 'calls': [['SACK', 54, 162, 70, -50]]}, 'calm'),
 ('Filed in nineteen-oh-seven. Approved in nineteen-oh-eight.', {'g': 'stamp', 'title': 'CARPET SWEEPER|AND CLEANER', 'filed': 'SEPT. 14, 1907', 'date': 'JUNE 2, 1908', 'big': True, 'at': 2.2}, 'slow'),
 ('The patent was bought that same year. By a leather goods maker named Hoover.', {'g': 'fig', 'fig': 'vac2', 'figno': '2', 'draw': False}, 'calm'),
 ('Plugged into the light bulb socket.', {'g': 'fig', 'fig': 'vac1', 'figno': '1', 'draw': False}, 'punch'),
]
