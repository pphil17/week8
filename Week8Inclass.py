#!/usr/bin/env python
#Take the input of DNA and then give it a reverse complement.

#Complementing:
#Convert DNA sequence to Uppercase
complement = []
dnaSeq= input("Enter your DNA Sequence here: ")
dnaSeq= dnaSeq.upper()

#Reversing:
print (dnaSeq)
print ("Reverse Sequence")
rdnaSeq = dnaSeq[::-1]

for b in rdnaSeq:
      if b == "A":
         complement.append("T")
      elif b == "T":
         complement.append("A")
      elif b == "C":
         complement.append("G")
      elif b == "G":
         complement.append("C")

complementcomplete = " ".join(complement)
print(complementcomplete)
