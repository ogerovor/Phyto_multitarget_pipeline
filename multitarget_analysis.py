import pandas as pd
bioactivity = pd.read_csv('data/clean_bioactivity.csv')
flags = pd.read_csv('data/descriptors_with_flags.csv')

merged = bioactivity.merge(flags, on='molecule_chembl_id', how= 'left')
target_counts = merged.groupby('molecule_chembl_id')['target'].nunique()
multitarget_ids = target_counts[target_counts > 1].index

multitarget_compounds = merged[merged['molecule_chembl_id'].isin(multitarget_ids)]
top_candidates = multitarget_compounds[
    (multitarget_compounds['passes_lipinski'] == True) &
    (multitarget_compounds['passes_veber'] == True)
]

top_candidates.to_csv('data/multitarget_candidates.csv', index = False)
print(len(multitarget_ids), "multi-target compounds")
print(top_candidates['molecule_chembl_id'].nunique(), "drug-like multi-target compounds")

top_candidates_sorted = top_candidates.sort_values('standard_value')
top_candidates_sorted.to_csv('data/multitarget_candidates_ranked.csv', index = False)

print(top_candidates_sorted[['molecule_chembl_id','target','standard_value']].head(10))