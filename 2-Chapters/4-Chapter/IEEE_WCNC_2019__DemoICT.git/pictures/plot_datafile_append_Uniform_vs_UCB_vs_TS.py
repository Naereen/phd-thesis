#!/usr/bin/env python3
# -*- coding: utf8 -*-

""" Plot the datafile 'append' for an Object which uses the Uniform, or UCB, or TS algorithm.

Quite hacky.
"""

import sys, os, os.path, glob

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns


def palette(nb):
    """ Use a smart palette from seaborn, for nb different plots on the same figure.

    - Ref: http://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn.hls_palette
    """
    return sns.hls_palette(nb + 1)[:nb]


def makemarkers(nb):
    """ Give a list of cycling markers. See http://matplotlib.org/api/markers_api.html

    .. note:: This what I consider the *optimal* sequence of markers, they are clearly differentiable one from another and all are pretty.

    Examples:

    >>> makemarkers(7)
    ['o', 'D', 'v', 'p', '<', 's', '^']
    >>> makemarkers(12)
    ['o', 'D', 'v', 'p', '<', 's', '^', '*', 'h', '>', 'o', 'D']
    """
    allmarkers = ['o', 'D', 'v', 'p', '<', 's', '^', '*', 'h', '>']
    longlist = allmarkers * (1 + int(nb / float(len(allmarkers))))  # Cycle the good number of time
    return longlist[:nb]  # Truncate


def parse_one_line(line):
    """ Get one line of a file in this format
        16:17:266:2864    3:4:194:2443

    and return a couple of lists

        [16,17,266,2864], [3,4,194,2443]
    """
    line_trial, line_success = line.split('    ')
    one_trial = [int(s) for s in line_trial.split(':')]
    one_success = [int(s) for s in line_success.split(':')]
    return one_trial, one_success


def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    horizon = len(lines)
    # hack to read number of lines
    nb_arm = lines[0].split('    ')[0].count(':') + 1
    # create data
    trials = np.zeros((horizon, nb_arm), dtype=int)
    successes = np.zeros((horizon, nb_arm), dtype=int)
    # read it and fill them
    print("For file", filename)  # DEBUG
    for i, line in enumerate(lines):
        try:
            one_trial, one_success = parse_one_line(line)
            trials[i, :] = one_trial
            successes[i, :] = one_success
        except Exception as e:
            print("For line", i, "containing", line)
            print("  one_trial =", one_trial, "and one_success =", one_success)
            raise e
    # compute success rates
    all_arms_tried = np.min(trials, axis=1) > 0
    success_rates = successes[all_arms_tried] / trials[all_arms_tried]
    mean_success_rates_all_arms = np.sum(successes[all_arms_tried], axis=1) / np.sum(trials[all_arms_tried], axis=1)
    return mean_success_rates_all_arms, success_rates, successes, trials


def get_datas():
    files = {
        "UCB": glob.glob("generator_SU_V6_impl_cc_data_file_1_append__*.txt"),
        "Uniform": glob.glob("generator_SU_V6_impl_cc_data_file_2_append__*.txt"),
        # FIXME do some simulations with Thompson Sampling
        "TS": glob.glob("generator_SU_V6_impl_cc_data_file_3_append__*.txt"),
    }
    datas = {
        algo: [
            read_data(filename)[0]
            for filename in files_algo
        ]
        for algo, files_algo in files.items()
    }
    return datas


def plot_data(datas,
        figurename='plot_datafile_append_Uniform_vs_UCB_vs_TS',
        extensions=('eps', 'png', 'pdf'),
    ):
    nb_algos = len(datas.keys())
    # 1. cut data that are too large
    # compute min length of data for each algo
    min_length = min([
        min([
            len(data)
            for data in datas_algo
        ])
        for algo, datas_algo in datas.items()
    ])
    print("min_length =", min_length)

    min_length = min(min_length, 2000)

    # then cut the other to this length
    smaller_datas = {
        algo: [
            data[:min_length]
            for data in datas_algo
        ]
        for algo, datas_algo in datas.items()
    }
    print("smaller_datas =", smaller_datas)

    # 2. get mean data on X repetitions (eg 10)
    mean_datas = {
        algo: np.mean(datas_algo, axis=0)
        for algo, datas_algo in smaller_datas.items()
    }
    print("mean_datas =", mean_datas)
    nb_repetitions = [
        len(smaller_data)
        for smaller_data in smaller_datas.values()
    ]
    assert len(set(nb_repetitions)) == 1, "Error: some algorithms don't have the same number of repetitions! nb_repetitions = {}".format(nb_repetitions)
    nb_repetition = nb_repetitions[0]

    colors = palette(nb_algos)
    markers = makemarkers(nb_algos)

    # 3. plot data
    plt.figure()
    for i, (algo, mdata) in enumerate(mean_datas.items()):
        plt.plot(mdata, label=algo, color=colors[i], marker=markers[i], markevery=(i / 50., 0.1), lw=3, ms=8)
    plt.title("Comparison of mean successful communication rate")
    plt.xlabel("Time steps $t = 1 ... {}$. {} repetition{}. Objects use 4 channels.".format(min_length, nb_repetition, "s" if nb_repetition > 1 else ""))
    plt.ylim(0, 1)  # percentage !
    # plt.gca().yaxis.set_major_formatter(PercentFormatter)
    plt.ylabel("Successful communication rate (in percentage)")
    plt.legend()
    # 4. save figure
    for ext in extensions:
        plt.savefig("{}.{}".format(figurename, ext))
    # Show it FIXED move to the end after saving
    plt.show()


def main():
    datas = get_datas()
    plot_data(datas)


if __name__ == '__main__':
    main()
