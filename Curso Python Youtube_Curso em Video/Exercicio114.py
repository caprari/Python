import urllib
import urllib.request

try:
    site = str(input('Informe o site para validação: (Ex: http://www.site.com.br): '))
    urllib.request.urlopen(site)
except urllib.error.URLError:
    print('Problemas para acessar o site informado!')
    print('   - 1) Verifique sua conexão!')
    print('   - 2) Verifique o site informado')
except:
    print('O site não foi informado corretamente no formato http://www.site.com.br!')
else:
    print('O site está acessível!')
