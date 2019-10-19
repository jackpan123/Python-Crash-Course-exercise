def make_car(manufacturer, model, **car_info):
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model

    for key, value in car_info.items():
        car_profile[key] = value

    return car_profile

car_profile = make_car('subaru', 'ourback', color='blue', tow_package=True)
print(car_profile)