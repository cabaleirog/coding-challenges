import os
import sys
import re
import argparse
import logging
import time
from urllib.request import urlopen

import bs4
from getpass import getpass
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)


class Parser:
    def __init__(self, folder=None):
        self.folder = folder
        self.url = None
        self.name = None
        self.time_limit = None
        self.difficulty = None
        self.description = None
        self.input_format = None
        self.output_format = None
        self.notes = None
        self.sample_tests = []
        self.tags = []

        self.filename = None
        self.challenge_file_path = None
        self.challenge_test_path = None

    def create_coding_file(self):
        path = f'{self.folder}/{self.filename}.py'

        if os.path.isfile(path):
            logger.error('File %s already exists. Aborting.', path)
            return False

        with open(path, 'w', encoding='utf8') as f:
            # Docstring
            f.write(f'"""{self.name}.\n\n')

            if self.difficulty:
                f.write(f'- Difficulty: {self.difficulty}\n\n')

            f.write(f'{self.url}\n\n')

            f.write('{}\n\n'.format(self.pep8_lines(self.description)))

            if self.input_format:
                f.write('Input:\n\n')
                f.write('{}\n\n'.format(self.pep8_lines(self.input_format)))

            if self.output_format:
                f.write('Output:\n\n')
                f.write('{}\n\n'.format(self.pep8_lines(self.output_format)))

            f.write('"""\n')

            # Basic logging
            logging_conf = """
                import logging

                ch = logging.StreamHandler()
                ch.setLevel(logging.DEBUG)

                logger = logging.getLogger()
                logger.setLevel(logging.DEBUG)
                logger.addHandler(ch)
            """
            self.text_block_to_file(logging_conf, f)
            f.write('\n\n')

            # Code section
            main_code = """
                def solve(*args):
                    return '...'


                def main():
                    for _ in range(int(input().strip())):
                        args = input().strip().split()
                        result = solve(*args)
                        print(result)


                if __name__ == '__main__':
                    main()
            """
            self.text_block_to_file(main_code, f)

        logger.info(f'Main file created successfully: {path}')

    def create_testing_file(self):
        path = f'{self.folder}/tests/{self.filename}_test.py'

        if os.path.isfile(path):
            logger.error('File %s already exists. Aborting.', path)
            return False

        with open(path, 'w', encoding='utf8') as f:
            f.write('from utils.test_utils import assert_time_limit\n')
            f.write(f'from {self.folder}.{self.filename} import solve\n\n\n')

            test_statement = """
                def test_sample_test_case():
                    args = ['Arg0', 'Arg1', 'ArgN']
                    expected = 'Expected Value'
                    assert solve(*args) == expected
            """
            self.text_block_to_file(test_statement, f)
            f.write('\n\n')

            # Time limit test.
            f.write(f'# Time limit: {self.time_limit}.\n')
            test_statement = """
                def test_time_limit():
                    args = []
                    assert_time_limit(0, solve, *args)
            """
            self.text_block_to_file(test_statement, f)

        logger.info(f'Test file created successfully: {path}')

    @staticmethod
    def text_block_to_file(text_block, file_obj):
        lines = text_block.split('\n')
        if not lines[0].strip():
            lines = lines[1:]
        left_margin = len(lines[0]) - len(lines[0].lstrip())
        for i, line in enumerate(lines):
            file_obj.write(line[left_margin:].rstrip())
            if i < len(lines) - 1:
                file_obj.write('\n')

    @staticmethod
    def pep8_lines(paragraphs):
        def fix_length(s):
            line_width = 0
            lines = []
            line = []
            for word in s.split():
                line_width += 1 + len(word.strip())
                if line_width > 79:
                    lines.append(line)
                    line_width = len(word.strip())
                    line = []
                line.append(word.strip())
            if line:
                lines.append(line)
            return '\n'.join([' '.join(x) for x in lines])
        return '\n\n'.join(fix_length(p) for p in paragraphs)


class Base:
    folder = ''

    def __init__(self, username=None, password=None, driver=None):
        self.username = username
        self.password = password
        self.driver = driver
        self.details = Parser(self.folder)

    def create_files(self, details):
        # Challenge problem file
        self.details.create_coding_file()
        self.details.create_testing_file()

    @staticmethod
    def element_to_text(elements):
        res = []
        if not isinstance(elements, list):
            elements = elements.contents
        for element in elements:
            if element.name == 'p':
                res.append(element.text.strip())
            elif element.name == 'ul':
                for li in element.find_all('li'):
                    res.append('- {}'.format(li.text.strip()))
            elif element.name == 'ol':
                for k, li in enumerate(element.find_all('li')):
                    res.append('{}. {}'.format(k + 1, li.text.strip()))
            else:
                logger.warning('Unhandled element <%s> found.', element.name)
        return res


class HackerRank(Base):
    folder = 'hacker_rank'

    def login(self):
        driver = self.driver

        driver.get('https://www.hackerrank.com')

        # Wait for the page to load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "HackerRank-homepage")))

        try:
            driver.find_element_by_xpath('//a[contains(@href, "/login")]').click()
        except Exception as e:
            print(e)
            time.sleep(3)
            driver.find_element_by_xpath('//a[contains(@href, "/login")]').click()

        logger.info(f'Successfully logged in to __ with user {self.username}')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login")))

        xpath = '//div[@id="login"]//input[@id="login"]'
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(self.username)

        xpath = '//div[@id="login"]//input[@id="password"]'
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(self.password)

        xpath = '//div[@id="login"]//button[@type="submit"]'
        element = driver.find_element_by_xpath(xpath)
        element.click()

        return True

    def get_source(self, url):
        self.driver.get(url)
        time.sleep(5)
        _ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hackdown-content")))
        return self.driver.page_source

    def parse(self, url):
        source = self.get_source(url)
        soup = bs4.BeautifulSoup(source, 'html.parser')

        details = self.details
        details.url = url

        element = soup.find('h2', attrs={'class': re.compile('-name')})
        name = element.get_text(strip=True)
        filename = name.replace(' ', '_').replace('-', '_').lower()
        details.name = name
        details.filename = filename

        element = soup.find('span', attrs={'class': re.compile('difficulty')})
        details.difficulty = element.text

        element = soup.find('div', attrs={'class': 'hackdown-content'})
        details.description = self.element_to_text(element)

        return details


class Codeforces(Base):
    folder = 'codeforces'

    def login(self):
        pass  # Not needed for Codeforces

    def get_source(self, url):
        return urlopen(url).read()

    def parse(self, url):
        source = self.get_source(url)
        soup = bs4.BeautifulSoup(source, 'html.parser')

        details = self.details
        details.url = url

        name = soup.find('div', attrs={'class': 'title'}).text

        if name[1] == '.' and name[2] == ' ':
            filename = name[3:].replace(' ', '_').replace('-', '_').lower()
            name = 'Problem {} - {}'.format(name[0], name[3:])
        logger.info('Name is %s', name)

        details.filename = filename
        details.name = name

        _, limit = soup.find('div', attrs={'class': 'time-limit'})
        details.time_limit = limit

        # Problem description.
        header_div = soup.find('div', attrs={'class': 'header'})
        details.description = self.element_to_text(
            header_div.find_next_sibling('div'))

        # Input format
        _, *elems = soup.find('div', attrs={'class': 'input-specification'})
        details.input_format = self.element_to_text(elems)

        # Output format
        _, *elems = soup.find('div', attrs={'class': 'output-specification'})
        details.output_format = self.element_to_text(elems)

        # Notes
        details.notes = self.element_to_text(
            soup.find('div', attrs={'class': 'note'}))

        # Sample test cases
        tests = []
        element = soup.find('div', attrs={'class': 'sample-test'})
        inputs = element.find_all('div', attrs={'class': 'input'})
        outputs = element.find_all('div', attrs={'class': 'output'})
        for i, j in zip(inputs, outputs):
            _in = '\n'.join([x for x in i.find('pre') if isinstance(x, str)])
            _ou = '\n'.join([x for x in j.find('pre') if isinstance(x, str)])
            tests.append([_in, _ou])
        details.sample_tests = tests

        # Tags
        element = soup.find_all('span', attrs={'class': 'tag-box'})
        details.tags = [x.get_text(strip=True) for x in element]

        return details


def main():
    choices = (
        ('Codeforces', Codeforces),
        ('HackerRank', HackerRank))

    print('Choose the website ...')  # TODO: Complete the statement.
    for i, (name, _) in enumerate(choices):
        print(f'{i}: {name}')

    try:
        choice, choice_cls = choices[int(input().strip())]
        # choice, choice_cls = choices[0]
    except Exception as e:
        logger.error('Wrong input. %s.', e)
        raise

    kwargs = {}
    if choice in ['HackerRank']:
        # Credentials
        print(f'Provide your credentials for {choice}:')
        # kwargs['username'] = input('Username:')
        # kwargs['password'] = getpass('Password:')
        kwargs['username'] = 'mydarksoul69@gmail.com'  # TODO: Debug only
        kwargs['password'] = 'l>^cFr8%D7Vtcyd6SM'  # TODO: Debug only

        driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
        kwargs['driver'] = driver

    # obj = choice_cls(username, password, driver)

    # try:
    #     obj.login()
    # except Exception as e:
    #     logger.error('Unable to login to HackerRank. %s.', e)
    #     driver.quit()
    #     sys.exit(1)

    # Keep alive so we dont need to insert credentials every time.
    # while True:
    #     url = input('Challenge URL: ')
    #     details = obj.parse(url)
    #     obj.create_files(details)
    # driver.quit()

    url = input('Challenge URL: ')
    obj = choice_cls(**kwargs)
    obj.login()
    details = obj.parse(url)
    obj.create_files(details)


if __name__ == '__main__':
    main()
# https://www.hackerrank.com/contests/hourrank-26/challenges/cloudy-day