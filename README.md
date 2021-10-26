<h1 align="center">Book Bin</h1>

My goal here is to create an attractive e-commerce book site. The site will have a library of books that users can purchase to be sent to their homes. The site will also feature reviews of books that registered users can write and upload themselves. All books will have a star rating out of five where all registered users can rate the books they have read, with the overall rating being displayed. Registered users will also have the ability to create their own lists which will be displayed on their profile page, for example their favourite books list or their reading list for books they want to read next. These lists could be public, viewable to anyone, or private, only viewable to the user who created the list. Registered users will also be eligable for certain deals/offers and will have the ability to sign up for a subscription service.

## User Experience (UX)

- ### User Stories

    - #### Non-registered users

        1. As a non-registered user, I want to browse the books available at this site.

        2. As a non-registered user, I want to search for a specific book to purchase.

        3. As a non-registered user, I want to read reviews and ratings of a book I am interested in.

        4. As a non-registerd user, I want to sign up to write reviews, create lists, and recieve offers and deals.

    - #### Registered users

        1. As a registered user, I want to login/logout of my account.

        2. As a registered user, I want to recover my password as I have forgotten it.

        3. As a registered user, I want to receive an email confirmation after registering.
        
        4. As a registered user, I want to write a review of a book I have recently read.

        5. As a registered user, I want to make a reading list of the books I want to read next.

        6. As a registered user, I want to sign up for the subscription service.

- ### Design

    - The color scheme for the site will be white and maroon.

    - The main font of the site will be x with Sans Serif as the fallback font.

- ### Wireframes

## Features

## Technologies Used

### Languages Used

### Frameworks, Libaries, and Programs Used

## Testing

### Testing User Stories

### Further Testing

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

## Credits

### Code

- [Code for overlay from Code Institute Boutique Ado project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/71413627006c4cac9b18a1de1e12a4ff/)

- [Script for update/remove button logic taken from Code Institute Boutique Ado project. Script is used in bag.html](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/01a6e729849c489b88b9a6810f05c47d/)

- [Code for quantity form taken from Code Institute Boutique Ado project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/21e3b111100f5c8daa4bc6e9565bde09980b33d8/products/templates/products/product_detail.html)

- [Code for button logic taken from. Code is used in quantity_input_script.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/0a5335f2e95f58b10207ea57cedcdd063251a3ff/products/templates/products/includes/quantity_input_script.html)

- [Code for toasts taken from Code Institute Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/e5323862cc7563f65526f0108f37c57ad92f7931/templates/includes/toasts)

- [Code for checkout models](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/faaa31bcbd1bcc5fdf7d54c57d51c031df9d7460/checkout/models.py)

### Content

### Media

- [hero image](https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1590&q=80)

### Acknowledgements