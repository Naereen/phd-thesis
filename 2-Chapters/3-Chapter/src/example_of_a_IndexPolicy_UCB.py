from numpy import sqrt, log
from .IndexPolicy import IndexPolicy

class UCB(IndexPolicy):
  """ The UCB policy for bounded bandits.
  Reference: [Lai & Robbins, 1985]. """

  def computeIndex(self, arm):
    r""" Compute the current index, at time t and
    after :math:`N_k(t)` pulls of arm k:

    .. math::

        I_k(t) = \frac{X_k(t)}{N_k(t)}
        + \sqrt{\frac{2 \log(t)}{N_k(t)}}.
    """
    if self.pulls[arm] < 1:  # forced exploration
      return float('+inf')   # in the first steps
    else:                    # or compute UCB index
      estimated_mean = (self.rewards[arm] / self.pulls[arm])
      exploration_bias = sqrt((2 * log(self.t)) / self.pulls[arm])
      return estimated_mean + exploration_bias