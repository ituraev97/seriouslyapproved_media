# SERIOUSLY APPROVED · FILE 007 · Short s1 (template: drawing reveal) — US 544,419. Facts/quotes: ../../sources.md
FMT = "short"
NUM = 'US 544,419'
HOOK = 'LOOK AT|THIS [HAT]'
HOOK2 = 'A HAT WITH|A [LAMP] · 1895'
HOOK_SWITCH = 2
TAIL = 2.4
Q_DYN = 'a dynamo carried upon a bicycle, or what not'
LINES = [
 ("This is a real patent from eighteen ninety-five. A policeman's hat.", {'g': 'fig', 'fig': 'hat1', 'figno': '1', 'draw': False}, 'slow'),
 ("On the band is an electric lamp. The wires lead down over the body to some source of electrical energy, like a battery in the pocket.", {'g': 'fig', 'fig': 'hat1', 'figno': '1', 'draw': False, 'calls': [['LAMP', 46, 330, 70, 60]]}, 'calm'),
 ("It was approved. Filed in June, approved in August.", {'g': 'stamp', 'title': 'ELECTRIC-WIRE-CONTAINING|HAT OR CAP BAND', 'filed': 'JUNE 10, 1895', 'date': 'AUG. 13, 1895', 'at': 1.0}, 'punch'),
 ("Otherwise, the patent promises, it is worn just the same as any ordinary hat or cap.", {'g': 'quote', 'q': 'The hat or cap will otherwise be worn just the same as any ordinary hat or cap', 'hit': 'any ordinary hat', 'src': 'US 544,419 · description'}, 'calm'),
 ("And if you do not have a battery, there is a dynamo carried upon a bicycle.", {'g': 'quote', 'q': Q_DYN, 'hit': 'or what not', 'src': 'US 544,419 · description', 'hide': True}, 'calm'),
 ("Or what not.", {'g': 'quote', 'q': Q_DYN, 'hit': 'or what not', 'src': 'US 544,419 · description', 'typed': False}, 'punch'),
]
