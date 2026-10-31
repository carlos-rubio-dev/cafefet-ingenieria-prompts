VEREDICTO: El proceso de creación de pedidos en CafeFET es una secuencia crítica que garantiza la integridad financiera, la 

operatividad del negocio y la satisfacción del estudiante usuario. Este flujo no debe ser un mero trámite administrativo, sino 

un sistema robusto de control preventivo diseñado para evitar errores humanos antes de que ocurran transacciones irreversibles. 

La primera validación indispensable es la verificación del saldo disponible en la cuenta del estudiante. El sistema debe 

consultar en tiempo real las reservas financieras y confirmar que el monto total del pedido solicitado no exceda los fondos 

disponibles. Esta validación es fundamental porque CafeFET opera bajo un modelo de crédito estudiantil estricto; sin ella, se 

generarían deudas impagables o se comprometería la solvencia de usuarios con dificultades económicas. Si el saldo es 

insuficiente, el sistema debe bloquear inmediatamente la creación del pedido y presentar al usuario una notificación clara 

indicando el monto faltante, obligándolo a realizar un depósito antes de continuar.



La segunda validación crucial es la comprobación de los horarios de atención. El sistema debe restringir la capacidad de crear 

pedidos exclusivamente dentro de las franjas horarias operativas definidas para cada ubicación física o virtual. Permitir 

pedidos fuera de horario no solo generaría caos logístico en la cocina, sino que también violaría los acuerdos contractuales con 

el personal de servicio. Cuando un intento se realiza fuera del horario permitido, el sistema debe rechazar la solicitud y 

sugerir al usuario las horas disponibles más cercanas, fomentando una planificación adecuada de su tiempo libre.



También es imperativo validar los días permitidos de operación. CafeFET tiene días cerrados específicos donde no se atiende a 

ningún cliente; intentar crear un pedido en estos días debe resultar en un error inmediato. Esta regla protege la seguridad del 

personal y asegura que el negocio funcione solo cuando está plenamente operativo. Además, la disponibilidad de productos es una 

validación dinámica y vital. El sistema debe verificar si los artículos seleccionados están en stock real antes de confirmar el 

pedido. Si un producto agotado o con baja cantidad se incluye en el carrito, el pedido no puede ser aceptado. Esto previene la 

frustración del cliente al recibir un pedido incompleto o productos defectuosos y permite al personal reordenar materiales a 

tiempo.



Finalmente, debe existir una validación sobre el límite de productos por transacción para evitar abusos o errores de cálculo 

masivos que puedan saturar el sistema. Si un usuario intenta añadir más cantidad de un mismo producto del que está permitido en 

un solo pedido, la creación debe fallar. Cuando cualquier una de estas reglas no se cumple, el proceso de creación debe 

detenerse automáticamente sin generar ningún registro de transacción pendiente. El sistema debe mostrar al estudiante un mensaje 

de error específico que identifique exactamente cuál fue la causa del rechazo (falta de saldo, horario incorrecto, producto 

agotado, etc.), permitiendo una corrección rápida y directa antes de intentar nuevamente el proceso.



