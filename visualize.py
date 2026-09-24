import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/descriptors_with_flags.csv')

plt.figure(figsize=(8,6))
colors = df['passes_lipinski'].map({True: 'green', False: 'red'})
plt.scatter(df['LogP'], df['TPSA'], c=colors, alpha=0.5,s=10)
plt.xlabel('LogP')
plt.ylabel('TPSA')
plt.title('Drug-likeness: LogP vs TPSA (green = passes Lipinski)')
plt.savefig('data/logp_tpsa_plot.png', dpi=150)
print("saved plot")