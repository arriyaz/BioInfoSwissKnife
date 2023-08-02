# rename-fasta-file.py
# Rename the filename of a fasta file from
# its sequence id in header line.


from Bio import SeqIO
import argparse
import os

def rename_fasta_file(input_file, output_folder=None):
    with open(input_file, "r") as infile:
        for record in SeqIO.parse(infile, "fasta"):
            # Extract the sequence ID from the header line
            sequence_id = record.id
            new_filename = f"{sequence_id}.fasta"

            # Determine the output folder path
            if output_folder:
                output_folder_path = output_folder
            else:
                output_folder_path = os.path.abspath('.')
            
            # Create the output folder if it doesn't exist
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)

            # Save the renamed record to a new FASTA file
            new_file_path = os.path.join(output_folder_path, new_filename)
            with open(new_file_path, "w") as outfile:
                SeqIO.write(record, outfile, "fasta")
    
    print("\nYour fasta file has been renamed.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="rename-fasta-file",
        description="Rename the FASTA file with sequence ID from Fasta header")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input FASTA file.")
    parser.add_argument("-o", "--output", dest="output_folder", default=None, help="Output folder to save the renamed FASTA file.")
    args = parser.parse_args()

    rename_fasta_file(args.input_file, args.output_folder)
