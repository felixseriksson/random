import numpy as np
import seaborn as sns
from statsmodels.stats.meta_analysis import combine_effects

# dummy data
mean_effect = np.array([61.00,61.40,62.21,62.30,62.34,62.60,62.70,62.84,65.90])
var_effect = np.array([0.2025,1.2100,0.0900,0.2025,0.3844,0.5625,0.0676,0.0225,1.8225])
idx = ['lab1','lab2','lab3','lab4','lab5','lab6','lab7','lab8','lab9']

# meta-analysis and forest plot
results = combine_effects(mean_effect, var_effect, method_re="chi2", use_t=True, row_names=idx)
sns.set_style("darkgrid")
print(results.summary_frame())
fig = results.plot_forest()
fig.show()
input()