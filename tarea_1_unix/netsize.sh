file=`wc -l < n44.txt`
columns=`awk "{print NF}" n44.txt |head -n 1`

echo "El numero de filas y columnas es: $file, $columns" >> netsize.txt

