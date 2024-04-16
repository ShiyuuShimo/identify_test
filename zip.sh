#!/bin/sh

# clean up output file
rm list.txt
touch list.txt

rm -rf output
mkdir output

# zip text file
for i in {1..5}
do
	zip ${i}.zip ${i}.txt

	size_t=`wc -c < ${i}.txt`
	size_t=${size_t// /}
	size_z=`wc -c < ${i}.zip`
	size_z=${size_z// /}

	echo "'t${i}.txt': ${size_t}" >> list.txt
	echo "'z${i}.zip': ${size_z}" >> list.txt

	# create merged text file and zip them
	for j in {1..5}
	do
		#if [ ${i} != ${j} ] ; then
			cat output/${i}${j}.txt ${i}.txt ${j}.txt >> output/${i}${j}.txt
			zip output/${i}${j}.zip output/${i}${j}.txt

			size_t=`wc -c < output/${i}${j}.txt`
			size_t=${size_t// /}
			size_z=`wc -c < output/${i}${j}.zip`
			size_z=${size_z// /}

			echo "'t${i}${j}.txt': ${size_t}" >> list.txt
			echo "'z${i}${j}.zip': ${size_z}" >> list.txt
		#fi
	done
done