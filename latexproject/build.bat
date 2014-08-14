
biber main
lualatex --interaction=nonstopmode --output-format=pdf main.tex
makeindex -s nomencl.ist -t main.nlg -o main.nls main.nlo

