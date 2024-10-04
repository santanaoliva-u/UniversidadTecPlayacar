
## Reporte de configuracion de punto a punto
	 
#### Configuracion de punto a punto 

### **Material Necesario:**
- **2 Computadoras** con puertos Ethernet.
- **1 Cable Ethernet** (de categoría CAT5 o superior). Asegúrate de que el cable tenga conectores RJ45 en ambos extremos.

### **Paso 1: Preparación del Cable**
#### a) Tipo de Cable
- **Cable Directo:** Es el más utilizado actualmente ya que la mayoría de las computadoras modernas soportan *Auto-MDIX*. Esto significa que el cable puede funcionar correctamente sin importar la disposición de los hilos internos.
- **Cable Cruzado:** Se utiliza en casos donde al menos una de las computadoras no soporta *Auto-MDIX*. Este tipo de cable invierte el orden de algunos hilos para permitir la comunicación directa.

Si no estás seguro de si tus computadoras soportan *Auto-MDIX*, utiliza un cable cruzado.

### **Paso 2: Conexión del Cable**
1. **Inserta un extremo del cable RJ45** en el puerto Ethernet de la primera computadora.
2. **Inserta el otro extremo del cable** en el puerto Ethernet de la segunda computadora.
3. Verifica que las luces de los puertos Ethernet se enciendan. Esto indica que la conexión física está establecida correctamente.

### **Paso 3: Configuración de Red Manual desde la Terminal**

#### **Para Sistemas Linux:**

##### 1. **Identificar la interfaz de red**
   - Abre la terminal y escribe:
     ```bash
     ifconfig
     ```
     o
     ```bash
     ip a
     ```
   - Encuentra el nombre de tu interfaz Ethernet (por ejemplo, `eth0`, `enp0s3`, etc.).

##### 2. **Configurar la primera computadora:**
   - Ejecuta el siguiente comando para asignar una dirección IP:
     ```bash
     sudo ifconfig eth0 192.168.1.1 netmask 255.255.255.0 up
     ```
   - Reemplaza `eth0` por el nombre de tu interfaz si es diferente.

##### 3. **Configurar la segunda computadora:**
   - En la terminal de la segunda computadora, asigna otra dirección IP:
     ```bash
     sudo ifconfig eth0 192.168.1.2 netmask 255.255.255.0 up
     ```

#### **Para Windows:**

1. Presiona `Windows + R`, escribe `cmd` y presiona Enter para abrir la terminal.
2. En la primera computadora, escribe:
   ```bash
   netsh interface ip set address name="Ethernet" static 192.168.1.1 255.255.255.0
   ```
3. En la segunda computadora, escribe:
   ```bash
   netsh interface ip set address name="Ethernet" static 192.168.1.2 255.255.255.0
   ```

#### **Para macOS:**

1. Abre la Terminal (`Aplicaciones > Utilidades > Terminal`).
2. Para la primera computadora, ingresa:
   ```bash
   sudo ifconfig en0 192.168.1.1 netmask 255.255.255.0 up
   ```
3. En la segunda computadora, ingresa:
   ```bash
   sudo ifconfig en0 192.168.1.2 netmask 255.255.255.0 up
   ```
   *Nota: Reemplaza `en0` si tu interfaz tiene otro nombre.*

### **Paso 4: Comprobación de la Conexión**

1. En la terminal de la primera computadora, realiza un *ping* a la segunda computadora:
   ```bash
   ping 192.168.1.2
   ```
2. En la terminal de la segunda computadora, realiza un *ping* a la primera computadora:
   ```bash
   ping 192.168.1.1
   ```
   
   ¡Entendido! A continuación, he elaborado un documento detallado para tu proyecto de conexión punto a punto utilizando el cable RJ45, abarcando todos los puntos que mencionaste.

---

## **Conexión Punto a Punto Usando Cable RJ45 – Guía Detallada**

### **Materia:**  
Redes y Comunicaciones

### **Integrantes:**
- [Tu nombre u otros integrantes]

### **Nombre del Docente:**
- [Nombre del docente]

### **Lugar y Fecha:**
- [Lugar y fecha donde se realizó la práctica]

---

### **Marco Teórico**
La configuración de una conexión punto a punto es una práctica fundamental en redes de comunicación que permite el intercambio de datos entre dos dispositivos sin la necesidad de un intermediario como un switch o un router. Este tipo de conexión resulta ideal para transferencias rápidas de archivos, configuración de redes privadas o para compartir recursos entre dos computadoras.

Para este ejercicio, utilizamos el cable Ethernet con conectores RJ45, siguiendo la topología de red punto a punto. En este proceso, abordamos tanto la configuración física (conexión del cable) como la configuración lógica (asignación de direcciones IP y el intercambio de datos).

### **Herramientas Utilizadas**
1. **Cable Ethernet CAT5 (o superior) con conectores RJ45:** Permite la transmisión de datos entre ambas computadoras.
2. 
3. **2 Computadoras:** Ambas con puertos Ethernet operativos.
4. **Terminal (para Linux/macOS) o Símbolo del Sistema (para Windows):** Utilizado para configurar la red manualmente y comprobar la conexión.
5. **Software para compartir archivos:** Para verificar la transferencia de datos entre las computadoras.

---

### **Conceptos Usados en la Práctica**

#### **Cable RJ45**
El RJ45 es el conector estándar utilizado para cables de red Ethernet. Permite conectar dispositivos a una red, y en nuestro caso, es el medio físico que facilita la comunicación entre dos computadoras.

#### **Comandos Utilizados:**
- `ifconfig`: En sistemas Linux/macOS, este comando configura la dirección IP y la máscara de subred.
- `ping`: Utilizado para verificar la conectividad entre dos dispositivos.
- `netsh`: En Windows, este comando configura los parámetros de red.

#### **Topología de Red Punto a Punto**
Se refiere a una conexión directa entre dos dispositivos, en la que cada dispositivo actúa tanto como cliente como servidor. Esto garantiza que ambos puedan compartir y recibir datos sin la necesidad de un dispositivo intermedio.

---

### **Descripción del Procedimiento**

#### **1. Preparación del Cable y Conexión Física**
Para empezar, seleccionamos un cable Ethernet CAT5 con conectores RJ45 en ambos extremos. Confirmamos que era un cable cruzado, lo cual es necesario si nuestras computadoras no tienen la función *Auto-MDIX*. En caso de que ambas computadoras soporten *Auto-MDIX*, podríamos utilizar un cable directo sin problemas.

1. Primero, verificamos el estado del cable, asegurándonos de que los conectores RJ45 estaban en buen estado.
2. Conectamos un extremo del cable a la computadora 1 y el otro extremo a la computadora 2. En ambos casos, confirmamos que las luces de los puertos Ethernet se encendieron, indicando que la conexión física estaba establecida.

#### **2. Configuración Lógica – Asignación de Direcciones IP**

##### **En la Computadora 1:**
- Abrimos la terminal y ejecutamos el comando:
  ```bash
  sudo ifconfig eth0 192.168.1.1 netmask 255.255.255.0 up
  ```
  Este comando asigna la dirección IP `192.168.1.1` a la interfaz `eth0` y establece la máscara de subred `255.255.255.0`. 

##### **En la Computadora 2:**
- De igual forma, abrimos la terminal y ejecutamos:
  ```bash
  sudo ifconfig eth0 192.168.1.2 netmask 255.255.255.0 up
  ```
  Asignando así la dirección IP `192.168.1.2`.

%3E Nota: En sistemas Windows, la configuración se realizó de la siguiente manera:
>
> - Computadora 1:  
>   ```bash
>   netsh interface ip set address name="Ethernet" static 192.168.1.1 255.255.255.0
>   ```
> - Computadora 2:  
>   ```bash
>   netsh interface ip set address name="Ethernet" static 192.168.1.2 255.255.255.0
>   ```

#### **3. Comprobación de la Conexión**
- En la terminal de la computadora 1, ejecutamos:
  ```bash
  ping 192.168.1.2
  ```
  y en la computadora 2:
  ```bash
  ping 192.168.1.1
  ```
Ambos comandos respondieron correctamente, confirmando la conexión.

#### **4. Configuración para Compartir Archivos**
##### **En Windows:**
1. Abrimos el "Centro de redes y recursos compartidos."
2. Seleccionamos "Cambiar configuración de uso compartido avanzado."
3. Activamos "Habilitar la detección de redes" y "Habilitar el uso compartido de archivos e impresoras."
4. Desde el explorador de archivos, seleccionamos la carpeta a compartir, clic derecho → "Propiedades" → pestaña "Compartir" → "Uso compartido avanzado," y configuramos los permisos.

##### **En Linux:**
- Instalamos `samba` usando:
  ```bash
  sudo apt install samba
  ```
- Configuramos el archivo `/etc/samba/smb.conf` y agregamos:
  ```bash
  [Compartido]
  path = /ruta/de/la/carpeta
  available = yes
  valid users = nombre_usuario
  read only = no
  browsable = yes
  public = yes
  writable = yes
  ```

---

### **Resultados Obtenidos**
Tras completar la configuración, logramos la conexión exitosa entre ambas computadoras. Pudimos compartir archivos y datos directamente, comprobando la transferencia eficiente a través de la red punto a punto. Los comandos `ping` confirmaron la conectividad sin pérdida de paquetes, y las carpetas compartidas fueron accesibles desde ambas computadoras.

### **Posibles Errores y Soluciones**
1. **Problemas de conexión física:** Asegurarnos de que el cable RJ45 esté bien conectado en ambos puertos.
2. **Configuración incorrecta de IP:** Confirmar que las IPs asignadas estén en la misma subred (ejemplo: `192.168.1.x`).
3. **Conflictos de firewall:** Desactivar temporalmente el firewall para comprobar la conectividad.

---

### **Conclusión**
La realización de la conexión punto a punto utilizando un cable Ethernet RJ45 nos permitió comprender la importancia de las configuraciones físicas y lógicas en la comunicación de redes. Fue posible observar cómo dos computadoras pueden interactuar de forma directa y eficiente, sin intermediarios. También aprendimos a configurar manualmente las direcciones IP y a compartir recursos, lo que refuerza los fundamentos de la creación y administración de redes pequeñas.

### **Recomendaciones**
- Utilizar cables de calidad y verificar su estado antes de la conexión.
- Tener conocimientos básicos de comandos de red en la terminal para una configuración más rápida.
- Documentar cada paso durante la configuración para facilitar la solución de problemas en el futuro.](<¡Entendido! A continuación, he elaborado un documento detallado para tu proyecto de conexión punto a punto utilizando el cable RJ45, abarcando todos los puntos que mencionaste.

---

## **Conexión Punto a Punto Usando Cable RJ45 – Guía Detallada**

### **Materia:**  
Redes y Comunicaciones

### **Integrantes:**
- [Tu nombre u otros integrantes]

### **Nombre del Docente:**
- [Nombre del docente]

### **Lugar y Fecha:**
- [Lugar y fecha donde se realizó la práctica]

---

### **Marco Teórico**
La configuración de una conexión punto a punto es una práctica fundamental en redes de comunicación que permite el intercambio de datos entre dos dispositivos sin la necesidad de un intermediario como un switch o un router. Este tipo de conexión resulta ideal para transferencias rápidas de archivos, configuración de redes privadas o para compartir recursos entre dos computadoras.

Para este ejercicio, utilizamos el cable Ethernet con conectores RJ45, siguiendo la topología de red punto a punto. En este proceso, abordamos tanto la configuración física (conexión del cable) como la configuración lógica (asignación de direcciones IP y el intercambio de datos).

### **Herramientas Utilizadas**
1. **Cable Ethernet CAT5 (o superior) con conectores RJ45:** Permite la transmisión de datos entre ambas computadoras.
2. **2 Computadoras:** Ambas con puertos Ethernet operativos.
3. **Terminal (para Linux/macOS) o Símbolo del Sistema (para Windows):** Utilizado para configurar la red manualmente y comprobar la conexión.
4. **Software para compartir archivos:** Para verificar la transferencia de datos entre las computadoras.

---

### **Conceptos Usados en la Práctica**

#### **Cable RJ45**
El RJ45 es el conector estándar utilizado para cables de red Ethernet. Permite conectar dispositivos a una red, y en nuestro caso, es el medio físico que facilita la comunicación entre dos computadoras.

#### **Comandos Utilizados:**
- `ifconfig`: En sistemas Linux/macOS, este comando configura la dirección IP y la máscara de subred.
- `ping`: Utilizado para verificar la conectividad entre dos dispositivos.
- `netsh`: En Windows, este comando configura los parámetros de red.

#### **Topología de Red Punto a Punto**
Se refiere a una conexión directa entre dos dispositivos, en la que cada dispositivo actúa tanto como cliente como servidor. Esto garantiza que ambos puedan compartir y recibir datos sin la necesidad de un dispositivo intermedio.

---

### **Descripción del Procedimiento**

#### **1. Preparación del Cable y Conexión Física**
Para empezar, seleccionamos un cable Ethernet CAT5 con conectores RJ45 en ambos extremos. Confirmamos que era un cable cruzado, lo cual es necesario si nuestras computadoras no tienen la función *Auto-MDIX*. En caso de que ambas computadoras soporten *Auto-MDIX*, podríamos utilizar un cable directo sin problemas.

1. Primero, verificamos el estado del cable, asegurándonos de que los conectores RJ45 estaban en buen estado.
2. Conectamos un extremo del cable a la computadora 1 y el otro extremo a la computadora 2. En ambos casos, confirmamos que las luces de los puertos Ethernet se encendieron, indicando que la conexión física estaba establecida.

#### **2. Configuración Lógica – Asignación de Direcciones IP**

##### **En la Computadora 1:**
- Abrimos la terminal y ejecutamos el comando:
  ```bash
  sudo ifconfig eth0 192.168.1.1 netmask 255.255.255.0 up
  ```
  Este comando asigna la dirección IP `192.168.1.1` a la interfaz `eth0` y establece la máscara de subred `255.255.255.0`. 

##### **En la Computadora 2:**
- De igual forma, abrimos la terminal y ejecutamos:
  ```bash
  sudo ifconfig eth0 192.168.1.2 netmask 255.255.255.0 up
  ```
  Asignando así la dirección IP `192.168.1.2`.

%3E Nota: En sistemas Windows, la configuración se realizó de la siguiente manera:
>
> - Computadora 1:  
>   ```bash
>   netsh interface ip set address name="Ethernet" static 192.168.1.1 255.255.255.0
>   ```
> - Computadora 2:  
>   ```bash
>   netsh interface ip set address name="Ethernet" static 192.168.1.2 255.255.255.0
>   ```

#### **3. Comprobación de la Conexión**
- En la terminal de la computadora 1, ejecutamos:
  ```bash
  ping 192.168.1.2
  ```
  y en la computadora 2:
  ```bash
  ping 192.168.1.1
  ```
Ambos comandos respondieron correctamente, confirmando la conexión.

#### **4. Configuración para Compartir Archivos**
##### **En Windows:**
1. Abrimos el "Centro de redes y recursos compartidos."
2. Seleccionamos "Cambiar configuración de uso compartido avanzado."
3. Activamos "Habilitar la detección de redes" y "Habilitar el uso compartido de archivos e impresoras."
4. Desde el explorador de archivos, seleccionamos la carpeta a compartir, clic derecho → "Propiedades" → pestaña "Compartir" → "Uso compartido avanzado," y configuramos los permisos.

##### **En Linux:**
- Instalamos `samba` usando:
  ```bash
  sudo apt install samba
  ```
- Configuramos el archivo `/etc/samba/smb.conf` y agregamos:
  ```bash
  [Compartido]
  path = /ruta/de/la/carpeta
  available = yes
  valid users = nombre_usuario
  read only = no
  browsable = yes
  public = yes
  writable = yes
  ```

---

### **Resultados Obtenidos**
Tras completar la configuración, logramos la conexión exitosa entre ambas computadoras. Pudimos compartir archivos y datos directamente, comprobando la transferencia eficiente a través de la red punto a punto. Los comandos `ping` confirmaron la conectividad sin pérdida de paquetes, y las carpetas compartidas fueron accesibles desde ambas computadoras.

### **Posibles Errores y Soluciones**
1. **Problemas de conexión física:** Asegurarnos de que el cable RJ45 esté bien conectado en ambos puertos.
2. **Configuración incorrecta de IP:** Confirmar que las IPs asignadas estén en la misma subred (ejemplo: `192.168.1.x`).
3. **Conflictos de firewall:** Desactivar temporalmente el firewall para comprobar la conectividad.

---

### **Conclusión**
La realización de la conexión punto a punto utilizando un cable Ethernet RJ45 nos permitió comprender la importancia de las configuraciones físicas y lógicas en la comunicación de redes. Fue posible observar cómo dos computadoras pueden interactuar de forma directa y eficiente, sin intermediarios. También aprendimos a configurar manualmente las direcciones IP y a compartir recursos, lo que refuerza los fundamentos de la creación y administración de redes pequeñas.

### **Recomendaciones**
- Utilizar cables de calidad y verificar su estado antes de la conexión.
- Tener conocimientos básicos de comandos de red en la terminal para una configuración más rápida.
- Documentar cada paso durante la configuración para facilitar la solución de problemas en el futuro.

---

Espero que esta guía detallada cumpla con lo que necesitas y sirva como un documento completo para tu proyecto. ¡No dudes en añadir más detalles según lo requieras!>)