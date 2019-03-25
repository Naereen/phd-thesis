We thank our three reviewers for their careful readings and comments, and we address below specific concerns raised by reviewers 2 and 3.

The typo noted by reviewer 1 in the Algorithm was corrected.


# Response to Reviewer 2

- "In the introduction, the paper claims to answer [...]".

We changed this sentence in the introduction, to reflect what is announced in the abstract and what is actually proved in the paper, thanks for the remark.

- "An (advanced) extension [...] *Corralling a Band of Bandit Algorithms* by Agarwal et al. in COLT 2017".

That is indeed an advanced extension, and we will try to look into it in the future.

- "Lemma 2 is not correct: It assumes that the regret will increase when the last epoch is extended from time $T$ to time $T_{L_T}$. Strictly speaking, this is not even defined, because there are no rewards beyond time $T$".

Our definition of the reward streams defines $(Y_{k,t})_{t\in\mathbb{N}}$, and not just $Y_{k,0},\dots,Y_{k,T}$.
Furthermore, the upper bound in Lemma 2 refers to regret with horizon $T_i - T_{i-1}$ only for an algorithm which uses this horizon, so according to the definition of $r(t)$ (top of page 2), the reward $r(t)$ is actually well defined here.

- "But even being more liberal it is incorrect, because the regret is not monotonically increasing in T. If the result is restated in terms of a bound on the regret, however, then it can be salvaged [...]".

Thanks for mentioning this, and indeed the regret is monotonically increasing for stochastic models but could not be for generic adversarial models.
However, it is true for oblivious adversaries, which is our case of interest as we defined the reward streams $(Y_{k,t})_{t\in\mathbb{N}}$ (if they are fixed from the beginning they cannot be adaptive to the player's actions).
We will be clearer on this point in the final version, by announcing when needed that we mean "oblivious adversary" when we think of "possibly non-stochastic models".

- "The paper's interpretation of Theorem 5 is that geometric doubling does not preserve logarithmic regret, but I would view it as saying that we only pay one extra $\log(T)$ factor, which is not so bad. So I would not interpret this as a negative result".

Thanks, that is another, valid, point of view. We wanted to highlight the fact that an order-optimal algorithm (for problem-dependent bounds, ie, logarithmic regret) becomes sub-optimal when the geometric doubling trick is used.
But we added a remark stating that we only pay one extra $\log(T)$ factor (and depending on the value of $\delta$, it can be not so bad or very bad), to be clearer on this point.

- "Theorems 5 and 9 [...]".

Thank you for your suggestion, we did modify both theorems according to what you suggest.

- "In Theorems 4 and 7, referring to the constant factor overhead as a *loss* is confusing in the context of the bandit setting".

We agree that indeed loss is misleading in the context of online learning, we changed it to multiplicative *overhead*.

- "Definition 6 is ungrammatical".

Definitions 3 and 6 were slightly modified to be grammatically correct, thank you for noticing.


# Response to Reviewer 3

- "While this may be a useful reference point for future work, the results are rather unsurprising".

The necessity of using an exponential doubling trick to preserve problem-dependent bounds (ie, logarithmic) was maybe a known fact (see for instance [*UCB revisited*, Auer et al, 2010]) but, to the best of our knowledge, it was not proved before (Theorem 5).
Additionally, our lower bound in Theorem 9 showing that an extra $\log(T)$ term is paid when using an exponential doubling trick for problem-independent bounds (ie, in $\sqrt{T}$) is also new.

- "I'm especially not convinced with the usefulness of the doubling technique on lower bound".

This part of the paper should actually be understood the other way around: we do not demonstrate the usefulness of the doubling technique on lower bound (that is, to prove that it can be used to preserve a lower bound), but we do the opposite. We use a lower bound to prove that for certain doubling tricks *cannot* be used to preserve certain upper bounds.
For example, Theorem 5 shows that a geometric doubling trick is not increasing fast enough to preserve logarithmic regret bounds. Failing to prove an upper bound is not enough to support this claim, and to the best of our knowledge, proving an actual lower bound like Theorem 5 is the only possible approach.

- "Why are these results limited to the multi-armed bandits problem? All statements seem to be agnostic of the partial information setting".

Thanks for noting that. Indeed, we believe that our upper bound (Ths 4 and 7) can be extended to other feedback models (eg, full information) and we will mention it in the final version. It is a bit less clear for the lower bounds, as Lemma 2 requires a *stochastic* bandit feedback.
It might be true as well for online learning against a stochastic adversary, but the bandit case is more interesting anyways.

- "Doubling techniques often get tricky for problem-dependent bounds, because the regret scales not only in $T$ but also in other functions of the input (reward sequence). [...]".

As this paper is motivated by doubling tricks on stochastic bandit algorithms, we did not consider this type of "problem-dependent" bounds (eg, second-order bounds or bounds that depend on the loss of the best action). But we will look into this work, thanks for mentioning it.
