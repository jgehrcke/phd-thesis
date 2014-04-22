#!/bin/bash

biber main
lualatex --interaction=nonstopmode --output-format=pdf main.tex

#if [ $? -eq 0 ]; then
#    okular main.pdf
#fi


