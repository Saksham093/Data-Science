# Q. Counting DNA Nucleotides
f = open("./rosalind_dna.txt", "r")
s = f.read()
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))
# ------------------------------------------------------------