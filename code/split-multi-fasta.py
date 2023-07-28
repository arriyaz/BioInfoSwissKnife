from Bio import SeqIO

def split_multi_fasta(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        output_file = f"{record.id}.fasta"
        with open(output_file, "w") as outfile:
            SeqIO.write(record, outfile, "fasta")

if __name__ == "__main__":
    input_file = "data/all-contigs.fa"  # Replace with the path to your multi-FASTA file
    split_multi_fasta(input_file)


