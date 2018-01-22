#!/bin/sh
python3 i0sn_generator0.0.1.py -color="Green" -pdate='2018-01-22' -sku='B' -num=13 -vendor='Meomo'
python3 i1sql_generator0.0.1.py
python3 i2combine_img.py
