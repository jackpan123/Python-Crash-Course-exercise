def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关于用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile

profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(profile)
    # for key, value in user_profile_1.items():
    #     print(key + " " + value)