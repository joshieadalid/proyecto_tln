import re
from typing import List, Optional


def normalizar_texto(texto: str) -> str:
    texto = texto.lower()  # convertir a minúsculas
    texto = re.sub(r'á', 'a', texto)
    texto = re.sub(r'é', 'e', texto)
    texto = re.sub(r'í', 'i', texto)
    texto = re.sub(r'ó', 'o', texto)
    texto = re.sub(r'ú', 'u', texto)
    texto = re.sub(r'[^\w\s]', '', texto)  # eliminar puntuación
    return texto


def maxima_puntuacion(texto: str, frase: str) -> int:
    if frase in texto:
        return 100  # máxima puntuación por coincidencia exacta
    else:
        return 0  # no hay coincidencia


def identificar_frase(texto: str, frases: List[str]) -> Optional[str]:
    texto_preprocesado = normalizar_texto(texto)
    mejor_puntuacion = 0
    mejor_frase = None

    for frase in frases:
        frase_normalizada = normalizar_texto(frase)
        puntuacion = maxima_puntuacion(texto_preprocesado, frase_normalizada)
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_frase = frase

    return mejor_frase


def main():
    frases: List[str] = ["Lomas de San Lorenzo", "El Rosario", "La Herradura"]
    texto: str = "pelean a balazos lomas de san lorenzo..."
    frase_seleccionada: Optional[str] = identificar_frase(texto, frases)
    print(f"Frase seleccionada: {frase_seleccionada}")


if __name__ == '__main__':
    main()
