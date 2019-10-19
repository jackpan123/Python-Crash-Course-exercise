import unittest
from city_function import get_city_country

class CityTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_country(self):
        """是否可以正确处理像santiago,chile这样的字符串"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago,Chile')

    def test_city_country_population(self):
        """是否可以正确处理像santiago,chile,5000000这样的字符串"""
        city_country = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country, 'Santiago,Chile - population 5000000')


unittest.main()