---
date: 2024-10-03T16:02
tags:
  - Tarea
  - Universidad
  - jueves
cssclasses:
  - tarea
  - jueves
  - center-titles
  - center-images
author: youname
institution: Universidad TUP
course: Nombre del Curso
professor: Nombre del Profesor
---


![[/99 - Meta/attachments/img/Pasted image 20240923160919.png]]




### [213 FUNDAMENTOS DE REDES 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6030 "213 FUNDAMENTOS DE REDES 25-1")
#### [PROF.-HECTOR LEONEL PEREZ RAMIREZ](https://moodle.tecplayacar.edu.mx/user/view.php?id=9023&course=6030)


![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]





## **Datos del Estudiante**

- **Nombre**: Jesus Uriel Santana Oliva
- Grado : 1 -B
- **Institución**: Tec Playacar
- Fecha: _jueves, octubre 3º, 2024_
- Ubicacion : Playa del Carmen
- 
###### **Actividad
- [x] Revisión de formato APA. ✅ 2024-10-03
- [x] Finalizar la bibliografía. ✅ 2024-10-03
- [x] Verificar coherencia en la argumentación. ✅ 2024-10-03
- [x] Insertar gráficos relevantes. ✅ 2024-10-03

<br>
### 1. **TCP (Transmission Control Protocol)**
![[../../../../../99 - Meta/attachments/img/Pasted image 20241003160026.png]]

#### Descripción General
TCP es un protocolo de transporte **orientado a la conexión** que garantiza la entrega confiable de datos entre dos dispositivos. Se asegura de que los datos lleguen en el orden correcto y sin errores, utilizando técnicas como la numeración de secuencias y acuses de recibo (ACK). Es el protocolo más usado en Internet, especialmente en aplicaciones donde la fiabilidad es crítica, como la navegación web, el correo electrónico o la transferencia de archivos.

#### Características
- **Orientado a conexión:** Antes de transferir datos, TCP establece una conexión entre los hosts mediante un proceso conocido como **three-way handshake** (apretón de manos de tres vías).
- **Control de flujo:** TCP regula la cantidad de datos enviados por la red para evitar la congestión.
- **Control de congestión:** Ajusta la velocidad de transmisión para adaptarse a la capacidad de la red.
- **Corrección de errores:** TCP verifica que los paquetes de datos lleguen sin errores y en el orden correcto.

#### Uso Típico
TCP se usa comúnmente en servicios como:
- **HTTP/HTTPS**: para navegación web.
- **SMTP**: para correos electrónicos.
- **FTP**: para la transferencia de archivos.

#### Ejemplo en Linux (comando desde terminal)
Con `nc` o `netcat`, puedes simular una conexión TCP:

**Servidor TCP:**
```bash
nc -l 12345
```

**Cliente TCP:**
```bash
nc localhost 12345
```
Esto crea una conexión TCP en el puerto 12345. El servidor escucha en ese puerto y el cliente se conecta a `localhost` en el mismo puerto.

#### Script en Bash para TCP:
```bash
#!/bin/bash
# Script de ejemplo para establecer una conexión TCP

echo "Iniciando servidor TCP en el puerto 8080"
nc -l 8080 &
sleep 1
echo "Conectando al servidor desde el cliente"
nc localhost 8080
```

### 2. **UDP (User Datagram Protocol)**
![[../../../../../../99 - Meta/attachments/img/Pasted image 20241003160100.png]]
	
#### Descripción General
UDP es un protocolo de transporte **sin conexión**. A diferencia de TCP, UDP no garantiza la entrega de datos, pero es mucho más rápido. Se utiliza en aplicaciones donde la velocidad es más importante que la fiabilidad, como el **streaming de video**, los juegos en línea o los sistemas de **DNS**.

#### Características
- **No orientado a conexión:** No establece una conexión antes de enviar datos.
- **Sin control de flujo o congestión:** No hay mecanismos para controlar la cantidad de datos enviados.
- **No garantiza entrega o el orden de los paquetes:** No realiza reenvío en caso de errores.
- **Menor overhead:** Dado que no utiliza procesos de control de errores o retransmisiones, es más eficiente que TCP.

#### Uso Típico
UDP es comúnmente usado en:
- **DNS**: para resolver nombres de dominio.
- **Streaming de video y audio**.
- **Juegos en línea**.

#### Ejemplo en Linux (comando desde terminal)
Con `nc`, puedes simular una conexión UDP:

**Servidor UDP:**
```bash
nc -u -l 12345
```

**Cliente UDP:**
```bash
nc -u localhost 12345
```

#### Script en Bash para UDP:
```bash
#!/bin/bash
# Script de ejemplo para establecer una conexión UDP

echo "Iniciando servidor UDP en el puerto 9090"
nc -u -l 9090 &
sleep 1
echo "Conectando al servidor desde el cliente"
nc -u localhost 9090
```

### 3. **SCTP (Stream Control Transmission Protocol)**
![[../../../../../../99 - Meta/attachments/img/Pasted image 20241003160132.png]]

#### Descripción General
SCTP es un protocolo de transporte similar a TCP pero ofrece funcionalidades adicionales, como la capacidad de manejar múltiples flujos de datos dentro de una sola conexión. Es especialmente útil en aplicaciones que requieren una combinación de fiabilidad y baja latencia.

#### Características
- **Multistreaming:** Puede enviar varios flujos de datos simultáneamente sin que el retraso en uno afecte a los demás.
- **Orientado a conexión:** Similar a TCP, pero permite la transmisión de múltiples flujos de datos.
- **Corrección de errores y acuses de recibo.**
- **Soporte para redundancia de enlaces:** SCTP puede utilizar múltiples rutas de red para mayor fiabilidad.

#### Uso Típico
SCTP se utiliza en:
- **Telefonía IP** (VoIP).
- Redes de señalización en telecomunicaciones.

#### Ejemplo en Linux (comando desde terminal)
Para trabajar con SCTP necesitas instalar herramientas como `lksctp-tools`:

**Servidor SCTP:**
```bash
sctp_darn -H localhost -P 2000
```

**Cliente SCTP:**
```bash
sctp_test -H localhost -P 2000
```

#### Script en Bash para SCTP:
```bash
#!/bin/bash
# Script de ejemplo para establecer una conexión SCTP

echo "Iniciando servidor SCTP en el puerto 2000"
sctp_darn -H localhost -P 2000 &
sleep 1
echo "Conectando al servidor desde el cliente"
sctp_test -H localhost -P 2000
```

### 4. **SSL (Secure Sockets Layer)**
![[../../../../../../99 - Meta/attachments/img/Pasted image 20241003160146.png]]

#### Descripción General
SSL es un protocolo criptográfico que proporciona comunicación segura a través de una red. SSL fue el precursor de TLS, pero aún se menciona comúnmente. Su principal objetivo es ofrecer **confidencialidad**, **integridad** y **autenticación** en la comunicación entre dos partes, asegurando que los datos no puedan ser interceptados.

#### Uso Típico
SSL es utilizado en:
- **Navegación web segura** (HTTPS).
- **Transferencias de correo electrónico seguras.**

#### Ejemplo en Linux (comando desde terminal)
Para establecer una conexión SSL:

**Cliente SSL con `openssl`:**
```bash
openssl s_client -connect google.com:443
```

### 5. **TLS (Transport Layer Security)**
![[../../../../../../99 - Meta/attachments/img/Pasted image 20241003160219.png]]

#### Descripción General
TLS es la versión mejorada y más segura de SSL. Es ampliamente utilizado para proteger las comunicaciones en Internet y garantizar que los datos transferidos entre un cliente y un servidor no sean interceptados ni alterados.

#### Características
- **Confidencialidad:** Utiliza cifrado para proteger la información.
- **Integridad:** Verifica que los datos no hayan sido modificados durante el tránsito.
- **Autenticación:** Mediante certificados digitales.

#### Uso Típico
TLS se utiliza en:
- **HTTPS**: para proteger la navegación web.
- **Correo electrónico seguro**.

#### Ejemplo en Linux (comando desde terminal)
Para ver los detalles de una conexión TLS:

```bash
openssl s_client -connect example.com:443
```

#### Script en Bash para TLS:
```bash
#!/bin/bash
# Script para comprobar la conexión TLS de un servidor web

echo "Verificando conexión TLS con google.com"
openssl s_client -connect google.com:443
```

### Conclusión y Resumen
- **TCP** es para conexiones fiables y con control de errores.
- **UDP** es rápido, pero no garantiza la entrega de datos.
- **SCTP** es una mezcla entre TCP y UDP, con soporte para múltiples flujos de datos.
- **SSL/TLS** son protocolos que aseguran la comunicación mediante cifrado.



## **Recursos**

https://www.cloudflare.com/es-es/learning/ssl/transport-layer-security-tls/
_SCTP_. (n.d.). Juniper.Net. Retrieved October 3, 2024, from https://www.juniper.net/documentation/mx/es/software/junos23.4/agf-user-guide/topics/concept/agf-sctp-amf.html
https://www.fortinet.com/lat/resources/cyberglossary/tcp-ip#:~:text=%C2%BFQu%C3%A9%20es%20TCP%3F,a%20trav%C3%A9s%20de%20una%20red.

> [!note] **Nota**  
> Recuerda que las referencias deben estar en formato APA y alineadas con las exigencias de la universidad.

---
<center>
  <div style="display: inline-block; padding: 15px; border: 2px solid #ccc; border-radius: 10px; background: transparent; box-shadow: 0 0 15px rgba(255,255,255,0.3); text-align: center; transition: transform 0.3s, box-shadow 0.3s;">
    <img src="https://avatars.githubusercontent.com/u/47199647?v=4" alt="Foto del Estudiante" style="width: 80px; height: 80px; border-radius: 50%; margin-bottom: 10px; border: 2px solid #ccc; transition: transform 0.3s;">
    <div style="font-family: Arial, sans-serif; color: #ccc;">
      <strong style="color: #fff;">Alumno:</strong> Jesús Uriel Santana Oliva<br>
      <strong style="color: #fff;">Curso:</strong> Nombre<br>
      <strong style="color: #fff;">Grado:</strong> 1 - B
    </div>
  </div>
</center>


Calificacion : 10
