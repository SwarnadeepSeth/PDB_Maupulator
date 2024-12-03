# pdbM: PDB File Manipulation Tool

![pdbM Logo](https://raw.githubusercontent.com/SwarnadeepSeth/PDB_Maupulator/refs/heads/main/logo.webp=20x20)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Operations](#available-operations)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Troubleshooting](#troubleshooting)
- [Acknowledgements](#acknowledgements)

## Introduction

**pdbM** is a versatile command-line tool designed to simplify manipulating Protein Data Bank (PDB) files. Whether you need to renumber atoms and residues, rename chain identifiers, or add element columns, pdbM provides an easy-to-use interface to perform these tasks efficiently. Ideal for bioinformaticians, structural biologists, and researchers working with molecular structures, pdbM streamlines the preprocessing of PDB files for further analysis or visualization.

## Features

- **Rename Chain Identifiers by Atom Number**: Change chain identifiers starting from a specific atom serial number.
- **Rename Chain Identifiers by Residue Number**: Modify chain identifiers beginning at a specified residue number.
- **Rename Chain and Reinitialize Residue Numbers**: Update chain identifiers and reset residue numbering.
- **Renumber Atom IDs**: Sequentially renumber atom serial numbers starting from 1.
- **Renumber Residue IDs**: Sequentially renumber residue identifiers starting from 1.
- **Add Element Column**: Automatically populate the element column based on atom names.
- **Convert PDB to Other Formats**: Utilize Open Babel to convert PDB files to formats like MOL2, PDBQT, XYZ, and more.

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Open Babel** *(Optional)*: Required for converting PDB files to other formats.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pdbM.git
   cd pdbM
   ```

2. **Make the Installation Script Executable**

   Ensure the `install.sh` script has execute permissions:

   ```bash
   chmod +x install.sh
   ```

3. **Run the Installation Script**

   ```bash
   ./install.sh
   ```

   This script performs the following actions:
   - Adds a shebang to the `pdbM.py` script.
   - Makes the script executable.
   - Creates a symbolic link in `/usr/local/bin` for easy access.

## Usage

Run `pdbM` from the command line to start the PDB file manipulation program.

```bash
pdbM
```

Upon execution, you will be presented with a menu to select the desired operations.

## Available Operations

1. **Rename the chain identifier by atom number**
2. **Rename the chain identifier by residue number**
3. **Rename the chain identifier and reinitialize residue numbers**
4. **Renumber atom IDs**
5. **Renumber residue IDs**
6. **Add an element column**
7. **Convert PDB to other format**

### Performing Multiple Operations

You can perform multiple operations sequentially by entering comma-separated operation numbers. The tool will execute each operation in the order specified and save the final output to `protein.pdb`.

## Examples

### Example 1: Renumber Atom IDs, Residue IDs, and Add Element Column

1. **Run pdbM**

   ```bash
   pdbM
   ```

2. **Select Operations**

   ```
   Enter the operation numbers (comma-separated): 4,5,6
   ```

3. **Follow Prompts**

   The tool will sequentially:
   - Renumber atom serial numbers starting from 1.
   - Renumber residue identifiers starting from 1.
   - Add element information based on atom names.

4. **Result**

   The final manipulated PDB file is saved as `protein.pdb`.

### Example 2: Convert PDB to MOL2 Format

1. **Run pdbM**

   ```bash
   pdbM
   ```

2. **Select Operation**

   ```
   Enter the operation numbers (comma-separated): 7
   ```

3. **Specify Output Format**

   ```
   Enter the desired output format (e.g., 'mol2', 'pdbqt', 'xyz'): mol2
   ```

4. **Result**

   The converted file `protein.mol2` is generated.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please [open an issue](https://github.com/yourusername/pdbM/issues) on GitHub. Pull requests are also appreciated.

### Steps to Contribute

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add YourFeature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Troubleshooting

### Common Issues

1. **Script Not Executable**

   If you encounter permission issues, ensure the script is executable:

   ```bash
   chmod +x /usr/local/bin/pdbM
   ```

2. **Shebang Line Missing**

   Ensure the first line of `pdbM.py` is:

   ```python
   #!/usr/bin/env python3
   ```

3. **Open Babel Not Installed**

   If you intend to use the format conversion feature, install Open Babel:

   ```bash
   sudo apt-get install openbabel
   ```

4. **Symbolic Link Errors**

   If the symbolic link is broken, reinstall using the `install.sh` script.

### Error Messages

- **`import-im6.q16: attempt to perform an operation not allowed by the security policy 'PS'`**

  This error typically occurs when the system misinterprets the Python script as an ImageMagick command. Ensure the shebang line is correctly set and the script is executable.

## Acknowledgements

- **Open Babel**: For providing powerful file conversion capabilities.
- **Biopython**: For inspiration and useful modules related to PDB file handling.
- **The Python Community**: For extensive libraries and support.

---

*For any further assistance, please contact [swdseth@gmail.com](mailto:swdseth@gmail.com).*
