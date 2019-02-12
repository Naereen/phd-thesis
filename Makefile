# Quick Makefile to compile easily the report (make pdf)
FILE = PhD_thesis__Lilian_Besson
IN   = $(FILE).tex
OUT  = $(FILE).pdf

quick:	pdf
all:	clean pdf evince clean
pdf:	$(OUT)

.PHONY:	quick all pdf evince compress clean send_zamok latexstats lint proselint

.SUFFIXES:
.SUFFIXES: .md .tex .pdf

# Construction rules
.md.pdf:
	pandoc --verbose --include-in-header header.tex -s -t latex -o $@ $<
	-evince $@ >/dev/null 2>/dev/null &

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
	-mv -vf *.fls *.fdb_latexmk *.ps *.dvi *.htoc *.tms *.tid *.lg *.log *.id[vx] *.vrb *.toc *.snm *.nav *.htmp *.aux *.tmp *.out *.haux *.hidx *.bbl *.blg *.brf *.lof *.ilg *.ind *.meta *.fdb_latexmk *.fls *.synctex*busy* *.loa *.lof *.lot *.maf *.mtc* *.nlo /tmp/ 2>/dev/null

# Sender
send_zamok:
	CP $(OUT) besson@zamok.crans.org:~/www/phd/articles/.$(OUT)

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
