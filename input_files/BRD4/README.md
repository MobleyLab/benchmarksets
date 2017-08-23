# BRD4(1) Benchmark Set Input Files

## File descriptions

This set of files contains PDB, sdf, and mol2 files for all the benchmark ligands and a PDB file for the apo BRD4(1), as well as AMBER parameter (.prmtop) and coordinate files (.crds and .pdb) for all solvated complexes. The files for each ligand/solvated complex are named according to Table 7 in the associated ligand benchmark paper, and the apo BRD4(1) crystal structure PDB file is named 4lyi.pdb (from its PDB ID). Compounds 3, 4, and 8a are named after their IDs in their respective references, also indicated on Table 7.

## Methods

The structures for all ligands except Compound 8a (a non-binder) were obtained directly from their co-crystal structures with BRD4(1), which are identified in Table 7. The initial structure of Compound 8a was downloaded from the PubChem database with CID 2295889. All ligands have zero charge, and the hydrogens were added using openbabel [1](#Boy11). The partial charges for the ligand atoms were assigned using antechamber [2](#Cas16) with the AM1-BCC charge model [3](#Jak02), generating a mol2 file, which was then converted to sdf format with antechamber. The starting configurations for all the solvated complexes, except BRD4(1) bound to Compound 8a, were obtained directly from their respective co-crystal structures. In the case of Compound 8a, the latter was docked into the apo BRD4(1) using AutoDock Vina [4](#Tro10), generating a similar binding mode as Compound 4. All ions/molecules besides the protein and ligand were removed before solvation. The parameters for the protein were obtained from the AMBERff14SB protein force-field [5](#Mai15), and the partial charges for the ligands as described above. The bonded and Lennard-Jones parameters for the ligands were obtained from the Amber General Force Field (GAFF) [6](#Wan04), also using antechamber. Each solvated complex has 11000 TIP3P water molecules with 32 Na+ and 35 Cl- ions (0.15 M NaCl), with TIP3P-specific ion parameters from Joung and Cheatham [7](#Jou13).


## Experimental binding free energies and binding enthalpies

|Protein|Ligand|PubChem ID| Exp ΔG |Exp ΔG SEM |Exp ΔH |Exp ΔH SEM |Comp. Studies|
|----|--------------------------|--------|------|----------|------|----------|-------------|
|BRD4(1)|Compound 8a     |  2295889 |  NB <sup>a,c</sup> [8](#Vid13)  |  -   |    -   |   -   |    -          |
|BRD4(1)|Compound 4      |  975713  |  NS <sup>a,d</sup> [8](#Vid13)  |  -   |    -   |   -   |    -          |
|BRD4(1)|XD1             |  234105  | -5.95 <sup>b</sup> [9](#Luc13)  |  -   | -11.40 |   -   | [15](#Hei17)  |
|BRD4(1)|Quinazolin      |  2927305 | -6.36 <sup>a</sup> [10](#Fis12) | 0.17 |    -   |   -   | [15](#Hei17),[16](#Ald16)|
|BRD4(1)|Alprazolam      |  2118    | -7.40 <sup>b</sup> [11](#Fil12) | 0.05 | -6.96  |  0.05 | [16](#HenGil) |
|BRD4(1)|RVX-208         | 24871506 | -7.84 <sup>b</sup> [12](#Pic13) | 0.06 | -7.88  |  0.06 | [15](#Hei17),[16](#Ald16)|
|BRD4(1)|Bzt-7           | 20350618 | -8.16 <sup>b</sup> [11](#Fil12) | 0.03 | -6.16  |  0.03 | [15](#Hei17),[16](#Ald16)|
|BRD4(1)|RVX-OH          | 24962985 | -8.99 <sup>b</sup> [12](#Pic13) | 0.07 |-11.73  |  0.07 | [15](#Hei17),[16](#Ald16)|
|BRD4(1)|JQ1(+)          | 46907787 | -9.64 <sup>b</sup> [13](#Fil10) | 0.02 | -8.42  |  0.02 | [16](#Ald16)  |
|BRD4(1)|Compound 3      |    N/A   |-10.41 <sup>a</sup> [14](#Geh13) | 0.23 |   -    |   -   | [15](#Hei17)  |

<sup>a</sup> Obtained using Alphascreen; <sup>b</sup> Obtained using Isothermal Titration Calorimetry; <sup>c</sup> Non-binder (inactive at 250μM); <sup>d</sup> No saturation (32% inhibition at 250μM). 

## References

1. <a name="Boy11"></a> O’Boyle NM, Banck M, James CA, Morley C, Vandermeersch T, Hutchison GR. (2011) Open Babel: An open chemical toolbox J Cheminform 3:33. doi: 10.1186/1758-2946-3-33
2. <a name="Cas16"></a> Case DA, Betz, RM, Botello-Smith W, Cerutti, DS, Cheatham III TE, Darden, TA, Duke RE, Giese TJ, Gohlke H, Goetz AW, Homeyer N, Izadi S, Janowski P, Kaus J, Kovalenko A, Lee TS, LeGrand S, Li P, Lin C, Luchko T, Luo R, Madej B, Mermelstein D, Merz KM, Monard G, Nguyen H, Nguyen HT, Omelyan I, Onufriev A, Roe DR, Roitberg A, Sagui C, Simmerling CL, Swails J, Walker RC, Wang J, Wolf RM, Wu X, Xiao L, York DM, Kollman PA. (2016) AMBER 16, University of California, San Francisco.
3. <a name="Jak02"></a> Jakalian A, Jack DB, Bayly CI. (2002) Fast, efficient generation of high-quality atomic charges. AM1-BCC model: II. Parameterization and validation. J Comput Chem 23:1623−1641. doi: 10.1002/jcc.10128
4. <a name="Tro10"></a> Trott O, Olson AJ. (2010) AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization and multithreading. J Comput Chem 31:455-461. doi: 10.1002/jcc.21334
5. <a name="Mai15"></a> Maier JA, Martinez C, Kasavajhala K, Wickstrom L, Hauser KE, Simmerling C. (2015) ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from ff99SB. J Chem Theory Comput 11:3696−3713. doi: 10.1021/acs.jctc.5b00255
6. <a name="Wan04"></a> Wang J, Wolf RM, Caldwell JW, Kollman PA, Case DA. (2004) Development and Testing of a General Amber Force Field. J Comput Chem 25:1157-1174. doi: 10.1002/jcc.20035
7. <a name="Jou13"></a> Joung IS, Cheatham TE. (2008) Determination of Alkali and Halide Monovalent Ion Parameters for Use in Explicitly Solvated Biomolecular Simulations. J Phys Chem B 112:9020−9041. doi: 10.1021/jp8001614
8. <a name="Vid13"></a> Vidler LR, Filippakopoulos P, Fedorov O, Picaud S, Martin S, Tomsett M, Woodward H, Brown N, Knapp S, Hoelder S. (2013) Discovery of novel small-molecule inhibitors of BRD4 using structure-based virtual screening. J Med Chem 56:8073–8088. doi: 10.1021/jm4011302
9. <a name="Luc13"></a> Lucas X, Wohlwend D, Hugle M, Schmidtkunz K, Gerhardt S, Schule R, Jung M, Einsle O, Gunther S. (2013) 4-Acyl pyrroles: Mimicking acetylated lysines in histone code reading. Angew Chem Int Ed 52:14055–14059. doi: 10.1002/anie.201307652
10. <a name="Fis12"></a> Fish PV, Filippakopoulos P, Bish G, Brennan PE, Bunnage ME, Cook AS, Federov O, Gerstenberger BS, Jones H, Knapp S, Marsden B, Nocka K, Owen DR, Philpott M, Picaud S, Primiano MJ, Ralph MJ, Sciammetta N, Trzupek JD. (2012) Identification of a chemical probe for bromo and extra C-terminal bromodomain inhibition through optimization of a fragment-derived hit. J Med Chem 55:9831–9837. doi: 10.1021/jm3010515
11. <a name="Fil12"></a> Filippakopoulos P, Picaud S, Fedorov O, Keller M, Wrobel M, Morgenstern O, Bracher F, Knapp S. (2012) Benzodiazepines and benzotriazepines as protein interaction inhibitors targeting bromodomains of the BET family. Bioorg Med Chem, 20:1878–1886. doi: 10.1016/j.bmc.2011.10.080
12. <a name="Pic13"></a> Picaud S, Wells C, Felletar I, Brotherton D, Martin S, Savitsky P, Diez-Dacal B, Philpott M, Bountra C, Lingard H, Fedorov O, Muller S, Brennan PE, Knapp S, Filippakopoulos P. (2013) RVX-208, an inhibitor of BET transcriptional regulators with selectivity for the second bromodomain. PNAS 110:19754–19759. doi: 10.1073/pnas.1310658110
13. <a name="Fil10"></a> Filippakopoulos P, Qi J, Picaud S, Shen Y, Smith WB, Fedorov O, Morse EM, Keates T, Hickman TT, Felletar I, Philpott M, Munro S, McKeown MR, Wang Y, Christie AL, West N, Cameron MJ, Schwartz B, Heightman TD, La Thangue N, French CA, Wiest O, Kung AL, Knapp S, Bradner JE. (2010) Selective inhibition of BET bromodomains. Nature 468:1067–1073. doi: 10.1038/nature09504
14. <a name="Geh13"></a> Gehling VS, Hewitt MC, Vaswani RG, Leblanc Y, Cote A, Nasveschuk CG, Taylor AM, Harmange JC, Audia JE, Pardo E, Joshi S, Sandy P, Mertz JA, Sims III RJ, Bergeron L, Bryant BM, Bellon S, Poy F, Jayaram H, Sankaranarayanan R, Yellapantula S, Srinivasamurthy NB, Birudukota S, Albrecht BK. (2013) Discovery, design, and optimization of isoxazole azepine BET inhibitors. ACS Med Chem Lett 4:835–840. doi: 10.1021/ml4001485
15. <a name="Hei17"></a> Heinzelmann G, Henriksen NM, Gilson MK. (2017) Attach-pull-release calculations of ligand binding and conformational changes on the first BRD4 bromodomain. J Chem Theory Comput 13:3260–3275. doi: 10.1021/acs.jctc.7b00275
16. <a name="Ald16"></a> Aldeghi M, Heifetz A, Bodkin MJ, Knapp S, and Biggin PC. (2016) Accurate calculation of the absolute free energy of binding for drug molecules. Chem Sci 7:207–218. doi: 10.1039/c5sc02678d

