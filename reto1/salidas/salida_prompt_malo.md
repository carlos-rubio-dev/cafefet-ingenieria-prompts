Para crear una función robusta para gestionar pedidos, necesitamos definir qué datos son 

esenciales (ID del cliente, productos, cantidades, precios) y cómo calcular el total.



A continuación, te presento una solución completa utilizando \*\*JavaScript\*\* (que es universal y 

fácil de adaptar a otros lenguajes como Python o C#). He incluido validaciones básicas y un 

cálculo automático del subtotal e impuestos.



\### Ejemplo en JavaScript



Esta función crea un objeto `pedido` con todos los detalles necesarios y valida que no se 

agreguen productos sin cantidad ni precio.



```javascript

/\*\*

&#x20;\* Función para crear un nuevo pedido

&#x20;\* @param {string} clienteId - Identificador único del cliente

&#x20;\* @param {Array} items - Array de objetos { nombre, cantidad, precioUnitario }

&#x20;\* @param {number} impuestoPorcentaje - Porcentaje de impuestos (ej. 16)

&#x20;\* @returns {Object} El objeto pedido creado con todos los cálculos

&#x20;\*/

function crearPedido(clienteId, items, impuestoPorcentaje = 0) {

&#x20;   // Validaciones iniciales

&#x20;   if (!clienteId || clienteId.trim() === "") {

&#x20;       throw new Error("El ID del cliente es obligatorio.");

&#x20;   }



&#x20;   if (!Array.isArray(items)) {

&#x20;       throw new Error("La lista de productos debe ser un array.");

&#x20;   }



&#x20;   let subtotal = 0;

&#x20;   

&#x20;   // Procesar cada ítem del pedido

&#x20;   items.forEach(item => {

&#x20;       const cantidad = item.cantidad || 0;

&#x20;       const precio = item.precioUnitario || 0;



&#x20;       if (cantidad <= 0 || isNaN(cantidad)) {

&#x20;           throw new Error(`La cantidad para "${item.nombre}" debe ser un número positivo.`);

&#x20;       }

&#x20;       

&#x20;       if (isNaN(precio) || precio < 0) {

&#x20;           throw new Error(`El precio unitario para "${item.nombre}" es inválido.`);

&#x20;       }



&#x20;       const totalItem = cantidad \* precio;

&#x20;       subtotal += totalItem;

&#x20;   });



&#x20;   // Calcular impuestos y total final

&#x20;   const impuestoTotal = subtotal \* (impuestoPorcentaje / 100);

&#x20;   const totalFinal = subtotal + impuestoTotal;



&#x20;   // Construir el objeto pedido

&#x20;   return {

&#x20;       idPedido: Date.now().toString(), // Genera un ID único basado en la fecha

&#x20;       clienteId: clienteId,

&#x20;       fechaCreacion: new Date().toISOString(),

&#x20;       items: items.map(item => ({

&#x20;           nombre: item.nombre,

&#x20;           cantidad: item.cantidad,

&#x20;           precioUnitario: item.precioUnitario,

&#x20;           totalItem: (item.cantidad \* item.precioUnitario).toFixed(2)

&#x20;       })),

&#x20;       subtotal: subtotal.toFixed(2),

&#x20;       impuestoPorcentaje: impuestoPorcentaje,

&#x20;       impuestoTotal: impuestoTotal.toFixed(2),

&#x20;       totalFinal: totalFinal.toFixed(2)

&#x20;   };

}



// --- Ejemplo de uso ---



const pedidoEjemplo = crearPedido(

&#x20;   "C001", 

&#x20;   \[

&#x20;       { nombre: "Laptop", cantidad: 1, precioUnitario: 800 },

&#x20;       { nombre: "Mouse", cantidad: 2, precioUnitario: 25 }

&#x20;   ],

&#x20;   16 // 16% de IVA

);



console.log("Pedido creado:", pedidoEjemplo.idPedido);

console.log(`Total a pagar: $${pedidoEjemplo.totalFinal}`);

```



\### Explicación de la lógica



1\.  \*\*Validaciones\*\*: Antes de procesar, verificamos que el cliente exista y que los productos 

tengan cantidades y precios válidos. Esto evita errores en base de datos o cálculos 

incorrectos.

2\.  \*\*Cálculo Automático\*\*: La función suma automáticamente `cantidad \* precio` 

para obtener el subtotal, luego aplica el porcentaje de impuestos y calcula el total final.

3\.  \*\*Generación de ID\*\*: Se utiliza `Date.now()` para generar un identificador único basado en 

la hora actual del sistema. En una aplicación real, esto podría venir de una base de datos o 

ser asignado por un servidor.

4\.  \*\*Formato de Moneda\*\*: Se usa `.toFixed(2)` para asegurar que los precios siempre muestren 

dos decimales (centavos), evitando problemas de precisión flotante en JavaScript.



\### ¿Cómo adaptarlo a tu caso?



Si necesitas esta función en otro lenguaje o con requisitos específicos, por favor indícamelo:

\*   \*\*Lenguaje:\*\* ¿Prefieres Python, C#, Java o PHP?

\*   \*\*Base de Datos:\*\* ¿Necesitas que la función también inserte los datos en una base de datos 

(SQL)?

\*   \*\*Especificidades:\*\* ¿Hay algún campo extra que deba incluirse (ej. dirección de envío, 

método de pago)?

