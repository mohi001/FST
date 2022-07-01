from FST import FST

fst = FST()
AZ = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

fst.add_state("q0", False)
fst.add_set_transition("q0", AZ, "q0")
fst.add_state("qs", False)
fst.add_state("qf", True)
fst.add_transition("qs", "", "s", "qf")

# ##[xzso] -> ##[xzso]es
fst.add_state("qes", False)
fst.add_transition("q0", "x", "x", "qes")
fst.add_transition("q0", "z", "z", "qes")
fst.add_transition("q0", "s", "s", "qes")
fst.add_transition("q0", "o", "o", "qes")
fst.add_transition("qes", "", "e", "qs")

# ##[sc]h -> ##[sc]hes
fst.add_state("qch", False)
fst.add_state("qsh", False)
fst.add_transition("q0", "c", "c", "qch")
fst.add_transition("q0", "s", "s", "qsh")
fst.add_transition("qsh", "h", "h", "qes")
fst.add_transition("qch", "h", "h", "qes")
fst.add_transition("qch", "", "", "qs")

# y
# #[CONSONANTS]y -> #[CONSONANTS]ies
fst.add_state("qcons", False)
fst.add_set_transition("q0", CONSONANTS, "qcons")
fst.add_transition("qcons", "y", "i", "qes")
# #[VOWELS]y -> #[VOWELS]ies
fst.add_state("qvow", False)
fst.add_set_transition("q0", VOWELS, "qvow")
fst.add_transition("qvow", "y", "y", "qs")

# #fe -> #ves || #f -> #ves
fst.add_state("qv", False)
fst.add_transition("q0", "f", "v", "qv")
fst.add_transition("qv", "", "", "qes")
fst.add_transition("qv", "e", "e", "qs")


fst.run("bus")
fst.run("marsh")
fst.run("lunch")
fst.run("tax")
fst.run("blitz")
fst.run("truss")
fst.run("tuc")
fst.run("city")
fst.run("puppy")
fst.run("ray")
fst.run("boy")
fst.run("wolf")
fst.run("wife")
fst.run("potato")
fst.run("tomato")
