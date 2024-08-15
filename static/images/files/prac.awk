#!/usr/bin/gawk
BEGIN {
  FS = ":"
  i = 1
}

{
  print $1 >> "passwd.txt"
}

END {
  
}

