#!/bin/sh
sed -nf change.sed $1 | col -b | sort | uniq | grep -Fxv -f slovar.txt
