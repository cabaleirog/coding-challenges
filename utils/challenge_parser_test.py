import unittest

from selenium import webdriver

from utils.new_challenge import Parser, HackerRank, Codeforces


class TestCodeforces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_codeforces_challenge_detailsA(self):
        URL = 'http://codeforces.com/contest/935/problem/A'
        obj = Codeforces(None, None, self.driver)
        obj.get_problem(URL)
        self.assertEqual(URL, obj.details.url)
        self.assertIn('Fafa and his Company', obj.details.name)
        self.assertEqual(2, len(obj.details.sample_tests))

    def test_codeforces_challenge_detailsB(self):
        URL = 'http://codeforces.com/contest/935/problem/B'
        obj = Codeforces(None, None, self.driver)
        obj.get_problem(URL)
        self.assertEqual(URL, obj.details.url)
        self.assertIn('Fafa and the Gates', obj.details.name)
        self.assertEqual(3, len(obj.details.sample_tests))
