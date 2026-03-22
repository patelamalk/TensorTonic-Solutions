import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = np.array(
        [i*p + (1-i)*(1-p) for i in x]
    )
    mean = p
    var = p * (1-p)
    
    return (pmf, mean, var)