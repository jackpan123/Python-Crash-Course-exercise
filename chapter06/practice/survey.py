favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

survey = ['jen', 'sarah', 'edward', 'phil', 'jack', 'pan']

for name in survey:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for survey!")
    else:
        print(name.title() + ", woulid you like to accept my survey?")
