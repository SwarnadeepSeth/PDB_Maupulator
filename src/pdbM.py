#!/usr/bin/env python3

import os

def rename_chain_by_atomnum(pdb_file, output_file, start_atom, new_chain):
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom_serial_number = int(line[6:11].strip())
                if atom_serial_number >= start_atom:
                    line = line[:21] + new_chain + line[22:]
            outfile.write(line)

def rename_chain_by_resid(pdb_file, output_file, start_residue, new_chain):
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                residue_number = int(line[22:26].strip())
                if residue_number >= start_residue:
                    line = line[:21] + new_chain + line[22:]
            outfile.write(line)

def rename_chain_and_reinit_residues(pdb_file, output_file, start_residue, new_chain):
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_residue_number = 1
        chain_switched = False

        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                residue_number = int(line[22:26].strip())

                # If the residue number is greater than or equal to the start_residue, switch chain and reinitialize residue number
                if residue_number >= start_residue:
                    line = line[:21] + new_chain + f"{current_residue_number:>4}" + line[26:]
                    chain_switched = True
                    current_residue_number += 1
                else:
                    chain_switched = False
                
            outfile.write(line)

# Function to renumber atom IDs
def renumber_atomID(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        atom_id = 1
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Modify the atom ID (columns 7-11 in PDB format)
                new_line = f"{line[:6]}{atom_id:5d}{line[11:]}"
                outfile.write(new_line)
                atom_id += 1
            else:
                outfile.write(line)

# Function to renumber residue IDs
def renumber_residueID(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_resid = None
        new_resid = 1
        resid_map = {}
        
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Extract the old resid (columns 23-26)
                old_resid = line[22:26].strip()
                
                # Map the old resid to a new sequential resid
                if old_resid not in resid_map:
                    resid_map[old_resid] = new_resid
                    new_resid += 1
                
                # Replace the resid in the line
                updated_line = f"{line[:22]}{resid_map[old_resid]:>4}{line[26:]}"
                outfile.write(updated_line)
            else:
                outfile.write(line)

# Function to add an element column to a PDB file
def add_element_column(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Extract the atom name (columns 13-16)
                atom_name = line[12:16].strip()
                
                # Determine the element type (usually the first letter of the atom name)
                element = atom_name[0]
                
                # If the atom name starts with a digit (e.g., '1H'), the element is the second character
                if atom_name[0].isdigit():
                    element = atom_name[1]
                
                # Format the element column (columns 77-78)
                updated_line = f"{line[:76]}{element:>2}{line[78:]}"
                outfile.write(updated_line)
            else:
                outfile.write(line)

# Function to assign segment IDs to a PDB file
def assign_segment_ids(pdb_file, output_file):
    with open(pdb_file, 'r') as file:
        lines = file.readlines()

    current_chain = None
    current_residue = None
    segment_letter = 'A'
    segment_number = 1

    with open(output_file, 'w') as out_file:
        for line in lines:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Extract the chain ID (column 21) and residue number (columns 22-26)
                chain_id = line[21].strip()
                residue_id = line[22:26].strip()

                # Check if we have encountered a new chain
                if chain_id != current_chain:
                    current_chain = chain_id
                    segment_letter = 'A'  # Reset to 'A' for the new chain
                    segment_number = 1  # Reset to 1 for the new chain
                    current_residue = None  # Reset residue tracking
                
                # Check if we have encountered a new residue within the same chain
                if residue_id != current_residue:
                    current_residue = residue_id
                    segment_id = f'{segment_letter}{segment_number}'
                    segment_number += 1

                    # Once segment_number exceeds 99, increment the letter and reset number to 1
                    if segment_number > 99:
                        segment_letter = chr(ord(segment_letter) + 1)
                        segment_number = 1
                
                # Modify the PDB line to include the segment ID (columns 72-76 for segment ID)
                new_line = line[:72] + segment_id.rjust(4) + line[76:]

                # Write modified line to the output file
                out_file.write(new_line)
            else:
                # For non-ATOM lines, just copy them as-is
                out_file.write(line)

# =============================================================================
# Function to perform the selected operations
def perform_operations(pdb_file, output_file, operations):

    # Copy the pdb file to the output file
    os.system(f"cp {pdb_file} {output_file}")

    current_file = output_file
    tmp_file = "tmp.pdb"  # Temporary file to hold intermediate results

    for op in operations:
        if op == 1:
            start_atom = int(input("Enter the atom serial number from which the chain should be changed: "))
            new_chain = input("Enter the new chain identifier: ")
            rename_chain_by_atomnum(current_file, tmp_file, start_atom, new_chain)

        elif op == 2:
            start_residue = int(input("Enter the residue number from which the chain should be changed: "))
            new_chain = input("Enter the new chain identifier: ")
            rename_chain_by_resid(current_file, tmp_file, start_residue, new_chain)

        elif op == 3:
            start_residue = int(input("Enter the residue number from which the chain should be changed: "))
            new_chain = input("Enter the new chain identifier: ")
            rename_chain_and_reinit_residues(current_file, tmp_file, start_residue, new_chain)

        elif op == 4:
            renumber_atomID(current_file, tmp_file)

        elif op == 5:
            renumber_residueID(current_file, tmp_file)

        elif op == 6:
            add_element_column(current_file, tmp_file)

        elif op == 7:
            assign_segment_ids(current_file, tmp_file)

        elif op == 8:
            output_format = input("Enter the desired output format (e.g., 'mol2', 'pdbqt', 'xyz'): ")
            if output_format == 'pdbqt':
                os.system(f"obabel {current_file} -O {tmp_file}.pdbqt -xr")
            else:
                os.system(f"obabel {current_file} -O {tmp_file}.{output_format}")

        # Overwrite the current file with the result for the next operation
        os.replace(tmp_file, current_file)

# =============================================================================
# User input and main program
pdb_file = input("Enter the input PDB file: ")  # Input PDB file
output_file = input("Enter the output PDB file: ")  # Output PDB file

print("="*100)
print("\t\t\t\tPDB FILE MANIPULATION PROGRAM")
print("="*100)

print("Input PDB file: ", pdb_file)
print("Output PDB file: ", output_file)

print("="*100)
print("Select operations to perform (comma-separated):")
print("> 1. Rename the chain identifier by atom number")
print("> 2. Rename the chain identifier by residue number")
print("> 3. Rename the chain identifier and reinitialize residue numbers")
print("> 4. Renumber atom IDs")
print("> 5. Renumber residue IDs")
print("> 6. Add an element column")
print("> 7. Assign segment IDs")
print("> 8. Convert PDB to other format")
print("CTRL+C to exit")
print("="*100)

# Input operations as comma-separated values
operation_input = input("Enter the operation numbers (comma-separated): ")
operations = [int(op.strip()) for op in operation_input.split(",")]

perform_operations(pdb_file, output_file, operations)

# Cleanup if needed
if os.path.exists("tmp.pdb"):
    os.remove("tmp.pdb")

print("All operations completed. Final PDB file saved as:", output_file)
