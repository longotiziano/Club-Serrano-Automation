# Proyecto de automatización Club Serrano.
Luego de una profunda investigación y análisis de mi trabajo como cajero en el bar Club Serrano, identifiqué
una serie de tareas repetitivas y automatizables que podrían llevarse a cabo de manera efectiva gracias a la
realización de un programa, por lo que a ello me dediqué.

## Tareas identificadas.
* Las tareas identificadas a la hora de hacer el análisis fueron:
    - Enviado de emails
    - Agregado de tarjetas manual
    - Medidas que reduzcan la posibilidad del error humano, como por ejemplo: cantidad específica de dígitos 
    para números de operación en caso de tratarse de pago con Mercado Pago, no permitir duplicados, alertar en
    caso de tipeo sospechoso...
    - Mapeo de mesas disponibles y "matadas".
    - Alternado entre conteo de efectivo para libre comodidad del cajero y su propia administración. La 
    alternación variaría entre contado de billetes individual y cantidad total. 4
    - Variedad de shortcuts para la comodidad del cajero.
    - Creación del Excel en un formato presentable, todo en una misma interfaz de usuario.
    - Recordatorio de tareas comunicativas con administración y checklist de cierre de caja.
    - Un pequeño bloc de notas que sirva de recordatorio para las distintas circuentancias que se puede ver
    adversado el cajero, tales como promociones del día, comunicaciones, entre otros.
    - Guardado automático de progreso.
    - Panel de guardado de Excel con historial ordenado.
    - "Puntos de guardado" que permitan mucha más facilidad a la hora del arqueo de caja.

## Organización del proyecto.
Para la comodidad y orden, decidí (en cada módulo) implementar un orden de "jerarquía" en cuanto el llamado de
bibliotecas o importado de funciones y clases, el cual se basa en primero llamar a los distintos archivos y
luego a los frameworks o librerías, todo en orden alfabético.