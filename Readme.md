**Hoja de Trabajo No 2: Una Alcancía** 

**Nombre: Juan Sebastián Ibarra Salas**	

**ID:**

Enunciado: Analice la siguiente lectura e identifique el mundo del problema, lo que se 

espera de la aplicación y las restricciones para desarrollarla. 

Se quiere construir un programa para manejar una alcancía. En la alcancía es posible guardar monedas de distintas denominaciones: $50, $100, $200, $500 y $1000. No se guardan billetes o monedas de otros valores. 

El programa debe dar las siguientes opciones: (1) agregar una moneda de una de las denominaciones que maneja, (2) informar cuantas monedas tiene de cada denominación, (3) calcular el total de dinero ahorrado y (4) romper la alcancía, vaciando su contenido. 

**Requerimientos funcionales.** 

Describa los siguientes requerimientos funcionales de la aplicación. 

|**Nombre** |R1 – Guardar una moneda de $50 en la alcancía.|
| :- | :- |
|**Resumen**|Permite que el programa guarde la información de un valor que se ha agregado |
|**Entrada**|Moneda|
|**Resultado**|Se ha guardado la moneda de $50|

|**Nombre**|R2 – Contar el número de monedas de $50 que hay en la alcancía. |
| :- | :- |
|**Resumen**|Permite contar las monedas de 50 que están dentro de la alcancía.|
|**Entrada**|Ninguna|
|**Resultado**|Se han contado el total de monedas de $50 de forma exitosa.|

|**Nombre** |R3 – Calcular el total de dinero ahorrado en la alcancía. |
| :- | :- |
|**Resumen**|Permite contar el total de monedas que se encuentren dentro de la alcancía |
|**Entrada**|Ninguna|
|**Resultado**|Se muestra el total guardado en la alcancía|

|**Nombre**|R4 – Romper la alcancía. |
| :- | :- |
|**Resumen**|Permite retirar el total de monedas guardadas en la alcancía y dando un valor de 0|
|**Entrada**|ninguna|
|**Resultado**|La alcancía se ha roto y retira el total del dinero guardado |

**Entidades del mundo.** 

Identifique las entidades del mundo y descríbalas brevemente. 

|**Entidad**|**Descripción**|
| :- | :- |
|Alcancía|Representa la cantidad de dinero ahorrado.|

**Características de las entidades.** 

Identifique las características de cada una de las entidades y escriba la clase en UML con el tipo de datos adecuado. 

**Entidad 1**

|**Atributos**|**Valores posibles**|
| :- | :- |
|**Moneda de $50**|**50**|
|**Moneda de $100**|**100**|
|**Moneda de $200**|**200**|
|**Moneda de $500**|**500**|
|**Moneda de $1000**|**1000**|
|**Estado de alcancía.**|**1 abierto 2 cerrado**|


**Diagrama UML**

|Alcancía|
| :- |
|Agregar moneda|
|Estado de alcancía |

**Métodos de las entidades.** 

Complete las siguientes descripciones de métodos y escriba su implementación en el lenguaje Python.

|**Clase** |Alcancía|
| :- | :- |
|**Nombre** |AgregarMoneda50|
|**Parámetros**|Alcancía, moneda de 50|
|**Retorno**|Ninguno |
|**Descripción**|Se agrega una moneda de valor 50|



|**Implementación en Python** |
| :- |
||

|**Clase** |Alcancía|
| :- | :- |
|**Nombre** |AgregarMoneda500|
|**Parámetros**|Alcancía, moneda de 500|
|**Retorno**|Ninguno|
|**Descripción**|Se agrega una moneda de valor 500|



|**Implementación en Python** |
| :- |
||

|**Clase** |Alcancía|
| :- | :- |
|**Nombre** |darTotalDinero|
|**Parámetros**|Alcancía|
|**Retorno**|Mostrar el total de dinero guardado |
|**Descripción**|Se muestra el total del dinero guardado en la alcancía |



|**Implementación en Python** |
| :- |
||

|**Clase** |Alcancía|
| :- | :- |
|**Nombre** |darNumeroMonedas100 |
|**Parámetros**|Alcancía, total monedas de 100|
|**Retorno**|Total, de monedas de 100 registradas en la alcancía |
|**Descripción**|Se cuentan las monedas de 100 que se han registrado |



|**Implementación en Python** |
| :- |
||

|**Clase** |Alcancía|
| :- | :- |
|**Nombre** |romperAlcancia|
|**Parámetros**|Alcancia|
|**Retorno**|Total de monedas |
|**Descripción**|Se borra el total de monedas almacenadas anteriormente|



|**Implementación en Python** |
| :- |
||


