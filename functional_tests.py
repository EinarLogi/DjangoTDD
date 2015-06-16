from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_Start_a_list_and_retrieve_it_later(self):
        #check out homepage
        self.browser.get('http://localhost:8000')

        #the page title and header should mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        #you are invited to enter a to-do item straight away

        #you type "Buy peacock feathers" into a text box

        #When you hit enter, the page updates, and the page lists
        #"1: Buy peacock feathers" as an item in a to-do list

        #There is still a text box inviting her to add another item. you
        #enters "Use peacock feathers to make a fly" 

        #The page updates again, and now shows both items on your list

        #You wonder whether the site will remember the list. You see that the site has
        #generated a unique URL for you  -- there is some 
        #explanatory text to that effect

        #You visit that URL - your to-do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


