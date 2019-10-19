def get_city_country(city, country, population=''):
    """获取格式化的城市及国家的字符串"""
    if population:
        city_country = city.title() + ',' + country.title() + ' - population ' + population
    else:
        city_country = city.title() + ',' + country.title()
    return city_country