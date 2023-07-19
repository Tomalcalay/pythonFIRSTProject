import unittest
import mainProject


class Testadd(unittest.TestCase):
    def test_value(self):
        from mainProject import get_user_value
        assert get_user_value()

    def test_result(self):
        import projectClassILS
        result = projectClassILS.ILS.calculate(5)
        assert result == 1.4000000000000001


    def test_file(self):
        list_results = mainProject.third_screen(5)
        results_file = open('C:/Users/nadav2022/PycharmProjects/pythonFIRSTProject/results_list.txt', 'r')
        content = results_file.read()
        assert content == str(list_results)
        results_file.close()

