Projecto pensado para monitorear archivos

cuenta con una parte Front y una back.

## Front

Es un script que se instala en el cliente
se debe configurar los archivos  que debe monitorear

Luego se debe crear una tarea programada cada X tiempo para correr y ejecutar el script.

Dicho script informa al servidor el estado de los archivos seleccionados.

## Back

Es un sistema realizado en django que recibe información y la muestra.

Realiza calculos para ver al antiguedad del archivo y que se puedan tomar acciones correctivas
