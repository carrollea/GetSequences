import sys
import re
import Bio
from Bio import SeqIO
#Note: biopython installed on our lab anaconda
#Can load by using the following in the command line before using the program
#module use -a /projects/academic/zhenw/programs/modulefiles/Allluas
#module load anaconda3
#validating input
if len(sys.argv) != 4:
    print("Usage: python3 ProFilter.py [fasta] [min length] [max length]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

ID_fasta = [] #Make a list that will put matching fasta sequences in 

#Now go through the fasta file and change the ID to something smaller and select for sequeences of a certian length
with open(fa1) as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        if len(record.seq) > x and len(record.seq) < y and record.seq[0]=='M':       #only take seqeunces of a certain length 
            ID_fasta.append(record) 
      
#Now will output a fasta file from the ID_fasta sequecnes. 
SeqIO.write(ID_fasta, "out.fasta", "fasta")

