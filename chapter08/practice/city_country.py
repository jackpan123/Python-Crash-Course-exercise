def city_country(city, country):
    full_city_name = '"' + city.title() + ' ' + country.title() + '"'
    return full_city_name

print(city_country('fuzhou', 'china'))
print(city_country('fuan', 'china'))
print(city_country('suyang', 'china'))