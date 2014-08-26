#!/bin/bash

gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
    -dFirstPage=6 -dLastPage=7 \
    -sOutputFile=p6p7.pdf ../latexproject/main.pdf



pdftk p5-nofont-inkscape-annotated_01.pdf p6p7.pdf output summary.pdf

