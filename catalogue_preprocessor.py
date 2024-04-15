import json
from typing import List

from catalogoT import CatalogoColoniasCoordenadas, CatalogoColoniasPuntos


def calcular_centroide(coordenadas: List[List[float]]) -> List[float]:
    x_coords = [c[0] for c in coordenadas]
    y_coords = [c[1] for c in coordenadas]
    centroide_x = sum(x_coords) / len(x_coords)
    centroide_y = sum(y_coords) / len(y_coords)
    return [centroide_x, centroide_y]


def procesar_colonias(archivo_entrada: str, archivo_salida: str) -> None:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        datos: CatalogoColoniasCoordenadas = json.load(file)

    nuevas_colonias = []
    for colonia in datos["features"]:
        coordenadas = colonia["geometry"]["coordinates"][0]  # Asumiendo polígonos simples
        centroide = calcular_centroide(coordenadas)
        nueva_colonia = {"type": "Feature", "properties": colonia["properties"],  # Copiando las propiedades originales
                         "geometry": {"type": "Point", "coordinates": centroide}}
        nuevas_colonias.append(nueva_colonia)

    nuevo_json: CatalogoColoniasPuntos = {"type": "FeatureCollection", "crs": datos["crs"], "features": nuevas_colonias}

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        json.dump(nuevo_json, file, ensure_ascii=False, indent=4)


def main() -> None:
    # Usar las funciones
    archivo_entrada = 'datos/catálogo-de-colonias.json'
    archivo_salida = 'datos/colonias_centroides.json'
    procesar_colonias(archivo_entrada, archivo_salida)
    print("El archivo de centroides ha sido creado exitosamente.")


if __name__ == '__main__':
    main()
