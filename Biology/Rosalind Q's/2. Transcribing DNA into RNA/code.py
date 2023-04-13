def rna(ss):
    ss = ss.replace('T', 'U')
    return ss


# Q. Counting DNA Nucleotides
f = open("./rosalind_rna.txt", "r")
s = f.read()

print(rna(s))
