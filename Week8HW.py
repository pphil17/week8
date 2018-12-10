#!/usr/bin/env python

#Decide whether you want to translate or pull codon
#Enter DNA sequence after you have choosen one of the following choices

print("Choose from the choices below. Do you want to:")
print("1. Translate a protein-coding DNA sequence into a amino acids")
print("2. Randomly draw a pull from the sequence")

choice = input("Enter your choice: ")

#If you wish to do option 1, enter your DNA sequence
if choice == "1":
    dnaSeq = input("Please enter your DNA sequence (in all caps): ")

#Converting DNA sequence --> RNA sequence
#T (Thymine) in DNA must be replaced with U (Uracil) in RNA
    rnaSeq=dnaSeq.replace("T","U")
    print("DNA sequence to RNA sequence: "+rnaSeq)

#Amino Acid dictionary:
    codon_AA = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu",			# DB: Can't use --> in a variable name
          "UUG":"Leu", "UCU":"Ser","UCC":"Ser", "UCA":"Ser",
          "UCG":"Ser", "UAA":"Stop", "UAU":"Try","UAC":"Tyr",
          "UAG":"Stop", "UGU":"Cys", "AAA":"Lys", "AAC":"Asn",
          "AAG":"Lys", "AAU":"Asn", "UGA":"Stop",
          "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
          "AGA":"Arg", "AGG":"Arg", "AGU":"Ser", "AGC":"Ser",
          "AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
          "CAA":"Gln", "CAG":"Gln", "CAU":"His", "CAC":"His",	# DB: Forgot a comma
          "CCG":"Pro", "CCA":"Pro", "CCC":"Pro", "CCU":"Pro",
          "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
          "GAA":"Glu", "GAG":"Glu", "GAC":"Asp", "GAU":"Asp",
          "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
          "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
          "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",	# DB: Forgot a comma
          "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val"}	# DB: Need closing }

    # Converting RNA to Amino Acids
    proteinSeq = ""
    for r in range(0, len(rnaSeq), 3):	# DB: RNAseq needs to be renamed to rnaSeq
        if rnaSeq[r:r+3] in codon_AA:	# DB: Forgot ":" and dictionary name incorrect
            proteinSeq += codon_AA[rnaSeq[r:r+3]]
    print("Protein Sequence: "+proteinSeq)	# DB: This should be outside the for loop

#If user choose option 2
else:
      dnaSeq = input ("Please enter DNA sequnece in caps: ")
      codon = [dnaSeq[r:r+3] for r in range(0, len(dnaSeq), 3)] # DB: Some problems with the syntax on this line
      print(codon)

#Codon choosen randomly from DNA sequence entered
      import random		# DB: Best to put this at the top of the script
      randomCodon = random.choice(codon)
      print(randomCodon)

# DB: Overall, the logical flow of the code was good, but there were lots of small syntax 
#     errors to fix.
