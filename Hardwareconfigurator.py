import pymysql.cursors
import os
from colorama import init, Fore
import uuid
import sys

class hardware_configurator:
	
	class utils:
		def clear_console_window():
			os.system('cls' if os.name=='nt' else 'clear')

		def general_data_formatting(data):
			data = data.replace('{', '').replace('[', '').replace('}', '').replace(']', '').replace("'", '').replace('€,', '€\n')
			return data

		def create_connection_to_database(host, username, password, databasename, port, charset):
			return pymysql.connect(host=host,
								user=username,
								password=password,
								database=databasename,
								charset=charset,
								cursorclass=pymysql.cursors.DictCursor)

	class motherboard_data:
		
		motherboard_model = ''
		motherboard_price = 0.0
		
		def motherboard_choice_handler():

			motherboard_choice = int(input(Fore.MAGENTA + 'Please enter the number of the component you want to get: '))
			if motherboard_choice == 1:
				return 'MSI Z390-A PRO Intel Z390', 104.0	
			elif motherboard_choice == 2:
				return 'MSI B550-A Pro AMD B550', 108.0

		def get_motherboard_data():

			try:
		
				hardware_configurator.utils.clear_console_window()
					
				connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
				with connection.cursor() as cursor:
					cursor.execute('SELECT motherboard_ID,Motherboard_Name, Motherboard_Price from motherboard_tbl')
					raw_motherboard_rows = cursor.fetchall()
					connection.close()
			
					raw_motherboard_data = str(raw_motherboard_rows)
			
					cleaned_motherboard_data = hardware_configurator.utils.general_data_formatting(raw_motherboard_data)
					cleaned_motherboard_data = cleaned_motherboard_data.replace('motherboard_ID', 'Nr.').replace('Motherboard_Name', 'Motherboard').replace('Motherboard_Price', 'Price').replace(' Nr.', 'Nr.')
			
					print(Fore.GREEN + cleaned_motherboard_data)
			
					hardware_configurator.motherboard_data.motherboard_model, hardware_configurator.motherboard_data.motherboard_price = hardware_configurator.motherboard_data.motherboard_choice_handler()

			except pymysql.err.OperationalError:
				print('Can´t connect to the Database')
	
	class cpu_data:
		cpu_model = ''
		cpu_price = 0.00

		def cpu_choice_handler():
			
			if hardware_configurator.motherboard_data.motherboard_model == 'MSI Z390-A PRO Intel Z390':
				
				cpu_choice = int(input(Fore.MAGENTA + 'Please enter the number of the component you want to get: '))

				if cpu_choice == 1:
					return 'i7 9700K', 277.00
				elif cpu_choice == 2:
					return 'i7 8700K', 337.99

			elif hardware_configurator.motherboard_data.motherboard_model == 'MSI B550-A Pro AMD B550':
				
				cpu_choice = int(input(Fore.MAGENTA + 'Please enter the number of the component you want to get: '))

				if cpu_choice == 3:
					return 'Ryzen 5 1600', 129.00
				elif cpu_choice == 4:
					return 'Ryzen 5 3600', 199.00

		def get_cpu_data():
			
			if hardware_configurator.motherboard_data.motherboard_model == 'MSI Z390-A PRO Intel Z390':
				try:
		
					hardware_configurator.utils.clear_console_window()
						 
					connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
					with connection.cursor() as cursor:
					
							cursor.execute('SELECT Cpu_ID,Cpu_Name, Cpu_Speed, Cpu_Price from cpu_tbl WHERE Cpu_Sockel = "1151"')
							raw_cpu_rows = cursor.fetchall()
							connection.close()
			
							raw_cpu_data = str(raw_cpu_rows)
			
							cleaned_cpu_data = hardware_configurator.utils.general_data_formatting(raw_cpu_data)
							cleaned_cpu_data = cleaned_cpu_data.replace('Cpu_ID', 'Nr.').replace('Cpu_Name', 'Cpu').replace('Cpu_Speed', 'Speed').replace('Cpu_Price', 'Price').replace(' Nr.', 'Nr.')
			
							print(Fore.GREEN + cleaned_cpu_data)
		
							hardware_configurator.cpu_data.cpu_model, hardware_configurator.cpu_data.cpu_price = hardware_configurator.cpu_data.cpu_choice_handler()


				except pymysql.err.OperationalError:
					print('Can´t connect to the Database')
		
			elif hardware_configurator.motherboard_data.motherboard_model == 'MSI B550-A Pro AMD B550':
				try:
		
					hardware_configurator.utils.clear_console_window()
						 
					connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
					with connection.cursor() as cursor:
					
							cursor.execute('SELECT Cpu_ID,Cpu_Name, Cpu_Speed, Cpu_Price from cpu_tbl WHERE Cpu_Sockel = "AM4"')
							raw_cpu_rows = cursor.fetchall()
							connection.close()
			
							raw_cpu_data = str(raw_cpu_rows)
			
							cleaned_cpu_data = hardware_configurator.utils.general_data_formatting(raw_cpu_data)
							cleaned_cpu_data = cleaned_cpu_data.replace('Cpu_ID', 'Nr.').replace('Cpu_Name', 'Cpu').replace('Cpu_Speed', 'Speed').replace('Cpu_Price', 'Price').replace(' Nr.', 'Nr.')
			
							print(Fore.GREEN + cleaned_cpu_data)
		
							hardware_configurator.cpu_data.cpu_model, hardware_configurator.cpu_data.cpu_price = hardware_configurator.cpu_data.cpu_choice_handler()


				except pymysql.err.OperationalError:
					print('Can´t connect to the Database')	
	class ram_data:
		ram_model = ''
		ram_price = 0.0

		def ram_choice_handler():
			
			ram_choice = int(input(Fore.MAGENTA + 'Please enter the number of the component you want to get: '))

			if ram_choice == 1:
					return 'Patriot Viper 4', 45.49
			elif ram_choice == 2:
					return 'Crucial Ballistix', 81.80
			elif ram_choice == 3:
					return 'G.Skill Rip Jaws V', 159.40
		
		def get_ram_data():
		
			try:
		
				hardware_configurator.utils.clear_console_window()
													
				connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
				with connection.cursor() as cursor:
					
						cursor.execute('SELECT ram_ID,ram_Name, ram_Memory, ram_Price from ram_tbl')
						raw_ram_rows = cursor.fetchall()
						connection.close()
			
						raw_ram_data = str(raw_ram_rows)
			
						cleaned_ram_data = hardware_configurator.utils.general_data_formatting(raw_ram_data)
						cleaned_ram_data = cleaned_ram_data.replace('ram_ID', 'Nr.').replace('ram_Name', 'RAM').replace('ram_Memory', 'Memory').replace('ram_Price', 'Price').replace(' Nr.', 'Nr.')
			
						print(Fore.GREEN + cleaned_ram_data)
		
						hardware_configurator.ram_data.ram_model, hardware_configurator.ram_data.ram_price = hardware_configurator.ram_data.ram_choice_handler()


			except pymysql.err.OperationalError:
					print('Can´t connect to the Database')
	
	class gpu_data:
		gpu_model = ''
		gpu_price = 0.0

		def gpu_choice_handler():
			
			gpu_choice = int(input(Fore.MAGENTA + 'Please enter the number of the component you want to get: '))

			if gpu_choice == 1:
					return 'Nvidia GeForce RTX 3090 Founders Edition', 2499.99
			elif gpu_choice == 2:
					return 'MSI GeForce RTX 3060 Gaming X', 899.00
			elif gpu_choice == 3:
					return 'MSI GeForce GTX 1650 D6 Ventus XS OCV2', 289.00
			elif gpu_choice == 4:
					return 'ASUS Phoenix GeForce GTX 1050 Ti', 198.99
		
		def get_gpu_data():
			try:
		
				hardware_configurator.utils.clear_console_window()
													
				connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
				with connection.cursor() as cursor:
					
						cursor.execute('SELECT gpu_ID,gpu_Name, gpu_Memory, gpu_Price from gpu_tbl')
						raw_gpu_rows = cursor.fetchall()
						connection.close()
			
						raw_gpu_data = str(raw_gpu_rows)
			
						cleaned_gpu_data = hardware_configurator.utils.general_data_formatting(raw_gpu_data)
						cleaned_gpu_data = cleaned_gpu_data.replace('gpu_ID', 'Nr.').replace('gpu_Name','GPU').replace('gpu_Memory', 'Memory').replace('gpu_Price', 'Price').replace(' Nr.', 'Nr.')
			
						print(Fore.GREEN + cleaned_gpu_data)
		
						hardware_configurator.gpu_data.gpu_model, hardware_configurator.gpu_data.gpu_price = hardware_configurator.gpu_data.gpu_choice_handler()


			except pymysql.err.OperationalError:
					print('Can´t connect to the Database')
	
	class console_stuff:
		Summe = 0

		def instruction_console_print():
			init()

			hardware_configurator.utils.clear_console_window()

			print(Fore.BLUE + 'Welcome to the Hardware Configurator')
			print(Fore.BLUE +'In the following you will go step by step through the Hardware configuration process.')
			print(Fore.BLUE +'It only will show components which are compatible with your hardware.')
			print(Fore.BLUE + 'Please enter the number of the component you want to get on the next screens and press enter afterwards to continue')
			input(Fore.MAGENTA + "Press Enter to continue...")
	
			hardware_configurator.motherboard_data.get_motherboard_data()
			hardware_configurator.cpu_data.get_cpu_data()
			hardware_configurator.ram_data.get_ram_data()
			hardware_configurator.gpu_data.get_gpu_data()
			hardware_configurator.console_stuff.results()

		def results():
				
				hardware_configurator.utils.clear_console_window()
				
				print(Fore.CYAN + 'Summary:')
				print(Fore.YELLOW + 'Motherboard: ', Fore.GREEN + hardware_configurator.motherboard_data.motherboard_model, 'Price: %s' % (hardware_configurator.motherboard_data.motherboard_price,) + '€')
				print(Fore.YELLOW + 'Cpu: ', Fore.GREEN + hardware_configurator.cpu_data.cpu_model, 'Price: %s' % (hardware_configurator.cpu_data.cpu_price,) + '€')
				print(Fore.YELLOW + 'Ram: ', Fore.GREEN + hardware_configurator.ram_data.ram_model, 'Price: %s' % (hardware_configurator.ram_data.ram_price,) + '€')
				print(Fore.YELLOW + 'Gpu: ', Fore.GREEN + hardware_configurator.gpu_data.gpu_model, 'Price: %s' % (hardware_configurator.gpu_data.gpu_price,) + '€')
				
				hardware_configurator.console_stuff.Summe = hardware_configurator.motherboard_data.motherboard_price + hardware_configurator.cpu_data.cpu_price + hardware_configurator.ram_data.ram_price + hardware_configurator.gpu_data.gpu_price
				hardware_configurator.console_stuff.Summe = round(hardware_configurator.console_stuff.Summe, 2)
				print(Fore.GREEN + 'Summe: %s' % (hardware_configurator.console_stuff.Summe,) + '€')
				
				
				order_questions = str(input('If you want to order the components enter "y" else "n": '))

				if order_questions == "y":
					hardware_configurator.utils.clear_console_window()
					print(Fore.GREEN + 'Order is set you gonna get an E-mail later, with the next instructions')
					hardware_configurator.write_data_to_database.write_order_in_db(hardware_configurator.motherboard_data.motherboard_model, hardware_configurator.cpu_data.cpu_model, hardware_configurator.ram_data.ram_model, hardware_configurator.gpu_data.gpu_model, hardware_configurator.console_stuff.Summe)
				
				elif order_questions == "n":
					print(Fore.GREEN + 'The Process has been canceled')
					sys.exit(0)
	
	class write_data_to_database:

		def write_order_in_db(Motherboard, Cpu, Ram, Gpu, Price):
			try:
				
				id = uuid.uuid1()
				connection = hardware_configurator.utils.create_connection_to_database('127.0.0.1', 'root', '', 'hardware_db', 3360, 'utf8mb4')
		
				with connection.cursor() as cursor:
						
						
						command = "INSERT INTO orders_tbl (order_ID, Motherboard, Cpu, Ram, Gpu, Price) VALUES (%s, %s, %s, %s, %s, %s)"
						val = id, hardware_configurator.motherboard_data.motherboard_model, hardware_configurator.cpu_data.cpu_model, hardware_configurator.ram_data.ram_model, hardware_configurator.gpu_data.gpu_model, "%s" % hardware_configurator.console_stuff.Summe + "€"
						cursor.execute(command, val)
						connection.commit()
						connection.close()

			except pymysql.err.OperationalError:
					print('Can´t connect to the Database')

hardware_configurator.console_stuff.instruction_console_print()