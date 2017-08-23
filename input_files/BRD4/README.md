# BRD4(1) Benchmark Set Input Files

## File descriptions

This set of files contains PDB, sdf, and mol2 files for all the benchmark ligands and a PDB file for the apo BRD4(1), as well as AMBER parameter (.prmtop) and coordinate files (.crds and .pdb) for all solvated complexes. The files for each ligand/solvated complex are named according to Table 7 in the associated ligand benchmark paper, and the apo BRD4(1) crystal structure PDB file is named 4lyi.pdb (from its PDB ID). Compounds 3, 4, and 8a are named after their IDs in their respective references, also indicated on Table 7.

## Methods

The structures for all ligands except Compound 8a (a non-binder) were obtained directly from their co-crystal structures with BRD4(1), which are identified in Table 7. The initial structure of Compound 8a was downloaded from the PubChem database with CID 2295889. All ligands have zero charge, and the hydrogens were added using openbabel [1]. The partial charges for the ligand atoms were assigned using antechamber [2] with the AM1-BCC charge model [3], generating a mol2 file, which was then converted to sdf format with antechamber. The starting configurations for all the solvated complexes, except BRD4(1) bound to Compound 8a, were obtained directly from their respective co-crystal structures. In the case of Compound 8a, the latter was docked into the apo BRD4(1) using AutoDock Vina [4], generating a similar binding mode as Compound 4. All ions/molecules besides the protein and ligand were removed before solvation. The parameters for the protein were obtained from the AMBERff14SB protein force-field [5], and the partial charges for the ligands as described above. The bonded and Lennard-Jones parameters for the ligands were obtained from the Amber General Force Field (GAFF) [6], also using antechamber. Each solvated complex has 11000 TIP3P water molecules with 32 Na+ and 35 Cl- ions (0.15 M NaCl), with TIP3P-specific ion parameters from Joung and Cheatham [7].

## References

1. O’Boyle NM, Banck M, James CA, Morley C, Vandermeersch T, Hutchison GR. (2011) J Cheminform 3:33. doi: 10.1186/1758-2946-3-33
2. Case DA, Betz, RM, Botello-Smith W, Cerutti, DS, Cheatham III TE, Darden, TA, Duke RE, Giese TJ, Gohlke H, Goetz AW, Homeyer N, Izadi S, Janowski P, Kaus J, Kovalenko A, Lee TS, LeGrand S, Li P, Lin C, Luchko T, Luo R, Madej B, Mermelstein D, Merz KM, Monard G, Nguyen H, Nguyen HT, Omelyan I, Onufriev A, Roe DR, Roitberg A, Sagui C, Simmerling CL, Swails J, Walker RC, Wang J, Wolf RM, Wu X, Xiao L, York DM, Kollman PA. (2016) AMBER 16, University of California, San Francisco.
3. Jakalian A, Jack DB, Bayly CI. (2002) Fast, efficient generation of high-quality atomic charges. AM1-BCC model: II. Parameterization and validation. J Comput Chem 23:1623−1641. doi: 10.1002/jcc.10128
4. Trott O, Olson AJ. (2010) AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization and multithreading. J Comput Chem 31:455-461. doi: 10.1002/jcc.21334
5. Maier JA, Martinez C, Kasavajhala K, Wickstrom L, Hauser KE, Simmerling C. (2015) ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from ff99SB. J Chem Theory Comput 11:3696−3713. doi: 10.1021/acs.jctc.5b00255
6. Wang J, Wolf RM, Caldwell JW, Kollman PA, Case DA. (2004) Development and Testing of a General Amber Force Field. J Comput Chem 25:1157-1174. doi: 10.1002/jcc.20035
7. Joung IS, Cheatham TE. (2008) Determination of Alkali and Halide Monovalent Ion Parameters for Use in Explicitly Solvated Biomolecular Simulations. J Phys Chem B 112:9020−9041. doi: 10.1021/jp8001614


CD Set 1: Experimental binding free energy and binding enthalpy

Guest ID labels with 's' (e.g., s9) indicate supplementary guests to the core set listed in the associated paper. All values in kcal/mol.

Host	Guest	Guest ID	Exp ΔG a	Exp ΔG SEM a	Exp ΔH a	Exp ΔH SEM a	Comp. Studies
aCD	1-butylamine	1	-1.575	0.019	-2.17	0.05	1
aCD	1-hexylamine	2	-3.533	0.004	-4.19	0.02	1
aCD	1-octylamine	3	-4.606	0.007	-5.46	0.03	1
aCD	cyclopentanol	4	-2.130	0.016	-2.74	0.02	1
aCD	cycloheptanol	5	-2.510	0.060	-2.99	0.23	1
aCD	butanoate	6	-1.506	0.036	-2.53	0.12	1
aCD	hexanoate	7	-3.380	0.005	-3.40	0.02	1
aCD	octanoate	8	-4.622	0.017	-4.89	0.03	1
aCD	n-methylbutylamine	s9	-1.685	0.018	-2.57	0.06	1
aCD	1-methylbutylamine	s10	-1.764	0.020	-2.68	0.07	1
aCD	1-pentylamine	s11	-2.720	0.004	-3.28	0.02	1
aCD	n-methylhexylamine	s12	-3.516	0.012	-4.20	0.08	1
aCD	1-methylhexylamine	s13	-3.604	0.004	-4.28	0.02	1
aCD	1-heptylamine	s14	-4.137	0.004	-4.66	0.02	1
aCD	1-methylheptylamine	s15	-4.166	0.004	-4.74	0.02	1
aCD	cyclobutanol	s16	-2.022	0.016	-2.75	0.05	1
aCD	cyclooctanol	s17	-3.227	1.135	-0.93	0.32	1
aCD	pentanoate	s18	-2.596	0.005	-2.75	0.01	1
aCD	trans-2-hexenoate	s19	-3.344	0.010	-4.12	0.06	1
aCD	trans-3-hexenoate	s20	-3.011	0.010	-3.36	0.05	1
aCD	heptanoate	s21	-3.991	0.013	-4.19	0.09	1
aCD	6-heptenoate	s22	-3.597	0.004	-4.48	0.02	1
a) Experimental Data: Rekharsky MV, Mayhew MP, Goldberg RN, Ross PD, Yamashoji Y, Inoue Y. (1997) Thermodynamic and nuclear magnetic resonance study of the reactions of α-and β-cyclodextrin with acids, aliphatic amines, and cyclic alcohols. J Phys Chem B. 101(1):87-100. doi: 10.1021/jp962715n

Computational Studies: 1) Niel M. Henriksen and Michael K. Gilson. Evaluating Force Field Performance in Thermodynamic Calculations of Cyclodextrin Host–Guest Binding: Water Models, Partial Charges, and Host Force Field Parameters. Journal of Chemical Theory and Computation. Article ASAP. DOI: 10.1021/acs.jctc.7b00359
