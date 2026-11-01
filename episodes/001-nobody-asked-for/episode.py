# SERIOUSLY APPROVED · FILE 001 · THE SHELF — "12 Real Patents Nobody Asked For (All Approved)"
# Long video, 1920x1080. Facts and quotes: sources.md (checked against the patent scans' OCR and Google Patents).
FMT = "long"
TAIL = 3.0

def P(num, title, year):
    return dict(num=num, hook=title, side=f"{num} · {year}")

DOG = P("US 5,023,850", "THE [DOG] WATCH", 1991)
MASK = P("US 885,802", "THE [POP-OUT]|FACE", 1908)
DHAT = P("US 4,969,317", "A SUN HAT|FOR [DOGS]", 1990)
FORK = P("US 5,421,089", "THE FORK|WITH A [TIMER]", 1995)
FHAT = P("US 3,735,423", "THE [FAN] HAT", 1973)
PICNIC = P("US 4,436,214", "THE [SPIKED]|PICNIC CHEST", 1984)
CAT = P("US 5,952,925", "A [WARNING]|FOR BIRDS", 1999)
GRAF = P("US 5,675,318", "THE [GRAFFITI]|BOUNCER", 1997)
TOIL = P("US 4,437,430", "A TOILET|FOR [CATS]", 1984)
BIB = P("US 5,755,186", "A [BIB]|FOR CATS", 1998)
BED = P("US 4,441,222", "THE BED|[MAKER]", 1984)
BEAUTY = P("US 1,913,083", "THE [BLUSH]|MASK", 1933)

def chap(n, d, title, lines):
    return dict(g="title", kicker=f"PATENT No. {n} OF 12", numeral=str(n), title=title, lines=lines, **d)

def stamp(d, title, filed, issued, **k):
    return dict(g="stamp", title=title, filed=filed, date=issued, **d, **k)

def quote(d, q, hit, src, **k):
    return dict(g="quote", q=q, hit=hit, src=src, **d, **k)

def fig(d, key, figno, **k):
    return dict(g="fig", fig=key, figno=figno, **d, **k)

INTRO = dict(hook="NOBODY|ASKED FOR [THESE]", side="FILE 001 · THE SHELF")
END = dict(hook="ALL [APPROVED]", side="SERIOUSLY APPROVED · FILE 001")

LINES = [
 # ---------- cold open ----------
 ("This is a dog. Wearing a wristwatch.", fig(DOG, "dog1", "1", ring=[426, 277, 170]), "slow"),
 ("And that watch is a real invention, filed with the United States Patent Office.", fig(DOG, "dog1", "1", draw=False), "calm"),
 ("It was approved.", stamp(DOG, "CLOCK FOR|DOG TIME", "JUL. 9, 1990", "JUN. 11, 1991"), "punch"),
 ("Somebody invented it. Somebody filed it. And somebody at the patent office said yes. Today, twelve real patents. Nobody asked for any of them.", dict(g="title", kicker="THE SHELF · FILE 001", title="12 Real Patents|Nobody Asked For", lines=["Real drawings. Real quotes.", "Real approval stamps."], stamp=True, at=6.5, **INTRO), "calm"),

 # ---------- 1 · dog watch ----------
 ("Number one.", chap(1, DOG, "Clock for|Dog Time", ["US 5,023,850", "Filed 1990 · Issued 1991"]), "punch"),
 ("The official title is: Clock for keeping time at a rate other than human time.", quote(DOG, "Clock for keeping time at a rate other than human time", "other than human time", "US 5,023,850 · title"), "calm"),
 ("The idea is simple. A dog lives about eleven years. A human lives about seventy-seven. So a dog year is seven of ours.", fig(DOG, "dog1", "1", draw=False), "calm"),
 ("If the watch is set for dog time, the hands move about the watch face seven times faster than the rate of human time.", quote(DOG, "If the watch is set for dog time, the hands will move about the watch face seven times faster than the rate of human time.", "seven times faster", "US 5,023,850 · description"), "calm"),
 ("It goes on the paw with a Velcro strap. For ease of application.", fig(DOG, "dog1", "1", draw=False, ring=[426, 277, 170]), "calm"),
 ("Welcome to dog time.", fig(DOG, "dog1", "1", draw=False, ring=[426, 277, 170]), "slow"),
 ("And the patent explains exactly what that means in real life.", quote(DOG, "A one-hour ride in an automobile will register seven hours on a dog watch.", "seven hours", "US 5,023,850 · description", hide=True), "calm"),
 ("A one-hour ride in an automobile will register seven hours on a dog watch.", quote(DOG, "A one-hour ride in an automobile will register seven hours on a dog watch.", "seven hours", "US 5,023,850 · description", typed=False), "slow"),
 ("It also puts the owner's schedule into perspective. If a dog is kept inside during an eight or nine hour day, the dog watch will show fifty-six to sixty-three hours. Approximately two and a half days.", quote(DOG, "the elapsed time on the dog watch will be 56 to 63 hours, or approximately two and one-half days.", "approximately two and one-half days", "US 5,023,850 · description"), "slow"),
 ("There's even a chirp alarm. The patent expects the dog to react to it, which will appear to a human as a response to the time.", quote(DOG, "this chirp alarm is likely to produce a response from the dog which will appear to a human as a response to the time, with comic effect.", "with comic effect", "US 5,023,850 · description"), "calm"),
 ("The inventors also had a second use in mind. For people.", quote(DOG, "This comic effect can be taken advantage of by using the watch as an official time piece for a potentially dull meeting.", "a potentially dull meeting", "US 5,023,850 · description", hide=True), "calm"),
 ("This comic effect can be taken advantage of by using the watch as an official time piece for a potentially dull meeting.", quote(DOG, "This comic effect can be taken advantage of by using the watch as an official time piece for a potentially dull meeting.", "a potentially dull meeting", "US 5,023,850 · description", typed=False), "slow"),
 ("Filed in nineteen ninety. Approved in nineteen ninety-one.", stamp(DOG, "CLOCK FOR|DOG TIME", "JUL. 9, 1990", "JUN. 11, 1991", at=2.4), "slow"),

 # ---------- 2 · toy mask ----------
 ("Number two. We go back to nineteen oh six.", chap(2, MASK, "Toy|Mask", ["US 885,802", "Filed 1906 · Issued 1908"]), "calm"),
 ("This is a toy mask. On the left, a normal face. On the right, the same mask. A few seconds later.", fig(MASK, "mask12", "1 & 2"), "calm"),
 ("Eyes. Ears. Nose. Lips. They all come out.", fig(MASK, "mask12", "1 & 2", draw=False, vb="462 0 462 636"), "slow"),
 ("The features are made of thin folded paper, or thin flexible rubber. They lie flat inside the mask until you need them.", fig(MASK, "mask12", "1 & 2", draw=False), "calm"),
 ("How? There's a pipe behind the mask. You put it in your mouth.", fig(MASK, "mask4", "4"), "calm"),
 ("And, quote: by blowing through the pipe the feature will be protruded.", quote(MASK, "by blowing through the pipe the feature will be protruded", "protruded", "US 885,802 · description"), "slow"),
 ("Don't want a pipe in your mouth? There's a second option. A small bellows. Carried in your pocket.", fig(MASK, "mask4", "4", draw=False), "calm"),
 ("And the patent sums it all up in one confident sentence.", quote(MASK, "The uses of the device for purposes of amusement will be obvious.", "will be obvious", "US 885,802 · description", hide=True), "calm"),
 ("The uses of the device for purposes of amusement will be obvious.", quote(MASK, "The uses of the device for purposes of amusement will be obvious.", "will be obvious", "US 885,802 · description", typed=False), "slow"),
 ("The patent claims, quote, means to protrude the features at the will of the wearer.", quote(MASK, "means to protrude the features at the will of the wearer", "at the will of the wearer", "US 885,802 · claim 1"), "calm"),
 ("At the will of the wearer. Approved in nineteen oh eight.", stamp(MASK, "TOY|MASK", "JULY 18, 1906", "APR. 28, 1908", at=2.2), "slow"),

 # ---------- 3 · dog sun hat ----------
 ("Number three. Back to the dogs.", chap(3, DHAT, "Animal|Hat", ["US 4,969,317", "Filed 1989 · Issued 1990"]), "calm"),
 ("This is a sun hat. For a dog. With a chin strap.", fig(DHAT, "doghat4", "4"), "calm"),
 ("The problem, according to the patent: in hot weather and bright sunlight, many dogs spend most of the day outdoors. As a result, these animals often overheat.", quote(DHAT, "As a result, these animals often overheat.", "often overheat", "US 4,969,317 · description"), "calm"),
 ("So the hat has a brim, a head covering, two ear straps and two chin straps. Plus ear protection, eye and face protection, and a rear neck protection portion.", fig(DHAT, "doghat4", "4", draw=False), "calm"),
 ("The patent is worried about your dog's eyes.", quote(DHAT, "Also, sunlight is harmful for animals' eyes, as they have no means to protect themselves from harmful ultraviolet rays.", "no means to protect themselves", "US 4,969,317 · description"), "calm"),
 ("So the hat has a brim. And inside the hat, a sponge.", fig(DHAT, "doghat4", "4", draw=False), "calm"),
 ("You soak the sponge in water. It keeps your dog's head cool. Slowly. From the top.", fig(DHAT, "doghat4", "4", draw=False, vb="40 0 356 300"), "slow"),
 ("And in case you were wondering about the ears, the patent has you covered.", quote(DHAT, "The animal hat 10 can also accommodate an animal with floppy ears.", "floppy ears", "US 4,969,317 · description", hide=True), "calm"),
 ("The animal hat ten can also accommodate an animal with floppy ears.", quote(DHAT, "The animal hat 10 can also accommodate an animal with floppy ears.", "floppy ears", "US 4,969,317 · description", typed=False), "slow"),
 ("Approved. Nineteen ninety.", stamp(DHAT, "ANIMAL|HAT", "APR. 24, 1989", "NOV. 13, 1990", at=0.3), "punch"),

 # ---------- 4 · fork with timer ----------
 ("Number four. Dinner.", chap(4, FORK, "Fork with|Timer", ["US 5,421,089", "Filed 1994 · Issued 1995"]), "calm"),
 ("This is a fork. A normal, four-prong dinner fork.", fig(FORK, "fork1", "1"), "calm"),
 ("Except the handle has a red light, a green light, and a countdown timer.", fig(FORK, "fork1", "1", draw=False, vb="0 0 430 560"), "calm"),
 ("Red means wait. Green means you're allowed to take the next bite.", fig(FORK, "fork1", "1", draw=False, vb="0 0 430 560"), "slow"),
 ("The official purpose: providing a cue to a user, after an elapsed period of time, that another bite of food using the fork may be taken.", quote(FORK, "providing a cue to a user after an elapsed period of time for indicating that another bite of food using the fork may be taken", "another bite of food", "US 5,421,089 · description"), "calm"),
 ("The timer counts down from a preset period of up to ninety-nine seconds. Then the light turns green. You may now chew.", fig(FORK, "fork1", "1", draw=False, vb="0 0 430 560"), "slow"),
 ("The patent is very optimistic about it.", quote(FORK, "This invention could be truly helpful to people and extremely appealing since it does not require denial or starvation.", "extremely appealing", "US 5,421,089 · description"), "calm"),
 ("And of course, there's a premium model.", quote(FORK, "Deluxe versions could have a chime and beep.", "Deluxe versions", "US 5,421,089 · description", hide=True), "calm"),
 ("Deluxe versions could have a chime and beep.", quote(FORK, "Deluxe versions could have a chime and beep.", "Deluxe versions", "US 5,421,089 · description", typed=False), "punch"),
 ("A fork that beeps at you. Approved in nineteen ninety-five.", stamp(FORK, "FORK WITH|TIMER", "MAY 26, 1994", "JUN. 6, 1995", at=2.0), "slow"),

 # ---------- 5 · fan hat ----------
 ("Number five. Nineteen seventy-one.", chap(5, FHAT, "Hat with|Ventilating Means", ["US 3,735,423", "Filed 1971 · Issued 1973"]), "calm"),
 ("A hat. With a battery-powered fan built into the brim. Blowing air down onto your face.", fig(FHAT, "fanhat1", "1"), "calm"),
 ("Inside the hat there's a chamber. Inside the chamber, a miniature electric fan, powered by a replaceable battery. A switch on the side of the hat turns it on and off.", fig(FHAT, "fanhat1", "1", draw=False), "calm"),
 ("Why not just hold a fan? The patent saw that question coming.", fig(FHAT, "fanhat1", "1", draw=False, vb="0 100 520 460"), "calm"),
 ("As a result the user obtains the same effect as if a battery powered hand fan is used, but has the additional benefit of having both hands free.", quote(FHAT, "As a result the user obtains the same effect as if a battery powered hand fan is used, but has the additional benefit of having both hands free.", "both hands free", "US 3,735,423 · description"), "calm"),
 ("And the fan can run in reverse. The patent says the motor can be of the type which reverses direction of rotation.", quote(FHAT, "the motor can be of the type which reverses direction of rotation", "reverses direction", "US 3,735,423 · description"), "calm"),
 ("So it can also pull air away from your face. Approved, nineteen seventy-three.", stamp(FHAT, "FAN|HAT", "AUG. 25, 1971", "MAY 29, 1973", at=2.4), "slow"),

 # ---------- 6 · spiked picnic chest ----------
 ("Number six. The beach.", chap(6, PICNIC, "Anti-Theft|Picnic Device", ["US 4,436,214", "Filed 1982 · Issued 1984"]), "calm"),
 ("You want to go swimming. But you don't want anyone to steal your picnic.", fig(PICNIC, "picnic1", "1"), "calm"),
 ("So this chest has a handle inside. Turn it, and spikes drive down. Into the sand.", fig(PICNIC, "picnic4", "4"), "slow"),
 ("The patent calls it a locking spike assembly. And yes, the lid also has a combination lock.", quote(PICNIC, "a novel locking spike assembly of the type which can be inserted into soft soil or sand and selectively anchored therein.", "locking spike assembly", "US 4,436,214 · description"), "calm"),
 ("The chest is now anchored to the beach. The patent is proud of this.", quote(PICNIC, "Furthermore, no one has previously proposed any means for anchoring a picnic chest directly to the sand", "anchoring a picnic chest directly to the sand", "US 4,436,214 · description"), "calm"),
 ("And it describes the dream. The entire party of picnickers or bathers can leave the chest unattended. And go swimming.", quote(PICNIC, "permitting the entire party of picnickers or bathers to leave the chest unattended and go swimming", "go swimming", "US 4,436,214 · description"), "slow"),
 ("Approved, nineteen eighty-four.", stamp(PICNIC, "SPIKED|PICNIC CHEST", "DEC. 20, 1982", "MAR. 13, 1984", at=0.3), "punch"),

 # ---------- 7 · cat collar for birds ----------
 ("Number seven. A cat. And a bird.", chap(7, CAT, "Collar for a|Cat", ["US 5,952,925", "Filed 1998 · Issued 1999"]), "calm"),
 ("The full title is: Collar for a cat for warning a bird of the presence of the cat.", fig(CAT, "catbird", "1 & 2"), "calm"),
 ("It's a burglar alarm. For birds. Worn by the burglar.", fig(CAT, "catbird", "1 & 2", draw=False), "punch"),
 ("The collar sends out a sound. And the patent specifies who it's for.", quote(CAT, "which are only audible to the bird 14.", "only audible to the bird", "US 5,952,925 · description", hide=True), "calm"),
 ("Only audible to the bird.", quote(CAT, "which are only audible to the bird 14.", "only audible to the bird", "US 5,952,925 · description", typed=False), "slow"),
 ("It even has a light sensor. The collar switches off when there is not enough light. Because the birds are asleep.", quote(CAT, "inoperative when there is not enough light.", "not enough light", "US 5,952,925 · claim 11"), "calm"),
 ("Approved in nineteen ninety-nine.", stamp(CAT, "BIRD-WARNING|CAT COLLAR", "MAY 28, 1998", "SEP. 14, 1999", at=0.3), "punch"),

 # ---------- 8 · graffiti ----------
 ("Number eight. The city.", chap(8, GRAF, "Graffiti Prevention|Apparatus", ["US 5,675,318", "Filed 1996 · Issued 1997"]), "calm"),
 ("This patent begins by describing the problem. In its own words.", quote(GRAF, "the deliberate defacement of otherwise aesthetically pure and unblemished surfaces by decadent or otherwise indecent individuals.", "decadent or otherwise indecent individuals", "US 5,675,318 · description"), "calm"),
 ("Graffiti, it says, is generally an assault on the visual pleasures of man.", quote(GRAF, "is generally an assault on the visual pleasures of man.", "the visual pleasures of man", "US 5,675,318 · description"), "slow"),
 ("And it identifies the weapon. Spray paint cans, it says, are the tools of choice.", quote(GRAF, "Spray paint cans are the tools of choice.", "the tools of choice", "US 5,675,318 · description"), "calm"),
 ("The solution: sensors in the wall. When someone sprays, the system reacts.", fig(GRAF, "graffiti1", "1"), "calm"),
 ("Another version goes after the can itself. A valve in the spray can stops the paint when the intruder is detected.", fig(GRAF, "graffiti5", "5", draw=False), "calm"),
 ("In one version, an electromagnetic field sends the paint back.", fig(GRAF, "graffiti5", "5"), "calm"),
 ("There is one small requirement. For the magnetic version to work, the paint has to be mixed with magnetic material first. Before it goes into the can.", quote(GRAF, "the marking material is combined with a magnetic material prior to or at the time of loading the spray canister.", "combined with a magnetic material", "US 5,675,318 · description"), "slow"),
 ("The patent describes the repulsion of the fluid back from the electromagnetic field onto the intruder.", quote(GRAF, "the repulsion of the fluid back from the electromagnetic field onto the intruder, thus “marking” him for later identification.", "onto the intruder", "US 5,675,318 · description"), "slow"),
 ("Thus marking him for later identification. Approved, nineteen ninety-seven.", stamp(GRAF, "GRAFFITI|PREVENTION", "MAY 6, 1996", "OCT. 7, 1997", at=2.4), "slow"),

 # ---------- 9 · cat toilet ----------
 ("Number nine. Back to cats. And their litter box.", chap(9, TOIL, "Cat Toilet|Trainer", ["US 4,437,430", "Filed 1982 · Issued 1984"]), "calm"),
 ("This plastic tray clips onto the front of a normal human toilet. The cat uses the tray. Over the toilet.", fig(TOIL, "cattoilet1", "1"), "calm"),
 ("The training method: put in less and less cat litter, until the cat uses the tray without it.", quote(TOIL, "if progressively smaller amounts of cat litter are placed in the receptacle until such time as the cat uses the receptacle without the benefit of the cat litter in it.", "without the benefit of the cat litter", "US 4,437,430 · description"), "calm"),
 ("And the humans? The patent thought about that too.", quote(TOIL, "The device takes up approximately 1/6 of the open area of the toilet bowl so that the commode can be used by cats and humans without removing the receptacle.", "cats and humans", "US 4,437,430 · description"), "slow"),
 ("Shared bathroom. And when the training is done, the patent has a plan for the tray.", quote(TOIL, "At that point the invention 10 can be passed on to someone else who may have a similar problem.", "passed on to someone else", "US 4,437,430 · description", hide=True), "calm"),
 ("At that point the invention can be passed on to someone else who may have a similar problem.", quote(TOIL, "At that point the invention 10 can be passed on to someone else who may have a similar problem.", "passed on to someone else", "US 4,437,430 · description", typed=False), "slow"),
 ("A gift. Approved, nineteen eighty-four.", stamp(TOIL, "CAT TOILET|TRAINER", "APR. 26, 1982", "MAR. 20, 1984", at=0.6), "punch"),

 # ---------- 10 · cat bib ----------
 ("Number ten. Remember the bird-warning collar? This is the low-tech version.", chap(10, BIB, "Bird Predation|Deterrent Shield", ["US 5,755,186", "Filed 1997 · Issued 1998"]), "calm"),
 ("It's a flap of fabric that hangs from the cat's collar. Like a bib.", fig(BIB, "catbib1", "1"), "calm"),
 ("When the cat tries to pounce, the bib gets in the way.", fig(BIB, "catbib1", "1", draw=False), "slow"),
 ("Why not just put a bell on the cat? The patent has thoughts. Often the cat learns to stalk in a way which keeps the bell silent.", quote(BIB, "often the cat learns to stalk in a way which keeps the bell silent.", "keeps the bell silent", "US 5,755,186 · description"), "calm"),
 ("The bib even has a hole in it. So the cat's tags can still hang in front.", fig(BIB, "catbib1", "1", draw=False), "calm"),
 ("The patent opens with a deep thought about people.", quote(BIB, "The attitudes of pet owners are as hard to overcome as a cat's natural hunting instincts.", "as hard to overcome", "US 5,755,186 · description"), "calm"),
 ("And it describes a hard choice. Often people face the choice of either having a cat or feeding the birds.", quote(BIB, "Often people face the choice of either having a cat or feeding the birds.", "either having a cat or feeding the birds", "US 5,755,186 · description"), "slow"),
 ("Now you can have both. Approved, nineteen ninety-eight.", stamp(BIB, "CAT|BIB", "MAR. 7, 1997", "MAY 26, 1998", at=1.4), "slow"),

 # ---------- 11 · bed maker ----------
 ("Number eleven. The bedroom.", chap(11, BED, "Automatic|Bed Maker", ["US 4,441,222", "Filed 1981 · Issued 1984"]), "calm"),
 ("Making a bed takes about a minute. So someone built a machine for it.", fig(BED, "bedmaker1", "1"), "calm"),
 ("A motorized frame of arms and rollers travels up the bed, pulling the covers flat.", fig(BED, "bedmaker1", "1", draw=False, vb="0 0 732 760"), "calm"),
 ("It runs on an electric motor in a box under the bed. The reversing type. With a sprocket and chain drive.", fig(BED, "bedmaker1", "1", draw=False), "calm"),
 ("The covers are held at the foot of the bed by, quote, a tree-like frame.", quote(BED, "Covers and sheets carried on the bed are held securely to the foot of the bed by a tree-like frame", "a tree-like frame", "US 4,441,222 · description"), "calm"),
 ("And when the job is done, each arm returns to the foot of the bed empty.", quote(BED, "Upon reaching the headboard of the bed, each arm extends beyond the free end of the covers and returns to the foot of the bed empty.", "returns to the foot of the bed empty", "US 4,441,222 · description"), "slow"),
 ("The bed is made. Approved, nineteen eighty-four.", stamp(BED, "AUTOMATIC|BED MAKER", "JUL. 30, 1981", "APR. 10, 1984", at=1.4), "slow"),

 # ---------- 12 · beauty mask ----------
 ("And number twelve. Nineteen thirty-two.", chap(12, BEAUTY, "Beauty|Mask", ["US 1,913,083", "Filed 1932 · Issued 1933"]), "calm"),
 ("This is a beauty mask. It is not as relaxing as it sounds.", fig(BEAUTY, "beautymask1", "1"), "calm"),
 ("The idea: you sit under a tanning lamp wearing the mask. Only two small holes are open. Over the cheeks.", fig(BEAUTY, "beautymask1", "1", draw=False, vb="250 0 500 520"), "calm"),
 ("The light could come from the sun, electric sunlamps, or violet-ray lamps.", quote(BEAUTY, "such as the sun, electric sunlamps, violet-ray lamps, and the like, may be used.", "violet-ray lamps", "US 1,913,083 · description"), "calm"),
 ("And the cheek panels are coated thinner toward the hole. For, quote, a desirably toned coloring of the skin.", quote(BEAUTY, "whereby to provide for a desirably toned coloring of the skin.", "desirably toned", "US 1,913,083 · description"), "slow"),
 ("So only your cheeks get color. A natural blush. Made by a lamp.", quote(BEAUTY, "an enhanced natural coloring of restricted area of the face, such as the cheeks, may be produced.", "such as the cheeks", "US 1,913,083 · description"), "slow"),
 ("And for everything below the face, there's an apron. To cover the neck, shoulders and adjacent anatomy of the wearer.", quote(BEAUTY, "an apron attached to the lower portion of the face covering to cover the neck, shoulders and adjacent anatomy of the wearer", "adjacent anatomy", "US 1,913,083 · claim"), "slow"),
 ("Adjacent anatomy. Approved, nineteen thirty-three.", stamp(BEAUTY, "BEAUTY|MASK", "APR. 14, 1932", "JUN. 6, 1933", at=1.6), "slow"),

 # ---------- close ----------
 ("So which one is the most approved?", dict(g="title", kicker="THIS WEEK'S", title="Most|Approved", lines=["Voted by nobody.", "Decided by us."], **END), "question"),
 ("We're going with the dog watch. Because somewhere, there is a meeting that feels like seven hours.", fig(DOG, "dog1", "1", draw=False, ring=[426, 277, 170]), "calm"),
 ("Every quote in this video is word for word from the patent. The numbers are in the description, so you can check them yourself.", dict(g="title", kicker="SOURCES", title="All Real.|All Approved.", lines=["5,023,850 · 885,802 · 4,969,317", "5,421,089 · 3,735,423 · 4,436,214", "5,952,925 · 5,675,318 · 4,437,430", "5,755,186 · 4,441,222 · 1,913,083"], **END), "calm"),
 ("New weird patents every day. Subscribe, and we'll stamp it.", dict(g="title", kicker="SERIOUSLY APPROVED", title="Real patents.|Somehow approved.", lines=["New patents every day."], stamp=True, at=2.6, **END), "calm"),
]
