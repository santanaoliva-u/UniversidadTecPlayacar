---
date: 2024-10-03T19:11
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

### [211 DISEÑO ESTRUCTURADO DE ALGORITMOS 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6029 "211 DISEÑO ESTRUCTURADO DE ALGORITMOS 25-1")
#### [PROF.-DANIEL GUILLERMO CONRADO MOGUEL](https://moodle.tecplayacar.edu.mx/user/view.php?id=10360&course=6029)
![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]




# Examen Evaluacion
## **Datos del Estudiante**

- **Nombre de Equipo**:
	- 👀  Jesus Uriel Santana Oliva
	- 👀 7335 Ever Lopez Panti 
- Grado : 1 -B
- **Institución**: Tec Playacar
- Fecha: _jueves, octubre 3º, 2024_
- Ubicacion : Playa del Carmen

###### **Actividad
- [x] Revisión de formato APA. ✅ 2024-10-03
- [x] Finalizar la bibliografía. ✅ 2024-10-03
- [x] Verificar coherencia en la argumentación. ✅ 2024-10-03
- [x] Insertar gráficos relevantes. ✅ 2024-10-03

> [!success] Terminada
> Tarea Terminada
> 

---
<br>
## Introducción

![[../../../../../99 - Meta/attachments/img/Pasted image 20241003191450.png]]

En este documento, detallaré el proceso de creación de un algoritmo en pseudocódigo que permite determinar el área y el volumen de un cilindro, dados su radio (R) y su altura (H). A lo largo del desarrollo, reflexionaré sobre las decisiones que tomé y los desafíos que enfrenté, con el fin de ofrecer una visión más humanizada del proceso de programación.

## Planteamiento del Problema

El primer paso fue entender el problema que debía resolver: calcular el área y el volumen de un cilindro. Para ello, recordé las fórmulas matemáticas fundamentales:

- **Área lateral y total** del cilindro:
$$
A = 2 \pi R (R + H)
$$

- **Volumen** del cilindro:
$$
V = \pi R^2 H
$$

Estas fórmulas son esenciales en la geometría, y mi tarea consistía en implementarlas en un algoritmo que permitiera la interacción con el usuario para obtener los resultados deseados.


## Diseño del Algoritmo
	
![[../../../../../99 - Meta/attachments/img/Captura de pantalla_2024-10-03_19-17-38.png]]

![[../../../../../99 - Meta/attachments/img/Untitled diagram-2024-10-04-002812.png]]
### 1. Definición de la Estructura del Código

Comencé definiendo el propósito general del algoritmo, que es calcular el área y el volumen del cilindro. Para ello, decidí utilizar el pseudocódigo, un formato que permite estructurar mis ideas antes de la implementación real en un lenguaje de programación.

```pseudocódigo
Proceso calcularCilindro
    Definir R Como Real
    Definir H Como Real
    Definir A Como Real
    Definir V Como Real
```

### 2. Solicitud de Datos al Usuario

Después de definir la estructura básica, el siguiente paso fue solicitar los datos necesarios al usuario: el radio y la altura del cilindro. Este paso es crucial, ya que la interacción con el usuario es fundamental para cualquier programa.

```pseudocódigo
    Escribir "Ingrese el radio (R):"
    Leer R
    Escribir "Ingrese la altura (H):"
    Leer H
```

Reflexionando sobre este paso, consideré la importancia de proporcionar instrucciones claras al usuario. Una interfaz amigable facilita la comprensión y mejora la experiencia general al utilizar el programa.

### 3. Cálculo del Área y Volumen

Con los datos del usuario en mano, pasé a implementar las fórmulas matemáticas para calcular el área y el volumen. La lógica detrás de esto es simple, pero requiere precisión para evitar errores en los cálculos.

```pseudocódigo
    A <- 2 * PI * R * (R + H)
    V <- PI * (R^2) * H
```

En este paso, decidí utilizar constantes como \( \pi \) para asegurar la precisión de mis cálculos. Esto también me permitió reflexionar sobre la importancia de la precisión en la programación.

### 4. Presentación de Resultados

Finalmente, el paso crucial es comunicar los resultados al usuario de manera clara y concisa. Para ello, opté por mostrar el área y el volumen calculados, asegurando que la información fuera fácil de entender.

```pseudocódigo
    Escribir "El área del cilindro es: ", A
    Escribir "El volumen del cilindro es: ", V
Fin Proceso
```

Es aquí donde la presentación de los resultados se vuelve fundamental. He aprendido que una buena comunicación de resultados no solo muestra el trabajo realizado, sino que también proporciona al usuario la información necesaria de manera efectiva.

## Ejemplos de Cálculo

Para validar que el algoritmo funciona correctamente, presento a continuación ejemplos con valores específicos para el radio (R) y la altura (H). Esto no solo demuestra la funcionalidad del código, sino que también permite a los usuarios visualizar cómo aplicar las fórmulas en diferentes escenarios.

- **Ejemplo 1**: Para $(R = 3)$ y $(H = 5)$:
  - Cálculo del área:
  $$
  A = 2 \pi (3) (3 + 5) = 150.7964
  $$
  - Cálculo del volumen:
  $$
  V = \pi (3^2)(5) = 141.3717
  $$

- **Ejemplo 2**: Para $(R = 2)$ y $(H = 10)$:
  - Cálculo del área:
  $$
  A = 2 \pi (2)(2 + 10) = 150.7964
  $$
  - Cálculo del volumen:
  $$
  V = \pi (2^2)(10) = 125.6637
  $$

Estos ejemplos refuerzan la comprensión de cómo aplicar el algoritmo y validan su precisión.

### Codigo:
```pseint
Proceso calcularCilindro
    Definir R Como Real
    Definir H Como Real
    Definir A Como Real
    Definir V Como Real
    Definir pia Como Real
    Pia <- 3.14159265358979
    
    Escribir "Ingrese el radio (R):"
    Leer R
    Escribir "Ingrese la altura (H):"
    Leer H
    
    A <- 2 * Pia * R * (R + H)
    V <- Pia * (R^2) * H
    
    Escribir "El área del cilindro es: ", A
    Escribir "El volumen del cilindro es: ", V
Fin Proceso

```
<br>

![[../../../../../99 - Meta/attachments/img/Captura de pantalla_2024-10-03_19-20-07.png]]

Test del profe :
![[../../../../../99 - Meta/attachments/img/aaaaaaaaa.png]]

Correcto 💯