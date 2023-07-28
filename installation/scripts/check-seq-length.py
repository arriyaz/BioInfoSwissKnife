# check-seq-length.py

from Bio import SeqIO
import argparse

def check_sequence_length(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        seq_id = record.id
        seq_length = len(record.seq)
        print(f"{seq_id}\t{seq_length}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the length of sequences in a FASTA file.")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input FASTA file.")
    args = parser.parse_args()

    check_sequence_length(args.input_file)
