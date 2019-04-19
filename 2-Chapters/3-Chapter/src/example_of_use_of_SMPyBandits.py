""" Example of use of SMPyBandits.
See https://SMPyBandits.GitHub.io/API.html for more details!"""
import numpy as np
np.random.seed(0)  # for reproducibility

from SMPyBandits.Arms import Bernoulli
arms = [Bernoulli(0.1), Bernoulli(0.9)]

from SMPyBandits.Environment import MAB
my_MAB_problem = MAB(arms)
nbArms = my_MAB_problem.nbArms  # 2 arms !

from SMPyBandits.Policies import UCB
my_UCB_algo = UCB(nbArms)
my_UCB_algo.startGame()  # reset internal memory

horizon = 1000
for t in range(horizon):  # simulation loop
    chosen_arm = my_UCB_algo.choice()
    observed_reward = my_MAB_problem.draw(chosen_arm)
    my_UCB_algo.getReward(chosen_arm, observed_reward)

cumulated_reward = sum(my_UCB_algo.rewards)  # random!
number_of_plays  = sum(my_UCB_algo.pulls)    # horizon = 1000
mean_reward = cumulated_reward / number_of_plays
print("The UCB algorithm obtains here a mean reward =", mean_reward)