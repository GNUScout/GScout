#
# Makefile for Latex
##

LATEX=latex
PDFLATEX=pdflatex

main=memtfg.tex
mainsin=$(main:.tex=)
pdf=$(main:.tex=.pdf)
bbl=$(main:.tex=.bbl)
bib=$(wildcard *.bib)
imgs=$(wildcard img/pdf/*.pdf img/png/*.png img/eps/*.eps)
sources=$(wildcard *.tex)

all: $(pdf)

$(dvi): $(main) $(bbl) $(imgs) $(sources)
	$(LATEX) $(mainsin)
	$(LATEX) $(mainsin) 

$(bbl): $(bib) $(src) $(sources)
	$(PDFLATEX) $(mainsin)
	bibtex $(mainsin)

$(pdf): $(main) $(bbl) $(imgs) $(sources)
	$(PDFLATEX) $(mainsin)
	$(PDFLATEX) $(mainsin)

clean:
	rm -rf *.log *.out *.aux *.dvi *.bbl *.blg *-diff.*

mrproper:
	$(MAKE) clean && rm -rf *~ *.backup $(pdf)

diff:
		latexbatchdiff $(main) $(sources)

