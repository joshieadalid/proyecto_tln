import re
from typing import List, Dict, KeysView, Optional

import nltk
from nltk.corpus import stopwords

import alcaldias_b
import catalogoT
import categorias as cats
from tweetT import Tweet, cargar_tweets


def normalizar_texto(texto: str) -> List[str]:
    # Remover puntuaciones y convertir a minúsculas
    palabras = re.findall(r'\b\w+\b', texto.lower())
    # Filtrar palabras de parada
    stop_words = set(stopwords.words('spanish'))
    return [palabra for palabra in palabras if palabra not in stop_words]


def clasificar_texto(texto: str, categorias: Dict[str, List[str]]) -> List[str]:
    palabras_texto: set[str] = set(normalizar_texto(texto))
    coincidencias: Dict[str, int] = {}
    texto_limpio: str = texto.lower()

    for categoria, frases_clave in categorias.items():
        for frase in frases_clave:
            if frase in texto_limpio or any(palabra in palabras_texto for palabra in frase.split()):
                coincidencias[categoria] = coincidencias.get(categoria, 0) + 1

    return sorted(coincidencias, key=coincidencias.get, reverse=True)


def print_detalles(tweet) -> None:
    detalles = f"""
    Texto del tweet: {tweet['text']}
    Usuario: {tweet['user']['name']} (@{tweet['user']['username']})
    Fecha: {tweet['date']}
    Likes: {tweet['stats']['likes']}, Retweets: {tweet['stats']['retweets']}
    """
    print(detalles)


def main() -> None:
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    tweets: list[Tweet] = cargar_tweets('datos/tweets.json')
    print(f"Se cargaron {len(tweets)} tweets.")
    tweet = tweets[1]
    print_detalles(tweet)

    texto_tweet: str = tweet['text']
    categorias: dict[str, list[str]] = cats.obtener_categorias()
    categorias_tweet: list[str] = clasificar_texto(texto_tweet, categorias)
    print(f"Categorías encontradas: {categorias_tweet}")
    catalogo: KeysView[str] = catalogoT.cargar_colonias('datos/colonias_centroides.json').keys()
    colonias: list[str] = list(catalogo)
    colonia: Optional[str] = alcaldias_b.identificar_frase(texto_tweet, colonias)
    print(f"Colonia: {colonia}")


if __name__ == '__main__':
    main()
