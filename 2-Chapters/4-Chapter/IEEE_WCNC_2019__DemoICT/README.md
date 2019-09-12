# GNU Radio Implementation of MALIN: « Multi-Armed bandits Learning for Internet-of-things Networks »
This repository contains the LaTeX code of a research article written by [Lilian Besson](https://perso.crans.org/besson/) and [Rémi Bonnefoi](https://remibonnefoi.wordpress.com) and [Christophe Moy](https://moychristophe.wordpress.com/), entitled "GNU Radio Implementation of MALIN: « Multi-Armed bandits Learning for Internet-of-things Networks »".

We are glad to announce that [this article](https://perso.crans.org/besson/articles/BBM__IEEE_WCNC_2019.pdf) was accepted for the [IEEE WCNC 2018](http://wcnc2019.ieee-wcnc.org/authors/call-papers/) conference in April 2019.

- PDF : [BBM__IEEE_WCNC_2019.pdf](https://hal.inria.fr/hal-02006825/document)
- HAL notice : [BBM__IEEE_WCNC_2019](https://hal.inria.fr/hal-02006825/)
- BibTeX : [BBM__IEEE_WCNC_2019.bib](https://hal.inria.fr/hal-02006825/bibtex)

[![Published](https://img.shields.io/badge/Published%3F-yes-green.svg)](https://hal.inria.fr/hal-02006825)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-finished-green.svg)](https://bitbucket.org/lbesson/gnu-radio-implementation-of-malin-multi-arm-bandits-learning/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)

> [I (Lilian Besson)](http://perso.crans.org/besson/) have [started my PhD](http://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research in 2017 and 2018.

----

## Abstract

We implement an IoT network the following way: one gateway, one or several intelligent (i.e., learning) objects, embedding the proposed solution, and a traffic generator that emulates radio interferences from many other objects. Intelligent objects communicate with the gateway with a wireless ALOHA-based protocol, which does not require any specific overhead for the learning. We model the network access as a discrete sequential decision making problem, and using the framework and algorithms from Multi-Armed Bandit (MAB) learning, we show that intelligent objects can improve their access to the network by using low complexity and decentralized algorithms, such as UCB and Thompson Sampling. This solution could be added in a straightforward and costless manner in LoRaWAN networks, just by adding this feature in some or all the devices, without any modification on network side.

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/badges.svg)](https://bitbucket.org/lbesson/gnu-radio-implementation-of-malin-multi-arm-bandits-learning/src/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

© 2018 [Lilian Besson](https://perso.crans.org/besson/) and [Rémi Bonnefoi](https://remibonnefoi.wordpress.com) and [Christophe Moy](https://moychristophe.wordpress.com/).

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://bitbucket.org/lbesson/gnu-radio-implementation-of-malin-multi-arm-bandits-learning/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/bitbucket.org/lbesson/gnu-radio-implementation-of-malin-multi-arm-bandits-learning/README.md?pixel)](https://bitbucket.org/lbesson/gnu-radio-implementation-of-malin-multi-arm-bandits-learning/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-overleaf](https://img.shields.io/badge/Made%20with-OverLeaf-1f425f.svg)](https://www.overleaf.com/)
[![forthebadge made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](http://perso.crans.org/besson/)
