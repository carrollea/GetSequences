# GetSequences
Python code for retrieving and filtering fasta sequences of interest 

This code gets sequences of interest from a fasta file. This is good for filtering large cds or protein fasta files from genomes for only the sequences of interest
A file containing the IDs of the sequences of interest are provided along with a fasta file for the genome
The program will only return fasta files that are within the provided length range
The program will produce two outputs. 1) a fasta file of the sequences of interest and 2) a file of only the ids of the sequences

The nuc_filter.py program is for filtering nucleotide sequences. 
The pro_getID_filter is for protein sequences and filters for those that have a start codon "M". 

## Inputs 

- fasta -fasta file that contains the sequences of interest along with sequences you don't need
- ID file -a file containing IDs corresponding to your sequences of interest. Must be the same as the IDs used in the fasta file.
- min length -the minimum length of your sequence
- max length -the maximum length of your sequence 

### Example
```
python3 pro_getID_filter [fasta] [ID file] [min length] [max length]
```

## Outputs 
Two files will be created 

- out.fasta -a new fasta file containing only your sequences of interest
- New_IDs.txt -a file containing only the ids of the sequences that are in the new fasta file
