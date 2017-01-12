import string
def DNA_Strand2 (dna):
    reference = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([reference[c] for c in dna])

print(DNA_Strand2("AAAAGGTAC"))
