""" Example of use of SMPyBandits.
See https://smpybandits.github.io/API.html for more"""
import numpy as np
np.random.seed(0)  # for reproducibility

from SMPyBandits.Arms import Bernoulli
arms = [Bernoulli(0.1), Bernoulli(0.9)]

from SMPyBandits.Environment import MAB
my_MAB_problem = MAB(arms)
nbArms = my_MAB_problem.nbArms

from SMPyBandits.Policies import UCB
my_UCB_algo = UCB(nbArms)
my_UCB_algo.startGame()  # reset internal memory

horizon = 1000
for t in range(horizon):
    chosen_arm = my_UCB_algo.choice()
    observed_reward = my_MAB_problem.draw(chosen_arm)
    my_UCB_algo.getReward(chosen_arm, observed_reward)

cumulated_reward = sum(my_UCB_algo.rewards)
number_of_plays = sum(my_UCB_algo.pulls)  # = 1000
mean_reward = cumulated_reward / number_of_plays
print("The UCB algorithm obtains here a mean reward =", mean_reward)