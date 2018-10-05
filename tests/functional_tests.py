from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Kieth has discovered a new to-do app
        #  and checks this web page
        self.browser.get("http://0.0.0.0:5050")
        # He noticed the page title and header mention to-do list
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")
        # He is invited to enter a to-do item
        # He types "Buy bread" into a text box
        # When he hits enter, the page updates and now the page lists
        # "1. Buy bread" as an item in a to-do list

        # There is still a text box inviting to add another item
        # He enters "Slice the bread"
        # Sites remembers a list and generates unique url for him
        # When he visits the url the to-do list is still there.
        # Now he can leave the page






if __name__ == "__main__":
    unittest.main(warnings="ignore")
