QAStepik_Final_Project.  https://stepik.org/lesson/199980/step/6?unit=174035
* Test Suite for multipage website.
 
![skills_1](https://user-images.githubusercontent.com/83756447/150677710-48598c21-7c03-47e0-992d-1898e0ed610b.jpg)
![skills_2](https://user-images.githubusercontent.com/83756447/150677712-cb63946e-fe52-4a6e-92f7-b50afa51af12.jpg)
![skills_3](https://user-images.githubusercontent.com/83756447/150677714-ad8bdcde-17cc-45b1-af23-b9c440669e26.jpg)

# Pytest + Selenium in Page Object pattern.

![qa-test-project-file-structure](https://user-images.githubusercontent.com/83756447/150680724-f35b81a4-b4c5-4cdd-803f-049d2341432e.jpg)


pytest -v --tb=line --language=en -m need_review

    Runs 4 @pytest.mark.need_review from 12 tests:
    All asserts are located in separate Page Object files and activate through P.O. methods.
    All locators are located in locators.py Page Object file.
    Basepage.py consists base parent class and have helper methods for all inherited objects:
          is_element_present(self, how, what) and is_not_element_present(self, how, what, timeout= *):
          "how" takes (css, id, xpath, ...) string as arguments and "what" takes selectors as arguments from locators.py 
    ---------------------
    * test_user_can_add_product_to_basket
      - Test uses "def Setup" for test Class group: to create new user>login>check if it is loginned
      - Opens Product Page>keep stored Price and Name of Product for future check
      - Activate P.O. method: No message about adding Product to cart should be at Product Page (negative test)
      - Activate P.O. method: Adding Product to Cart
      - Activate P.O. method: Asserts that Add to Cart message presents (pozitive test)
      - Activate P.O. method: Check if Name and Price in Cart are same as at Product Page
      - Quits browser through @pytest.fixture in conftest.py 
      
    * test_guest_can_add_product_to_basket
      - Same test as above
      - without new user registration
      - test uses parametrization to run list of product links
      - test marks all fail tests from list of product links as XFAIL
      
    * test_guest_cant_see_product_in_basket_opened_from_product_page
      - From Product Page open Cart
      - Activates P.O. method of asserts that Cart is empty
      - Activate P.O. method asserts that Message about empty cart presents on Cart Page
      
    * test_guest_can_go_to_login_page_from_product_page
      - test uses method from BasePage(parent) class to open link from any pages
