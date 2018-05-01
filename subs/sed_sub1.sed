#!/usr/bin/sed -nfe

s/<font\ color[=#A-Za-z0-9]*>//g
s/\[\([^]]*\)\]//g
s/[A-Z:]*<\/font>//g

s/<i>//g
s/<\/i>//g
s/^[0-9:,\ ->]*//
/^\s$/d

p
