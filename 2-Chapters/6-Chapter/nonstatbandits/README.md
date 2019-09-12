# "The Generalized Likelihood Ratio Test meets klUCB: an Improved Algorithm for Piece-Wise Non-Stationary Bandits"
This repository contains the LaTeX code of a research article written by [Lilian Besson](https://perso.crans.org/besson/) and [Emilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html), entitled "The Generalized Likelihood Ratio Test meets klUCB: an Improved Algorithm for Piece-Wise Non-Stationary Bandits".

We are working on [this article](https://perso.crans.org/besson/articles/BK__COLT_2019.pdf).

- PDF : [BK_COLT_2019.pdf](https://hal.inria.fr/hal-02006471/document)
- HAL notice : [BK_COLT_2019](https://hal.inria.fr/hal-02006471/)
- BibTeX : [BK_COLT_2019.bib](https://hal.inria.fr/hal-02006471/bibtex)
- Source code and documentation: [on GitHub](http://smpybandits.github.io/NonStationaryBandits.html)

[![Published](https://img.shields.io/badge/Published%3F-waiting-orange.svg)](https://hal.inria.fr/hal-02006471)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-almost%20finished-orange.svg)](https://bitbucket.org/lbesson/combining-the-generalized-likelihood-ratio-test-and-kl-ucb-for/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)

> [I (Lilian Besson)](https://perso.crans.org/besson/) have [started my PhD](https://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research in 2019.

----

## Abstract

In this paper, we propose a new algorithm for the piece-wise i.i.d. non-stationary bandit problem, when the rewards are bounded. Our proposal, GLRklUCB, combines an efficient bandit algorithm, kl-UCB, with an efficient, parameter-free, change-point detector, the Bernoulli Generalized Likelihood Ratio Test, for which we provide new theoretical guarantees of independent interest. We analyze two variants of our strategy, based on local restarts and global restarts and show their regret is upper-bounded by $O(U_T sqrt(T \log(T)))$ if the number of change-points $U_T$ is unknown, and $O(sqrt(U_T T log(T))$ if $U_T$ is known. We present extensive numerical experiments showing that GLRklUCB outperforms all the passive and adaptive algorithms from the literature, and highlight the benefit of local restarts.

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/badges.svg)](https://bitbucket.org/lbesson/combining-the-generalized-likelihood-ratio-test-and-kl-ucb-for/src/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

© 2019 [Lilian Besson](https://perso.crans.org/besson/) and [Emilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html).

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://bitbucket.org/lbesson/combining-the-generalized-likelihood-ratio-test-and-kl-ucb-for/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/bitbucket.org/lbesson/combining-the-generalized-likelihood-ratio-test-and-kl-ucb-for/README.md?pixel)](https://bitbucket.org/lbesson/combining-the-generalized-likelihood-ratio-test-and-kl-ucb-for/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-overleaf](https://img.shields.io/badge/Made%20with-OverLeaf-1f425f.svg)](https://www.overleaf.com/)
[![forthebadge made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://perso.crans.org/besson/)
