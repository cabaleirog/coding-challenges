import os
import sys
import argparse
import logging
import time

from getpass import getpass
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from challenge_template import TEMPLATE_CHALLENGE_FILE, TEMPLATE_TEST_FILE


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)


class RenameMe:
    def __init__(self, folder=None):
        self.folder = folder
        self.url = None
        self.name = None
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

    def set_file_blablabla(self):
        self.filename = self.name.replace(' ', '_').replace('-', '_').lower()
        self.challenge_file_path = f'{self.folder}/{self.filename}.py'
        self.challenge_test_path = f'{self.folder}/tests/{self.filename}_test.py'

        # FIXME: This doesnt go here. :p
        self.description = self.pep8_lines(self.description)

    @staticmethod
    def pep8_lines(text):
        line_width = 0
        lines = []
        line = []
        for word in text.split():
            line_width += 1 + len(word.strip())
            if line_width > 79:
                lines.append(line)
                line_width = len(word.strip())
                line = []
            line.append(word.strip())
        if line:
            lines.append(line)
        return '\n'.join([' '.join(x) for x in lines])


class Base:
    folder = ''

    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver
        self.details = RenameMe(self.folder)

    def create_files(self, details):
        # Challenge problem file
        self.details.set_file_blablabla()
        path = self.details.challenge_file_path
        if os.path.isfile(path):
            logger.error('File %s already exists. Aborting.', path)
        else:
            with open(path, 'w', encoding='utf8') as f:
                f.write(TEMPLATE_CHALLENGE_FILE.format(**details.__dict__))
                logger.info('File %s created.', path)

        # Challenge test file
        path = self.details.challenge_test_path
        if os.path.isfile(path):
            logger.error('File %s already exists. Aborting.', path)
        else:
            with open(path, 'w', encoding='utf8') as f:
                f.write(TEMPLATE_TEST_FILE.format(**details.__dict__))
                logger.info('File %s created.', path)


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

    def get_problem(self, url):
        driver = self.driver

        # Gathering challenge information
        driver.get(url)

        details = {'url': url}

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hackdown-content")))

        xpath = '//h2[contains(@class, "challenge")]'
        details['name'] = driver.find_element_by_xpath(xpath).text

        xpath = '//span[contains(@class, "difficulty")]'
        details['difficulty'] = driver.find_element_by_xpath(xpath).text

        xpath = '//div[@class="hackdown-content"]'
        element = driver.find_element_by_xpath(xpath)
        description = '\n\n'.join(pep8_lines(x) for x in element.text.split('\n'))
        details['description'] = description

        # File creation
        # TODO: Use regex to replace all invalid characters
        filename = details['name'].replace(' ', '_').replace('-', '_').lower()

        details['filename'] = filename
        details['challenge_file_path'] = f'{self.folder}/{filename}.py'
        details['challenge_test_path'] = f'{self.folder}/tests/{filename}_test.py'

        logger.debug('Challenge name: %s', details['name'])
        logger.debug('Difficulty: %s', details['name'])

        return details


class Codeforces(Base):
    folder = 'codeforces'

    def login(self):
        pass  # Not needed for Codeforces

    def get_problem(self, url):
        driver = self.driver

        # Gathering challenge information
        driver.get(url)

        details = self.details
        details.url = url

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title")))

        # WebDriver Element
        problem = driver.find_element_by_class_name('problem-statement')

        name = problem.find_element_by_class_name('title')
        name = name.get_attribute('textContent')
        if name[1] == '.' and name[2] == ' ':
            name = name[3:]
        details.name = name

        time_limit = problem.find_element_by_class_name('time-limit')
        details.time_limit = time_limit.get_attribute('textContent')

        xpath = '//div[@class="header"]/following-sibling::div/p'
        description = problem.find_elements_by_xpath(xpath)
        description = '\n\n'.join([p.get_attribute('textContent').strip() for p in description])
        details.description = description
        print(description)

        # Input format
        xpath = '//div[@class="input-specification"]//p'
        ps_input = problem.find_elements_by_xpath(xpath)
        ps_input = '\n'.join([p.get_attribute('textContent').strip() for p in ps_input])
        details.input_format = ps_input
        print(ps_input)

        # Output format
        xpath = '//div[@class="output-specification"]//p'
        ps_output = problem.find_elements_by_xpath(xpath)
        ps_output = '\n'.join([p.get_attribute('textContent').strip() for p in ps_output])
        details.output_format = ps_output
        print(ps_output)

        # Notes
        xpath = '//div[@class="note"]//p'
        ps_note = problem.find_elements_by_xpath(xpath)
        ps_note = '\n'.join([p.get_attribute('textContent').strip() for p in ps_note])
        details.notes = ps_note
        print(ps_note)

        # Sample test cases
        xpath = '//div[@class="sample-tests"]/div[@class="sample-test"]/div//pre'
        for i, t in enumerate(problem.find_elements_by_xpath(xpath)):
            if i % 2 == 0:
                test_input = t.get_attribute('innerHTML').split('<br>')
                test_input = '\n'.join([x.strip() for x in test_input if x])
            else:
                test_output = t.get_attribute('innerHTML').split('<br>')
                test_output = '\n'.join([x.strip() for x in test_output if x])
                # Add the input and output to the list.
                details.sample_tests.append([test_input, test_output])

        print('Sample test cases:')
        for t in details.sample_tests:
            print('>>> Input')
            print(t[0])
            print('>>> Output')
            print(t[1])
            print('-----')

        # Tags
        print('Tags:')
        xpath = '//div[@id="sidebar"]//div[contains(text(), "tags")]/following-sibling::div//div[contains(@class, "roundbox")]//span'
        try:
            tags = problem.find_elements_by_xpath(xpath)
        except Exception:
            logger.debug('Tags not found.')
        else:
            details.tags = [x.text.strip() for x in tags if x]
            for tag in details.tags:
                print(tag)
            return details

    # def get_problem(self, url):
    #     driver = self.driver

    #     # Gathering challenge information
    #     driver.get(url)

    #     details = {'url': url}

    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "title")))

    #     # WebDriver Element
    #     problem = driver.find_element_by_class_name('problem-statement')

    #     name = problem.find_element_by_class_name('title')
    #     details['name'] = name.text

    #     time_limit = problem.find_element_by_class_name('time-limit')
    #     details['time_limit'] = time_limit.text

    #     xpath = '//div[@class="header"]/following-sibling::div//p'
    #     description = problem.find_elements_by_xpath(xpath)
    #     description = '\n\n'.join([x.text for x in description])
    #     details['description'] = description
    #     print(description)

    #     # Input format
    #     xpath = '//div[@class="input-specification"]//p'
    #     ps_input = problem.find_elements_by_xpath(xpath)
    #     ps_input = '\n'.join([x.text.strip() for x in ps_input])
    #     details['input_format'] = ps_input
    #     print(ps_input)

    #     # Output format
    #     xpath = '//div[@class="output-specification"]//p'
    #     ps_output = problem.find_elements_by_xpath(xpath)
    #     ps_output = '\n'.join([x.text.strip() for x in ps_output])
    #     details['output_format'] = ps_output
    #     print(ps_output)

    #     # Notes
    #     xpath = '//div[@class="note"]//p'
    #     ps_note = problem.find_elements_by_xpath(xpath)
    #     ps_note = '\n'.join([x.text.strip() for x in ps_note])
    #     details['notes'] = ps_note
    #     print(ps_note)

    #     # Sample test cases
    #     xpath = '//div[@class="sample-tests"]/div[@class="sample-test"]/div//pre'
    #     details['sample_tests'] = []
    #     for i, t in enumerate(problem.find_elements_by_xpath(xpath)):
    #         if i % 2 == 0:
    #             test_input = t.get_attribute('innerHTML').split('<br>')
    #             test_input = '\n'.join([x.strip() for x in test_input if x])
    #         else:
    #             test_output = t.get_attribute('innerHTML').split('<br>')
    #             test_output = '\n'.join([x.strip() for x in test_output if x])
    #             # Add the input and output to the list.
    #             details['sample_tests'].append([test_input, test_output])

    #     print('Sample test cases:')
    #     for t in details['sample_tests']:
    #         print('>>> Input')
    #         print(t[0])
    #         print('>>> Output')
    #         print(t[1])
    #         print('-----')

    #     # Tags
    #     print('Tags:')
    #     xpath = '//div[@id="sidebar"]//div[contains(text(), "tags")]/following-sibling::div//div[contains(@class, "roundbox")]//span'
    #     try:
    #         tags = problem.find_elements_by_xpath(xpath)
    #     except Exception:
    #         details['tags'] = []
    #         logger.debug('Tags not found.')
    #     else:
    #         details['tags'] = [x.text.strip() for x in tags if x]
    #         for tag in details['tags']:
    #             print(tag.text)
    #         return details


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-v', '--verbosity')
    # parser.add_argument('-f', '--folder')

    # choices = ('CodeChef', 'Codeforces', 'HackerRank', 'Topcoder')
    choices = (
        ('Codeforces', Codeforces),
        ('HackerRank', HackerRank))

    print('Choose the website ...')  # TODO: Complete the statement.
    for i, (name, _) in enumerate(choices):
        print(f'{i}: {name}')

    try:
        choice, choice_cls = choices[int(input().strip())]
    except Exception as e:
        logger.error('Wrong input. %s.', e)
        raise

    # Credentials
    print(f'Provide your credentials for {choice}:')
    # username = input('Username:')
    # password = getpass('Password:')
    username = 'mydarksoul69@gmail.com'  # TODO: Debug only
    password = 'l>^cFr8%D7Vtcyd6SM'  # TODO: Debug only

    driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')

    obj = choice_cls(username, password, driver)

    try:
        obj.login()
    except Exception as e:
        logger.error('Unable to login to HackerRank. %s.', e)
        driver.quit()
        sys.exit(1)

    # Keep alive so we dont need to insert credentials every time.
    while True:
        url = input('Challenge URL: ')
        details = obj.get_problem(url)
        obj.create_files(details)
    driver.quit()


if __name__ == '__main__':
    main()
# https://www.hackerrank.com/contests/hourrank-26/challenges/cloudy-day