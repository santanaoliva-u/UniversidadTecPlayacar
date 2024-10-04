### Corrección del Código Menú




![[99 - Meta/attachments/img/aa.png]]

Voy a explicar de manera resumida cómo identifiqué y corregí los errores en el código original.

#### 1. Análisis del código original
El código presenta un menú que ofrece opciones de recomendación según la selección del usuario. El problema principal que encontré fue la falta de validación de la entrada y un mal manejo de tipos de datos en la variable `OP`.

#### 2. Declaración de la variable `OP`
El código usaba `OP` sin haberla declarado previamente. Para evitar errores y garantizar un correcto funcionamiento, declaré `OP` como **carácter**, asegurando que siempre sea tratada como una cadena de texto.

```pseudocodigo
Definir OP Como Caracter
```

#### 3. Validación de la entrada
No se validaba adecuadamente la entrada del usuario. Esto podría causar problemas si se introducen valores fuera del rango esperado (1-5) o caracteres no numéricos. Implementé una validación para que solo se consideren valores correctos, asignando `0` a cualquier entrada inválida.

```pseudocodigo
Si OP = "1" O OP = "2" O OP = "3" O OP = "4" O OP = "5" Entonces
    OpcionNumérica <- ConvertirANumero(OP)
Sino
    OpcionNumérica <- 0
FinSi
```

#### 4. Corrección de la estructura `Segun`
El código original tenía conflictos porque `OP` era un carácter, y `Segun` esperaba un número. Para corregir esto, usé una nueva variable `OpcionNumérica`, garantizando que siempre sea numérica y que `Segun` funcione adecuadamente.

```pseudocodigo
Segun OpcionNumérica Hacer
    1: // Opción 1
    2: // Opción 2
    3: // Opción 3
    4: // Opción 4
    5: // Salir
    De otro modo: // Opción inválida
        Escribir "Opción no válida"
FinSegun
```

#### 5. Ajuste en la condición de salida
El bucle `Repetir...Hasta Que OP=5` no funcionaba correctamente debido al conflicto de tipos. Cambié la condición a `Hasta Que OpcionNumérica = 5`, permitiendo que la comparación se realice entre valores enteros.

```pseudocodigo
Hasta Que OpcionNumérica = 5
```


```pseint
Proceso menu
    Definir OP Como Caracter  // Inicialmente definimos OP como un carácter (cadena)
    Definir OpcionNumérica Como Entero // Nueva variable para almacenar la opción numérica
    Repetir
        // mostrar menú
        Limpiar Pantalla
        Escribir "Menú de recomendaciones"
        Escribir "   1. Literatura"
        Escribir "   2. Cine"
        Escribir "   3. Música"
        Escribir "   4. Videojuegos"
        Escribir "   5. Salir"
        
        // ingresar una opción
        Escribir "Elija una opción (1-5): "
        Leer OP
        
        // Verificar si la entrada está dentro de los valores válidos (carácter entre '1' y '5')
        Si OP = "1" O OP = "2" O OP = "3" O OP = "4" O OP = "5" Entonces
            OpcionNumérica <- ConvertirANumero(OP) // Convertir la opción a un número y almacenarla
        Sino
            OpcionNumérica <- 0  // Asignar un valor inválido para controlar el error
        FinSi
        
        // procesar esa opción
        Segun OpcionNumérica Hacer
            1:
                Escribir "Lecturas recomendables:"
                Escribir " + Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)"
                Escribir " + El juego de Ender (Orson Scott Card)"
                Escribir " + El sueño de los héroes (Adolfo Bioy Casares)"
            2:
                Escribir "Películas recomendables:"
                Escribir " + Matrix (1999)"
                Escribir " + El último samurái (2003)"
                Escribir " + Cars (2006)"
            3:
                Escribir "Discos recomendables:"
                Escribir " + Despedazado por mil partes (La Renga, 1996)"
                Escribir " + Búfalo (La Mississippi, 2008)"
                Escribir " + Gaia (Mägo de Oz, 2003)"
            4:
                Escribir "Videojuegos clásicos recomendables:"
                Escribir " + Día del tentáculo (LucasArts, 1993)"
                Escribir " + Terminal Velocity (Terminal Reality/3D Realms, 1995)"
                Escribir " + Death Rally (Remedy/Apogee, 1996)"
            5:
                Escribir "Gracias, vuelva pronto"
            De otro modo:
                Escribir "Opción no válida"
        FinSegun
        
        Escribir "Presione enter para continuar"
        Esperar Tecla
        
    Hasta Que OpcionNumérica = 5
FinProceso
```

