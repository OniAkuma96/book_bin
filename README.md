<h1 align="center">Book Bin</h1>

[View the live project here.](https://book-bin.herokuapp.com/)

[Link to GitHub Repository](https://github.com/OniAkuma96/book_bin)

![AmIResponsive mockup](/media/amiresponsive-ms4.png)

My goal here is to create an attractive e-commerce book site. The site will have a library of books that users can purchase to be sent to their homes. The site will also feature reviews of books that registered users can write and upload themselves. All books will have a star rating out of five where all registered users can rate the books they have read, with the overall rating being displayed. I will use Stripe for a payment system and registered users will have the ability to save their delivery info to their profile and view their order history.

## User Experience (UX)

- ### User Stories

    - #### Non-registered users

        1. As a non-registered user, I want to browse the books available at this site.

        2. As a non-registered user, I want to search for a specific book to purchase.

        3. As a non-registered user, I want to read reviews and ratings of a book I am interested in.

        4. As a non-registerd user, I want to sign up.

    - #### Registered users

        1. As a registered user, I want to login/logout of my account.

        2. As a registered user, I want to recover my password as I have forgotten it.

        3. As a registered user, I want to receive an email confirmation after registering.
        
        4. As a registered user, I want to write a review of a book I have recently read.

- ### Design

    - The color scheme for the site will be white and maroon.

    - The main font of the site will be IBM Plex Sans with Sans Serif as the fallback font.

- ### Wireframes

    - These are the wireframes that I made for this project. They can be found in /static/wireframes/ folder. Please note these were early plans I made before I started the development of the site and do not match the final product.

    ![Homepage Web](/static/wireframes/homepage-web.png)
    ![All Products Web](/static/wireframes/shop-web.png)
    ![Product Detail Web](/static/wireframes/product-detail-web.png)
    ![Homepage Tablet](/static/wireframes/homepage-tablet.png)
    ![All Products Tablet](/static/wireframes/shop-tablet.png)
    ![Product Detail Tablet](/static/wireframes/product-detail-tablet.png)
    ![Homepage Mobile](/static/wireframes/homepage-mobile.png)
    ![All Products Mobile](/static/wireframes/shop-mobile.png)
    ![Product Detail Mobile](/static/wireframes/product-detail-mobile.png)

## Features

### Existing Features

- Navigation bar
    - Home logo button
    - All books button allows users to see all books on site
    - Book genre allows users to filter by category
    - Search bar allows users to search by title, author, or sub-genre
    - Profile dropdown allows non-registered users to sign-in or register, allows registered users to view their profile or logout, and allows store owners to access the product management page for adding, editing, and deleting products
    - Bag link with auto updating price value
    - Logo, all books, and genre buttons collapse on medium screens and smaller

- Responsive on all device sizes
    - Products page will feature 6 books per row on extra large screens, 4 per row on large, 3 per row on medium, and 1 per row on small.

- Full CRUD functionality for superusers.

### Features Left to Implement

- Ideally I wanted the overall rating from reviews of a specific product to be displayed on the all products page but was not sure how to pass that infomation to it as it would need the product id of all the products

## Technologies Used

### Languages Used

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Javascript](https://www.javascript.com/)

- [Python 3](https://docs.python.org/3/)

### Frameworks, Libaries, and Programs Used

- [Bootstrap v4.4](https://getbootstrap.com/)
    - For a responsive website framework

- [Bootstrap Toasts](https://getbootstrap.com/docs/4.3/components/toasts/)
    - For displaying messages to users throughout the site

- [Django](https://docs.djangoproject.com/en/3.2/)
    - For a full-stack framework

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - For Django login, logout, registering, email confirmation, password changes/reset, and everything to do with account authentication

- [Django Countries](https://pypi.org/project/django-countries/)
    - For the dropdown country selector on checkout page and profile

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - For styling and laout of all forms on site

- [jQuery](https://jquery.com/)
    - Used for simple DOM manipulation. Mainly in the logic for quantity buttons on product detail and bag pages

- [Google fonts](https://fonts.google.com/)
    - For a variety of fonts

- [Font Awsome](https://fontawesome.com/)
    - For icons

- [Git](https://git-scm.com/)
    - For version control through the Gitpod terminal to commit to Git and Push to GitHub

- [GitHub](https://github.com/)
    - Used to store the projects code after being pushed from Git

- [Heroku](https://www.heroku.com)
    - For deployment

- [Amazon Web Services](https://aws.amazon.com/)
    - For hosting of static files and media

## Testing

- For validation of HTML I used [W3C Nu HTML checker](https://validator.w3.org/nu/)
    - ![HTML checker results](/media/nu-html-checker-ms4.png)
    - These were the results from the validator. As for errors 1-4 I thought the duplicated id was not a problem as one is for the desktop navbar and the other for mobile collapsable navbar.

- For validation of CSS I used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - All CSS passed with no errors.

### Testing User Stories

- Non-Registered Users

    1. As a non-registered user, I can click on the all books link or the shop now button on the homepage to browse all avaliable books

    2. As a non-registered user, I can use the search bar in the middle of the navbar to search for a book by title, author, or genre

    3. As a non-registered user, I can navigate to a book I am interested in by clicking on the cover and reading any reviews that have been posted below

    4. As a non-registered user, I can sign up by clicking the account icon and clicking sign up from the navbar

- Registered Users

    1. As a registered user, I can login/logout of my account using the account icon in the navbar

    2. As a registered user, I can recover my password by using the forgot password link on the login page

    3. As a registered user, I will receive an email to confirm my account after registering as shown in this picture:

        - ![Email conformation](/media/ms4-email.png)

    4. As a registered user, I can click the write a review link below a book's details to be taken to the page to write a review

### Further Testing

- Testing the navbar
    - Tested all links, searching, and genre filtering on desktop, tablet and mobile

- Testing adding/removing products from bag
    - Users can add items to their bag in the desired quantity, from 1 to 99 users cannot select less then 1 or more then 99 as intended
    - Users can update quantity of an item in their bag as intended
    - Users can completely remove items from their bag

- Testing Stripe payments
    - First I tested a successful payment with card number 4242 4242 4242 4242. The loading spinner correctly comes up, the order is successful and the order summary is correctly displayed with a toast message to the user that their order was successful. However the confirmation email does not send and the webhook is getting a 500 error and I'm not sure how to fix this
    - Next I tested an unsuccessful payment with card number 4000 0000 0000 9995. The payment fails and a message is displayed to the user telling them they have insufficient funds.
    - Testing webhooks: Here is the test for a payment_intent.payment_failed through the deployed heroku site:
        ![payment failed](/media/wh-test-payment-failed.png)
    - Testing successful payment
        - I will now add some pictures showing that a successful order will be created in the database, successful webhook will be recieved on Stripe, and an email will be sent to the email address provided in the order form.
        - ![Test order delivery form](/media/successful-order-test-1.png)
        - ![Test order site confirmation](/media/successful-order-test-2.png)
        - ![Test order created in database](/media/successful-order-test-3.png)
        - ![Test order successful webhook from Stripe](/media/successful-order-test-4.png)
        - ![Test order email sent](/media/successful-order-test-5.png)
    

- Testing Review posting
    - Tested review posting by logging in and trying to submit for without comment to make sure it's required. Then by submitting a valid review which succeeds
    - As shown in the picture below the overall rating is calculated correctly and reviews display all the correct info
    - ![Review test picture](/media/review-post-test.png)

- Testing CRUD functionality for superusers
    - Tested adding a product
    - Tested editing a product
    - Tested deleting a product

### Known Bugs

## Deployment

- Here are the steps I went through to deploy my project. I used Heroku for deployment and AWS to store static files.

- Part 1 - deploying to Heroku

    1. I created a new app on Heroku with the region closest to me, Europe.

    2. Next I submitted an order form for the Heroku Postgres add-on which is needed for the database. I used the free plan for this project. I also had to install dj_database_url and psychopg2 and freeze to requirements.txt in gitpod for this to work.

    3. Next I imported dj_database_url to my project's settings.py file and rewrote the databases code to use dj_database_url. As I am now connecting to postgres for my database I need to run all migrations again. So I did this using: python3 manage.py migrate.

    4. Next I imported all my product data. As I had made a json fixtures file I could do this by using loaddata command in gitpod.

    5. Next I created a superuser for my new database using createsuperuser command in gitpod.

    6. Now that my new database is setup I also removed the Heroku database url from settings.py so it does not appear in version control.

    7. Next I created an if statement in settings.py to see if the variable 'DATABASE_URL' is in the environment variables. If it is then we tell our project to use that url for our database setting, and if not then use the default sqlite3 configuration.

    8. Installed gunicorn and freeze it to requirements.txt. Gunicorn will act as web server.

    9. Created Procfile to tell Heroku to create a web dyno.

    10. Logged in to Heroku in gitpod CLI using command heroku login -i and entering credentials. Then temporarily disabled collection of static files so Heroku will not try to collect static files when I deploy, command heroku config:set DISABLE_COLLECTSTATIC=1

    11. Added host name of Herkou app to allowed hosts in settings.py with localhost added too so it will still work in gitpod.

    12. To deploy to Heroku I first initialized Heroku git remote with command heroku git:remote -a app name, then pushed to Heroku with git push heroku.

    13. Next I setup my app so it would automatically deploy to Heroku when I push to github by clicking connect to Github button on deploy tab of app, finding repository and connecting the two. Lastly I enabled automatic deploys.

    14. Generated django secret key, added to config variables in Heroku, and in settings.py changed secret_key variable to get from environment. Now when pushing to github I can see a build in progress on Heroku which means automatic deployment is working.

- Part 2 - Using AWS to host static files

    1. Created new S3 bucket with the region closest to my location and unchecking block all public access setting.

    2. Enabled static website hosting in bucket's properties settings tab.

    3. Changed settings in permissions tab of bucket - cors configorations to allowedheaders: authorization, allowedmethods of GET, all allowedorigins and exposeheaders.

    4. Next in bucket policy setting clicked generate policy to create a security policy for bucket. The type being S3, allowing all principals and the action is get object. Pasted in amazon resource name and clicked add statement, then generate policy, then copied policy to bucket policy editor.

    5. Navigated to access control list tab and set list objects permission for everyone under public access section.

    6. Went back to AWS services menu to click on IAM to create a user to access bucket.

    7. Created new group for user to be in.

    8. Next created policy for group. Searched for S3 and imported S3 full access policy. Copied ARN from bucket policy and pasted it into the resource section of policy.

    9. Navigate back to groups and attatch policy just created to group.

    10. Create user and put user in group. Then downloaded users credentials csv.

    11. Installed boto3 and django-storages then freeze requirements to requirements.txt, and added storages to installed apps in settings.py

    12. In settings.py added a line of code to check if use aws is true and if it is to get the aws access key and secret key from the environment variables in Heroku.

    13. Created custom_storages.py to tell our app where the static and media files are located.

    14. Commit changes and push to github - static files are now in bucket and loading on Heroku url.

    15. Set aws s3 cache parameters in settings.py

    16. Created new folder in S3 bucket called media. Uploaded book covers and other media images to folder and granted public read access to these objects.

    17. Added stripe keys to Heroku config vars.

    18. Created new webhook endpoint that sends webhooks to heroku location. Added webhook signing secret to heroku config vars.

## Credits

### Code

- This project was based on Code Institute's Boutique Ado walkthrough project and parts of that project have been reused here. Those parts would be:
    - [Bag App](/bag/)
    - [Checkout App](/checkout/)
    - [Profiles App](/profiles/)
    - [The quantity input logic](/products/templates/products/includes/quantity_input_script.html)
    - [Bootstrap Toasts](/templates/includes/toasts/)

### Content

### Media

- [homepage hero image](https://wallpaperscraft.com/wallpaper/book_reading_glasses_208214)

### Acknowledgements