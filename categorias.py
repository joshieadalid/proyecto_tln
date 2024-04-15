from typing import Dict, List

# Diccionario que almacena las categorías y sus respectivas palabras clave
CATEGORIAS: Dict[str, List[str]] = {
    "Robo a transeúnte en vía pública": ["robo", "transeúnte", "vía pública", "sin violencia", "con violencia",
                                         "asaltar"],
    "Robo de vehículo": ["robo", "vehículo", "coche", "auto", "sin violencia", "con violencia"],
    "Robo a negocio con violencia": ["robo", "negocio", "tienda", "con violencia"],
    "Robo a repartidor": ["robo", "repartidor", "entrega", "sin violencia", "con violencia"],
    "Robo a pasajero a bordo del metro": ["robo", "pasajero", "metro", "sin violencia", "con violencia"],
    "Violación": ["violación", "abuso sexual"], "Homicidio doloso": ["homicidio", "doloso", "asesinato", "matar"],
    "Lesiones dolosas por disparo de arma de fuego": ["lesiones", "dolosas", "disparo", "arma de fuego", "balazo"],
    "Robo a pasajero a bordo de microbús": ["robo", "pasajero", "microbús", "sin violencia", "con violencia"],
    "Robo a casa habitación con violencia": ["robo", "casa", "habitación", "domicilio", "con violencia"],
    "Robo a cuentahabiente saliendo del cajero con violencia": ["robo", "cuentahabiente", "cajero", "con violencia"],
    "Robo a pasajero a bordo de taxi": ["robo", "pasajero", "taxi", "con violencia"],
    "Robo a transportista": ["robo", "transportista", "carga", "sin violencia", "con violencia"],
    "Secuestro": ["secuestro", "plagiado", "raptado"]}


def obtener_categorias() -> Dict[str, List[str]]:
    """
    Retorna el diccionario de categorías.
    """
    return CATEGORIAS
