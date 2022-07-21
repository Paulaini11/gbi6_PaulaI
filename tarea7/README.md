# **Bioinformatica** 
![Image text](https://github.com/Paulaini11/gbi6_PaulaI/blob/main/tarea6/descarga.png) 

### Datos del estudiante 
- Paula Iñiguez 
- 23 años
### Datos del equipo 
Nombre del dispositivo	DESKTOP-4UHLUS9
Procesador	Intel(R) Core(TM) i5 CPU       M 460  @ 2.53GHz   2.53 GHz
RAM instalada	4.00 GB (3.86 GB utilizable)
Id. del dispositivo	BDA64E05-3CD2-4A57-B563-76CC3EFD9E20
Id. del producto	00331-10000-00001-AA298
Tipo de sistema	Sistema operativo de 64 bits, procesador x64
Lápiz y entrada táctil	La entrada táctil o manuscrita no está disponible para esta pantalla
## Detalles de la tarea 
- Se creo el cuaderno de  t7_iris.ipynb. 
- Cargue la data "iris.csv"
- Calcule la media y desviación estandar para 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'. 
- utilice lo siguiente para calcular la media y la desviacion 
lista = []
for i in range(1, 5, 1):
    colsec = data.iloc[:,i] #se escoge la columna i
    media = colsec.mean() #calculas la media de la columna i
    sd = np.std(colsec) #calculas la desviacion estandar en la columna i
    lista.append([media,sd]) #agrego media y desviacion estandar a la lista llamada lista
print(lista)

- Utilice las medias y desviaciones estandar para crear una data de distribución normal.
- Grafique las curvas de distribución normal donde se tenga colors y leyendas para cada tipo de variable.  
- Cree un repositorio en GitHub de nombre tarea7 y guardar los dos archivos de la tarea. 
