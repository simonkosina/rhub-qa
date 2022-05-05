class BasePage(object):
    """
    Base page object.
    """

    def __init__(self, context):
        self.browser = context.browser

    def visit(self, url: str):
        """
        Go to the provided url and maximize the window.

        Arguments
        ---------
        url: str
            URL to go to.
        """

        self.browser.get(url)
        self.browser.maximize_window()

    def find_element(self, loc: tuple):
        """
        Find the provided element in the browser.

        Arguments
        ---------
        loc: tuple
            Locator and the attribute value, e.g. loc = (By.ID, "username")
        """

        return self.browser.find_element(*loc)

    def input(self, el, text: str):
        """
        Inputs text into the provided element.

        Arguments
        ---------
        el: any
            Element to enter the text into.
        text: str
            Text to enter.
        """

        el.click()
        el.clear()
        el.send_keys(text)

    def __getattr__(self, attr: str):
        """
        Searches the `locators` dictionary defined in the class
        and returns an element based on the record found in the dictionary.

        Arguments
        ---------
        attr: str
            Name of the attribute to find an element for.

        Usage
        -----
        class LoginPage(BasePage):
            locators = {
                "confirm_btn": (By.ID, "kc-login"),
            }

        login_page = LoginPage(context)\\
        login_page.confirm_btn.click()
        """

        if self.locators and attr in self.locators:
            return self.find_element(self.locators[attr])
        else:
            raise AttributeError(attr)
