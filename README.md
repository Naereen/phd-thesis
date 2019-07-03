# "My PhD thesis"
## « Multi-players Bandit Algorithms for Internet of Things Networks »
This repository contains the LaTeX code of my PhD thesis, written by [Lilian Besson](https://perso.crans.org/besson/), entitled "Multi-players Bandit Algorithms for Internet of Things Networks".

## Calendar
- I started to think about the outline in January 2019, I started to play with the template end of January, and to seriously write middle of February 2019.
- I expect to finish in July 2019.

## Advisors, reviewers, jury
- Thanks to my advisors: [Christophe Moy](https://moychristophe.wordpress.com/) and [Émilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html).
- Thanks to the reviewers: [Vianney Perchet](https://sites.google.com/site/vianneyperchet/) and [Nathalie Mitton](http://researchers.lille.inria.fr/~mitton/).
- Thanks to the dear member of my jury reviewers: [Patrick Maillé](http://perso.telecom-bretagne.eu/patrickmaille/), [Raphaël Féraud](https://www.researchgate.net/profile/Raphael_Feraud/) and [Richard Combes](http://rcombes.supelec.free.fr/).

## Links
TODO

- PDF : [PhD_thesis__Lilian_Besson.pdf](https://perso.crans.org/besson/phd/articles/PhD_thesis__Lilian_Besson.pdf)
- HAL notice : [PhD_thesis__Lilian_Besson](https://hal.inria.fr/hal-XXX/)
- BibTeX : [PhD_thesis__Lilian_Besson.bib](https://hal.inria.fr/hal-XXX/bibtex)
- Source code and documentation: [https://smpybandits.github.io/](https://smpybandits.github.io/).

[![Published](https://img.shields.io/badge/Published%3F-work%20in%20progress-red.svg)](https://hal.inria.fr/hal-XXX)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-in%20progress-red.svg)](https://github.com/Naereen/phd-thesis/commits/master)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)

> [I (Lilian Besson)](https://perso.crans.org/besson/) have [started my PhD](https://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research in 2019.

----

## About this thesis
### In English

#### Title
**Multi-players Bandit Algorithms for Internet of Things Networks**

#### Summary
In this PhD thesis, we study wireless networks and reconfigurable end-devices that can access Cognitive Radio networks, in unlicensed bands and without central control. We focus on Internet of Things networks (IoT), with the objective of extending the devices' battery life, by equipping them with low-cost but efficient machine learning algorithms, in order to let them automatically improve the efficiency of their wireless communications. We propose different models of IoT networks, and we show empirically on both numerical simulations and real-world validation the possible gain of our methods, that use Reinforcement Learning. The different network access problems are modeled as Multi-Armed Bandits (MAB), but we found that analyzing the realistic models was intractable, because proving the convergence of many IoT devices playing a collaborative game, without communication nor coordination is hard, when they all follow random active pattern. The rest of this manuscript thus studies two restricted models, first multi-players bandits in stationary problems, then non-stationary single-player bandits. We also detail another contribution, SMPyBandits, our open-source Python library for numerical MAB simulations, that covers all the studied models and more.

#### Keywords
Internet of Things (IoT), Cognitive Radio, Learning Theory, Collision Mitigation Sequential Learning, Reinforcement Learning, Multi-Armed Bandits (MAB), Decentralized Learning, Multi-Player Multi-Armed Bandits, Change Point Detection, Non-Stationary Multi-Armed Bandits

---

#### Résumé
Dans cette thèse de doctorat, nous étudions les réseaux sans fil et les appareils reconfigurables qui peuvent accéder à des réseaux de type radio intelligente, dans des bandes non licenciées et sans supervision centrale.
Nous considérons des réseaux actuels ou futures de l'Internet des Objets (IoT), avec l'objectif d'augmenter la durée de vie de la batterie des appareils, en les équipant d'algorithmes d'apprentissage machine peu coûteux mais efficaces, qui leur permettent d'améliorer automatiquement l'efficacité de leurs communications sans fil.
Nous proposons deux modèles de réseaux IoT, et nous montrons empiriquement, par des simulations numériques et une validation expérimentale réaliste, le gain que peuvent apporter nos méthodes, qui se reposent sur l'apprentissage par renforcement.
Les différents problèmes d'accès au réseau sont modélisés avec des Bandits Multi-Bras (MAB), mais leur analyse est difficile à réaliser,
car il est délicat de prouver la convergence d'un grand nombre d'appareils jouant à un jeu collaboratif sans communication ni aucune coordination, lorsque les appareils suivent tous un modèle d'activation aléatoire.
Le reste de ce manuscrit étudie donc deux modèles restreints, d'abord des bandits multi-joueurs dans des problèmes stationnaires, puis des bandits mono-joueur non stationnaires.
Nous détaillons également une autre contribution, la bibliothèque Python open-source SMPyBandits, qui permet des simulations numériques de problèmes MAB, qui couvre les modèles étudiés et d'autres.

#### Titre
**Algorithmes de Bandits Multi-Joueurs pour les Réseaux de l'Internet des Objets**

#### Mot clés
Internet des Objets (IoT), Radio Intelligente, Théorie de l'apprentissage, Apprentissage séquentiel de l'atténuation des collisions, Apprentissage par renforcement, Bandits multi-bras (MAB), Apprentissage décentralisé, Bandits multi-bras multi-joueurs, Détection des points de changement, Bandits multi-bras non stationnaires

----

## How to compile the PDF?
- You will need a complete TeX distribution, like TeX Live, and PDFLaTeX, as well as GNU `make`, `git`, and `latexmk`,
- First, `git clone` this repository,
```bash
$ git clone https://github.com/Naereen/phd-thesis/
$ cd phd-thesis/
```
- Then, simply run `make pdf` (or `latexmk -pdflatex=pdflatex -pdf PhD_thesis__Lilian_Besson.tex`)
```bash
$ make pdf
```
- It should produce the file [`PhD_thesis__Lilian_Besson.pdf`](https://perso.crans.org/besson/phd/articles/PhD_thesis__Lilian_Besson.pdf) (PDF/X for online version).
- It was only tested on a GNU/Linux machine, under XUbuntu 18.04.

### How to compile to get a printable version?
- In `PhD_thesis__Lilian_Besson.tex`, add the `print` option to the `\documentclass{0-Misc/PhDThesisPSnPDF}` line.

### How to compile to get a PDF/A archivable version?
- FIXME

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/badges.svg)](https://https://github.com/Naereen/phd-thesis/src/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

The template is inspired from [@kks32/phd-thesis-template](https://github.com/kks32/phd-thesis-template), also released under the [MIT License](https://github.com/kks32/phd-thesis-template/blob/master/license.md).

© 2019 [Lilian Besson](https://perso.crans.org/besson/) and collaborators.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://https://github.com/Naereen/phd-thesis/commits/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/phd-thesis/README.md?pixel)](https://https://github.com/Naereen/phd-thesis/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://perso.crans.org/besson/)
