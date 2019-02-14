# Quick Makefile to compile easily the report (make pdf)
SHELL=/usr/bin/env /bin/bash
FILE = PhD_thesis__Lilian_Besson
IN   = $(FILE).tex
OUT  = $(FILE).pdf

all:	clean pdf evince clean
quick:	pdf
pdf:	$(OUT)

.PHONY:	quick all pdf evince compress clean send_zamok latexstats lint proselint

.SUFFIXES:
.SUFFIXES: .tex .pdf

# Construction rules
.tex.pdf:
	latexmk -pdflatex="pdflatex --shell-escape %O %S" -pdf $<
	-pdfinfo $@ | grep -v ':[ \t]\+no' | grep --color=always "^[A-Za-z ]\+:"
	-evince $@ >/dev/null 2>/dev/null &

# Utility for the PDF
evince:
	-evince $(OUT) &

compress:
	PDFCompress $(OUT)

# Cleaner
clean:
	-mv -vf *.fls *.fdb_latexmk *.ps *.dvi *.htoc *.tms *.tid *.lg *.log *.idv *.idx *.vrb *.toc *.snm *.nav *.htmp *.aux *.aex *.tmp *.out *.haux *.hidx *.bbl *.blg *.brf *.lof *.ilg *.ind *.meta *.fdb_latexmk *.fls *.synctex*busy* *.loa *.lof *.lot *.lol *.maf *.mtc* *.nlo *.nls /tmp/ 2>/dev/null

# Sender
send_zamok:
	CP $(OUT) besson@zamok.crans.org:~/www/phd/articles/.$(OUT)

bib2html:
	bibtex2html -s mybibstyle.bst -u -charset utf-8 -linebreak *.bib

bib2txt:	bib2html
	html2text all-phd-thesis.html | head -n-2 > all-phd-thesis.txt

stats:
	-echo "\nCommit stats :" | tee ./complete-stats.txt
	+git-complete-stats.sh   | tee -a ./complete-stats.txt
	-echo "\nCalendar :"     | tee -a ./complete-stats.txt
	-git-cal --ascii         | tee -a ./complete-stats.txt
	git wdiff ./complete-stats.txt

cloudwords:
	-generate-word-cloud.py -s -m 180 -t "Words from LaTeX sources - PhD Thesis - (C) 2016-2019 Lilian Besson" ./*.tex ./*/*.tex ./*/*/*.tex
	generate-word-cloud.py -f -o cloudwords_latex_sources.png -m 180 -t "Words from LaTeX sources - PhD Thesis - (C) 2016-2019 Lilian Besson" ./*.tex ./*/*.tex ./*/*/*.tex
	-generate-word-cloud.py -s -m 180 -t "Words from Python code - PhD Thesis - (C) 2016-2019 Lilian Besson" ~/SMPyBandits.git/*.py ~/SMPyBandits.git/*/*.py ~/SMPyBandits.git/*/*/*.py ~/SMPyBandits.git/*/*/*/*.py
	generate-word-cloud.py -f -o cloudwords_python_code.png -m 180 -t "Words from Python code - PhD Thesis - (C) 2016-2019 Lilian Besson" ~/SMPyBandits.git/*.py ~/SMPyBandits.git/*/*.py ~/SMPyBandits.git/*/*/*.py ~/SMPyBandits.git/*/*/*/*.py


# Linters!
latexstats:
	latexstats.sh $(IN)
	latexstats.sh $(IN) | sed -r "s:\x1B\[[0-9;]*[mK]::g" > latexstats.txt

lint:	write-good.sh write-good

proselint:
	time proselint $(IN) | tee proselint_report.txt

write-good:
	time write-good --no-passive --no-weasel --no-tooWordy --no-adverb $(IN) | tee writegood_report.txt

write-good.sh:
	time write-good.sh $(IN) | tee writegood_sh_report.txt
