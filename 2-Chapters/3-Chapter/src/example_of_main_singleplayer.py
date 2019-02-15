""" An example of a simple 'main' script.
Main scripts load the config, run the simulations, and plot them/
For the single player case.
"""
from example_of_configuration_singleplayer import configuration
from SMPyBandits.Environment import Evaluator

configuration['showplot'] = True
evaluation = Evaluator(configuration)

# Start the evaluation and then print final ranking
# and do and show plot, for each environment
for envId, env in enumerate(evaluation.envs):
    # Evaluate just that env
    evaluation.startOneEnv(envId, env)

# Compare them
for envId, env in enumerate(evaluation.envs):
    evaluation.plotHistoryOfMeans(envId)

    print("\nGiving all the vector of final regrets ...")
    evaluation.printLastRegrets(envId)
    print("\nGiving the final ranking ...")
    evaluation.printFinalRanking(envId)

    print("\n\n- Plotting the last regrets...")
    evaluation.plotLastRegrets(envId, boxplot=True)

    print("\nGiving the mean and std running times ...")
    evaluation.printRunningTimes(envId)
    evaluation.plotRunningTimes(envId)

    print("\nGiving the mean and std running times ...")
    evaluation.printMemoryConsumption(envId)
    evaluation.plotMemoryConsumption(envId)

    print("\n\n- Plotting the mean reward...")
    evaluation.plotRegrets(envId, meanReward=True)

    print("\n\n- Plotting the regret...")
    evaluation.plotRegrets(envId)

    print("\n- Plotting the probability of picking the best arm...")
    evaluation.plotBestArmPulls(envId)

    print("\n- Plotting the histograms of regrets...")
    evaluation.plotLastRegrets(envId, sharex=True, sharey=True)

# Done
print("Done for simulations example_of_main_singleplayer ...")
