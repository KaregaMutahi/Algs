def DNA_strand(dna):
    dna = dna.replace("A", "t")
    dna = dna.replace ("T", "A")
    dna = dna.replace ("t", "T")

    dna = dna.replace ("C", "g")
    dna = dna.replace ("G","C")
    dna = dna.replace ("g", "G")

    return dna

print(DNA_strand("ATTGGGAATTCAGC"))
