---
date: 2024-10-02T19:13
tags:
  - Tarea
  - Universidad
  - miércoles
cssclasses:
  - tarea
  - miércoles
  - center-titles
  - center-images
author: youname
institution: Universidad TUP
course: Nombre del Curso
professor: Nombre del Profesor
---

---

![[/99 - Meta/attachments/img/Pasted image 20240923160919.png]]
### [211 DISEÑO ESTRUCTURADO DE ALGORITMOS 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6029 "211 DISEÑO ESTRUCTURADO DE ALGORITMOS 25-1")
#### [PROF.-DANIEL GUILLERMO CONRADO MOGUEL](https://moodle.tecplayacar.edu.mx/user/view.php?id=10360&course=6029)
![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]





## **Datos del Estudiante**

- **Equipo**: 
	- 4493 Jesus Uriel Santana Oliva
	- 7335 Ever Lopez Panti
- Grado : 1 -B
- **Institución**: Tec Playacar
- Fecha: _miércoles, octubre 2º, 2024_
- Ubicacion : Playa del Carmen
- 
###### **Actividad
- [x] Revisión de formato APA. ✅ 2024-10-02
- [x] Finalizar la bibliografía. ✅ 2024-10-02
- [x] Verificar coherencia en la argumentación. ✅ 2024-10-02
- [x] Insertar gráficos relevantes. ✅ 2024-10-02

> [!success] Terminada
> Tarea Terminada
> 

---
<br>
Diseño y Funcionamiento de un Programa de Calculadora

## Resumen

El presente trabajo tiene como objetivo describir el diseño y funcionamiento de un programa de calculadora simple, que realiza operaciones aritméticas básicas como suma, resta, multiplicación y división. A través de un enfoque didáctico, se explicarán los conceptos fundamentales de la programación, la estructura del pseudocódigo, y se proporcionará un análisis detallado de cada componente del programa.

## 1. Introducción

### 1.1. Contexto

La programación de calculadoras es un ejercicio fundamental en la educación informática, que permite a los estudiantes familiarizarse con la lógica de programación y los principios de entrada y salida de datos.

### 1.2. Objetivos

- Entender la lógica detrás de un programa de calculadora.
- Aprender a estructurar un pseudocódigo eficazmente.
- Desarrollar habilidades para implementar condiciones y bucles en un programa.

### 1.3. Estructura de la Tesis

La tesis se dividirá en varias secciones que abordan los conceptos básicos, la implementación en pseudocódigo, y un análisis del funcionamiento del programa.

## 2. Fundamentos de Programación

### 2.1. Definición de Programa

Un programa es un conjunto de instrucciones que una computadora sigue para realizar una tarea específica. En este caso, se trata de realizar operaciones aritméticas.

### 2.2. Elementos de un Programa

- **Entrada**: Los datos que el usuario proporciona al programa (números y operaciones).
- **Proceso**: Las operaciones realizadas sobre los datos ingresados (suma, resta, etc.).
- **Salida**: Los resultados que el programa devuelve al usuario.

## 3. Estructura del Pseudocódigo

### 3.1. ¿Qué es el Pseudocódigo?

El pseudocódigo es una representación informal de un algoritmo que utiliza un lenguaje similar al natural para describir los pasos a seguir. Es independiente de la sintaxis de un lenguaje de programación específico.

### 3.2. Estructura del Pseudocódigo para la Calculadora
![[../../../../../../99 - Meta/attachments/img/Captura de pantalla_2024-10-02_19-11-27.png]]
A continuación, se presenta el pseudocódigo para la calculadora, seguido de explicaciones detalladas sobre cada sección.

```plaintext
Proceso Calculadora
    Escribir "Bienvenid@ a la calculadora"
    Escribir "Para seleccionar una operación, escriba:"
    Escribir "1 para Suma"
    Escribir "2 para Resta"
    Escribir "3 para Multiplicación"
    Escribir "4 para División"
    
    // Leer la operación
    Leer operacion
    
    // Verificar que el usuario ingresó una opción válida
    Si operacion > 0 y operacion < 5 Entonces
        Escribir "Ingrese el primer número:"
        Leer numero1
        Escribir "Ingrese el segundo número:"
        Leer numero2 
        
        Si operacion = 1 Entonces 
            Escribir "El resultado de la Suma es:"
            resultado = numero1 + numero2
        Fin Si
        
        Si operacion = 2 Entonces
            Escribir "El resultado de la Resta es:"
            resultado = numero1 - numero2
        Fin Si
        
        Si operacion = 3 Entonces
            Escribir "El resultado de la Multiplicación es:"
            resultado = numero1 * numero2
        Fin Si
        
        Si operacion = 4 Entonces
            Escribir "El resultado de la División es:"
            resultado = numero1 / numero2
        Fin Si
        
        Escribir "El resultado es: ", resultado
    Sino
        Escribir "Esa no es una operación válida."
    Fin Si
Fin Proceso
```

## 4. Análisis del Pseudocódigo

### 4.1. Flujo del Programa

- **Inicio**: Se da la bienvenida al usuario.
- **Selección de Operación**: Se muestran las opciones de operaciones y se lee la elección del usuario.
- **Validación de Entrada**: Se verifica que la opción ingresada sea válida.
- **Ingreso de Números**: Se solicitan los números para realizar la operación.
- **Ejecución de la Operación**: Dependiendo de la operación seleccionada, se realizan los cálculos.
- **Mostrar Resultados**: Se muestra el resultado de la operación.
- **Manejo de Errores**: Si la opción no es válida, se informa al usuario.

### 4.2. Condicionales

Se utilizan instrucciones condicionales para determinar qué operación realizar, basándose en la entrada del usuario. Esto es fundamental en la programación, ya que permite la toma de decisiones.

## 5. Implementación en Lenguaje de Programación

### 5.1. Lenguajes de Programación

Una vez que el pseudocódigo está definido, se puede implementar en cualquier lenguaje de programación. En esta sección, se proporcionará un ejemplo en Python, C++ o Java, según la preferencia.

### 5.2. Ejemplo de Implementación en Python

```python
def calculadora():
    print("Bienvenid@ a la calculadora")
    print("Para seleccionar una operación, escriba:")
    print("1 para Suma")
    print("2 para Resta")
    print("3 para Multiplicación")
    print("4 para División")

    operacion = int(input("Ingrese la operación: "))

    if 1 <= operacion <= 4:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if operacion == 1:
            print("El resultado de la Suma es:", numero1 + numero2)
        elif operacion == 2:
            print("El resultado de la Resta es:", numero1 - numero2)
        elif operacion == 3:
            print("El resultado de la Multiplicación es:", numero1 * numero2)
        elif operacion == 4:
            print("El resultado de la División es:", numero1 / numero2)
    else:
        print("Esa no es una operación válida.")

calculadora()
```

## 6. Conclusiones

### 6.1. Resumen de Aprendizajes

El desarrollo de un programa de calculadora proporciona una comprensión sólida de los conceptos de programación, como la entrada/salida de datos, el uso de condicionales, y la estructuración lógica del código.

### 6.2. Futuras Mejoras

Se sugiere que futuras versiones de esta calculadora incluyan funciones avanzadas, como la capacidad de realizar operaciones con números complejos, almacenar resultados, o trabajar con funciones matemáticas más complejas.

## 7. Referencias
Robledano, A. (2019, junio 18). Qué es pseudocódigo y por qué es esencial en programación. _OpenWebinars.net_. https://openwebinars.net/blog/que-es-pseudocodigo/

---
