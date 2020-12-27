# Sustainable BookCycle

[![Mockup](https://i.ibb.co/2qWsQg2/Read-Me-Intro-Picture.png)](https://i.ibb.co/2qWsQg2/Read-Me-Intro-Picture.png)

BookCycle is a fictitious pre-owned books recycling service in Singapore that buys used books from individuals and re-sell them. They operate an online storefront where customers can buy pre-owned books easily. The main problem they're trying to solve are users who find it cumbersome to sell their used books themselves and prefer an intermediary to help them deal with the logistics and operations of selling used books. Their social mission is also through the exchange of used books to encourage a more green behaviour that de-emphasises consumerist behavior. 

As such, Bookcycle website provides a modern, responsive book buying experience for customers who wants to learn more about the business and buy pre-owned books onine easily. With a shopping cart feature, it makes it easy for the customer to buy multiple books at a time and the integration with stripe checkout makes online payment via card all the more seamless. 

You can browse the website [here](https://sustainablebooks.herokuapp.com/).
You can access the admin dashboard [here](https://sustainablebooks.herokuapp.com/admin) 

Login Information
Admin:
* Username - edmundgoh
* Password - edmundgoh 

Customer:
* Username - peaceddy 
* Password - ruczA1-sywjik-wunnup

## User Experience

The online storefront introduces the user to the concept of the store and its purpose on an attractive homepage. Symbolising its modern values, the website is designed with two main colors, teal and coral peach. The green symbolises the mission of bookcycling and its green efforts. The coral peach is a complementary color to show the vibrancy of the community of book sharing and accentuates the call-to-action buttons. 

Open Sans and Montserrat font pairing is used to reflect the modernity and simplicity of the business as they are very clean and simple fonts. 

In general, the online storefront allows the user to: 
* Learn about the store concept from the homepage with three clear sections, Hero, Buying Books and Trade-in that explains the overview of the concept of the business very clearly upfront. 
* Buy pre-owned books 
* Add items to a shopping cart 
* Pay for items online 
* Create a user account and login to save their shopping cart history 
* To attract more customers and reduce the checkout steps, allow users to buy books without signing up for an account 
* Get information on how to trade-in books 

To guide the development, I visualised the concept with the core pages of Homepage, Browse Books and Cart Page which requires customise design on Figma. You can view the wireframes [here](https://www.figma.com/file/WH9n7sjWXB18WOa5MdOvtk/Untitled?node-id=0%3A1).

#### User Stories:
__Buying Book__ 
* As a customer who wants to buy books, I can see all the books currently available for purchase. 
* When I'm trying to find a specific book, I can search the book by its title. 
* When I'm trying to browse books of a specific genre, I can filter books by available Genres. 
* When I'm looking for a specific book within a genre, I can search the book with a title and filter it by Genre. 
* When buying multiple books, I can add multiple books I want to buy into a shopping cart so I can checkout all of them at once and only have to pay once. 
* When checking out, I can edit the quantity of books I want to buy at the shopping cart at the item level. 
* Before paying, I can see how much it costs in total so I know I am within my budget. 

__Trading in Book__
* When I'm interested about how to trade-in, I can get the instructions and information via the trade-in page. 

__Creating and Manage An Account__
* As a frequent customer, I can create an account to store my cart information to my account. 
* As a registered customer, I can change my password, edit my emails and logout from the store. 
* When creating my account, I can verify my email via the email verification sent upon a successful account creation step. 

## Features

### Existing Features

As a lightweight online commerce store to facilitate online book buying: 
* User Accounts - Allow users to sign up, login, logout, change password and change email 
* Browse Books - Display available books for sale with title, author and price information 
* Search Books - Search books by title and/or genre 
* Shopping Cart - View and add items to cart that shows line item, quantity per item and total cart cost 
* Checkout and Payment - Pay for items in cart with credit card supported by Stripe 
* Trade-in - Allow users to get instructions on how to sell books to the company 
 
 ### Possible Features To Be Implemented 
 * View Book Details - Allow user to go to a page for each book with more details like description and more pictures of the book 
 * View Purchases - Allow user to see past purchases 
 * Shipping - Allow user to provide shipping information 
 * Inventory System - Allow admin to indicate how many quantity are available for each book 
 
## Testing 

The responsive website is manually tested on two available devices to the creator: Macbook Pro 2019 16 Inch and a Iphone 11 Pro Max. 
For desktop, the website is tested on both safari and chrome. 
On iOS, the website is tested on safari only. 
The test scenarios can be found [here](https://docs.google.com/spreadsheets/d/1_0fRuHt0z8NrkiBz9JV5g0neqFOq3Fwk53Xs__CqkZU/edit?usp=sharing)

## Technology

* Heroku - For deployment 
* HTML
* CSS 
* JS
* Bootstrap 4
* Django
* Python 3
* Stripe
* Github
* Cloudinary - To host image uploads
* Gmail - To send emails
* Google Fonts

## Deployment

The project is deployed onto Heroku via Gitpod IDE using the following command lines: 

* `heroku login -i`
* `heroku create <APP NAME>`
* Creating a Procfile
* Changing `ALLOWED_HOSTS = ["sustainablebooks.herokuapp.com"]` in settings.py
* Generating requirements.txt `pip3 free --local > requirements.txt`
* Uploading .env credentials into Heroku Col Var. 
* `git add *`
* `git commit -m "message"`
* `git push heroku master`

## Credits

### Stock Images ###
From Unsplash
* Book with Leaf Photo by [Joanna Kosinska](https://unsplash.com/@joannakosinska?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/books-green?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText")
* Open Book by [Sam Rios](https://unsplash.com/@joannakosinska?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/books-green?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText")
* [FontAwesome](https://fontawesome.com/) Icons 

This project is created solely for educational purposes as part of Code Institute Full Stack Bootcamp

