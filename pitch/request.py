import urllib.request,json
from pitch.models import Quote


def get_quote():
    get_quote_url='http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        quote_data=url.read()
        quote_response=json.loads(quote_data)

        quote_results = None

        if quote_response:
            author = quote_response.get('author')
            quote = quote_response.get('quote')

        quote_results = Quote(author,quote)

    return quote_results