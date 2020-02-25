'''6. Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических и лабораторных 
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
не обязательно были все типы занятий. Сформировать словарь, содержащий название 
предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# 
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

my_dict = dict()

with open('text6.1.') as my_f:
    ilines = my_f.readlines()
    for i in ilines:
        i_spl = i.split()
        subject = i_spl[0]
        sum_auers = sum([int(x[:x.find('(')]) for x in i_spl[1:] if '(' in x])
        # Пока разбираюсь с этой строкой. Вероятно должен быть более простой аналог поиска чисел.
        my_dict[subject] = sum_auers

print(my_dict)
my_f.close()

# x = re.findall(i_spl)
# sum_auers = sum(x)