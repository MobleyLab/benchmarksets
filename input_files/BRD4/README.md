# BRD4(1) Benchmark Set Input Files

## File descriptions

This set of files comprises PDB, sd, and mol2 files for all the benchmark ligands and the apo BRD4(1), as well as AMBER parameter (.prmtop) and coordinate files (crds and pdb) for all solvated complexes. The files for each ligand/solvated complex are named according to Table 7 in the associated paper, and the apo BRD4(1) crystal structure file is named 4lyi (from its PDB ID). Compounds 3, 4, and 8a are named after their IDs in their respective references, which are indicated on Table 7.

## Methods

The structures for all ligands except Compound 8a (a non-binder) were obtained directly from their co-crystal structures with BRD4(1), which are identified in Table 7. The structure of Compound 8a was obtained from the PubChem database with CID 2295889. All ligands have zero charge, and the hydrogens were added using openbabel. The partial charges for each atom were obtained using antechamber with the AM1-BCC charge model, generating a mol2 file for each ligand, which was then converted to the pdb and sd formats using openbabel. The starting configurations for all the solvated complexes, except BRD4(1) bound to Compound 8a, were obtained diretly from their respective co-crystal structures. In the case of Compound 8a, the latter was docked into the apo BRD4(1) using AutoDock Vina, generating a similar binding mode as Compound 4. All ions/molecules besides the protein and ligand were removed before solvation. The parameters for the protein were assigned according to the AMBERff14SB force-field, and the partial charges for the ligands as described above. The bonded and Lennard-Jones parameters for the ligands were obtained from the Amber General Force Field (GAFF), also using antechamber. Each solvated complex has 11000 TIP3P water molecules with 32 Na+ and 35 Cl+ ions (0.15 M NaCl), with TIP3P-specific ion parameters from Joung and Cheatham.


