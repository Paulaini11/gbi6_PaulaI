#! /bin/bash
touch clase_for.txt
for i in $1
do
	x=`wc $i` # Impresion del nombre de fila
	echo "Archivo: $i, filas: $x" >> clase_for.txt # se esta guardando en un archivo txt
done
