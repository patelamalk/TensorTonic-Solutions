import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    return np.array([
        np.percentile(x, pctile, method='linear') for pctile in q
    ])
    
    