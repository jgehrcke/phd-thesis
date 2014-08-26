#!/bin/bash

gs -sDEVICE=pswrite -dNOCACHE -sOutputFile=- -q -dbatch -dNOPAUSE -dQUIET "$1" -c quit | ps2pdf - "`echo $1 | cut -f1 -d'.'`"-nofont.pdf

