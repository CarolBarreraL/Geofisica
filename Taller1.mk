IMAGENES = AEsfera.pdf ACilindro.pdf ALosa.pdf
erase = rm -r -f *.log *.aux 

taller1.pdf: taller1.tex $(IMAGENES)
	pdflatex taller1.tex
	$(erase)

taller1.tex: taller1.py
	python taller1.py
