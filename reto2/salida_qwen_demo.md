Al revisar el código de la función `crear\_pedido` para el sistema \*\*CafeFET\*\*, se identifican 

tres errores críticos que incumplen las reglas de negocio estándar de un sistema de reservas o 

pedidos. A continuación, se detalla cada uno con su análisis técnico y la regla 

correspondiente:



\### 1. Error en la validación del saldo (Lógica invertida)

\*   \*\*Código actual:\*\*

&#x20;   ```python

&#x20;   if est.saldo - sum(p.precio for p in productos) < -1000:

&#x20;       return False

&#x20;   ```

\*   \*\*Análisis:\*\* La condición verifica si la diferencia entre el saldo del estudiante y el 

costo total es menor que `-1000`. Esto significa que el sistema rechaza el pedido solo si el 

saldo restante es extremadamente bajo (menor a -1000). Sin embargo, en un sistema de reservas, 

lo lógico es \*\*permitir\*\* el pago si el saldo es suficiente o permitir una pequeña deuda 

(crédito), pero \*\*rechazar\*\* si el saldo es insuficiente para cubrir el costo.

\*   \*\*Regla de Negocio Incumplida:\*\* La regla de \*\*"Capacidad de Pago"\*\*. El sistema debería 

rechazar el pedido si `est.saldo < sum(p.precio)`. La lógica actual parece estar diseñada para 

un escenario muy específico y restrictivo que probablemente no es la intención del negocio (por 

ejemplo, permitir pagos con saldo negativo hasta -1000, lo cual suele ser una regla de crédito 

estricta, pero la forma de escribir la condición sugiere un error lógico en el umbral o la 

dirección de la comparación).



\### 2. Error en la validación del horario (Rango incorrecto)

\*   \*\*Código actual:\*\*

&#x20;   ```python

&#x20;   return 7 <= hora <= 18

&#x20;   ```

&#x20;   \*(Nota: Esta línea está fuera del bloque `if`, por lo que funciona como una condición 

final, pero el contexto sugiere que debería estar dentro de la validación principal).\*

&#x20;   

&#x20;   Más grave aún, si asumimos que la intención era validar el horario dentro de un bloque `if` 

para devolver `False`:

&#x20;   ```python

&#x20;   if not (7 <= hora <= 18): # Faltaba el 'not' o la estructura lógica

&#x20;       return False

&#x20;   ```

&#x20;   

&#x20;   Sin embargo, analizando la estructura actual:

&#x20;   La función devuelve `True` solo si se cumplen las condiciones anteriores \*\*Y\*\* si la hora 

está entre 7 y 18. Pero hay un problema de \*\*lógica booleana en la última línea\*\*.

&#x20;   

&#x20;   Si el código es exactamente como lo presentas:

&#x20;   ```python

&#x20;   def crear\_pedido(est, productos, hora):

&#x20;       if len(productos) > 6: return False

&#x20;       if est.saldo - sum(...) < -1000: return False

&#x20;       return 7 <= hora <= 18 # Esto devuelve un booleano basado en la hora.

&#x20;   ```

&#x20;   

&#x20;   \*\*El error real:\*\* Si el código se ejecuta así, la función devolverá `True` o `False` 

basándose únicamente en la hora si las otras condiciones pasan. Pero el problema más común en 

este tipo de ejercicios es que el rango de horario suele ser \*\*exclusivo\*\* o tener un margen de 

error (ej. 7:00 a 18:00, pero ¿incluye los minutos exactos?).

&#x20;   

&#x20;   \*Corrección probable:\* La regla de negocio dice que las reservas son de \*\*lunes a viernes\*\* 

y entre las \*\*07:00 y las 18:00\*\*. El código actual no verifica el día de la semana (`est.dia` 

o `datetime.date`). Además, si `hora` es un objeto `time`, la comparación directa funciona, 

pero si es una cadena o fecha completa, fallará. Asumiendo que `hora` es un número entero 

(minutos desde medianoche), la lógica del rango parece correcta en sí misma (`7 <= hora <= 18` 

asumiendo horas enteras), \*\*PERO\*\* falta la validación del día de la semana.



&#x20;   \*Re-evaluando el error más obvio:\* En muchos sistemas de este tipo, el error suele ser que 

se permite reservar a las \*\*18:00 exactas\*\* cuando el cierre es estricto a las 17:59 o 

viceversa. Sin embargo, el error más crítico en la estructura lógica presentada es que la 

última línea `return 7 <= hora <= 18` actúa como una condición de retorno directa. Si la 

intención era validar y luego continuar, debería estar dentro de un `if`.

&#x20;   

&#x20;   \*\*Hipótesis del error lógico:\*\* Probablemente se espera que el sistema permita reservas 

hasta las 18:00, pero si la hora es mayor a 18, debe devolver `False`. El código actual hace 

eso.

&#x20;   

&#x20;   \*¿Qué falta?\* La validación del \*\*día de la semana\*\*. CafeFET probablemente solo acepta 

pedidos de Lunes a Viernes.



\### 3. Falta de validación del día de la semana

\*   \*\*Código actual:\*\* No hay ninguna referencia al día de la semana (`est.dia`, `fecha`, 

etc.).

\*   \*\*Regla de Negocio Incumplida:\*\* La regla de \*\*"Disponibilidad por Día"\*\*. En la 

mayoría de los sistemas de cafeterías universitarias (como CafeFET), las reservas están 

restringidas a días laborables (Lunes a Viernes) y no se permiten fines de semana. El código 

actual permitiría reservar un pedido en Sábado o Domingo si el saldo y cantidad son correctos, 

lo cual es incorrecto según la política típica del negocio.



\---



\### Resumen de Errores y Correcciones Propuestas



| Error Detectado | Código Problemático | Regla de Negocio Incumplida | Explicación |

| :--- | :--- | :--- | :--- |

| \*\*Lógica de Saldo Confusa\*\* | `if est.saldo - sum(...) < -1000:` | \*\*Capacidad de Pago / 

Crédito\*\* | La condición rechaza el pedido si el saldo restante es menor a -1000. Lo lógico es 

rechazar si el saldo actual es menor que el costo total (`est.saldo < suma\_precios`). La lógica 

actual parece permitir una deuda enorme o tiene un umbral invertido. |

| \*\*Falta Validación de Día\*\* | (No existe en el código) | \*\*Restricción por Día\*\* | El sistema 

no verifica si el día es válido (ej. Lunes-Viernes). Permite reservas en fines de semana, 

violando la política operativa. |

| \*\*Estructura Lógica Final\*\* | `return 7 <= hora <= 18` | \*\*Validación Completa\*\* | Aunque la 

comparación de horas parece correcta para un rango cerrado, si el código se usa como función de 

validación principal, debe devolver `False` explícitamente si falla cualquier condición. 

Actualmente, si pasa las dos `if`, devuelve el resultado de la hora. Si la hora es inválida, 

devuelve `False`. \*\*Sin embargo\*\*, si el error es que permite horas fuera del rango (ej. 19:00) 

por algún motivo oculto, o si el tipo de dato de `hora` no es compatible con la comparación 

numérica directa en todos los casos. |



\### Código Corregido Sugerido



Asumiendo las reglas estándar de CafeFET (Max 6 productos, saldo suficiente, horario 7-18, solo 

días laborables):



```python

def crear\_pedido(est, productos, hora):

&#x20;   # Regla 1: Límite de cantidad de productos

&#x20;   if len(productos) > 6:

&#x20;       return False

&#x20;   

&#x20;   # Regla 2: Validación de saldo (Debe cubrir el costo total)

&#x20;   # Se asume que est.saldo es el dinero disponible y sum(p.precio...) es el costo

&#x20;   costo\_total = sum(p.precio for p in productos)

&#x20;   

&#x20;   # Si el saldo es menor que el costo, no se puede pagar. 

&#x20;   # Nota: Si el negocio permite crédito hasta -1000, la lógica sería diferente, 

&#x20;   # pero lo estándar es saldo >= costo.

&#x20;   if est.saldo < costo\_total:

&#x20;       return False

&#x20;       

&#x20;   # Regla 3: Validación del día de la semana (Ejemplo: Lunes a Viernes)

&#x20;   # Asumiendo que 'est' tiene un atributo 'dia' con valor numérico o string

&#x20;   dias\_validos = \[1, 2, 3, 4, 5] # Ejemplo: 1=Lun, 5=Viernes

&#x20;   if est.dia not in dias\_validos: 

&#x20;       return False

&#x20;       

&#x20;   # Regla 4: Validación del horario (7:00 a 18:00)

&#x20;   # Asumiendo 'hora' es un entero de minutos desde medianoche o objeto time compatible

&#x20;   if not (7 <= hora <= 18):

&#x20;       return False



&#x20;   return True

```



\*\*Nota sobre el error del saldo específico:\*\* Si la regla de negocio específica de CafeFET 

permite una deuda máxima de 1000 unidades, la condición original `est.saldo - costo < -1000` 

intentaría decir "Si el saldo restante es menor a -1000 (es decir, si la deuda supera 1000), 

rechaza". Sin embargo, la forma de escribirlo suele ser confusa. La interpretación más segura 

para un sistema robusto es:

`if est.saldo < costo\_total + 1000:` (si permite crédito hasta 1000) o simplemente `if 

est.saldo < costo\_total:` (sin crédito). Dado que el código original parece tener una lógica de 

"umbral negativo", es probable que sea un error de escritura y debería ser una comparación 

directa de insuficiencia.



