touch netsize_all.txt

for archivo in *.txt;
do
	number_files=`cat $archivo |wc -l`
	number_columns=`head - n 1 $archivo | tr -d " "| tr -d "\n" | wc -c`
	echo "$archivo $number_files, $archivo $number_columns" >> netsize_all.txt
done

