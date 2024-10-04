## Corrección del Código Menu

Voy a explicar paso a paso cómo identifiqué y corregí los errores en el código original. Este enfoque te permitirá entender el proceso lógico que seguí para llegar a la solución.

#### **1. Analizando el código original**

Primero, revisé el código original para entender su estructura y propósito. El código es un menú que ofrece recomendaciones según la opción seleccionada, pero noté algunos problemas que podrían impedir su correcto funcionamiento. El primer paso fue identificar los posibles errores y áreas de mejora.

#### **2. Identificación del primer error: el uso y la declaración de la variable `OP`**

Al revisar el código, noté que `OP` se utilizaba sin una declaración previa, lo que es una mala práctica porque no garantiza que `OP` tenga el tipo de dato correcto. Esto puede llevar a problemas cuando el usuario ingresa la opción.

- **Problema específico**: En el código, la comparación `Hasta Que OP=5` no es válida porque `OP` es tratada como un carácter (cadena), mientras que el número 5 es un entero. Este conflicto de tipos hace que el programa no funcione correctamente.

#### **Solución aplicada: Declaración explícita de la variable `OP`**

Para evitar este problema, declaré `OP` como `Caracter` al inicio del proceso:

```pseudocodigo
Definir OP Como Caracter
```

Esto asegura que `OP` siempre será tratada como una cadena de texto.

#### **3. Falta de validación de la entrada del usuario**

El código original no valida la entrada del usuario, lo que significa que cualquier valor ingresado fuera del rango 1-5, o incluso caracteres no numéricos, podría causar problemas. Por ejemplo, ingresar "a" o "@" provocaría un comportamiento inesperado.

#### **Solución aplicada: Validación detallada de la entrada `OP`**

Añadí un bloque de validación para asegurarme de que `OP` sea uno de los valores válidos ("1" a "5") antes de convertirlo a un número. Esto se logra con:

```pseudocodigo
Si OP = "1" O OP = "2" O OP = "3" O OP = "4" O OP = "5" Entonces
    OpcionNumérica <- ConvertirANumero(OP)
Sino
    OpcionNumérica <- 0  // Asignar un valor inválido para controlar el error
FinSi
```

Al hacer esto, nos aseguramos de que solo se conviertan en números las opciones válidas y que cualquier otra entrada sea tratada como inválida asignando `0` a `OpcionNumérica`.

#### **4. Problemas en la estructura de control `Segun OP Hacer`**

La estructura `Segun OP Hacer` funcionaba incorrectamente porque `OP` era un carácter y se necesitaba un número para que la selección de opciones funcionara como se esperaba. Esto generaba problemas, especialmente cuando se ingresaban valores no numéricos.

#### **Solución aplicada: Uso de `OpcionNumérica`**

Definí una nueva variable `OpcionNumérica` como `Entero` para manejar la conversión del valor ingresado. La estructura `Segun` se modificó para que funcione con `OpcionNumérica`:

```pseudocodigo
Segun OpcionNumérica Hacer
    1: // Acciones para la opción 1
    2: // Acciones para la opción 2
    3: // Acciones para la opción 3
    4: // Acciones para la opción 4
    5: // Acción de salida
    De otro modo: // Para cualquier valor no válido
        Escribir "Opción no válida"
FinSegun
```

De esta forma, la estructura `Segun` siempre recibe un valor numérico, eliminando el conflicto de tipos.

#### **5. Corrección de la condición de salida del bucle `Repetir...Hasta Que`**

El bucle `Hasta Que OP=5` no funcionaba correctamente debido al conflicto de tipos mencionado antes. Cambié la condición a `Hasta Que OpcionNumérica = 5`, garantizando que la comparación se realice entre valores enteros.

```pseudocodigo
Hasta Que OpcionNumérica = 5
```

#### **6. Prueba final del código**

![[../02 - Recursos/Captura de pantalla_2024-09-30_01-22-24.png]]

### **Código Corregido

```pseudocodigo
Proceso menuxd
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

