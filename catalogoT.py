import json
from typing import TypedDict, List, Dict


class CrsProperty(TypedDict):
    name: str


class Crs(TypedDict):
    type: str
    properties: CrsProperty


class FeatureProperty(TypedDict):
    cve_ent: str
    entidad: str
    cve_alc: str
    alc: str
    cve_col: str
    colonia: str
    clasif: str


class Geometry(TypedDict):
    type: str
    coordinates: List[List[List[float]]]


class Feature(TypedDict):
    type: str
    properties: FeatureProperty
    geometry: Geometry


class CatalogoColoniasCoordenadas(TypedDict):
    type: str
    crs: Crs
    features: List[Feature]


# Clase convertida
class PointGeometry(TypedDict):
    type: str
    coordinates: List[float]  # Cambio aquí para adaptarse a una estructura de punto


# Puedes usarlo con la misma estructura de Feature si lo deseas
class PointFeature(TypedDict):
    type: str
    properties: FeatureProperty
    geometry: PointGeometry


# Ejemplo de cómo podría definirse el catálogo si solo tuviera puntos
class CatalogoColoniasPuntos(TypedDict):
    type: str
    crs: Crs
    features: List[PointFeature]


def cargar_colonias(filename: str) -> Dict[str, str]:
    with open(filename, 'r', encoding='utf-8') as f:
        data: CatalogoColoniasPuntos = json.load(f)
    colonias = {feature['properties']['colonia']: feature['properties']['alc'] for feature in data['features']}
    return colonias
