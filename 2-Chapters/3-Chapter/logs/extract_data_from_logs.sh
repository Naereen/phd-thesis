#!/usr/bin/env bash
set -euo pipefail

texoutput=chapter3.tex
cp -vf ../$texoutput ./$texoutput

DEBUG=True
NOPLOTS=False
SAVEALL=False
N_JOBS=4
nbplayer=16

declare -i n_i
declare -i n_b
declare -i n_t
declare -i n_k

n_i=0
for N in 40 100 1000; do
    n_i+=1
    n_b=0
    for BAYES in False True; do
        n_b+=1
        n_t=0
        for T in 1000 5000 10000 50000; do
            n_t+=1
            n_k=0
            for K in 2 5 10 20 50; do
                n_k+=1
                log_file=main_py3_log__N${N}_BAYES${BAYES}_T${T}_K${K}__$(date +"%d-%m-%Y_%H-%M-%S").txt
                for n in $(seq 1 ${nbplayer}); do
                    grep "R^{${n}} = [0-9\.]* pm [0-9\.]*" $log_file
                    echo sed -i.backup s/"R^{${n}} = [0-9\.]* pm [0-9\.]*"/"R^{${n}} = [0-9\.]* pm [0-9\.]*"/g ./$texoutput
                    grep "M^{${n}} = [0-9\.]* pm [0-9\.]*" $log_file
                    grep "T^{${n}} = [0-9\.]* pm [0-9\.]*" $log_file
                done;
                # R^{[0-9\.]*}_{T=${T},K=${T}} = [0-9\.]* pm [0-9\.]*
                # R^{9}_{T_${n_t},K_${n_k}} = 0 \pm 0
                # ==>
                # R^{9}_{T_3,K_1} = 0 \pm 0
                # sed -i.backup s/''/''/g ./$texoutput
            done
        done
    done
done

cp -vf ./$texoutput ../$texoutput