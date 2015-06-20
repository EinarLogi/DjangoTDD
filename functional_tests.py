from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #check out homepage
        self.browser.get('http://localhost:8000')

        #the page title and header should mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #you are invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #you type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        #When you hit enter, the page updates, and the page lists
        #"1: Buy peacock feathers" as an item in a to-do list
     
        inputbox.send_keys(Keys.ENTER)

        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        #There is still a text box inviting her to add another item. you
        #enters "Use peacock feathers to make a fly" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER) 
        #The page updates again, and now shows both items on your list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')        
        #You wonder whether the site will remember the list. You see that the site has
        #generated a unique URL for you  -- there is some 
        #explanatory text to that effect
        self.fail('Finish the test!')
        #You visit that URL - your to-do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


