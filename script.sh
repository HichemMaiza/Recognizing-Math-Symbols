#!/bin/bash 


for i in *.inkml
do 
	base=$( basename $i .inkml)
	mkdir $base
	python3 test.py $i
	for j in $i*
	do
	mv $j $base/$j
	done
done 

