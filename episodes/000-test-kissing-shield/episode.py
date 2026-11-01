FMT = "short"
# SERIOUSLY APPROVED · test Short (reference episode) (~60 s) — Kissing Shield, US 5,727,565 (filed May 26, 1995; issued Mar 17, 1998)
# Quotes verbatim: description col. 2; claim 1. Voice: variant B (am_michael 1.06 + FX chain), owner's choice 02.11.2026.
VOICE = "am_michael"
_FX_UNUSED = "highpass=f=75,equalizer=f=140:t=q:w=1:g=2.5,equalizer=f=380:t=q:w=1.2:g=-2,equalizer=f=3200:t=q:w=1.4:g=2.5,equalizer=f=7500:t=q:w=1:g=-1.5,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2,aecho=0.85:0.5:28|51:0.12|0.07"
NUM = "US 5,727,565"
HOOK = "GUESS WHAT<br>THIS IS [FOR]"
HOOK2 = "THE [KISSING]<br>SHIELD · 1998"
HOOK_SWITCH = 4
ST = dict(title="KISSING|SHIELD", filed="MAY 26, 1995", date="MAR. 17, 1998")
CLAIM = "An apparatus for preventing the exchange of microorganisms between two persons engaged in the act of kissing"
DESC = "It can be used especially by a politician who kisses babies."
LINES = [
 ("This is a real invention. Guess what it's for.",                                    dict(g="fig", fig="f1"), "question"),
 ("A heart-shaped frame. On a handle. With a thin, flexible film stretched across it.", dict(g="fig", fig="f1", figno="1", draw=False, calls=[["FRAME",150,430,-210,-70],["HANDLE",283,690,60,40],["THIN FILM",300,390,70,-150]]), "calm"),
 ("You hold it up to your lips.",                                                        dict(g="fig", fig="f2", figno="2"), "slow"),
 ("And then you kiss someone. Through it.",                                              dict(g="fig", fig="f2", figno="2", draw=False, vb="10 150 380 380", ring=[128, 300, 150]), "punch"),
 ("It's called the Kissing Shield.",                                                     dict(g="stamp", **ST), "punch"),
 ("Every patent has to say exactly what it is. This one says:",                          dict(g="quote", q=CLAIM, hit="", src="US 5,727,565 · claim 1", hide=True), "calm"),
 ("An apparatus for preventing the exchange of microorganisms, between two persons engaged in the act of kissing.", dict(g="quote", q=CLAIM, hit="engaged in the act of kissing", src="US 5,727,565 · claim 1", typed=False), "slow"),
 ("And the patent names an ideal customer.",                                             dict(g="quote", q=DESC, hit="a politician who kisses babies", src="US 5,727,565 · col. 2", hide=True), "slow"),
 ("Especially, a politician who kisses babies.",                                         dict(g="quote", q=DESC, hit="a politician who kisses babies", src="US 5,727,565 · col. 2", typed=False), "punch"),
 ("That's not a joke. That's in the official text.",                                     dict(g="quote", q=DESC, hit="a politician who kisses babies", src="US 5,727,565 · col. 2", typed=False), "calm"),
 ("There's even a balloon version.",                                                     dict(g="fig", fig="f4", figno="4"), "calm"),
 ("With a printed message in the middle. Practice safe kissing.",                        dict(g="fig", fig="f4", figno="4", draw=False, vb="330 290 400 400"), "slow"),
 ("It was filed in nineteen ninety-five. A patent examiner reviewed it. And in nineteen ninety-eight, the answer was...", dict(g="stamp", big=True, nostamp=True, **ST), "slow"),
 ("Approved.",                                                                            dict(g="stamp", big=True, at=0.05, **ST), "punch"),
 ("So now, when you see this, you'll know exactly what it's for.",                      dict(g="fig", fig="f1", draw=False), "calm"),
]
TAIL = 3.6
