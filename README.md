# CafeFET 

## Integrantes

-   Yeison Fabian Cabrera Ortiz
-   Michell Andrea Fierro Orozco
-   Carlos Eduardo Rubio Almonacid

## Descripción del caso

CafeFET es un caso académico de una cafetería universitaria. El proyecto
trabaja con mensajes de usuarios relacionados con pedidos, consultas,
cancelaciones y reclamos. Se busca utilizar modelos de lenguaje y
técnicas de ingeniería de prompts para interpretar esos mensajes y
organizar la información de manera clara.

Para el caso se tienen en cuenta las reglas de funcionamiento de
CafeFET:

-   Los pedidos se realizan de lunes a sábado, entre las 7:00 a. m. y
    las 6:00 p. m.
-   Cada pedido puede contener máximo cinco productos.
-   El pago se realiza con el saldo de la tarjeta estudiantil y este no
    puede quedar negativo.
-   No se pueden solicitar productos agotados.
-   Si el pedido no se recoge dentro de los 30 minutos siguientes, se
    cancela y se devuelve el dinero.

## Herramientas, modelos y equipo

**Herramientas utilizadas:** Python, Ollama y `uv`.

**Modelos evaluados:** - `qwen3.5:4b` - `qwen3.5:0.8b`

**Equipo utilizado:** - Modelo: Dell Inspiron 15 3515. -
Sistema operativo: Windows 11, sistema de 64 bits. - Procesador: AMD
Ryzen 5 3450U with Radeon Vega Mobile Gfx, 2100 MHz. - Memoria RAM
instalada: 8 GB. - Gráficos: Radeon Vega Mobile Gfx integrada.

## Organización del repositorio

``` text
CafeFET/
├── reto1/
├── reto2/
├── reto3/
├── reto4/
├── bonus/
│   ├── analisis.md
│   ├── comun.py
│   ├── evalua.py
│   ├── reporte_json.py
│   ├── salida_evalua_08b.txt
│   ├── salida_evalua_4b.txt
│   ├── salida_reporte_08b.txt
│   ├── salida_reporte_4b.txt
│   ├── pyproject.toml
│   └── uv.lock
└── README.md
```

Las carpetas `reto1` a `reto4` contienen el desarrollo de cada reto. La
carpeta `bonus` contiene los programas, las ejecuciones de los dos
modelos y el análisis de resultados del Reto 5 Bonus.



## Reflexión

El desarrollo de CafeFET nos permitió comprobar que la calidad de una
respuesta de inteligencia artificial depende en gran medida de la
claridad del contexto y de las instrucciones. Al definir las reglas del
negocio, precisar el formato esperado e incluir ejemplos, las respuestas
se acercaron más a las necesidades del caso. En las pruebas de
clasificación del reto bonus, el prompt V2 superó al V1 en ambos modelos:
qwen3.5:4b pasó de 70 % a 100 % de aciertos y qwen3.5:0.8b, de 70 % a
90 %. Estos resultados corresponden al conjunto de diez mensajes
utilizado; no permiten asegurar el mismo desempeño ante cualquier mensaje
real.

A lo largo de los retos también vimos que una respuesta convincente o
bien estructurada puede contener errores. El modelo puede omitir una regla
del negocio, proponer una corrección equivocada, asumir requisitos que no
se especificaron o producir un JSON válido con datos mal interpretados.
Asimismo, descomponer una tarea y pedir una explicación paso a paso ayuda
a examinar el razonamiento, pero no garantiza que la conclusión sea
correcta. Por eso, las reglas de CafeFET y los criterios de aceptación
sirvieron como referencia para contrastar cada resultado.

Como equipo, concluimos que los modelos de lenguaje son útiles para
apoyar tareas como generar código, revisar requisitos, clasificar mensajes
y estructurar reportes, siempre que exista supervisión. En una aplicación
real ampliaríamos los casos de prueba con mensajes variados y ambiguos,
verificaríamos automáticamente las reglas críticas y solicitaríamos
aclaración cuando falten datos, en vez de permitir que el modelo los
invente. Así podríamos aprovechar su capacidad sin delegarle decisiones
que deben cumplir las condiciones del negocio.

