#!/bin/sh
python3 i0sn_generator0.0.1.py -color="Green" -pdate='2018-01-19' -sku='B' -num=1000 -vendor='Meomo'
python3 i1sql_generator0.0.1.py
python3 i2combine_img.py
