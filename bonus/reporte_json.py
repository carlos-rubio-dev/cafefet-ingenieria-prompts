"""Salida estructurada: pedidos de CafeFET validados con Pydantic."""

import argparse
from typing import Literal

from pydantic import BaseModel
from comun import preguntar


class Producto(BaseModel):
    nombre: str
    cantidad: int | None


class ReportePedido(BaseModel):
    tipo: Literal["pedido", "consulta", "cancelacion"]
    productos: list[Producto]
    hora_recogida: str | None
    observaciones: str | None
    requiere_aclaracion: bool
    aclaracion: str | None


REPORTES = [
    "Quiero un café con leche y dos empanadas para recoger a las 9:00.",
    "Necesito tres jugos de naranja para las 10 de la mañana.",
    "Quiero pedir algo para comer, todavía no sé qué.",
    "Me gustaría dos empanadas, pero no recuerdo a qué hora puedo recogerlas.",
    "¿Qué productos tienen disponibles hoy?",
    "Cancela mi pedido de un café que iba a recoger a las 11:00."
]


def procesar_reporte(texto, modelo):
    prompt = f"""
    Analiza el siguiente mensaje de un usuario de CafeFET.

    Extrae la información y devuelve únicamente los datos
    que correspondan al esquema JSON.

    Reglas:
    - tipo debe ser pedido, consulta o cancelacion.
    - Identifica los productos y sus cantidades.
    - Si se menciona un producto en singular sin cantidad,
      interpreta que solicita una unidad.
    - No inventes productos, cantidades ni horas.
    - Si no se proporciona una cantidad, utiliza null,
      excepto cuando el producto esté en singular.
    - Si no se proporciona una hora, utiliza null.
    - Para los pedidos, si falta la hora de recogida,
      requiere_aclaracion debe ser true.
    - Si faltan productos o la información es ambigua,
      requiere_aclaracion debe ser true.
    - Las consultas generales sobre disponibilidad
      no necesitan aclaración.
    - Si requiere_aclaracion es true, explica qué información falta.
    - Si no hay observaciones, utiliza null.
    - Si el mensaje es una consulta, no inventes un pedido.

    Mensaje:
    {texto}
    """

    respuesta = preguntar(
        prompt,
        modelo=modelo,
        formato=ReportePedido.model_json_schema()
    )

    return ReportePedido.model_validate_json(
        respuesta.message.content
    )


parser = argparse.ArgumentParser()
parser.add_argument("--modelo", default="qwen3.5:4b")
args = parser.parse_args()

for i, texto in enumerate(REPORTES, start=1):
    print(f"\n{'=' * 50}")
    print(f"CASO {i}: {texto}")

    try:
        reporte = procesar_reporte(texto, args.modelo)
        print(reporte.model_dump_json(indent=2))

    except Exception as error:
        print(f"Error al procesar el caso: {error}")
