#!/bin/bash
FILE=$1;
while read line; do
	echo $line;
	echo -e $(sdcv -u "English-Russian full dictionary" -n $line | tail -n +6 | sed -e 's/\*/\~/g' -e 's/$/\\n/');
	echo \ ;
	read -n 1 C < /dev/tty
	echo \ ;
	case "$C" in
		d)	sed -i "/^$line$/d" $1 ;;
		o)	echo \"$line >> $1.anki.txt; echo -e $(sdcv -u "English-Russian full dictionary" -n $line | tail -n +6 | sed -e 's/\(]\)\ /\]\"\#\"/' -e 's/\*/\~/g' -e "$ s/$/\"/" -e 's/$/\\n/') >> $1.anki.txt; sed -i "/^$line$/d" $1 ;;
	esac 
done < $FILE
 #sdcv -u "English-Russian full dictionary" -n perjury | tail -n +6
