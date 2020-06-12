import requests

query = 'Siapa kucing tercantik?'
api_result = requests.get('http://api.serpstack.com/search?access_key=392fb6da2083ccf6427359826b72f2aa&query=' + query + '&engine=google&google_domain=google.co.id&page=1&output=json&%20location=surabaya')
api_response = api_result.json()

for number, result in enumerate(api_response['organic_results']):
    if result['snippet'] != '':
        print(result['snippet'])
    break	
    
