# check-seq-length.py

from Bio import SeqIO
import argparse
import os

def check_sequence_length(input_files):

    for input_file in input_files:
        
        # Extract filename
        filename = os.path.basename(input_file)

        for record in SeqIO.parse(input_file, "fasta"):
            seq_id = record.id
            seq_length = len(record.seq)
            print(f"{filename}\t{seq_id}\t{seq_length}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="check-seq-length",
        description="Check the length of sequences in FASTA file[s].")
    parser.add_argument("-i", "--input", nargs="+", dest="input_file", required=True, 
                        help="Input FASTA file.")
    args = parser.parse_args()

    check_sequence_length(args.input_file)
