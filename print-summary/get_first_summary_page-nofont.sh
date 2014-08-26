#!/bin/bash

gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER \
    -dFirstPage=5 -dLastPage=5 \
    -sOutputFile=p5.pdf ../latexproject/main.pdf

# Now the first page of the summary is isolated and can be edited
# (annotated) in e.g. Inkscape. However, in order to prevent font
# rendering issues, convert all glyphs in the PDF to paths (outlines).
# That significantly increases the file size, but guarantees that
# no information is lost.
./text_to_outlines.sh p5.pdf

# Now proceed editing that page, save it as a new PDF, and then
# combine it with the remaining pages of the summary.

