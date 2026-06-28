from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import json
#No sé bien cual es el que no funciona por las dudas no tocar.

#Muchas de estas cosas son más para linux
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("start-maximized")
#NO TOCAR ESTO!!!!!!!!!!!!!
BUILD_TO_TEST = 0

def prepare_test(test_name_op,
                 op,
                 val1,
                 val2,
                 expectedResult=None,
                 expectedError=None):

	def runTest(self):
		print(f"\n {test_name_op} ", end="")
		self.operation.select_by_index(op)
		self.numberOne.send_keys(val1)
		self.numberTwo.send_keys(val2)
		self.calculateButton.click()
		time.sleep(1)
		if expectedError:
			self.assertTrue(self.error.is_displayed(),
			                "El mensaje de error debería mostrarse")
			self.assertEqual(self.error.text, expectedError)
			self.assertEqual(self.answer.get_attribute('value'), "",
			                 "El campo de respuesta debe estar vacío")
		elif expectedResult:
			answerValue = self.answer.get_attribute('value')
			self.assertEqual(answerValue, expectedResult)
		else:
			self.fail("El test no contiene ni error ni resultado esperado")
			# Si no hay ni error ni resultado, tira error
		time.sleep(1)
	return runTest


operators_dict = {
    "add": 0,
    "sub": 1,
    "mul": 2,
    "div": 3,
    "concatenate": 4,
}


class TestSequenceMeta(type):

	def __new__(mcs, name, bases, dict):
		with open("casosprueba.json") as f:
			casos = json.load(f)
			for test in casos:
				test_name = "test_%s" % test['caso']
				val1 = test['val1']
				val2 = test['val2']
				expectedResult = test.get('expectedResult', None)
				expectedError = test.get('expectedError', None)
				operators = test['op']
				if operators == "*":
					operators = ["add", "sub", "mul", "div", "concatenate"]
				if isinstance(operators, list) and expectedResult is not None:
					raise ValueError(
					    "No se puede especificar un resultado esperado para una lista de operadores"
					)

				if not isinstance(operators, list):
					operators = [operators]
				# Convertir los operadores a índices
				for op in operators:
					test_name_op = test_name + ("" if len(operators) == 1 else
					                            "_" + op)
					# Crear un método de prueba con los valores del test
					dict[test_name_op] = prepare_test(test_name_op,
					                                  operators_dict[op], val1,
					                                  val2, expectedResult,
					                                  expectedError)
		return type.__new__(mcs, name, bases, dict)


class Ej(unittest.TestCase, metaclass=TestSequenceMeta):
	@classmethod
	def setUpClass(cls):
		service = Service("/usr/bin/chromedriver") #ACA CAMBIAR EN CASO DE PROBAR EN OTRA PC
		#no sé como es en WINDOWS
		cls.driver = webdriver.Chrome(
		    service=service,
		    options=chrome_options
		)
		cls.driver.get("https://gerabarud.github.io/is3-calculadora/") #la página aca
		cls.refreshAndfindElements()
		for elem in cls.buildNum.all_selected_options:
		    print(elem.text)

	@classmethod
	def refreshAndfindElements(cls):
		cls.driver.refresh()
		time.sleep(1)
		cls.buildNum = Select(cls.driver.find_element(By.ID, "selectBuild"))
		cls.numberOne = cls.driver.find_element(By.NAME, "number1")
		cls.numberTwo = cls.driver.find_element(By.NAME, "number2")
		cls.calculateButton = cls.driver.find_element(By.ID, "calculateButton")
		cls.answer = cls.driver.find_element(By.ID, "numberAnswerField")
		cls.error = cls.driver.find_element(By.ID, "errorMsgField")
		cls.integerOnly = cls.driver.find_element(By.ID, "integerSelect")
		cls.clearButton = cls.driver.find_element(By.ID, "clearButton")
		cls.operation = Select(
		    cls.driver.find_element(By.NAME, "selectOperation"))
		cls.buildNum.select_by_index(
		    BUILD_TO_TEST)  #Selección global del prototipo

	def setUp(self):
		# Refrescar si hubo una división por cero para evitar el bloqueo
		if "divide by zero" in self.error.text.lower():
			self.refreshAndfindElements()

		self.clearButton.click()  #Limpia los campos antes de cada prueba
		self.numberOne.clear()
		self.numberTwo.clear()

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__ == "__main__":
	for i in range(10):
		BUILD_TO_TEST = i
		unittest.main(exit=False)
		print("\n\n\n\n\n\n\n\n")
