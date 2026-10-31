
"""Evaluación de prompts A/B para clasificar mensajes de CafeFET.

    uv run evalua.py
    uv run evalua.py --modelo qwen3.5:0.8b
"""

import argparse
import re
from comun import preguntar


# 10 casos etiquetados manualmente.
# Los casos 3, 6, 9 y 10 presentan cierta ambigüedad.

CASOS = [
    ("Quiero dos empanadas y un jugo para recoger a las 10:00.", "PEDIDO"),
    ("Guárdame un café con leche para las 9 de la mañana.", "PEDIDO"),
    ("Quiero pedir algo para desayunar, ¿qué me recomiendas?", "CONSULTA"),
    ("¿Hasta qué hora puedo hacer pedidos?", "CONSULTA"),
    ("Cancela mi pedido de dos empanadas.", "CANCELACION"),
    ("Ya no voy a poder pasar por lo que pedí.", "CANCELACION"),
    ("Me descontaron el dinero de la tarjeta, pero no recibí mi pedido.", "RECLAMO"),
    ("El jugo que me entregaron estaba en mal estado.", "RECLAMO"),
    ("Lo de siempre para las 10:00.", "PEDIDO"),
    ("No aparece mi pedido, ¿qué pasó?", "RECLAMO"),
]


# V1: prompt sencillo, sin definiciones ni ejemplos.

V1 = """Clasifica el mensaje de un usuario de CafeFET en UNA categoría:
PEDIDO, CONSULTA, CANCELACION o RECLAMO.
Responde solo con la categoría.
Mensaje: "{reporte}"
"""


# V2: prompt con definiciones y ejemplos.

V2 = """Clasifica el mensaje de un usuario de CafeFET en UNA categoría.

- PEDIDO: el usuario quiere solicitar uno o varios productos.
- CONSULTA: el usuario pregunta por productos, precios, horarios
  o información, sin solicitar una cancelación ni reportar un problema.
- CANCELACION: el usuario quiere cancelar un pedido realizado
  o informa que ya no va a recogerlo.
- RECLAMO: el usuario informa un problema con su pedido,
  el pago, los productos o el servicio.

Ejemplos:
"Quiero dos empanadas para las 10." -> PEDIDO
"¿Qué bebidas tienen disponibles?" -> CONSULTA
"Cancela mi pedido de café." -> CANCELACION
"Me cobraron, pero no recibí el pedido." -> RECLAMO

Si el mensaje es ambiguo, identifica la intención más probable
sin inventar información.

Responde únicamente con PEDIDO, CONSULTA, CANCELACION o RECLAMO.

Mensaje: "{reporte}"
"""


def clasificar(plantilla, reporte, modelo):
    respuesta = preguntar(
        plantilla.format(reporte=reporte),
        modelo=modelo,
        num_predict=20
    )

    texto = respuesta.message.content.upper()

    coincidencia = re.search(
        r"\b(PEDIDO|CONSULTA|CANCELACION|RECLAMO)\b",
        texto
    )

    return coincidencia.group(0) if coincidencia else texto.strip()


ap = argparse.ArgumentParser()
ap.add_argument("--modelo", default="qwen3.5:4b")
a = ap.parse_args()


print(f"Modelo utilizado: {a.modelo}")
print(f"Total de casos: {len(CASOS)}\n")

for nombre, plantilla in [("v1", V1), ("v2", V2)]:
    ok = 0

    print(f"===== RESULTADOS {nombre.upper()} =====")

    for i, (reporte, esperado) in enumerate(CASOS, start=1):
        obtenido = clasificar(plantilla, reporte, a.modelo)

        if obtenido == esperado:
            ok += 1
            estado = "CORRECTO"
        else:
            estado = "FALLO"

        print(f"Caso {i}: {estado}")
        print(f"Mensaje: {reporte}")
        print(f"Esperado: {esperado} | Obtenido: {obtenido}")
        print()

    print(f"Resultado {nombre}: {ok}/{len(CASOS)} casos correctos\n")
