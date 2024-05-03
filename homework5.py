my_list = ["яблоко", "киви", "груша", "мандарин", "ананас"]

print(my_list)
print([my_list[0], my_list[-1]])
print(my_list[2:6])

my_list[2] = "апельсин"

print(my_list)

my_dict = {"яблоко":"apple", "киви":"kiwi", "груша":"pear", "мандарин":"tangerine", "ананас":"pineapple"}
print(my_dict)
print(my_dict["яблоко"])
# меняем названия
my_dict["яблоко"] = "ibloko"
my_dict["киви"] = "kewe"
my_dict["груша"] = "grusha"
my_dict["мандарин"] = "mandarin"
my_dict["ананас"] = "ananas"
# добавляем элемент
my_dict["лимон"] = "lemon"

print(my_dict)