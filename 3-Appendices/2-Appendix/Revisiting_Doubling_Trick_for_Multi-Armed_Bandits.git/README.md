# "What Doubling Tricks Can and Can’t Do for Multi-Armed Bandits"
This repository contains the LaTeX code of a research article written by [Lilian Besson](https://perso.crans.org/besson/) and [Emilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html), entitled "What Doubling Tricks Can and Can’t Do for Multi-Armed Bandits".

We are working on [this article](https://www.overleaf.com/docs/12810651zvmysdqbpqzj/pdf.pdf).

- PDF : [BK_ALT_2019.pdf](https://hal.inria.fr/hal-01736357/document)
- HAL notice : [BK_ALT_2019](https://hal.inria.fr/hal-01736357/)
- BibTeX : [BK_ALT_2019.bib](https://hal.inria.fr/hal-01736357/bibtex)

[![Published](https://img.shields.io/badge/Published%3F-waiting-orange.svg)](https://hal.inria.fr/hal-01736357)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-almost%20finished-orange.svg)](https://bitbucket.org/lbesson/what-doubling-tricks-can-and-cant-do-for-multi-armed-bandits/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)

> [I (Lilian Besson)](https://perso.crans.org/besson/) have [started my PhD](https://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research in 2017 and 2018.

----

## Abstract

An online reinforcement learning algorithm is anytime if it does not need to know in advance the horizonTof the experiment. A well-known technique to obtain an anytime algorithm from any non-anytime algorithm is the "Doubling Trick". In the contexts of adversary or stochastic multi-armed bandits, the performance of an algorithm is measured by its regret, and we study two families of sequences of growing horizons (geometric and exponential) to generalize previously known results that certain doubling trick can be used to conserve certain regret bounds. In a broad setting, we prove that a geometric doubling trick can be used to conserve (adversary) bounds in R_T = O(sqrt(T)) but cannot conserve (stochastic) bounds in R_T = O(log(T)). We give insights as to why exponential doubling tricks may be better, as they conserve bounds in R_T = O(logT), and are close to conserving bounds in R_T = O(sqrt(T)).

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/badges.svg)](https://bitbucket.org/lbesson/what-doubling-tricks-can-and-cant-do-for-multi-armed-bandits/src/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

© 2017-2018 [Lilian Besson](https://perso.crans.org/besson/) and [Emilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html).

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://bitbucket.org/lbesson/what-doubling-tricks-can-and-cant-do-for-multi-armed-bandits/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/bitbucket.org/lbesson/what-doubling-tricks-can-and-cant-do-for-multi-armed-bandits/README.md?pixel)](https://bitbucket.org/lbesson/what-doubling-tricks-can-and-cant-do-for-multi-armed-bandits/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-overleaf](https://img.shields.io/badge/Made%20with-OverLeaf-1f425f.svg)](https://www.overleaf.com/)
[![forthebadge made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://perso.crans.org/besson/)
