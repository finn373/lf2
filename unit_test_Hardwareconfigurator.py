import unittest
from unittest.mock import patch
from unittest import TestCase

def motherboard_handle_input(number):
		
	motherboard_model = number
	
	if motherboard_model == 1:
		return 'MSI Z390-A PRO Intel Z390', 104.0
	elif motherboard_model == 2:
		return 'MSI B550-A Pro AMD B550', 108.0

def cpu_handle_input(number, motherboard):

	cpu_choice = number
	
	if motherboard == 'MSI Z390-A PRO Intel Z390':

		if cpu_choice == 1:
					return 'i7 9700K', 277.00
		elif cpu_choice == 2:
					return 'i7 8700K', 337.99

	elif motherboard == 'MSI B550-A Pro AMD B550':
		
		if cpu_choice == 3:
					return 'Ryzen 5 1600', 129.00
		elif cpu_choice == 4:
					return 'Ryzen 5 3600', 199.00

	

class TestHardwareConfigurator(TestCase):
	
	def test_motherboard_choice_intel(self):
		
		motherboard_model, motherboard_price = motherboard_handle_input(1)
		self.assertEqual(motherboard_model, 'MSI Z390-A PRO Intel Z390')
		self.assertEqual(motherboard_price, 104.0)


	def test_motherboard_choice_amd(self):
		
		motherboard_model, motherboard_price = motherboard_handle_input(2)
		self.assertEqual(motherboard_model, 'MSI B550-A Pro AMD B550')
		self.assertEqual(motherboard_price, 108.0)

	def test_cpu_choice_intel(self):
		
		cpu_model, cpu_price = cpu_handle_input(1, 'MSI Z390-A PRO Intel Z390')
		self.assertEqual(cpu_model, 'i7 9700K')
		self.assertEqual(cpu_price, 277.00)

	def test_cpu_choice_amd(self):

		cpu_model, cpu_price = cpu_handle_input(3, 'MSI B550-A Pro AMD B550')
		self.assertEqual(cpu_model, 'Ryzen 5 1600')
		self.assertEqual(cpu_price, 129.00)