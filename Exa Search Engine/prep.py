from exa_py import Exa

exa = Exa('8967131c-2976-4e4b-878e-72f1f6d1752a')
query = input('Search here: ')

response = exa.search(
    query,
    num_results=5,
    type='keyword',
    include_domains=['https://www.google.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()
