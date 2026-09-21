import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

compounds = pd.read_csv('data/smiles_lookup.csv')

descriptor_list = []

for index, row in compounds.iterrows():
    smiles = row['canonical_smiles']
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print("parsing failed")
    else:
        descriptor_list.append({
            'molecule_chembl_id':row['molecule_chembl_id'],
            'molwt': Descriptors.MolWt(mol),
            'LogP': Descriptors.MolLogP(mol),
            'TPSA': Descriptors.TPSA(mol),
            'HBD': Descriptors.NumHDonors(mol),
            'HBA': Descriptors.NumHAcceptors(mol),
            'RotB': Descriptors.NumRotatableBonds(mol)
        })
descriptors_df = pd.DataFrame(descriptor_list)
descriptors_df.to_csv('data/descriptors.csv', index= False)
print(descriptors_df.shape)
