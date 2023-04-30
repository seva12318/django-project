# TEACHERS

## Список всех преподавателей

GET /api/teachers/

Формат ответа:

	[
		{
			"id":3,
			"surname":"Гаврилова",
			"name":"Анастасия",
			"patr":"Андреевна",
			"user":3
		},
		{
			"id":4,
			"surname":"Пугачёв",
			"name":"Максим",
			"patr":"Сергеевич",
			"user":4
		},
	]


## Создать запись нового преподавателя

POST /api/teachers/

Формат запроса:

	{
		"surname":"Орноев",
		"name":"Виктор",
		"patr":"Константинович"
	}



Формат ответа:

	{
		"id":23,
		"surname":"Орноев",
		"name":"Виктор",
		"patr":"Константинович",
		"user":null
	}



## Редактировать поля преподавателя 



PATCH /api/teachers/\<id\>/ | id преподавателя

Формат запроса:

	{
		"surname":"test"
	}



Формат ответа:

	{
		"id":23,
		"surname":"test",
		"name":"Виктор",
		"patr":"Константинович",
		"user":null
	}



## Удалить преподавателя



DELETE /api/teachers/\<id\>/ | id преподавателя



## Получить список предметов, которые ведет авторизованный преподаватель


GET /api/teachers/subjects/

Формат ответа:

	{
		"subjects":
			[
				{
					"id":36,
					"level":"Пустой",
					"name":"Пустой урок",
					"time":"00:00",
					"teacher":1,
					"teacher_fio":"Шведина yes Александровна"
				}
			]
	}



## Получить ID авторизованного преподавателя



GET /api/teachers/user/



Формат ответа:

	{
		"teacher":
			[
				{
					"id":1
				}
			]
	}





# SCHOOLS 





## Список всех школ



GET /api/schools/



Формат ответа:

	[
		{
			"id":3,
			"title":"МБОУ г. Иркутска Лицей №1"
		},
		{
			"id":4,
			"title":"МБОУ г. Усолье-Сибирское Лицей №1"
		},
	]



## Создать новую школу



POST /api/schools/

Формат запроса:

	{
		"title":"Тестовая школа"
	}



Формат ответа:

	{
		"id":11,
		"title":"Тестовая школа"
	}



## Редактировать поле названия школы



PATCH /api/schools/\<id\>/ | id школы

Формат запроса:

	{
		"title":"Не тестовая школа"
	}



Формат ответа:

	{
		"id":11,
		"title":"Не тестовая школа"
	}



## Удалить школу



DELETE /api/schools/\<id\>/ | id школы







# LESSONS 





## Список уроков и домашних заданий

	

GET /api/lessons/



Формат ответа:

	[
		{
			"id":39,
			"subjects":8,
			"subjects_name":"3D-моделирование в программе Blender (продвинутый 8.15)",
			"topic":"Консультация по проектам. Симуляции физических явлений",
			"homework":"Определиться с темой индивидуальных и/или групповых проектов, начать первые шаги в их разработке.",
			"date":"2023-02-11"
		},
		{
			"id":36,		
			"subjects":9,
			"subjects_name":"Будущее науки: английский язык для международных образовательных проектов (начальный 10.00)",
			"topic":"Project Team Building and Research Questions",
			"homework":"Decide if you want to work in a team or by yourself; formulate your topic, research question, and describe a product you plan to develop",
			"date":"2023-02-11"}
	]



## Создать запись урока и ДЗ

	
POST /api/lessons/

Формат запроса:

	{
		"subjects":8
		"topic":"Тема урока",
		"date":"01.01.2023"
	}



Формат ответа:

	{
		"id":157,
		"subjects":8,
		"subjects_name":"3D-моделирование в программе Blender (продвинутый 8.15)",
		"topic":"Тема урока",
		"homework":"",
		"date":"01.01.2023"
	}



## Редактировать запись урока и ДЗ



PATCH /api/lessons/\<id\>/ | id урока

Формат запроса:

	{
		"homework":"ДЗ"
	}



Формат ответа:

	{
		"id":157,
		"subjects":8,
		"subjects_name":"3D-моделирование в программе Blender (продвинутый 8.15)",
		"topic":"Тема урока",
		"homework":"ДЗ",
		"date":"01.01.2023"
	}



## Удалить запись урока и ДЗ



DELETE /api/lessons/\<id\>/ | id урока





## Получить оценки за конкретный урок



GET /api/lessons/\<id\>/journal/ | id урока



Формат ответа:

	{
		"journal":
			[
				{
					"id":1510,
					"students":21,
					"students_name":"Петров Виктор Николаевич",
					"lessons":158,
					"mark":"5"
				}
			]
	}





## Проставление оценок



POST /api/lessons/\<id\>/get-marks/ | id урока

Формат запроса:

	{
		"students":21,
		"lessons":\<id\>,           | id урока
		"mark":"5"
	}





# JOURNALS 



## Получить оценки выставленные авторизованным преподавателем



GET /api/journals/



Формат ответа:

	[
		{
			"id":1510,
			"students":21,
			"students_name":"Петров Виктор Николаевич",
			"lessons":158,
			"mark":"5"
		}
	]



## Получить оценки определенного студента





GET /api/journals/\<id\>/lesson/ | id студента



Формат ответа:

	{
		"journal":
			[
				{
					"id":245,
					"students":31,
					"students_name":"Атучина Елизавета Дмитриевна",
					"lessons":33,
					"mark":"5"
				},
				{
					"id":347,
					"students":31,
					"students_name":"Атучина Елизавета Дмитриевна",
					"lessons":41,"mark":"3"
				}
			]
	}



## Оценки студентов с фильтром по школам


GET /api/journals/\<id\>/school/ | id школы



Формат ответа:

	{
		"journal":
			[
				{
					"id":334,
					"students":3,
					"students_name":"Боев Роман Леонидович",
					"lessons":39,
					"mark":"5"
				},
				{
					"id":451,
					"students":3,
					"students_name":"Боев Роман Леонидович",
					"lessons":50,
					"mark":"5"
				}
			]
	}



## Оценки студентов с фильтром по предмету



GET /api/journals/\<id\>/subject/ | id предмета



Формат ответа:

	{
		"sub-journal":
			[
				{
					"students":27,
					"students_name":"Сорокин Дамир Олегович",
					"num_class":"10б",
					"lessons":28,
					"date":"2023-02-18",
					"lessons_name":"Электроника и схемотехника (начальный 10.00)",
					"mark":"5"
				}
			]
	}







# SUBJECTS 



## Получить список предметов у авторизованного преподавателя



GET /api/subjects/



Формат ответа:

	[
		{
			"id":36,
			"level":"Пустой",
			"name":"Пустой урок",
			"time":"00:00",
			"teacher":1,
			"teacher_fio":"Шведина yes Александровна"
		}
	]



## Получить список тем предмета и ДЗ авторизованного преподавателя



GET /api/subjects/\<id\>/lessons/ | id предмета



Формат ответа:

	{
		"sub-lessons":
			[
				{
					"id":158,
					"subjects":36,
					"subjects_name":"Пустой урок (Пустой)",
					"topic":"Просто тема",
					"homework":"",
					"date":"20-01-2023"
				}
			]
	}



## Получить список студентов по предмету



GET /api/subjects/\<id\>/students/ | id предмета



Формат ответа:

	{
		"sub-journal":
			[
				{
					"id":62,
					"name":"Алиса",
					"surname":"Волкова",
					"patr":"Валерьевна",
					"school":4,
					"school_title":"МБОУ г. Усолье-Сибирское Лицей №1",
					"num_class":"10"
				},
				{
					"id":148,
					"name":"Арина",
					"surname":"Борисенко",
					"patr":"Руслановна",
					"school":6,
					"school_title":"МБОУ г.Иркутска СОШ №24",
					"num_class":"11а"
				}
			]
	}
