#!/usr/bin/env bash
set -euo pipefail

DEBUG=False
NOPLOTS=False
SAVEALL=True
N_JOBS=-1

declare -i nbexperiment
nbexperiment=0

for N in 1000; do
# for N in $N_JOBS; do
    # for BAYES in False True; do
    # for BAYES in False; do
    for BAYES in True; do
        # for T in 1000 2500 5000 10000 20000 25000 50000; do
        for T in 5000; do
            # for K in 2 4 8 12 16 20 32; do
            # for K in 2 4 8; do
            for K in 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32; do
                debut=$(date)
                nbexperiment+=1

                DEBUG=$DEBUG NOPLOTS=$NOPLOTS SAVEALL=$SAVEALL N_JOBS=$N_JOBS \
                N=$N T=$T K=$K BAYES=$BAYES mymake.sh --noFreeSMS single \
                && cp -f logs/main_py3_log.txt \
                    logs/main_py3_log__N${N}_BAYES${BAYES}_T${T}_K${K}__$(date +"%d-%m-%Y_%H-%M-%S").txt \
                && FreeSMS.py "Expérience #${nbexperiment}, commencée ${debut}, terminée ! Avec N=${N}, BAYES=${BAYES}, T=${T}, K=${K}."
            done
        done
        # for T in 15000 30000 35000 40000 45000; do
        # for T in 10000; do
        for T in 1000 2000 5000 10000 15000 20000 25000 30000 35000 40000 45000 50000; do
            # for K in 2 4 8 12 16 20 32; do
            for K in 8; do
            # for K in 6 10 14 18 22 24 26 28 32; do
            # for K in 2 4 8; do
                debut=$(date)
                nbexperiment+=1

                DEBUG=$DEBUG NOPLOTS=$NOPLOTS SAVEALL=$SAVEALL N_JOBS=$N_JOBS \
                N=$N T=$T K=$K BAYES=$BAYES mymake.sh --noFreeSMS single \
                && cp -f logs/main_py3_log.txt \
                    logs/main_py3_log__N${N}_BAYES${BAYES}_T${T}_K${K}__$(date +"%d-%m-%Y_%H-%M-%S").txt \
                && FreeSMS.py "Expérience #${nbexperiment}, commencée ${debut}, terminée ! Avec N=${N}, BAYES=${BAYES}, T=${T}, K=${K}."
            done
        done
    done
done
