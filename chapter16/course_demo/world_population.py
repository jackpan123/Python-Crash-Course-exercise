import json

from country_codes import get_country_code
# 将数据加载到一个列表中
filename = "chapter16/course_demo/data/population-data.json"
with open(filename) as f:
    pop_data = json.load(f)

    # 打印每个国家2010年到人口数量
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Region']
            population = int(float(pop_dict['Population']))

            code = get_country_code(country_name)
            if code:
                print(code + ": " + str(population))
            else:
                print('ERROR - ' + country_name)

            
