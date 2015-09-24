#!/bin/sh
echo '[' >./initial_data.json
cat ./import.csv |tr -d \" |awk -F"," ' { print " {\"pk\":" NR ", \"model\": \"showbase.podotchet\", \"fields\": {\"date_now\": \"2014-04-24\", \"comment\": \"\", \"inv_number\": \""$1"\" , \"list_t\": 1, \"price\": null, \"person\": \"\", \"place\": \"\", \"name_el\": \""$2"\", \"date_inv\": null, \"author\": 1, \"inv\": false }}, " } ' >>./initial_data.json
echo ']'>>./initial_data.json
rm ../db/1.db
cp ./initial_data.json ../fixtures/initial_data.json
#python ../manage.py migrate
#python ../manage.py createsuperuser