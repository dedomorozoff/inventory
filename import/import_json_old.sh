#!/bin/sh
echo '['
cat ./import.csv |tr -d \" |awk -F"," ' { print " \{\"pk\"\:" NR ", \"model\"\: \"showbase.podotchet\", \"fields\"\: \{\"date_now\"\: \"2014-04-24\", \"comment\"\: \"\", \"inv_number\"\: \""$1"\" , \"list_t\"\: 1, \"price\"\: null, \"person\"\: \"\", \"place\"\: \"\", \"name_el\"\: \""$2"\", \"date_inv\"\: null, \"author\"\: dedo, \"inv\"\: \"False\" \}\}\,\ " } '
echo ']'