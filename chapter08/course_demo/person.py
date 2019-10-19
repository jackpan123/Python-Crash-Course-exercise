def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musican = build_person('jimi', 'hendrix', age=23)
print(musican)