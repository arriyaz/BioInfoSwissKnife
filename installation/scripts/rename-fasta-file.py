# rename-fasta-file.py

from Bio import SeqIO
import argparse

def rename_fasta_file(input_file):
    with open(input_file, "r") as infile:
        for record in SeqIO.parse(infile, "fasta"):
            new_id = input_file.split(".")[0]
            record.id = new_id
            record.description = ""
            print(record.format("fasta"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename the FASTA file sequence ID.")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input FASTA file.")
    args = parser.parse_args()

    rename_fasta_file(args.input_file)
