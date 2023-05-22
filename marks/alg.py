import pandas as pd
import json
import xlsxwriter

class GroupDistribution:
	def __init__(self):
		self.jsonobj = self.json_create()
		self.subjects = self.subjects_list_init()
		self.student_lessons = self.count_of_lessons_list_create()
		self.groups = self.groups_init()
		self.groups_number = self.groups_number_init()
		self.groups_sizes = {'Инженерная графика' : [10, 2, 'Инженерка'],
	'Будущее науки: янглийский язык для международных образовательных проектов' : [10, 2, 'Английский язык'],
	'Весёлый китайский язык' : [10, 2, 'Китайский язык'],
	'Основы рыночных механизмов' : [10, 2, 'Основы рыночных механизмов'],
	'Современная энергетика' : [10, 2, 'Современная энергетика'],
	'Экспериментальная химия' : [10, 2, 'Экспериментальная химия'],
	'Технологическое предпринимательство' : [10, 2, 'Тех. предпринимательство'],
	'Инженерный дизайн в программе Компас' : [10, 2, 'Компас'],
	'Электроника и схемотехника' : [10, 2, 'Электроника и схемотехника'],
	'Геодезия' : [10, 2, 'Геодезия'],
	'3D-моделирование в программе Blender' : [30, 2, 'Blender'],
	'Цифровое моделирование городской среды' : [10, 2, 'Моделирование городской среды'],
	'Основы программирования на PYTHON' : [10, 2, 'Python'],
	'Методы и средства измерений в радиоэлектронных системах' : [10, 2, 'Радиоэлектроника']}
		self.groups_filling()
		self.group_size_check()
		self.groups.update({'Резерв' : set()})
		self.group_count_check()
		self.none_distribute()
		self.group_size_check()
		self.group_count_check()

	def json_create(self):
		with open('tables/data.json', encoding='utf-8') as f:
			templates = json.load(f)
		json_res = {}
		for i in templates[::-1]:
			json_res.update({i[0][1] : {}})
			for j in range(1,len(i)):
				if j == 3 and i[j][1]:
					json_res[i[0][1]].update({'name' : i[j][1]})
				elif j == 4:
					json_res[i[0][1]].update({'mail' : i[j][1]})
				elif j == 8:
					json_res[i[0][1]].update({'turn1' : i[j][1]})
				elif j == 9:
					json_res[i[0][1]].update({'turn2' : i[j][1]})
				elif j == 10:
					json_res[i[0][1]].update({'turn3' : i[j][1]})
				else:
					json_res[i[0][1]].update({i[j][0] : i[j][1]})
		mails = set()
		names = set()
		for i in json_res.copy():
			if json_res[i]['mail'] not in mails and json_res[i]['name'] not in names:
				mails.add(json_res[i]['mail'])
				names.add(json_res[i]['name'])
			else:
				del json_res[i]
		return(json_res)

	# Создание групп
	def groups_init(self):
		groups = {}
		[groups.update({(i,1) : []}) for i in self.subjects]
		return(groups)

	# Создание списка предметов
	def subjects_list_init(self):
		subjects = set()
		for i in self.jsonobj:
			[subjects.add((self.jsonobj[i]["turn"+str(j)])) for j in range(1,4)]
		return(subjects)

	# Создание счетчика предметов у каждого ученика
	def count_of_lessons_list_create(self):
		student_lessons = {}
		for i in self.jsonobj:
			if self.jsonobj[i]["name"] not in student_lessons:
				student_lessons[self.jsonobj[i]["name"]] = 0

		return(student_lessons)

	# Создание счетчика групп по предмету
	def groups_number_init(self):
		groups_number = dict()
		for i in self.jsonobj:
			if self.jsonobj[i]["turn1"] not in groups_number:
				groups_number.update({self.jsonobj[i]["turn1"] : 1})
			if self.jsonobj[i]["turn2"] not in groups_number:
				groups_number.update({self.jsonobj[i]["turn2"] : 1})
			if self.jsonobj[i]["turn3"] not in groups_number:
				groups_number.update({self.jsonobj[i]["turn3"] : 1})

		return(groups_number)

	# Заполнение групп учениками и счетчика предметов у каждого ученика
	def groups_filling(self):
		for i in self.jsonobj:
			if self.jsonobj[i]["turn1"] in self.subjects:
				self.groups[(self.jsonobj[i]["turn1"],1)].append(self.jsonobj[i]["name"])
				self.student_lessons[self.jsonobj[i]["name"]] += 1

			if self.jsonobj[i]["turn2"] in self.subjects:
				self.groups[(self.jsonobj[i]["turn2"],1)].append(self.jsonobj[i]["name"])
				self.student_lessons[self.jsonobj[i]["name"]] += 1

	# Проверка размерности групп - создание новых групп
	def group_size_check(self):
		for subject in list(self.groups):
			temp = []
			if subject == 'Резерв':
				continue
			while len(self.groups[subject]) > self.groups_sizes[subject[0]][0]:
				temp.append(self.groups[subject][-1])
				self.groups[subject].pop(-1)
			ex = {}
			if len(temp) % self.groups_sizes[subject[0]][0] != 0:
				for i in range(len(temp) // self.groups_sizes[subject[0]][0]):
					self.groups_number[subject[0]] += 1
					ex.update({i : []})
					for student in range(self.groups_sizes[subject[0]][0]):
						ex[i].append(temp[-1])
						temp.pop(-1)
			else:
				for i in range(len(temp) // self.groups_sizes[subject[0]][0]):
					self.groups_number[subject[0]] += 1
					ex.update({i : []})
					for student in range(self.groups_sizes[subject[0]][0]):
						ex[i].append(temp[-1])
						temp.pop(-1)
			for i in ex:
				self.groups.update({(subject[0], self.groups_number[subject[0]]+i) : ex[i]})

	# Проверка количества групп, добавление лишних в резерв
	def group_count_check(self):
		temp = []
		for subject in list(self.groups.copy())[::-1]:
			if subject == 'Резерв':
				continue
			if subject[1] > self.groups_sizes[subject[0]][1]:
				for i in self.groups[subject]:
					temp.append(i)
					self.student_lessons[i] -= 1
				self.groups_number[subject[0]] -= 1
				del self.groups[subject]
		for i in temp:
			self.groups['Резерв'].add(i)

	# Распределение резерва, далее требуется проверка размерности
	def none_distribute(self):
		for i in self.groups['Резерв'].copy():
			for j in self.jsonobj:
				if self.jsonobj[j]['name'] == i:
					for k in list(self.groups)[::-1]:
						if k[0] == self.jsonobj[j]['turn3']:
							self.groups[k].append(i)
							self.student_lessons[i] += 1
							break
					break
			self.groups['Резерв'].remove(i)
		for i in self.student_lessons:
			if self.student_lessons[i] == 0 or self.student_lessons[i] == 1:
				self.groups['Резерв'].add(i)

	def create_table(self):
		writer = pd.ExcelWriter('tables/groups.xlsx', engine='xlsxwriter')
		for group in self.groups:
			FIO = []
			Mail = []
			Phone = []
			for student in self.groups[group]:
				for information in self.jsonobj:
					if student == self.jsonobj[information]['name']:
						FIO.append(self.jsonobj[information]['name'])
						Mail.append(self.jsonobj[information]['mail'])
						Phone.append(self.jsonobj[information]['Ваш номер телефона для связи'])
			df = pd.DataFrame({'ФИО':FIO,'Почта':Mail,'Телефон':Phone})
			if group != 'Резерв':
				for name in self.groups_sizes:
					if name == group[0]:
						sheet_name = self.groups_sizes[name][2]+' '+str(group[1])
						break
			else:
				sheet_name = 'Резерв'
			df.to_excel(writer, sheet_name=sheet_name, index=False)
		writer.close()