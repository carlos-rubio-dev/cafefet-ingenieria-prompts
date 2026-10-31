```python
def crear_pedido(estudiante, productos, hora_pedido):
    """
    Valida si un estudiante puede realizar un pedido en CafeFET.
    
    Parámetros:
        estudiante (dict): Diccionario con la clave 'saldo' (float).
        productos (list): Lista de diccionarios con claves 'nombre', 'precio' y 'estado' 
('disponible' o 'agotado').
        hora_pedido (datetime.datetime): Objeto datetime representando la hora del pedido.
    
    Retorna:
        dict: {
            'valido': bool,
            'mensaje': str,
            'saldo_final': float (si es válido),
            'total': float (si es válido)
        }
    """
    import datetime
    
    # Regla 1: Horario de atención (Lunes a sábado, 7:00 a 18:00)
    if not (7 <= hora_pedido.hour < 18):
        return {
            'valido': False,
            'mensaje': "El horario de atención es de 7:00 a 18:00.",
            'saldo_final': None,
            'total': None
        }
    
    # Nota: Se asume que el día de la semana se puede inferir del objeto datetime si fuera 
necesario,
    # pero como no se especifica en los datos de entrada (solo hora), 
    # y la restricción dice "Lunes a sábado", indicaremos que falta el dato del día.
    # Para este ejemplo, asumiremos que 'hora_pedido' tiene un atributo 'weekday()' donde 
0=Monday...6=Sunday.
    if not hasattr(hora_pedido, 'weekday'):
        return {
            'valido': False,
            'mensaje': "Falta el dato del día de la semana en la hora del pedido.",
            'saldo_final': None,
            'total': None
        }
    
    # Verificar día (0=Lunes, 6=Domingo)
    if hora_pedido.weekday() == 6: # Domingo
        return {
            'valido': False,
            'mensaje': "Los pedidos solo se reciben de lunes a sábado.",
            'saldo_final': None,
            'total': None
        }

    saldo = estudiante.get('saldo', 0)
    
    # Regla 2: Máximo 5 productos por pedido
    if len(productos) > 5:
        return {
            'valido': False,
            'mensaje': "Se permite un máximo de 5 productos por pedido.",
            'saldo_final': None,
            'total': None
        }

    # Regla 3 y 4: Validar productos agotados y saldo negativo
    total_pedido = 0
    productos_validos = []
    
    for prod in productos:
        precio = prod.get('precio', 0)
        estado = prod.get('estado', '')
        
        # Si el producto está agotado, no se puede pedir
        if estado == 'agotado':
            return {
                'valido': False,
                'mensaje': "No se pueden pedir productos con estado 'agotado'.",
                'saldo_final': None,
                'total': None
            }
        
        total_pedido += precio
        productos_validos.append(prod)

    # Regla 5: Saldo nunca puede quedar negativo
    if saldo < total_pedido:
        return {
            'valido': False,
            'mensaje': "El saldo del carné no es suficiente para cubrir el pedido.",
            'saldo_final': None,
            'total': None
        }

    # Si pasamos todas las validaciones anteriores, el pedido es válido
    saldo_final = saldo - total_pedido
    
    return {
        'valido': True,
        'mensaje': "Pedido realizado con éxito.",
        'saldo_final': saldo_final,
        'total': total_pedido
    }

# --- Explicación de las validaciones realizadas ---
"""
1. Validación de Horario: Se comprueba que la hora del pedido esté entre 7 y 18 horas. 
   Si no cumple, se rechaza inmediatamente.
2. Validación de Día de la Semana: Se verifica que el día sea diferente al domingo (weekday() 
== 6).
   Nota: Esta regla depende de que el objeto datetime tenga el método weekday().
3. Validación de Cantidad: Se asegura que la lista de productos no supere los 5 elementos.
4. Validación de Estado del Producto: Se recorre la lista y se rechaza si alguno tiene estado 
'agotado'.
   Si hay un producto agotado, el pedido completo se cancela.
5. Validación Financiera: Se calcula el total del pedido y se compara con el saldo del 
estudiante.
   Si el saldo resultante sería negativo (saldo < total), el pedido se rechaza.

Nota sobre la Regla 6 ("Si el pedido no se recoge dentro de los 30 minutos..."):
Esta regla describe una consecuencia futura o un proceso post-validación inicial. 
Dado que la función `crear_pedido` valida si el estudiante *puede realizar* el pedido en este 
momento,
no es posible implementar la lógica de "espera por recolección" ni la devolución automática del 
saldo 
sin datos adicionales como:
- La hora actual real del sistema (para calcular los 30 minutos futuros).
- Un mecanismo para registrar el inicio del pedido y monitorear su estado.
Por lo tanto, esta regla se indica como requerida en un flujo de trabajo más amplio o una 
función asíncrona, 
pero no bloquea la validación inicial del pedido en sí misma.
"""
```
