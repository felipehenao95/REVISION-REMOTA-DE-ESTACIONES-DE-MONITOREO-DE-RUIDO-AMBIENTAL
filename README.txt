REMOTE REVIEW OF ENVIRONMENTAL NOISE MONITORING STATIONS

These programs are designed to carry out a remote review of different sound level meters that have wireless data transmission through a 3G internet module, which allows establishing an IP for each sound level meter in the network, through these IP's the program connects to each sound level meter and using HTTP commands, the necessary information is obtained to verify the correct operation of the equipment, data such as: the equipment load percentage, available space in the SD memory, equipment signal, measurement status and general observations such as electrical  check failures or acoustic overloads.

For the correct execution of the program, BEFORE the Internet connection must be deactivated (either by WIFI or Ethernet connection) and a USB modem must be connected, which must have the access credentials to the IP's of the monitoring network. Next, the step by step for the correct execution of the program is presented:

1. Execute the "automatic_check.py" file: this script will take the "IP_Estaciones.csv" file located in the same folder where the .py executable is located. Said Excel file stores the IP's of each sound level meter, once run the script, in the terminal of the IDE that is being used, it will tell us if the station connected or not connected remotely. Once the program has finished reviewing all the stations, an Excel file "non_connected.csv" will be created which stores the IP's of the sound level meters that did not connect in the current review.

2. Run the "automatic_check_non_conn.py" file: this script basically performs the same check as "automatic_check.py", but this executable defaults to the "non_connected.csv" file generated in the previous step, in order to perform a remote review again only for the stations that did not connect in the first review (step 1).

----------------------------------------------------------------------------------------------------------------------------------

REVISIÓN REMOTA DE ESTACIONES DE MONITOREO DE RUIDO AMBIENTAL

Estos programas están diseñados para realizar una revisión remota de distintos sonómetros que cuentan con una trasmisión de datos inalámbrica mediante un módulo de internet 3G, lo cual permite establecer una IP a cada sonómetro de la red. Mediante estas IP's el programa se conecta a cada sonómetro y haciendo uso de comandos HTTP se obtiene la información necesaria para verificar el correcto funcionamiento del equipo, datos como: el porcentaje de carga del equipo, espacio disponible en la memoria SD, señal del equipo, estado de medición y observaciones generales como fallas en chequeo eléctrico o sobrecarga acústica.

Para la correcta ejecución del programa, ANTES se debe desactivar la conexión a internet (ya sea por conexión WIFI o Ethernet) y se debe conectar un modem USB el cual debe contar con las credenciales de acceso a las IP's FIJAS de la red de monitoreo. a continuación, se presenta el paso a paso para la ejecución del programa:

1. Ejecutar el archivo "automatic_check.py": este script va a tomar el archivo "IP_Estaciones.csv" ubicado en la misma carpeta donde se encuentra el ejecutable .py, dicho archivo de Excel almacena las IP's de cada sonómetro, una vez se ejecute el script, en la terminal del IDE que se esté usando, nos indicara si la estación conecto o no conecto de forma remota. Una vez el programa haya terminado de revisar todas las estaciones, se creará un archivo de Excel "non_connected.csv" el cual almacena las IP's de los sonómetros que no conectaron en la revisión actual. 

2. Ejecutar el archivo "automatic_check_non_conn.py": este script básicamente realiza la misma revisión del "automatic_check.py", pero este ejecutable toma por defecto el archivo "non_connected.csv" generado en el paso anterior, para así, nuevamente realizar una revisión remota únicamente para las estaciones que no conectaron en la primera revisión (paso 1).
