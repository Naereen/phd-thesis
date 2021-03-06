""" An example of a configuration file to launch some the simulations
For the single-player case.
"""
from os import getenv  # to get command line variables

# Import arms
from SMPyBandits.Arms import *
# Import contained classes
from SMPyBandits.Environment import MAB
# Import single-player algorithms
from SMPyBandits.Policies import *

# HORIZON : number of time steps of the experiments.
# Warning Should be >= 10000 to be interesting "asymptotically".
HORIZON = int(getenv('T', 10000))

# REPETITIONS : number of repetitions of the experiments.
# Warning: Should be >= 10 to be statistically trustworthy.
REPETITIONS = int(getenv('N', 100))

# Number of jobs to use for the parallel computations.
# -1 means all the CPU cores, 1 means no parallelization.
N_JOBS = int(getenv('N_JOBS', -1))

# Number of arms for non-hard-coded problems
NB_ARMS = int(getenv('K', 3))

# Lower value of means
LOWER = float(getenv('LOWER', 0))
# Amplitude value of means
AMPLITUDE = float(getenv('AMPLITUDE', 1))

# Type of arms for non-hard-coded problems
ARM_TYPE = mapping_ARM_TYPE[str(getenv('ARM_TYPE', "Bernoulli"))]

# Means of arms for non-hard-coded problems
MEANS = uniformMeans(nbArms=NB_ARMS, delta=0.05,
    lower=LOWER, amplitude=AMPLITUDE, isSorted=True
)

# This dictionary configures the experiments
configuration = {
    # --- Duration of the experiment
    "horizon": HORIZON,
    # --- Number of repetition of the experiment (to have an average)
    "repetitions": REPETITIONS,
    # --- Parameters for the use of joblib.Parallel
    "n_jobs": N_JOBS,    # = nb of CPU cores
    # --- Should we plot the lower-bounds or not?
    "plot_lowerbounds": True,  # Default
    # --- Arms: a list of configuration of environments
    "environment": [
        {   # Use vector from command line
            "arm_type": ARM_TYPE,
            "params": MEANS
        },
    ],
    # --- Policies: a list of configuration of algorithms
    "policies": [
        # --- Stupid algorithm
        {
            "archtype": Uniform,   # The stupidest policy, fully uniform
            "params": {}
        }, {  # --- Fixed arm algorithm
            "archtype": TakeFixedArm,   # Take worse arm!
            "params": { "armIndex": 0 },
        }, {
            "archtype": TakeFixedArm,   # Take second worse arm!
            "params": { "armIndex": 1 },
        }, {
            "archtype": TakeFixedArm,   # Take third worse arm!
            "params": { "armIndex": min(2, nbArms - 1) },
        }, {  # --- UCB algorithm
            "archtype": UCBalpha,   # UCB with alpha=1 parameter
            "params": { "alpha": 1.0 }
        }, {  # --- Thompson algorithm
            "archtype": Thompson,
            "params": { "posterior": Beta }
        }, {  # --- KL UCB algorithm
            "archtype": klUCB,
            "params": { "klucb": klBern }
        },
    ]
}  # DONE

print("Loaded experiments configuration:")
print("configuration =", configuration)  # DEBUG
