import unittest

import categorias
from main import normalizar_texto, clasificar_texto, cargar_tweets


class TestTextoUtils(unittest.TestCase):

    def setUp(self):
        # Configuración previa a cada test.
        self.texto = "Hola, ¿cómo estás? ¡Bien, gracias!"
        self.texto_clasificar = ("PELEAN a BALAZOS LOMAS de SAN LORENZO Así acabaron muertos a tiros y en la calle, "
                                 "dos hombres. Dos días después, sujetos atacaron a balazos su velorio. Ahí mataron a "
                                 "otro más. Es la peligrosa @Alc_Iztapalapa @SSC_CDMX y @FiscaliaCDMX indagan.  "
                                 "Detalles #C4EnAlerta")
        self.categorias = categorias.obtener_categorias()

    def test_normalizar_texto(self):
        # Test para la función normalizar_texto
        resultado_esperado = ['hola', 'cómo', 'bien', 'gracias']
        self.assertEqual(normalizar_texto(self.texto), resultado_esperado)

    def test_clasificar_texto(self):
        # Test para la función clasificar_texto
        resultado_esperado = ["Homicidio doloso", 'Lesiones dolosas por disparo de arma de fuego']
        self.assertEqual(clasificar_texto(self.texto_clasificar, self.categorias), resultado_esperado)

    def test_clasificar_texto_sin_coincidencias(self):
        # Test para asegurar que la función clasificar_texto retorna una lista vacía si no hay coincidencias
        texto = "¡Hoy es un gran día para caminar!"
        resultado_esperado = []
        self.assertEqual(clasificar_texto(texto, self.categorias), resultado_esperado)

    def test_cargar_tweets_excepcion(self):
        # Test para verificar que cargar_tweets maneja correctamente los errores de archivos no encontrados
        with self.assertRaises(FileNotFoundError):
            cargar_tweets('ruta_inexistente.json')


# Esta parte permite ejecutar las pruebas si este archivo se ejecuta como script principal
if __name__ == '__main__':
    unittest.main()
