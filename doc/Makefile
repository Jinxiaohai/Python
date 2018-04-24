EXE=learnPython.pdf
SRC=learnPython.tex
BIB=learnPython.aux

$(EXE):$(SRC)
	xelatex $(SRC)

.PHONY.:look
look:
	evince learnPython.pdf

.PHONY.:clean
clean:
	$(RM) learnPython.aux learnPython.log learnPython.dvi learnPython.bbl learnPython.blg learnPython.toc learnPython.out learnPython.nav learnPython.snm learnPython.thm learnPython.lot learnPython.lof
