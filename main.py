import tkinter as tk
from tkinter import ttk
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import requests
import telebot



browser = webdriver.Chrome('/Users/nick/PycharmProjects/alicante/chromedriver')
browser.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')

# En este momento no hay citas disponibles
def rep():
	r = 0
	while 1 == 1:
		r += 1
		getcita()
		print(r)
	else:
		print('пошло дальше')
	# if "En este momento no hay citas disponibles" in getcita():
	# 	browser.find_element_by_id("btnSalir").click()
	# 	time.sleep(60)
	# 	getcita()
	# else:
	# 	print('Прошло дальше')
	# 	time.sleep(2)
	# 	browser.find_element_by_id("Teléfono").send_keys("+79643421749")
	# 	browser.find_element_by_id("emailUNO").send_keys("director.red@gmail.com")
	# 	browser.find_element_by_id("emailDOS").send_keys("director.red@gmail.com")
	# 	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	# 	browser.find_element_by_id("txtObservaciones").send_keys("Obtener un NIE para comprar un piso en la ciudad de Dénia")
	# 	browser.find_element_by_id("btnSiguiente").click()

def getcita():
	var_prov = prov.get()
	var_first_name = first_name.get()
	var_last_name = last_name.get()
	var_office = office.get()
	var_year = year.get()
	var_citizen = citizen.get()
	var_passport = passport.get()
	var_service = service.get()

	time.sleep(2)
	# выбираем регион
	
	multi = Select(browser.find_element_by_css_selector('[id="form"]'))
	multi.select_by_visible_text(var_prov)
	# нажимаем кнопку "подтвердить"
	browser.find_element_by_id("btnAceptar").click()
	# выбиаем место, где будет оказана услуга
	# CNP Denia, Avda Marquesado, 53
	multi1 = Select(browser.find_element_by_css_selector('[id="sede"]'))
	multi1.select_by_visible_text(var_office)
	time.sleep(2)
	# выбираем услугу, которую нужно плучить
	# Asignación de N.I.E.
	multi2 = Select(browser.find_element_by_css_selector('[id="tramiteGrupo[0]"]'))
	multi2.select_by_visible_text(var_service)
	time.sleep(2)
	# нажимаем кнопку "подтвердить"
	browser.find_element_by_id("btnAceptar").click()
	time.sleep(2)
	# прокручиваем вниз страницы
	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	# нажимаем кнопку "подтвердить"
	time.sleep(2)
	browser.find_element_by_id("btnEntrar").click()
	# ввод паспорта
	# 753718478
	browser.find_element_by_id("txtIdCitado").send_keys(var_passport)
	# прокручиваем вниз страницы
	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	# вводим фамилию и имя
	browser.find_element_by_id("txtDesCitado").send_keys(var_first_name + ' ' + var_last_name)
	# вводим год рождения
	browser.find_element_by_id("txtAnnoCitado").send_keys(var_year)
	# выбираем страну гражданства
	multi3 = Select(browser.find_element_by_css_selector('[id="txtPaisNac"]'))
	multi3.select_by_visible_text(var_citizen)
	# нажимаем кнопку "подтвердить"
	browser.find_element_by_id("btnEnviar").click()
	# нажимаем кнопку "подтвердить"
	time.sleep(2)
	browser.find_element_by_id("btnEnviar").click()
	time.sleep(2)
	browser.find_element_by_id("btnSalir").click()
	time.sleep(2)
	# browser.find_element_by_id("btnSalir").click()
	# получаем текст сообщения
	# texts = browser.find_element_by_class_name('mf-msg__info').text
	# return texts

# графический интерфейс
window = tk.Tk()
window.title('CITA')
window.geometry('600x450')
window.minsize(300,150)
window.maxsize(700,500)
frame_list = tk.Frame(window, width=500, height=300, bg="gray")
frame_list.place(relx=0, rely=0, relwidth=1, relheight=1)

items_prov = [
    'A Coruña', 'Albacete', 'Alicante', 'Almería', 'Araba', 'Asturias', 'Ávila', 'Badajoz',
	                    'Barcelona',
	  					'Bizkaia',
	  					'Burgos',
	  					'Cáceres',
	  					'Cádiz',
	  					'Cantabria',
	  					'Castellón',
	  					'Ceuta',
	  					'Ciudad Real',
	  					'Córdoba',
	  					'Cuenca',
	  					'Gipuzkoa',
	  					'Girona',
	  					'Granada',
	  					'Guadalajara',
	  					'Huelva',
	  					'Huesca',
	  					'Illes Balears',
	  					'Jaén',
	  					'La Rioja',
	  					'Las Palmas',
	  					'León',
	  					'Lleida',
	  					'Lugo',
	  					'Madrid',
	  					'Málaga',
	  					'Melilla',
	  					'Murcia',
	  					'Navarra',
	  					'Orense',
	  					'Palencia',
	  					'Pontevedra',
	  					'Salamanca',
	  					'S.Cruz Tenerife',
	  					'Segovia',
	  					'Sevilla',
	  					'Soria',
	  					'Tarragona',
	  					'Teruel',
	  					'Toledo',
	  					'Valencia',
	  					'Valladolid',
	  					'Zamora',
	  					'Zaragoza',

]

items_office = [
							'CNP Alcoy, Placeta Les Xiques, S/N',
							'CNP Alicante NIE, Campo de Mirra, 6',
							'CNP Alicante TIE, Campo de Mirra, 6',
							'CNP Benidorm, Apolo XI, 36',
							'CNP Benidorm TIE, Callosa D`Ensarria, 2',
							'CNP Comisaría Provincial, C/ Isabel la Católica, 25',
							'CNP Denia, Avda Marquesado, 53',
							'CNP Elche, El Abeto, 1',
							'CNP Elda, Lamberto Amat, 26',
							'CNP Orihuela, Sol, 34',
							'CNP Orihuela Costa, C/ Plaza Oriol, S/N',
							'CNP Torrevieja, Arquitecto Larramendi, 3',
							'OEX ALICANTE, EBANISTERIA, 4-6',
							'OEX ALTEA, SAN ISIDRO LABRADOR, 1',
]

items_service = [
						'Despliegue para ver trámites disponibles en esta provincia',
						'Asignación de N.I.E.',
						'Certificado de residente o no residente',
						'CERTIFICADOS UE',
						'POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)',

]

items_coutry = [
						'AFGANISTAN',
						'ALBANIA',
						'ALEMANIA',
						'ANDORRA',
						'ANGOLA',
						'ANGUILLA',
						'ANTIGUA Y BARBUDA',
						'ANTILLAS NL.',
						'APATRIDA',
						'ARABIA SAUDI',
						'ARGELIA',
						'ARGENTINA',
						'ARMENIA',
						'ARUBA',
						'AUSTRALIA',
						'AUSTRIA',
						'AZERBAYAN',
						'BAHAMAS',
						'BAHREIN',
						'BANGLADESH',
						'BARBADOS',
						'BELGICA',
						'BELICE',
						'BENIN',
						'BHUTAN',
						'BIELORRUSIA O BELARUS',
						'BOLIVIA',
						'BOSNIA-HERZEGOVINA',
						'BOTSWANA',
						'BRASIL',
						'BRUNEI DARUSSALAM',
						'BULGARIA',
						'BURKINA FASO',
						'BURUNDI',
						'CABO VERDE',
						'CAMBOYA',
'CAMERUN',
'CANADA',
'CENTROAFRICA REPUBLICA',
'CHAD',
'CHILE',
'CHINA',
'CHIPRE',
'COLOMBIA',
'COMORES',
'CONGO BRAZZAVILLE',
'COREA, REP. POP. DEMOC.',
'COREA, REPUBLICA',
'COSTA DE MARFIL',
'COSTA RICA',
'CROACIA',
'CUBA',
'DINAMARCA',
'DJIBOUTI',
'DOMINICA',
'DOMINICANA REPUBLICA',
'ECUADOR',
'EEUU',
'EGIPTO',
'EL SALVADOR',
'EL VATICANO',
'EMIRATOS ARABES UNIDOS',
'ERITREA',
'ESLOVAQUIA',
'ESLOVENIA',
'ESPAÑA',
'ESTONIA',
'ETIOPIA',
'FIDJI',
'FILIPINAS',
'FINLANDIA',
'FRANCIA',
'GABON',
'GAMBIA',
'GEORGIA',
'GHANA',
'GRANADA REPUBLICA',
'GRECIA',
'GUATEMALA',
'GUAYANA',
'GUINEA ECUATORIAL',
'GUINEA REPUBLICA',
'GUINEA-BISSAU',
'HAITI',
'HOLANDA',
'HONDURAS',
'HUNGRIA',
'INDIA',
'INDONESIA',
'IRAK',
'IRAN',
'IRLANDA',
'ISLANDIA',
'ISLAS MARSCHALL',
'ISRAEL',
'ITALIA',
'JAMAICA',
'JAPON',
'JORDANIA',
'KAZAJSTAN',
'KENIA',
'KIRGUISTAN',
'KIRIBATI',
'KUWAIT',
'LAOS',
'LAS MALDIVAS',
'LESOTHO',
'LETONIA',
'LIBANO',
'LIBERIA',
'LIBIA',
'LIECHTENSTEIN',
'LITUANIA',
'LUXEMBURGO',
'MACAO',
'MACEDONIA',
'MADAGASCAR',
'MALASIA',
'MALASIA - GRAN BRETAÑA',
'MALAWI',
'MALI',
'MALTA',
'MARRUECOS',
'MAURICIO',
'MAURITANIA',
'MEJICO',
'MICRONESIA',
'MOLDAVIA',
'MONACO',
'MONGOLIA',
'MONTENEGRO',
'MOZAMBIQUE',
'MYANMAR',
'NAMIBIA',
'NAURU',
'NEPAL',
'NICARAGUA',
'NIGER',
'NIGERIA',
'NORUEGA',
'NUEVA ZELANDA',
'OMAN',
'PAKISTAN',
'PALESTINA EONU',
'PANAMA',
'PAPUA NUEVA GUINEA',
'PARAGUAY',
'PERU',
'POLONIA',
'PORTUGAL',
'PUERTO RICO',
'QATAR',
'REINO UNIDO',
'REP. DEMOCRATICA DEL CONGO (EX-ZAIRE)',
'REPUBLICA CHECA',
'REUNION-COMO',
'RUANDA',
'RUMANIA',
'RUSIA',
'SALOMON',
'SAMOA OCCIDENTAL',
'SAN CRISTOBAL Y NEVIS',
'SAN MARINO',
'SAN VICENTE',
'SANTA LUCIA',
'SANTO TOME Y PRINCIPE',
'SEICHELLES',
'SENEGAL',
'SENEGAMBIA',
'SERBIA',
'SIERRA LEONA',
'SINGAPUR',
'SIRIA',
'SOMALIA',
'SRI LANKA',
'SUDAFRICA',
'SUDAN',
'SUECIA',
'SUIZA',
'SURINAM',
'SWAZILANDIA',
'TADJIKISTAN',
'TAIWAN',
'TANZANIA',
'THAILANDIA',
'TIMOR ORIENTAL',
'TOGO',
'TONGA',
'TRINIDAD Y TOBAGO',
'TUNEZ',
'TURKMENIA',
'TURQUIA',
'TUVALU',
'UCRANIA',
'UGANDA',
'URUGUAY',
'UZBEKISTAN',
'VANUATU',
'VENEZUELA',
'VIETNAM',
'YEMEN',
'ZAMBIA',
'ZIMBABWE',
]

first_name = tk.StringVar()
r_first_name = ttk.Entry(frame_list, textvariable=first_name)
l_first_name = ttk.Label(frame_list, text='Enter first name:')

last_name = tk.StringVar()
r_last_name = ttk.Entry(frame_list, textvariable=last_name)
l_last_name = ttk.Label(frame_list, text='Enter last name:')

prov = tk.StringVar()
r_prov = ttk.Combobox(frame_list, values=items_prov, textvariable=prov)
l_prov = ttk.Label(frame_list, text='PROVINCIAS DISPONIBLES:')

office = tk.StringVar()
r_office = ttk.Combobox(frame_list, values = items_office, textvariable=office)
l_office = ttk.Label(frame_list, text='Oficina:')

service = tk.StringVar()
r_service = ttk.Combobox(frame_list, values=items_service, textvariable=service)
l_service = ttk.Label(frame_list, text='TRÁMITES CUERPO NACIONAL DE POLICÍA:')

passport = tk.StringVar()
r_passport = ttk.Entry(frame_list, textvariable=passport)
l_passport = ttk.Label(frame_list, text='PASAPORTE:')

year = tk.StringVar()
r_year = ttk.Entry(frame_list, textvariable=year)
l_year = ttk.Label(frame_list, text='Año de nacimiento:')

citizen = tk.StringVar()
r_citizen = ttk.Combobox(frame_list, values=items_coutry, textvariable=citizen)
l_citizen = ttk.Label(frame_list, text='País de nacionalidad:')

button = ttk.Button(frame_list, text='Start', command=rep)

r_first_name.grid(row='0', column='1', sticky='w', padx=10, pady=10)
l_first_name.grid(row='0', column='0', sticky='e', padx=10, pady=10)
r_last_name.grid(row='1', column='1', sticky='w', padx=10, pady=10)
l_last_name.grid(row='1', column='0', sticky='e', padx=10, pady=10)
r_prov.grid(row='2', column='1', sticky='w', padx=10, pady=10)
l_prov.grid(row='2', column='0', sticky='e', padx=10, pady=10)
r_office.grid(row='3', column='1', sticky='w', padx=10, pady=10)
l_office.grid(row='3', column='0', sticky='e', padx=10, pady=10)
r_service.grid(row='4', column='1', sticky='w', padx=10, pady=10)
l_service.grid(row='4', column='0', sticky='e', padx=10, pady=10)
r_passport.grid(row='5', column='1', sticky='w', padx=10, pady=10)
l_passport.grid(row='5', column='0', sticky='e', padx=10, pady=10)
r_year.grid(row='6', column='1', sticky='w', padx=10, pady=10)
l_year.grid(row='6', column='0', sticky='e', padx=10, pady=10)
r_citizen.grid(row='7', column='1', sticky='w', padx=10, pady=10)
l_citizen.grid(row='7', column='0', sticky='e', padx=10, pady=10)
button.grid()

window.mainloop()


#bot = telebot.TeleBot("1915558086:AAEU43bBDdJvrd2NukpVPcn7XfYXzdYnhgk", parse_mode=None)
#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
#    if 1 == 1:
#        bot.send_message(message.from_user.id, text='Привет, мой создатель')
#bot.polling()