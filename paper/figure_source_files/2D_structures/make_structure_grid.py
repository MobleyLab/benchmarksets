#!/bin/env python

from openeye.oechem import *
from openeye.oedepict import *

# Depiction drawing on code from https://docs.eyesopen.com/toolkits/python/depicttk/imagegrid.html


def DrawMoleculeData(cell, moldata):

    gap = cell.GetHeight() / 4.0

    font = OEFont()
    font.SetAlignment(OEAlignment_Left)
    mol = moldata[3]

    data = "name = " + moldata[2]
    offset = gap
    cell.DrawText(OE2DPoint(0, offset), data, font)

    # Smiles
    offset += gap
    data =  moldata[1]
    cell.DrawText(OE2DPoint(0, offset), data, font)

    offset += gap
    data = "PubChem ID = " + moldata[0]
    cell.DrawText(OE2DPoint(0, offset), data, font)

# Load data
file = open('pubchem_smiles_names.csv', 'r')
text = file.readlines()
file.close()
data = []
molecules = []
for line in text[1:]:
    tmp = line.split(';')
    cid = tmp[0].strip()
    smiles = tmp[1].strip()
    name = tmp[2].strip()

    # Prep molecule too
    mol = OEGraphMol()
    mol.SetTitle(name)
    OESmilesToMol(mol, smiles)
    OEPrepareDepiction(mol)

    data.append( (cid, smiles, name, OEGraphMol(mol)) )
    molecules.append( OEGraphMol(mol))

# Do depiction

image = OEImage(1250, 6500)
image.Clear(OEColor(OELightGrey))


rows, cols = 24, 4
grid = OEImageGrid(image, rows, cols)
grid.SetMargins(50)
grid.SetCellGap(20)

opts = OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(), OEScale_AutoScale)


minscale = float("inf")
for mol in molecules:
    minscale = min(minscale, OEGetMoleculeScale(mol, opts))

opts.SetScale(minscale)
# Lay out a row
for r in range(0, grid.NumRows()):
    # Even rows are molecules, odd rows are info
    if r%2==0:

        # Determine indices and loop over molecules
        for col in range(cols):
            cell = grid.GetCell( r+1, col+1)
            idx = int(r/2)*cols + col
            #print r+1, col+1, idx
            if idx >= len(data):
                break

            #Display molecule
            disp = OE2DMolDisplay(data[idx][3], opts)
            OERenderMolecule(cell, disp)
    else:
        for col in range(cols):
            #Display labels for other rows
            cell = grid.GetCell(r + 1, col+1 )
            idx = int(r/2)*cols + col
            if idx >= len(data): break
            DrawMoleculeData(cell, data[idx])


OEWriteImage("MoleculeGrid.pdf", image)
