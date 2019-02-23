all: 12.png 13.png 32.png 34.png 64.png 68.png assignment.pdf

12.png : npcomputerxy.py
	python npcomputerxy.py 1 2 1 1 0 0.001 10000

13.png : npcomputerxy.py
	python npcomputerxy.py 1 3 1 1 0 0.001 10000

32.png : npcomputerxy.py
	python npcomputerxy.py 3 2 1 1 0 0.001 10000

34.png : npcomputerxy.py
	python npcomputerxy.py 3 4 1 1 0 0.001 10000

64.png : npcomputerxy.py
	python npcomputerxy.py 6 4 1 1 0 0.001 10000

68.png : npcomputerxy.py
	python npcomputerxy.py 6 4 1 1 0 0.001 10000

assignment.pdf : main.tex
	pdflatex main.tex