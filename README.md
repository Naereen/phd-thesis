# *My PhD thesis* : « Multi-players Bandit Algorithms for Internet of Things Networks »
This repository contains the LaTeX code of my PhD thesis, written by [Lilian Besson](https://perso.crans.org/besson/), entitled "Multi-players Bandit Algorithms for Internet of Things Networks".

## Calendar
- I started to think about the outline in January 2019, I started to play with the template end of January, and to seriously write middle of February 2019.
- I wrote intensely in March and May 2019.
- I finished the introduction and conclusion in June 2019.
- I sent the thesis to the reviewers on the 12th of July 2019.
- I received the first feedback on the 28th of August, and the second feedback on the 12th of September 2019.
- I defended on the 20th of November 2019, and [this repository was open-sourced](https://github.com/Naereen/phd-thesis/issues/22) on the 18th of November, just because I was too impatient to wait.

## Where & when?
- My defense happened the 20th of November 2019, at 10h30, in [CentraleSupélec (campus de Rennes)](http://www.rennes.centralesupelec.fr/). Room UBL. [Direction to come?](http://www.rennes.centralesupelec.fr/en/acces)
- It went very well, I am now proud to hold a Doctorate of Philosophy (PhD), in Telecommunications!

> See https://perso.crans.org/besson/phd/defense/ [this page](https://perso.crans.org/besson/phd/defense/) to get more details for coming to my defense!

## Advisors, reviewers, jury
- Thanks to my advisors: [Christophe Moy](https://moychristophe.wordpress.com/) and [Émilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/research.html).
- Thanks to the reviewers: [Vianney Perchet](https://sites.google.com/site/vianneyperchet/) and [Nathalie Mitton](http://researchers.lille.inria.fr/~mitton/).
- Thanks to the dear member of my jury reviewers: [Patrick Maillé](http://perso.telecom-bretagne.eu/patrickmaille/), [Raphaël Féraud](https://www.researchgate.net/profile/Raphael_Feraud/) and [Richard Combes](http://rcombes.supelec.free.fr/).

## Links
I submited the thesis on [Theses.fr](https://www.theses.fr/), it's in progress (TODO update links below when done).

- PDF : [PhD_thesis__Lilian_Besson.pdf](https://perso.crans.org/besson/phd/articles/PhD_thesis__Lilian_Besson.pdf)
- TEL notice : [PhD_thesis__Lilian_Besson](https://tel.inria.fr/tel-XXX/)
- BibTeX : [PhD_thesis__Lilian_Besson.bib](https://tel.inria.fr/tel-XXX/bibtex)
- Source code and documentation: [SMPyBandits.GitHub.io](https://smpybandits.github.io/).
- Slides used for the PhD defense : [PhD_thesis__Lilian_Besson__slides.pdf](https://perso.crans.org/besson/slides/2019_11__PhD_Defense__Multi-players_Bandit_Algorithms_for_Internet_of_Things_Networks/slides.pdf) ([and folder with the source](https://github.com/Naereen/slides/tree/master/2019_11__PhD_Defense__Multi-players_Bandit_Algorithms_for_Internet_of_Things_Networks))

[![Published](https://img.shields.io/badge/Published%3F-work%20in%20progress-red.svg)](https://tel.inria.fr/tel-XXX)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-in%20progress-red.svg)](https://github.com/Naereen/phd-thesis/commits/master)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://bitbucket.org/lbesson/ama)

----

## About this thesis

### 🇬🇧 In English
#### Title
**Multi-players Bandit Algorithms for Internet of Things Networks**.

#### Summary
In this PhD thesis, we study wireless networks and reconfigurable end-devices that can access Cognitive Radio networks, in unlicensed bands and without central control. We focus on Internet of Things networks (IoT), with the objective of extending the devices' battery life, by equipping them with low-cost but efficient machine learning algorithms, in order to let them automatically improve the efficiency of their wireless communications. We propose different models of IoT networks, and we show empirically on both numerical simulations and real-world validation the possible gain of our methods, that use Reinforcement Learning. The different network access problems are modeled as Multi-Armed Bandits (MAB), but we found that analyzing the realistic models was intractable, because proving the convergence of many IoT devices playing a collaborative game, without communication nor coordination is hard, when they all follow random active pattern. The rest of this manuscript thus studies two restricted models, first multi-players bandits in stationary problems, then non-stationary single-player bandits. We also detail another contribution, SMPyBandits, our open-source Python library for numerical MAB simulations, that covers all the studied models and more.

#### Keywords
Internet of Things (IoT), Cognitive Radio, Learning Theory, Collision Mitigation Sequential Learning, Reinforcement Learning, Multi-Armed Bandits (MAB), Decentralized Learning, Multi-Player Multi-Armed Bandits, Change Point Detection, Non-Stationary Multi-Armed Bandits.

---

### 🇫🇷 En français
#### Titre
**Algorithmes de Bandits Multi-Joueurs pour les Réseaux de l'Internet des Objets**.

#### Résumé
Dans cette thèse de doctorat, nous étudions les réseaux sans fil et les appareils reconfigurables qui peuvent accéder à des réseaux de type radio intelligente, dans des bandes non licenciées et sans supervision centrale.
Nous considérons des réseaux actuels ou futurs de l'Internet des Objets (IoT), avec l'objectif d'augmenter la durée de vie de la batterie des appareils, en les équipant d'algorithmes d'apprentissage machine peu coûteux mais efficaces, qui leur permettent d'améliorer automatiquement l'efficacité de leurs communications sans fil.
Nous proposons deux modèles de réseaux IoT, et nous montrons empiriquement, par des simulations numériques et une validation expérimentale réaliste, le gain que peuvent apporter nos méthodes, qui se reposent sur l'apprentissage par renforcement.
Les différents problèmes d'accès au réseau sont modélisés avec des Bandits Multi-Bras (MAB), mais leur analyse est difficile à réaliser,
car il est délicat de prouver la convergence d'un grand nombre d'appareils jouant à un jeu collaboratif sans communication ni aucune coordination, lorsque les appareils suivent tous un modèle d'activation aléatoire.
Le reste de ce manuscrit étudie donc deux modèles restreints, d'abord des bandits multi-joueurs dans des problèmes stationnaires, puis des bandits mono-joueur non stationnaires.
Nous détaillons également une autre contribution, la bibliothèque Python open-source SMPyBandits, qui permet des simulations numériques de problèmes MAB, qui couvre les modèles étudiés et d'autres.

#### Mot clés
Internet des Objets (IoT), Radio Intelligente, Théorie de l'apprentissage, Apprentissage séquentiel de l'atténuation des collisions, Apprentissage par renforcement, Bandits multi-bras (MAB), Apprentissage décentralisé, Bandits multi-bras multi-joueurs, Détection des points de changement, Bandits multi-bras non stationnaires.

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
- 😭 I didn't succeed in finding the correct options to the [pdfx](https://www.ctan.org/pkg/pdfx) LaTeX package (not like [Jill-Jênn Vie](https://github.com/jilljenn/phd/)) to compile my thesis to a PDF/A archivable PDF.
- But I managed to fix my PDF and make it a PDF/A archivable document by using the online service hosted online by [Facile.Cines.fr](https://facile.cines.fr/#correction).

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
