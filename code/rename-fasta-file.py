# rename-fasta-file.py

from Bio import SeqIO
import argparse
import os

def rename_fasta_file(input_file):
    with open(input_file, "r") as infile:
        for record in SeqIO.parse(infile, "fasta"):
            # Extract the sequence ID from the header line
            sequence_id = record.id
            new_filename = f"{sequence_id}.fasta"

            # Update the header line with the new sequence ID
            record.description = ""
            print(record.format("fasta"))

    # Rename the input file with the new filename
    os.rename(input_file, new_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename the FASTA file with sequence ID from Fasta header")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input FASTA file.")
    args = parser.parse_args()

    rename_fasta_file(args.input_file)