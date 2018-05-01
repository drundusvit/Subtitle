#!/bin/bash

FILE=$1
while read line; do
	echo $line;
	#echo "$(sdcv -n -u mueller $line | grep '^\[')";
	 (read -n 1 B
	 echo \ ;
	 echo \ ;
	 echo \ ;
	 echo \ ;
	 	case "$B" in
        		d)       sed -i "/^$line$/d" $1 ;;
        		n)       echo $line >> /home/damir/Загрузки/script/slovar.txt;  sed -i "/^$line$/d" $1;;
			*)	 echo $line >> $1.unk.txt; sed -i "/^$line$/d" $1;;
		esac
	) < /dev/tty
done < $FILE




