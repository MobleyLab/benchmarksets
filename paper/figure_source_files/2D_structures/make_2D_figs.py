#!/bin/env python

# Load csv data
file = open('pubchem_smiles.csv','r')
text = file.readlines()
file.close()

# Import depiction stuff
from openeye.oechem import *
from openeye.oeiupac import *
from openeye.oedepict import *

#Process file and depict structures
for line in text:
    #Skip lines starting w comment
    if line[0]=='#': continue

    #Otherwise depict and save
    tmp = line.split(',')
    cid = tmp[0]
    smiles = tmp[1].strip()
    mol = OEMol()
    OEParseSmiles(mol, smiles)
    OEPrepareDepiction(mol)
    OERenderMolecule(cid+'.pdf', mol)

