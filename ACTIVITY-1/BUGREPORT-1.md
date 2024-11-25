### Bug 0 

**Severity**
 Urgent - S1

**Summary**
- User is unable to view the correct product when clicking on any product in the grid view. 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Click on any product in the grid view (e.g. Sauce Labs Backpack)
- Observe the incorrect product is shown in the detailed view (displays Sauce Lab Fleece Jacket)

**Actual results**
- The incorrect product is displayed in the detailed view.

**Expected results**
- The correct product should be displayed in the detailed view when clicked on in the grid view.



### Bug 1 

**Severity**
 Urgent - S1

**Summary**
- User is unable to add or remove products to the cart from the grid or detailed product views.

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Attempt to add or remove a product from the grid or detailed product view
- View the item is not added or removed from the cart when the Add to cart/Remove button is clicked

**Actual results**
- The item is not added or removed from the cart when the Add to cart/Remove button is clicked

**Expected results**
- The item should be added or removed from the cart when the Add to cart/Remove button is clicked



### Bug 2

**Severity**
 Urgent - S1

**Summary**
- User is unable to view the cart to proceed to checkout. 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Add items to the cart 
- Click on the cart icon
- View the /cart.html page does not load

**Actual results**
- The user is not redirected to the /cart.html page when the cart icon is clicked

**Expected results**
- The user should be redirected to the /cart.html page when the cart icon is clicked



### Bug 3

**Severity**
 High - S2

**Summary**
- Invalid characters can be entered in the personal information fields on the 'Checkout: Your Information' page. 

**Steps to reproduce**
- Log into the application using the login credentials of the `standard_user`
- Add an item to your cart and proceed to checkout
- Enter special characters only in the first name, last name and postcode fields
- Click Continue

**Actual results**
- The user is able to proceed to the 'Checkout: Overview" page.

**Expected results**
- The user should not be able to enter special characters into these fields and progress in the checkout flow. 
- These fields should have validation to ensure the correct characters are added - alphabetical for name fields, alphanumeric for postcode field.



### Bug 4

**Severity**
 High - S2

**Summary**
- Incorrect product images are display on the product grid view. 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- View all products shown with an image of a dog with a ball in its mouth

**Actual results**
- All products on the product grid view display the same image
- Clicking on a product to view the detailed view displays the correct image

**Expected results**
- The image displayed in the product grid view should be specific to the product



### Bug 5 

**Severity**
 High - S2

**Summary**
- Sauce Labs Fleece Jacket item not found when viewing detailed view 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Click to view the detailed view of the Sauce Labs Fleece Jacket item
- View the item is not found and incorrect amount and description is displayed

**Actual results**
- Item is not found and incorrect description and amount is displayed

**Expected results**
- When viewing the detailed product view for the Sauce Labs Fleece Jacket item, the correct information should be displayed. 



### Bug 6

**Severity**
 High - S2

**Summary**
- Incorrect number of items displayed in cart when adding/removing items. 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Add/remove items to the cart 
- Observe the number of items added in the grid viw does not match the number on the cart icon

**Actual results**
- The number of items added to the cart in the grid view does not match the number of items displayed on the cart icon. 

**Expected results**
- The number of items added in the grid view should match the number of items displayed on the cart icon. 



### Bug 7

**Severity**
 High - S2

**Summary**
- User is unable to apply a filter to the product grid view. 

**Steps to reproduce**
- Log into the application using the credentials of the `problem_user`
- Apply any filter from the dropdown in the top right of the product grid view 

**Actual results**
- No filter is applied and the default 'Name (A to Z)' filter persists.

**Expected results**
- When a filter is applied, the product grid should be dynamically filtered by the selected filter. 



### Bug 8

**Severity**
- High - S2

**Summary**
- First item in the product grid view displays the incorrect image

**Steps to reproduce**
- Login to the application as `visual_user`
- View the first product in the grid displays the incorrect image, regardless of the filter added
- Click on the product to view the correct image in the product detailed view

**Actual results**
- The first product in the product grid view always displays an image of a dog.
- Clicking into the detailed view displays the correct image.

**Expected results**
- The correct image should be displayed for a product when viewing the grid and detailed views.  



### Bug 9

**Severity**
- Low - S3

**Summary**
- User is able to proceed to checkout with no items in cart. 

**Steps to reproduce**
- Login to the application as any user
- Ensure no items have been added to the cart
- Click on the cart icon
- Click the 'Checkout button'

**Actual results**
- The user is able to enter and complete the checkout flow. 

**Expected results**
- The user should not be able to enter and complete the checkout flow without any items in their cart. 



### Bug 10

**Severity**
- Low - S3

**Summary**
- Cart icon is not aligned to the top right of the page

**Steps to reproduce**
- Login to the application as `visual_user`
- View the cart icon at the top right of the page

**Actual results**
- The cart icon is not aligned to the top right of the page. 

**Expected results**
- The cart icon should be aligned to the top right of the page. 


### Bug 11

**Severity**
- Low - S3

**Summary**
- Add to cart/Remove button overflows the border of the product tile for the last item 

**Steps to reproduce**
- Login to the application as `visual_user`
- View the last product in the product grid view 
- Observe the Add to cart/Remove button overflows the border of the tile

**Actual results**
- The Add to cart/Remove button overflows the border of the tile.

**Expected results**
- The Add to cart/Remove button should be contained within the tile of the product in the product grid view.



### Bug 12

**Severity**
- Low - S3

**Summary**
- Hamburger icon/Close icon is not horizontally aligned

**Steps to reproduce**
- Login to the application as `visual_user`
- View the menu hamburger icon in the top left is not horizontally aligned
- Click on the hamburger icon to view the cancel icon is not horizontally aligned

**Actual results**
- The hamburger menu icon and the menu close icon are not horizontally aligned. 

**Expected results**
- The hamburger menu icon and the menu close icon should be horizontally aligned. 
