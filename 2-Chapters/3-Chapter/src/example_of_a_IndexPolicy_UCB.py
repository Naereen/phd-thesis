from numpy import sqrt, log          # mathematical functions
from IndexPolicy import IndexPolicy  # base class

class UCB(IndexPolicy):
    """ The UCB policy for bounded bandits.
    Reference: [Lai & Robbins, 1985], [Auer et al. 2020]. """

    def computeIndex(self, arm):
        r""" Compute the current index :math:`U_k(t)`, at time t (:attr:`self.t`)
        and after :math:`N_k(t)` pulls of arm k (``arm``):

        .. math:: U_k(t) = \frac{X_k(t)}{N_k(t)} + \sqrt{\frac{2 \log(t)}{N_k(t)}}.
        """
        if self.pulls[arm] < 1:    # forced exploration in the first steps
            return float('+inf')
        else:                      # or compute UCB index
            estimated_mean = self.rewards[arm] / self.pulls[arm]
            exploration_bias = sqrt((2 * log(self.t)) / self.pulls[arm])
            return estimated_mean + exploration_bias
