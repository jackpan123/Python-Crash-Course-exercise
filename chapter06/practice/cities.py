cities = {
    'fuan': {
        'country': 'china',
        'population': 220000,
        'fact': 'nice',
    },

    'fuzhou': {
        'country': 'china',
        'population': 2200000,
        'fact': 'like',
    },

    'hangzhou': {
        'country': 'china',
        'population': 230000,
        'fact': 'alibaba',
    },
}

for city, features in cities.items():
    print("\n" + city.title() + "'s feature is")
    print(features)