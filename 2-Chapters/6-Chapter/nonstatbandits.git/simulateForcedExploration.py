#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tqdm

means_0 = [0.1, 0.5, 0.9]
means_1 = [0.9, 0.5, 0.1]
maxMean = max(max(means_0), max(means_1))
nbArms = len(means_0)
horizon = 1000

def reward(arm, t):
    if t <= horizon/2:
        return np.random.binomial(1, means_0[arm])
    else:
        return np.random.binomial(1, means_1[arm])

def simulateBandit(bandit, detect):
    pulls = np.zeros(nbArms, dtype=int)
    all_pulls = [ ]
    rewards = np.zeros(nbArms)
    all_rewards = [ [] for i in range(nbArms) ]
    all_rewards_shared = [ ]
    last_restart = 0
    for t in range(horizon):
        choice = bandit(pulls, rewards, t - last_restart)
        pulls[choice] += 1
        all_pulls.append(choice)
        r = reward(choice, t)
        rewards[choice] += r
        all_rewards[choice].append(r)
        all_rewards_shared.append(r)
        # print(f"Time {t}, bandit chose {choice}, saw reward {r} (pulls = {pulls}, rewards = {rewards})")
        if detect(pulls, rewards, all_rewards, choice, r, t, last_restart):
            print(f"  CDP algorithm {detect.__name__} chose to restart at time {t}, previous restart was {last_restart}")
            last_restart = t
            pulls[:] = 0
            rewards[:] = 0
            all_rewards = [ [] for i in range(nbArms) ]
    # now compute the history of regret
    maxMeans = np.array(([max(means_0)] * (horizon//2)) + ([max(means_1)] * (horizon//2)))
    all_rewards_shared = np.array(all_rewards_shared)
    return np.cumsum(maxMeans - all_rewards_shared)
    return maxMean * horizon - np.sum(rewards)


def ucb(pulls, rewards, t, *args, **kwargs):
    if np.any(pulls <= 0):
        return np.random.choice(np.where(pulls <= 0)[0])
    indexes = rewards/pulls + np.sqrt(np.log(t) / pulls)
    return np.random.choice(np.where(np.isclose(indexes, np.max(indexes)))[0])


def dontdetect(pulls, rewards, all_rewards, arm, r, t, last_restart):
    return False

proba_of_random_detection = 0.01

def random_detection(pulls, rewards, all_rewards, arm, r, t, last_restart):
    if max(t, last_restart) <= horizon/2:
        return False
    else:
        return np.random.binomial(1, proba_of_random_detection)

w = 80
threshold_b = 20

def detect_chernoff(pulls, rewards, all_rewards, arm, r, t, last_restart):
    data = all_rewards[arm]
    if len(data) < w:
        return False
    last_data = data[-w:]
    left_sum = np.sum(last_data[:w//2])
    right_sum = np.sum(last_data[w//2:])
    return abs(left_sum - right_sum) >= threshold_b


alpha = 0.01
gamma = alpha / nbArms

def ucb_ForcedExploration(pulls, rewards, t, *args, **kwargs):
    if np.any(pulls <= 0):
        return np.random.choice(np.where(pulls <= 0)[0])
    assert np.all(pulls >= gamma*t), "Error: we really believe that n_i(t) - n_i(s) >= gamma (t - s) for any s <= t in sequence [last restart, current time] (for any current time)."
    if np.any(pulls <= alpha*t):
        return np.random.choice(np.where(pulls <= alpha*t)[0])
    indexes = rewards/pulls + np.sqrt(np.log(t) / pulls)
    return np.random.choice(np.where(np.isclose(indexes, np.max(indexes)))[0])

repetitions = 1
repetitions = 50

def main():
    plt.figure()

    print(f"\n\nSimulating UCB + no detection, for {repetitions} times...")
    results = [simulateBandit(ucb, dontdetect) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label="UCB")
    plt.plot(np.mean(results, axis=0), label="UCB")

    print(f"\n\nSimulating UCB with forced exploration + no detection, for {repetitions} times...")
    results = [simulateBandit(ucb_ForcedExploration, dontdetect) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label=fr"UCB + tracking $\alpha={alpha:.3g}$")
    plt.plot(np.mean(results, axis=0), label=fr"UCB + tracking $\alpha={alpha:.3g}$")

    print(f"\n\nSimulating UCB + random detection delay, for {repetitions} times...")
    results = [simulateBandit(ucb, random_detection) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label=fr"UCB + random CPD ($P={proba_of_random_detection}$ to detect after CP)")
    plt.plot(np.mean(results, axis=0), label=fr"UCB + random CPD ($P={proba_of_random_detection}$ to detect after CP)")

    print(f"\n\nSimulating UCB with forced exploration + random detection delay, for {repetitions} times...")
    results = [simulateBandit(ucb_ForcedExploration, random_detection) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label=fr"UCB + random CPD ($P={proba_of_random_detection}$ to detect after CP) + tracking $\alpha={alpha:.3g}$")
    plt.plot(np.mean(results, axis=0), label=fr"UCB + random CPD ($P={proba_of_random_detection}$ to detect after CP) + tracking $\alpha={alpha:.3g}$")

    print(f"\n\nSimulating M-UCB($w={w}$, $b={threshold_b}$), for {repetitions} times...")
    results = [simulateBandit(ucb, detect_chernoff) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label=f"M-UCB($w={w}$, $b={threshold_b}$)")
    plt.plot(np.mean(results, axis=0), label=f"M-UCB($w={w}$, $b={threshold_b}$)")

    print(f"\n\nSimulating M-UCB($w={w}$, $b={threshold_b}$) with forced exploration, for {repetitions} times...")
    results = [simulateBandit(ucb_ForcedExploration, detect_chernoff) for _ in tqdm.trange(repetitions)]
    # sns.distplot(results, label=fr"M-UCB($w={w}$, $b={threshold_b}$) + tracking $\alpha={alpha:.3g}$")
    plt.plot(np.mean(results, axis=0), label=fr"M-UCB($w={w}$, $b={threshold_b}$) + tracking $\alpha={alpha:.3g}$")

    plt.title(f"Distribution of regret after $T={horizon}$ time steps")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
