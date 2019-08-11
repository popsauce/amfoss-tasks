import requests

value = input()

headers = {
	'apikey': 'c33c7760-b114-11e9-9ecd-dbd875d36465',
}

params = (
	('q', value),
	('location', 'India'),
	('search_engine', 'google.com'),
	('gl', 'IN'),
	('hl', 'en')
)

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
