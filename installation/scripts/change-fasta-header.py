# change-fasta-header.py
# Change the header line of a fasta file
# with its filename.


from Bio import SeqIO
import argparse
import os

def change_fasta_header(input_file, output_folder= None):

    # Remove the filepath keep only filename
    filename = os.path.basename(input_file)

    with open(input_file, "r") as infile:
        for record in SeqIO.parse(infile, "fasta"):

            # Remove extension from filename
            # This filename will be used as header
            new_id = os.path.splitext(filename)[0]

            # Assign the filename as seq id in header
            record.id = new_id

            # There will be no additional description.
            record.description = ""

            # Just create a filename with id.
            new_filename = f"{new_id}.fasta"

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


    # Print confirmational message on terminal
    print("\nThe header file is replaced by filename\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="change-fasta-header",
        description="Change the fasta header with its filename")
    parser.add_argument("-i", "--input", dest="input_file", required=True, help="Input FASTA file.")
    parser.add_argument("-o", "--output", dest="output_folder", default=None, help="Output folder to save FASTA file with new header.")
    args = parser.parse_args()

    change_fasta_header(args.input_file, args.output_folder)

