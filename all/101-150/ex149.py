# ex149: # Crie uma função que identifique as partes de uma URL.
from requests import get
from requests import exceptions

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.6422.113 Safari/537.36 "
        "Edg/125.0.2535.67"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": (
        '"Chromium";v="125", "Microsoft Edge";v="125", '
        '"Not.A/Brand";v="24"'
    ),
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "DNT": "1",
    "TE": "trailers"
}

def url_parts(URL: str):
    if "." not in URL:
        return "Invalid URL"
    if "http" not in URL:
        URL = f"https://www.{URL}"

    try:
        r = get(URL, headers=headers)
    except exceptions.ConnectionError as conn_e:
        return f"Erro de Conexão: {conn_e}"
    except exceptions.Timeout as timeout_e:
        return f"Tempo limite de tentativa de conexão: {timeout_e}"
    except exceptions.InvalidURL as inv_url_e:
        return f"URL inválida: {inv_url_e}"
    except Exception as e:
        return f"Erro: {e}"
    else:
        return r.url


if __name__ == "__main__":
    print(url_parts("google.com"))  # https://www.google.com/
    print(url_parts("nasa.gov"))  # https://www.nasa.gov/
    print(url_parts("unknoooooownnnn.com"))  # Erro de Conexão: HTTPSConnectionPool(host='www.unknoooooownnnn.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000002811896B110>: Failed to resolve 'www.unknoooooownnnn.com' ([Errno 11001] getaddrinfo failed)"))
    print(url_parts("cia.gov"))  # https://www.cia.gov/
