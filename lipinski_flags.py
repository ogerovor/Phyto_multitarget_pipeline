import pandas as pd
df = pd.read_csv('data/descriptors.csv')

rule_mw = df['molwt'] <= 500
rule_logp = df['LogP'] <= 5
rule_hbd = df['HBD'] <= 5
rule_hba = df['HBA'] <= 10
rule_tpsa = df['TPSA'] <= 140
rule_rotb = df['RotB'] <= 10

violates_mw = (~rule_mw).astype(int)
violates_logp = (~rule_logp).astype(int)
violates_hbd = (~rule_hbd).astype(int)
violates_hba = (~rule_hba).astype(int)

violation_count = violates_mw + violates_logp + violates_hbd + violates_hba
passes_lipinski = violation_count <= 1

passes_veber = rule_tpsa & rule_rotb
passes_all = rule_mw & rule_logp & rule_hba & rule_hbd

df['violation_count'] = violation_count
df['passes_lipinski'] = passes_lipinski
df['passes_veber'] = passes_veber
df.to_csv('data/descriptors_with_flags.csv', index= False)

