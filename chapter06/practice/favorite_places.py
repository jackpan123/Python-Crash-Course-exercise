favorite_places = {
    'jack': ['beijing', 'paris'],
    'pan': ['neil'],
    'rose': ['new york'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favorite place is " + places[0].title())
    else:
        print("\n" + name.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place.title())