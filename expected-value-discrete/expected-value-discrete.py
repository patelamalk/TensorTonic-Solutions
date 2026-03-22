import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.sum(p) == 1:
        return np.sum(np.multiply(x, p))
    else:
        raise ValueError
