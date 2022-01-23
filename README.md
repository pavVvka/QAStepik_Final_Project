QAStepik_Final_Project.  https://stepik.org/lesson/199980/step/6?unit=174035
* Test Suite for multipage website.
 
![skills_1](https://user-images.githubusercontent.com/83756447/150677710-48598c21-7c03-47e0-992d-1898e0ed610b.jpg)
![skills_2](https://user-images.githubusercontent.com/83756447/150677712-cb63946e-fe52-4a6e-92f7-b50afa51af12.jpg)
![skills_3](https://user-images.githubusercontent.com/83756447/150677714-ad8bdcde-17cc-45b1-af23-b9c440669e26.jpg)

# Pytest + Selenium in Page Object pattern.
![qa-test-project-file-structure](https://user-images.githubusercontent.com/83756447/150374298-b96e756e-3823-4831-87fe-aed83264c3ef.jpg)


pytest -v --tb=line --language=en -m need_review

    runs 4 from 12 tests:
    All asserts are in separate Page Object files.
    ---------------------
    * test_user_can_add_product_to_basket
      - Test uses def Setup from Class group: to create new user>login>check if it is loginned
      - Opens Product Page>keep stored Price and Name of Product for fucher check
      - Activate P.O. method: No message about adding roduct to cart should be at Product Page (negative test)
      - Activate P.O. method: Adding Product to Cart
      - Activate P.O. method: Asserts that Add to Cart message presents (pozitive test)
      - Activate P.O. method: Check if Name and Price in Cart are same as at Product Page
      - Quits browser through @pytest.fixture in Conftest.py 
      
    * test_guest_can_add_product_to_basket
      - Same test as above
      - without new user registration
      - test uses parametrization to run list of product links
      - test marks all fail tests from list as XFAIL
      
    * test_guest_cant_see_product_in_basket_opened_from_product_page
      - From Product Page open Cart
      - Activates P.O. method of asserts that Cart is empty
      - Activate P.O. method asserts that Message about empty cart presents on Cart Page
      
    * test_guest_can_go_to_login_page_from_product_page
      - test uses method from BasePage(parent) class to open link from any pages
