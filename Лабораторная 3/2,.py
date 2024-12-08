# TODO Напишите функцию find_common_participants
def find_common_participants(g1, g2, k=','):
	u1 = set(g1.split(k))
	u2 = set(g2.split(k))
	s = u1.intersection(u2)
	return sorted(s)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
