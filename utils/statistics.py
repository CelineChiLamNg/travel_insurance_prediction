import numpy as np
import scipy.stats as stats
import pandas as pd

def ci_mean_analytical(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)
    margin = sem * stats.t.ppf((1 + confidence) / 2., len(data)-1)
    return (mean, mean - margin, mean + margin)


def ci_bootstrap(data, num_boots=1000, confidence=0.95):
    boots = [np.mean(np.random.choice(data, replace=True, size=len(data))) for _ in range(num_boots)]
    mean = np.mean(boots)
    lower, upper = np.percentile(boots, [(1-confidence)/2*100, (1 + confidence)/2*100])
    return (mean, lower, upper)

def chi2_test(df, feature, target):
    contingency_table = pd.crosstab(df[feature], df[target])
    chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2_stat, p_val

def ci_bootstrap_test(data, num_boots=1000, confidence=0.95):
    boots = [np.mean(np.random.choice(data, replace=True, size=len(data))) for _ in range(num_boots)]
    return boots