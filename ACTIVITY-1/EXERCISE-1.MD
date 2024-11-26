## TEST STRATEGY

1. Objective
The objective of the test strategy for this e-commerce application is to ensure that all critical features are reliable, user friendly and secure with no defects. The main flows involved which should be covered are login, filtering products, viewing products in the grid view and detailed view, adding/updating/removing items from the cart and checkout. These flows can be tested with a combination of manual and automated tests. 

2. Scope
Core functionalities to be tested which users engage with frequently:
- Login: Verify user authentication and error handling for incorrect credentials.
- Product Filtering: Ensure users can filter products accurately based on criteria (e.g., name, price).
- Product Grid and Detailed Views: Verify product details and ensure data is consistent across listings.
- Cart: Test adding, removing, and updating items in the cart.
- Checkout: Validate the checkout workflow, payment options, and form validation.

3. Types of Testing
To cover the application thoroughly, the strategy includes multiple testing types:
- Functional Testing: Ensures each feature works according to its requirements. Focus on verifying functionality such as successful logins, filtering accuracy, and adding items to the cart.
- End-to-End Testing: Covers end-to-end functionalities from login through checkout, simulating user behavior and interactions.
- UI Testing: Verifies visual elements like buttons and layout to ensure the UI is user-friendly and aligns with expected design.
- Regression Testing: After changes or fixes, tests previously covered functionality to catch any introduced regressions.
- Performance Testing: Ensures that pages like login, search, and checkout load within acceptable times, simulating different load scenarios.

4. Test Data Requirements
Identify the data necessary to validate different scenarios:
- User Data: Valid and invalid login credentials, ensuring realistic test coverage.
- Product Data: Sample data for a variety of product types, prices, and names.
- Cart and Order Data: Different order scenarios, including multiple items and payment method.

5. Environment Setup
Environments needed for testing:
- Staging/`dev` Environment: Ideally, testing should be done in an environment mirroring production. It should have stable test data and configurations.
- Browsers and Devices: Target the primary browsers (e.g., Chrome, Firefox) and devices (if mobile is supported) to reflect the user base.
- Test Automation Setup: Utilize Selenium WebDriver for browser interactions with Python, using a framework like Pytest to execute and manage test cases.


## TEST PLANS

- Log In/Log Out
    - When visiting the login page the user should be allowed to login with correct email and password.
    - When visiting the login page the user should not be allowed login with incorrect email and password.
    - Should be able to validate the username and password fields are case sensitive.
    - Should be able to login using the correct email and password when using browsers other than Chrome.
    - Should be able to display the Login CTA as active when there has been no characters entered in the username and password fields.
    - Should be able to display the error message "Epic sadface: Username is required" when the user clicks on the Login CTA when they have not entered any characters in the username or password fields.
    - When visiting the login page the user should be shown an error message when trying to login with an incorrect email and/or password.
    - Should be able to display the error message "Epic sadface: Username and password do not match any user in this service" when the user tries to login with an incorrect email and/or password.
    - Should be able to close an error message displayed by clicking 'x' and verify the message no longer appears.
    - Should not be able to close an error message and verify that the message persists.
    - Should be able to refresh the page after a successful login and verify the user's session persists.
    - Should not be able to refresh the page after successful login and verify the user is logged out of the application.
    - Should be able to redirect the user to the login page after a period of inactivity and session timeout.
    - Should be able to display a error message to the user after session timeout indicating they are required to login again.
    - Should be able to mask the password characters when the user enters characters in the password field.
    - Should not be able to display the password characters as unmasked in the password input field.
    - Should be able to copy and paste characters into the username and password fields. 
    - Should be able to redirect the user to the product grid view on successful login. 
    - Should not be able to allow access to the application when a locked out user attempts to login. 
    - When visiting the login page as a locked out user, should be able to display the error message "Epic sadface: Sorry, this user has been locked out." when the user enters in a username and password.
    - Should be able to logout of the application and be redirected back to the login page.
    - Should be able to display the username and password fields as empty once the user has logged out of the application. 
    - Should not be able to retain and prefill the username and password fields used to login when the user logs out of the application and is taken back to the login page.
    - When the user logs out and clicks the Back button, should not be able to give access to the application.
    - When the user logs out and clicks the Back button, should be able to display the error message "Epic sadface: You can only access '/inventory.html' when you are logged in.".
    - When the user logs out, should be able to deny access when the user attempts to view the application when the URL is updated.
    - When the user logs out and then updates the URL, should be able to display the error message "Epic sadface: You can only access '/inventory.html' when you are logged in.".
    - Should verify SQL injection is blocked on the sign in input fields.

- Filtering products
    - Should display the products in ascending alphabetical order when the "Name (A to Z)" filter is selected.
    - Should not display the products in descending alphabetical order when the "Name (A to Z)" filter is selected.
    - Should display the products in descending alphabetical order when the "Name (Z to A)" filter is selected.
    - Should not display the products in ascending alphabetical order when the "Name (Z to A)" filter is selected.
    - Should ensure filtered product names are sorted case-insensitively
    - Should display products in ascending order of price when the "Price (Low to High)" filter is selected.
    - Should not display products in descending order of price when the "Price (Low to High)" filter is selected.
    - Should display products in descending order of price when the "Price (High to Low)" filter is selected.
    - Should not display products in ascending order of price when the "Price (High to Low)" filter is selected.
    - Should verify that the filter selection persists when navigating between pages (e.g. returning to the product grid).
    - Should handle cases where multiple products have the same price and maintain a stable secondary sorting (e.g. sorted by name).
    - Should default to "Name (A to Z)" upon page load if no filter is explicitly applied
    - Should allow the user to switch between filters without reloading the page
    - Should display the selected filter at the top right of the page to indicate the applied filter
    - Should ensure no products are duplicated or missing after applying any filter.
    - Should verify that the applied filter is cleared upon logout and does not persist for a new session.

- Product grid view
    - Should display all products available in a grid layout after successful login.
    - Should adjust the grid layout dynamically for different screen sizes.
    - Should display product details (name, price, and thumbnail image) specific to each product in the grid.
    - Should be able to display product description for each item in the grid. 
    - Should maintain consistent grid alignment across various screen sizes and resolutions.
    - Should ensure that clicking the product image or name navigates to the product detailed view page.    
    - Should correctly display products based on active filters and sorting criteria.
    - Should not display any duplicate products in the grid view.
    - When a product is out of stock, should clearly display an "Out of Stock" badge or equivalent.
    - Should display the correct price for all products shown in the grid.
    - Should allow users to add products to the cart directly from the grid view, and see the cart icon be updated with number of items in the cart.
    - Should be able to add a product to the cart from the product grid view. 
    - Should ensure that the 'Add to Cart' button changes to 'Remove' when the product is added to the cart.
    - Should not be able to click on the 'Add to cart' button for an item and see the cart not updated.
    - Should ensure that adding or removing products updates the cart count and state without requiring a page reload.
    - Should not display the 'Add to cart' button as disabled.
    - Should show the correct product count in the grid view and cart when items are added or removed.

- Product detailed view
    - Should allow the user to navigate to the product detailed view by clicking the product name or image from the product grid.
    - Should display a 'Back to Products' button that navigates back to the product grid view.
    - Should be redirected back to the product grid view when the 'Back to Products' button is clicked.
    - Should retain the filter or sort state applied in the product grid when navigating back.
    - Should be able to display the correct product image, name, description, price and 'Add to Cart' or 'Remove' button based on the product state when viewing the detailed view. 
    - Should be able to display the same product details as displayed for the product in the product grid view. 
    - Should be able to add a product to the cart from the product detailed view. 
    - Should ensure the 'Add to Cart' button changes to 'Remove' when the product is added to the cart.
    - Should allow the user to add the product to the cart by clicking the 'Add to Cart' button. 
    - Should update the cart icon or badge to reflect the updated cart count after adding the product.
    - Should allow the user to remove the product from the cart by clicking the 'Remove' button.
    - Should display the correct button state ('Add to Cart' or 'Remove') when revisiting the detailed view for a product already in the cart.
    - Should display an error message if the product details fail to load

- Cart 
    - Should allow users to add products to the cart from the product grid view and product detail pages.
    - Should display a cart icon or badge that reflects the current number of items in the cart.
    - Should allow the user to open their cart by clicking on the cart icon.
    - Should allow multiple products to be added to the cart.
    - Should display an cart with no items when there have been no products added to the cart. 
    - Should display all added products in the cart, along with their names, prices, quantities, and description.
    - Should be able to verify items added to the cart persist when the session ends and the user logs back in. 
    - Should allow users to update the items in the cart by clicking the 'Remove' button and see the items are dynamically updated without needing to reload the page. 
    - Should update the cart count on the badge/icon immediately after removing an item.
    - Should be able to click on the product name in the cart and be redirected to the product detailed view. 
    - Should persist cart contents across different pages during the same session.
    - Should be able to display the 'Continue Shopping' button at the bottom of the cart. 
    - Should be able to display the 'Checkout' button at the bottom of the cart. 
    - Should be able to redirect the user to the product grid view when the 'Continue Shopping' button is clicked
    - Should be redirected to the 'Checkout: Your Information' page when the 'Checkout' button is clicked
    - Should prevent proceeding to checkout if the cart is empty.
    - Should not be able to proceed to the checkout when there are no items in the cart.
    - Should be able to refresh the page and validate that items in the cart persist. 

- Checkout 
    - Should allow users to proceed to the 'Checkout: Your Information' page when the 'Checkout' button is clicked on the cart page.
    - Should allow users to review their order summary before confirming the purchase.
    - Should be able to display the first name, last name and post code fields on the 'Checkout: Your Information' page. 
    - Should not be able to proceed in the checkout until the first name, last name and post code fields have been completed.
    - Should display an error message for each missing or invalid input (e.g., "First Name is required."). 
    - Should be able to validate correct data formats for each field (alphabetical for name fields, alphanumeric for postcode field). 
    - Should be able to navigate back to the cart when viewing the 'Checkout: Your Information' page and clicking the 'Cancel' button. 
    - Should be able to be redirected to the 'Checkout: Overview' page when user details have been added and the 'Continue' button is clicked. 
    - Should be able to validate the correct items in the user's cart are displayed on the 'Checkout: Overview' page. 
    - Should be able to display the product name, quantity, description and price of all items which have been added to the cart. 
    - Should be able to display the correct payment information to be used for the payment in the checkout. 
    - Should be able to mask sensitive card details in the payment information section and only display the last few digits of the card being used. 
    - Should be able to display the correct shipping information for the items in the checkout. 
    - Should be able to display the correct amount in the subtotal field (sum of individual product prices in the cart).
    - Should not be able to display the incorrect amount in the subtotal field (sum of individual product prices in the cart).
    - Should be able to display the tax amount underneath the subtotal amount 
    - Should be able to display the correct total amount (subtotal + tax) for all items in the cart. 
    - Should not be able to display the incorrect total amount (subtotal + tax) for all items in the cart. 
    - Should be able to be redirected to the product grid view when clicking 'Cancel' while on the 'Checkout: Overview' page. 
    - Should be able to be redirected to the 'Checkout: Complete' page when the user clicks on the 'Finish' button. 
    - Should redirect users to a confirmation or thank-you page after completing the checkout process.
    - Should be able to display the confirmation message 'Thank you for your order!' when viewing the 'Checkout: Complete' page. 
    - Should be able to display the 'Back Home' button when the user can see the order confirmation page. 
    - Should be redirected to the product grid view when the user clicks on the 'Back Home' button.
    - Should be able to clear the cart once the user has confirmed their order and are redirected back to the product grid view. 

## DECISIONS AND REASONS

### Selenium with Python
1. **Widespread Support for Browser Automation**
    - Selenium is a widely adopted tool for browser automation and supports all major browsers, including Chrome, Firefox, Edge, and Safari. This compatibility ensures robust cross-browser testing for e-commerce applications like SauceDemo to provide a consistent user experience.

    - Comprehensive Testing Coverage: Selenium allows testing dynamic and responsive web pages, which is essential for e-commerce platforms that use modern web technologies.

    - Customization: Selenium provides flexibility to write custom scripts to handle specific scenarios, such as pop-ups and dynamic content.

2. **Alignment with Organisation Tech Stack**
    - Python is used within the organisation, which simplifies the integration and learning curve for new testers or developers involved in automation.

    - Ease of Use: Python's simple syntax makes it accessible for beginners and efficient for experienced testers to write concise and readable test scripts.

    - Rich Ecosystem: Python has an extensive library ecosystem, enabling easy integration with complementary tools such as Pytest for test execution and reporting.

3. **Integration with Testing Libraries like Pytest**
    - Selenium integrates seamlessly with Python-based test libraries like Pytest, which enhances the testing process with the following benefits:
        - Robust Reporting: Pytest offers detailed logs and reporting capabilities. When paired with plugins like pytest-html, it provides insights into test results, failures, and coverage.
        - Parallel Test Execution: Pytest-xdist allows running multiple tests concurrently, reducing the overall test execution time, a critical factor for large e-commerce applications with numerous test cases.
        - Parameterisation: Pytest supports parameterized testing, allowing multiple datasets to be tested against the same test case, which is crucial for validating scenarios like login with different credentials or searching for various products.

4. **Real-World E-Commerce Needs**
    - Selenium is particularly suited to e-commerce applications due to its ability to handle complex user interactions:
        - User Journey Automation: Selenium can replicate complete user flows such as searching for products, adding them to a cart, and checking out—mimicking the exact behavior of real users.
        - Dynamic Element Handling: E-commerce sites often include elements that load asynchronously. Selenium provides robust support for handling dynamic elements using explicit and implicit waits.
        - Integration with CI/CD Pipelines: Selenium scripts can be integrated into CI/CD tools like GitHub Actions to ensure test execution is part of the deployment process, maintaining high product quality.

5. **Community Support and Documentation**
    - Selenium has a vast user base and extensive documentation, making it easier to troubleshoot issues or find resources to improve the automation framework. For Python, libraries like SeleniumBase provide additional abstractions for common use cases, further speeding up test development.