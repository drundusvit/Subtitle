#!/bin/sh
i=$(grep -c '^[^A-Z\.\"\-]' $1)
while [ "$i" -gt "10" ]; do
sed  -e 's/[^\.\?\"\!]$/&#/' -i -e '/#$/ {N;s/#\n/\ /}' $1
i=$(grep -c '^[^A-Z\.\"\-]' $1)
echo $i
done
grep -i -o -f idioms/idioms_homeenglish.ru_en_reg.txt $1 | sed -e 's/^\ //' -e 's/^\s$//' | sort -f | uniq > $1.idioms.txt
