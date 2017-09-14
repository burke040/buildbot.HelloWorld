import main
import unittest

class TestHelloWorld(unittest.TestCase):
	def test_helloWorld(self):
		self.assertEquals(main.hello(), "Hello World")

		
if __name__ == '__main__':
	unittest.main()
