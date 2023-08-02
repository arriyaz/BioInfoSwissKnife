# split-multi-fasta.py

from Bio import SeqIO
import argparse

def split_multi_fasta(input_file, output_dir):
    for record in SeqIO.parse(input_file, "fasta"):
        output_file = f"{output_dir}/{record.id}.fasta"
        with open(output_file, "w") as outfile:
            SeqIO.write(record, outfile, "fasta")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="split-multi-fasta",
        description="Split a multi-FASTA file into individual FASTA files.")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input multi-FASTA file.")
    parser.add_argument("-o", "--output", dest="output_dir", required=True, help="Output directory for individual FASTA files.")
    args = parser.parse_args()

    split_multi_fasta(args.input_file, args.output_dir)