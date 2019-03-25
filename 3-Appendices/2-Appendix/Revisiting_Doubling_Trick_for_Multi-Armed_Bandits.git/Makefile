# Makefile for a research article with simple latexmk compilation
main:	pdf
pdf:
	latexmk -gg -pdf Revisiting_Doubling_Trick_for_Multi-Armed_Bandits.tex

note:
	latexmk -gg -pdf A_note_on_the_Ei_function.tex

rebuttal:
	latexmk -gg -pdf Rebuttal_COLT_Paper_177.tex

clean:
	latexmk -c
	rm -vf *.bbl *.synctex.gz *.loa

latexstats:
	+rm -vf latexstats.txt
	latexstats.sh | tee latexstats.txt
