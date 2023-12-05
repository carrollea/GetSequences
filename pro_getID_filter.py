import sys
import re
import Bio
from Bio import SeqIO
#This code gets sequences of interest from a fasta file. 
#A file containing the IDs of the sequences of interest is provided along with a fasta file for the genome
#The program will only return fasta files that are within the provided length range
#The program will produce two outputs. 1) a fasta file of the sequences of interest and 2) a file of only the ids of the sequences

#validating input
if len(sys.argv) != 5:
    print("Usage: python3 ProFilter.py [fasta] [ID file] [min length] [max length]")
    sys.exit(1)

#Assigning inputs as objects 
fa1 = sys.argv[1]
fa2 = sys.argv[2]
x = int(sys.argv[3])
y = int(sys.argv[4])

ID = []    #Make and empty list that will put trinity IDs in 
ID_fasta = []   #Make a list that will put matching fasta sequences in 
New_ID = []

#Go through the ID input file, grab the first column and add it to the ID list.
with open(fa2, 'r') as fin:
    for line in fin:
        new_line = line.split()
        ID.append(new_line[0])


#Now go through the fasta file and change the ID to something smaller and select for sequences of a certain length
with open(fa1) as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        if record.id in ID and len(record.seq) > x and len(record.seq) < y and record.seq[0]=='M':       #only take sequences of a certain length that have a start codon 
#            print(record.seq[0:3])
            ID_fasta.append(record) 
            New_ID.append(record.id)

   
#print(ID_fasta)   
      
#Now will output a fasta file from the ID_fasta sequences. 
SeqIO.write(ID_fasta, "out.fasta", "fasta")

with open(r'New_IDs.txt', 'w') as f:
	for item in New_ID:
		f.write(f"{item}\n")
