# BRD4(1) Benchmark Set Input Files

## File descriptions

This set of files comprises PDB, sd, and mol2 files for all the benchmark ligands and the apo BRD4(1), as well as AMBER parameter (.prmtop) and coordinate files (.crds and .pdb) for all solvated complexes. The files for each ligand/solvated complex are named according to Table 7 in the associated ligand benchmark paper, and the apo BRD4(1) crystal structure file is named 4lyi (from its PDB ID). Compounds 3, 4, and 8a are named after their IDs in their respective references, also indicated on Table 7.

## Methods

The structures for all ligands except Compound 8a (a non-binder) were obtained directly from their co-crystal structures with BRD4(1), which are identified in Table 7. The initial structure of Compound 8a was downloaded from the PubChem database with CID 2295889. All ligands have zero charge, and the hydrogens were added using openbabel [1]. The partial charges for the ligand atoms were assigned using antechamber [2] with the AM1-BCC charge model [3], generating a mol2 file, which was then converted to the pdb and sd formats using openbabel. The partial charges for the apo BRD4 (in the 4lyi.mol2 file), were assigned according to the AMBERff14SB protein force-field [4]. The starting configurations for all the solvated complexes, except BRD4(1) bound to Compound 8a, were obtained directly from their respective co-crystal structures. In the case of Compound 8a, the latter was docked into the apo BRD4(1) using AutoDock Vina [5], generating a similar binding mode as Compound 4. All ions/molecules besides the protein and ligand were removed before solvation. The parameters for the protein were obtained from the AMBERff14SB protein force-field, and the partial charges for the ligands as described above. The bonded and Lennard-Jones parameters for the ligands were obtained from the Amber General Force Field (GAFF) [6], also using antechamber. Each solvated complex has 11000 TIP3P water molecules with 32 Na+ and 35 Cl- ions (0.15 M NaCl), with TIP3P-specific ion parameters from Joung and Cheatham [7].

## References

1. O’Boyle NM, Banck M, James CA, Morley C, Vandermeersch T, Hutchison GR. (2011) J Cheminform 3:33. doi: 10.1186/1758-2946-3-33
2. Case DA, Betz, RM, Botello-Smith W, Cerutti, DS, Cheatham III TE, Darden, TA, Duke RE, Giese TJ, Gohlke H, Goetz AW, Homeyer N, Izadi S, Janowski P, Kaus J, Kovalenko A, Lee TS, LeGrand S, Li P, Lin C, Luchko T, Luo R, Madej B, Mermelstein D, Merz KM, Monard G, Nguyen H, Nguyen HT, Omelyan I, Onufriev A, Roe DR, Roitberg A, Sagui C, Simmerling CL, Swails J, Walker RC, Wang J, Wolf RM, Wu X, Xiao L, York DM, Kollman PA. (2016) AMBER 16, University of California, San Francisco.
3. Jakalian A, Jack DB, Bayly CI. (2002) Fast, efficient generation of high-quality atomic charges. AM1-BCC model: II. Parameterization and validation. J Comput Chem 23:1623−1641. doi: 10.1002/jcc.10128
4. Maier JA, Martinez C, Kasavajhala K, Wickstrom L, Hauser KE, Simmerling C. (2015) ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from ff99SB. J Chem Theory Comput 11:3696−3713. doi: 10.1021/acs.jctc.5b00255
5. Trott O, Olson AJ. (2010) AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization and multithreading. J Comput Chem 31:455-461. doi: 10.1002/jcc.21334
6. Wang J, Wolf RM, Caldwell JW, Kollman PA, Case DA. (2004) Development and Testing of a General Amber Force Field. J Comput Chem 25:1157-1174. doi: 10.1002/jcc.20035
7. Joung IS, Cheatham TE. (2008) Determination of Alkali and Halide Monovalent Ion Parameters for Use in Explicitly Solvated Biomolecular Simulations. J Phys Chem B 112:9020−9041. doi: 10.1021/jp8001614

