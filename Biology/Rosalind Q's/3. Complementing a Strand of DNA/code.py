# Q. Complementing a Strand of DNA

R = {'A': 'T',
     'T': 'A',
     'C': 'G',
     'G': 'C'
     }


def reverse_com_dna(ss):
    ns = ""
    for u in ss:
        r = R[u]
        ns = ns + r
    return ns[::-1]


f = open("./rosalind_revc.txt", "r")
s = f.read()

print(reverse_com_dna(s))
