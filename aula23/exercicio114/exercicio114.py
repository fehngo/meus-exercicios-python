import urllib
import urllib.request

try:
    url = "http://www.pudim.com.br"

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    site = urllib.request.urlopen(req)
except URLError as erro:
    print(type(erro))
    print(f"Deu errado!! O erro encontrado foi: {erro}")
else:
    print("Tudo okkay")
