                                            
![Web Page view](/media/gg_home_page.png)

# README Table of contents

  - [**Project 5 Ecommerce - Golf Gear - Introduction**](#project-5-ecommerce---golf-gear---introduction)


  - [**Agile Methodology/Framework**](#agile-methodologyframework)


  - [**UI Designs**](#ui-designs)


  - [**Apps**](#apps)


  - [**Features**](#features)

  
  - [**Features to implement**](#features-left-to-implement)


  - [**Custom Logic**](#custom-logic)


  - [**Testing**](#testing)

  
  - [**Unfixed Bugs**](#unfixed-bugs)


  - [**Marketing Strategy**](#marketing-strategy)


  - [**Deployment**](#deployment)


  - [**Golf Gear Super User**](#golf-gear-super-user)


  - [**Credits**](#credits)


  - [**Project Summary**](#project-summary)

# Project 5 Ecommerce - Golf Gear - Introduction

Golf Gear is a website in which all avid golfers will love!  It allows all shoppers to visit, browse, create an account and finally purchase the items they desire.
A user will visit the site, be greeted with colourful and easy to navigate pages.  They can view all the products that are available, which range from clothing, clubs and accessories - everything a golfer needs!
In order to purchase an item, the user must create an account, which they can do easily via an available link, and by just filling in a few details - they are ready.
Once a user is logged in, they can then select any items in which they want to purchase... add them to thier basket and purchase...all with 4 clicks of a button and entering delivery information.
If the logged user can not make up thier mind and wish to log off and have a think...they can do so without issue - the next time they log in, thier basket items will still be held for them!
We accept payment via Paypal or Credit Card!
Enjoy the Site!

# User Goals
 - Visit and view a gallery of Golf Apparel and accessories 
 - Become a member of the site
 - Purchase golfing items
 - Signup to newletter
 - Provide feedback
 - Follow our growth journey

 # Business Goals
 - Display numerous and diverse golfing apparel and accessorie options
 - Allow for ease of purchase
 - Gain more users via enjoyable experience and references
 - Have customers sign up and revisit
 - Have users signup for newsletter


# Agile Methodology/Framework
- A big part of this project was to think ahead and plan, design, prioritise and timebox tasks.  It was a great way to make me think about smaller chunks of work and plan out my project.

- By more planning I felt that I could conceptulise and not get too far ahead, allowing me to focus on certain items of delivery, step by step, not to just focus on end result. 

- I learned how to use this via github and to break tasks down into manageable chunks of work, and again to focus on these as MVP vs everything I'd like to deliver. 

- In GitHub, I was able to create Issues, in which I could break down my User stories into milestones to help plan my tasks in a strategic way.

- Whilst using these facilities in GitHub, I was also able to prioritise my tasks also, this helped me during times of technical challenges.. this made me think in a way more in relation to MVP delivery and decide based on available time, what can be defined as must haves vs nice to haves, and in the end, wont haves.

- CRUD - I've designed, planned and executed all of the CRUD functions.  My application allows a user to:-
    - Create - New Accounts and also SuperUsers have the ability to create new products.
    - Read - Information is collected and stored, and is made readable on UI via the database. 
    - Update - Golf Gear products can be updated via the UI for SuperUsers.
    - Delete - All Golf Gear products can be deleted by SuperUsers.

<br>

# UI Designs 
- Part of the Agile design was to deisgn UI Mockups prior to coding and constructing.
- This is a good practise to allow me to visualize how the product will look and feel and to put myself in the users shoes from a visual point of view..
- I did mockups of all my pages (Home Page, main product page, basket, checkout) All these mockups can be found [HERE](https://drive.google.com/drive/folders/1nCceR4MK3c5pIexAGs8ByDaan0efUXiN)
- As can be seen by my original mockups, I had plans of having three seperate pages for product category.  This proved too difficult to manage and maintain, so decided to try and simplify.

- I also put together a mockup of Facebook page, this would in theory be an advertising tool to get more visibility and visitors.
![Web Page view](/media/golfgear_facebook.jpg)

<br>

# Apps

**On previous submission I had all logic in one entire app - I have now split them down into logical apps to allow for better organisation and also to allow for future additions to the site**

- __users__
    - The users app is to host and utilize all data in relation to the users - new and current.  

- __kev_estore__
    - kev_estore is the main product area App.  In this app belongs the main product page, where users can begin thier shopping experience.
    Within this app, it also contains the product management functionality - this allows an admin user to update, add and remove product items.

- __checkout__
    - The checkout app is where all the shopping, basket and purchasing happens - probably the core to the logic of the entire website.

- __contact__
    - The contact app is where the logic is housed for users that have prescribed to our site via newsletter


# Features

There are many features included in the shopping list application.

- __Secured Credentials__
    - A user must have login credentials to use the site
    - With login credentials, a user can only view thier own details
    - There is a create account function to allow users without login to create one and use site straight away.
    - Payment methods via PayPal will be secured to Logged in user, but the payment details will be available to the user and stored for next visit
    - SuperUser operations only visible to SuperUsers and not to normal customers.
    - Pages that require a login can only be viewed when a user is logged in... if attempted, they will be brought back to login page
    - Pages that require admin login can only be viewed by an admin and once again, if access attempted, the user will be brought back to current logged in page (current page)

<br>

- __Easy Navigation__
    - A user can easily navigate through the site via clear links and one click utilisation.
    - Pages are clear and concise, with no confusion
    - Product management page has clear options (Create/Update/Delete) and each option will take back to main product page with the relevant option on each product.
    - Create product will bring the user to a form in which they can create the specifics on a product (description, price, image)

<br>

- __Mobile Friendly__
    - Application is very device friendly.  This is very important for this app in particular to allow users to use on the go, when at shops for exmaple.  
    - All options available on Laptop/PC are available and clear on all mobile devices.
    - As a social media driven market, it was really important to focus on seamless functionality on mobile devices to align with the modern society needs.

<br>

- __Notifications/Messaging__
    - When actions complete by user, clear messaging will be displayed.
        - **Login**
        - **Logout**
        - **Account Creation**
        - **Product Creation**
        - **Product Update**
        - **Product Deletion**
        - **Additions/Removal from basket**


<br>

- __Bakset__
    - When a user adds an item from the product pages to the basket, the basket item numbers will automatically increment and will display this on the basket icon displayed on top corner of product page.
    When the user is happy that they have chosen all they want and have added to basket, they can then navigate easily to the basket where all the items chosen will be displayed along with images, descriptions, unit price and overall price of order.
    Another great feature in teh basket, id that a user can add to items...so by using an up or down arrow, the user can increase or decrease items required... the overall items will update along with overall cost of order... if the user wants to completely remove the item, the down arrow icon can be used until items =0...the item will automatically remove from basket and total updated.
    
    <br>

    ![Web Page view](/media/basket.png)

<br>

- __Purchase__
    - The user will experience a seamless purchasing experience.  Once they have viewed thier basket and happy with the items and cost...they will have the option to 'Checkout'.  This will bring them to a page which will once again display the items being purchased with totals, and also a form in which to enter shipping details for thier order.
    - Once the user has completed with shipping details, the user will then be prompted with payment options...which are Paypal or Credit Card.  Once either selected, the user will be prompted with Paypal options in order to complete thier payments.
    - The Payment integration with Paypal will take over and will deduct the relevant amounts from consumer and add to the seller accounts.
    - Email confirmation is sent to the user with the details outlined.

    <br>

    ![Web Page view](/media/checkout.png)

<br>

- __News Letter Signup__
    - As I want people to not only use the site, I also want them to be alerted to it.  A signup registration form is key to allowing this, it stores users details and allows for advertisements directly to thier inbox for all informational subjects....sales, promotions, changes to site and general updates.
    - I used the mailchimp service to provide my newsletter signup for users.  Its a fantastic and simple way to provide such a service

    <br>

    ![Web Page view](/media/newsletter.png)

- __Purchase Confirmation and Feedback Page__
    - Once a user completes a purchase, the site will provide a confirmation page and an opportunity to provide feedback of experience.
    - The customers basket will be reset to empty and all cost numbers reset to zero also.
    - Money will be removed from the buyers account and added to the business account.

    <br>

    ![Web Page view](/media/confirm_page.png)

- __Custom 'Page not found'__
    - A very important piece of functionality for user friendliness is the presence of a custom 'Page not found' page.  Without this, not only does it look really unprofessional, its very confusing for any user.  I created my own which clearly explains the issue and helps redirect the user back to the site without any confusion.

    <br>

    ![Web Page view](/static/images/custom_Page_404.png)


# Features left to implement

- Messaging - The messaging is not as I want it to be, it works for most pages but not all.  I would also like to have the message pop as an alert and not remain on screen - FIXED for most pages and messages, still not perfect for all actions.

- Overall better UI - I would spend more time on making the user interface a bit more fun and exciting, currently its very basic, with colours a little bland. 

- Guest functionality - My plan was to allow users to avail of all aspects of the site including purchasing items.  So a user would not have to register an account in order to purchase.  As it stands, only a registered user can purchase.
I did attempt to add this functionality, it was very complicated to decipher the items being chosen and added to basket etc from a non registered user.. I spent many hours to try to get this to work.. but I was getting down rabbit holes.  I was trying this via cookies and page elements.. to no avail.

- Multiple pages vs one.  My original plan and layout was to have numerous pages of products for better experience and design.  As I was developing my site and functionality, it was proving really difficult to pull the information when dealing with basket and incrementing items for purchasing etc..so I went back to one page.

- Views of products - As it stands the descriptions are very high level of the products, I would like to have added an option to click into item and to view more about it.... sizes available, colours, and perhaps a zoom option into the product. 

- I provided a feature in which a user can provide feedback of thier overall experience.  As it stands, this feedback does not get stored and utilised.  Ideally with more time, I would store this information so that I could use it to evaluate trends.  I would also expand this to allow for commentary feedback to allow for my context and rich feedback.

- An additional feature that would make the site more compelling is to have a history section for registered users.  I would like users to see all of thier older orders.  Currently the basket will remain in-tact for previous users visiting and will still hold old information... but not historical data.

- A wishlist - I think a good addition to the site would be that of a wishlist where a user can select an item from the product range that they like, but are not ready to purchase... this would allow a user to come back and then visit the products they had identified to perhaps purchase... this is also good for future growth to adapt ML logic to suggest to users some items they may like going forward.


# Custom Logic
 
 - Some feedback which was recieved was that it was not different enough from Boutique Ado - but I can honestly say that the logic used is completely original and authentic - I unfortunately did not get the chance to carry out the Boutique Ado exmaple.  
 - I have features that Boutique Ado does not, and the project flows differently... I would also point out that the coding standards and layout is not to the level of the project example as I tried to keep it as authentic.

# Testing

- There was a lot of testing throughout this project.  Each and every small change was tested as I went.  I wanted to avoid any last minute bulk testing and therefreo refactoring, so testing as I developed my way through was how I approached this.
<br>

- A large part of my testing was based on the selection of items and updating of Basket.  This was complicated coding and testing/retesting.. I struggled to make it work, and it took a long time with many hours of testing.
<br>

- Guest - Again, this took me a long time to try and develop... and of course test throughout.  I felt that it was then taking way too long, and had to make the tough decision to park it.

<br>

 - **Browser Testing** - As part of my testing I covered Browser testing across numerous platforms, Safari, chrome, firefox and IE.  I wanted to make sure my site worked and was compatible througout and for all users using different browsers. <br>Results [HERE](https://drive.google.com/drive/folders/1D__6g5NjkQZ9vb3SfgyrLV0bitUlqy8O)
 <br>

 - **Responsiveness** - As well as testing on browsers, it was very important that I verified that my site and all its functions behaved as expected with diffeerent screen sizes along with different devices.  This was also quite heavy lifting to make sure I got this working as expected, responsiveness is something I have struggled with in the past and continue to.. but I'm glad to say that any issues that I was finding, I was able to resolve. <br>Results <br> [MOBILE](https://drive.google.com/drive/folders/1NboPbTJ3-2qzwFWJV5NDS561Dms-LZq3)<br>
 [Screens](https://drive.google.com/drive/folders/1Q5Y-eD_81El7-ErJuMHIA9--oWUL5SSR)
 <br>

 - **Code Validation** - Part of the testing efforts are not just about the functional side of the product, its also very important that its Accessible, Performant and the code has been written using best practises.  It is also important that the code written is in the right format and using correct syntax etc.  I did this testing through the use of a number of tools - Lighthouse, HTML and CSS validators etc.  Again, this took a bit of back and forth with fixing some items, but I feel I have got most of the way there now.  I'm still having issues with some accessibility on on one of the pages inreation to lack of labels on a form - I'm struggling with this while using inherited form input fields in Django. <br>Results<br> [Lighthouse](https://drive.google.com/drive/folders/1zLquxiSuvXAekzqiUvh0BfdIq9TkaLUI)<br>
 [CSS](https://drive.google.com/drive/folders/1f49TG4VLdzKMOCEeol45E1Ezki6Yv-NR)<br>
 [HTML](https://drive.google.com/drive/folders/1KrVEsrA7aVR8-Q4cXBUwI2BOTyxCjiTJ)

 - **Use Case and Features** - All the above testing is great, but its of no value if the product does not do what it is meant to do!  As mentioned, I did test throughout as I was developing, and made sure that each use case was tested to make sure I was meeting the initial use cases.  While the majority of the use cases pass the test, there were a couple of which I think could be of a better quality.
 <br>Results <br>[HERE](https://docs.google.com/spreadsheets/d/1a-seLraqeUn-Lllj1iJ2cUO_Y-UU9poS/edit#gid=2126396143) 

 ## Unfixed Bugs

 - As I write this report, a current major issue I have is creating a user account that will also become a customer.. My model set up is with a seperate Customer table outside of the user... so after creating an account the user can not use the site as a customer until I add them via the admin utility... this is a big problem that I have been trying to fix unsuccesfully at this point.
 - (**The above is now fixed!**)

 - Messaging - My messages are being erratic... they seem to present themselves at times and other not.. it really is bothering me.  

 - Guest functionality - I'm not sure if this is a bug neccessarily, but its certainly something that feels like its missing - a website like this should allow no registered users to utilise. 

 - After an item which is present in the basket, then the SuperUser updates that product, once going back to basket the website throws an error.

 ## Marketing Strategy

 - The key strategy of marketing for my website is through organic social media marketing.  I will rely heavily on Facebook and the site created for it.  
   This will allow for many advantages : - 
    - Having direct access to many potential customers 24/7
    - Quick and regular feedback
    - Access to ongoing trends in the market
    - Low cost
    - Online reviews
    - Network expansion from widening connections
    - Far reaching campaigns

 - Repeat visitors will also be crucial, so I would fully expect to provide incentives via the newsletter in which people signup for.  Along with continued comms to connections on promotions, sales, new product lines etc.

 - ![Web Page view](/media/business_model.png)


# Deployment

### Local Deployment
- Requirements
     - An IDE of your choice such as GITPOD
     - You can clone the repository 
     ```
    git clone https://github.com/kevinmcsherry/Kev_Project5
    ```
    - Open the IDE and choose the base directory 
    - Install Django 
    ```
    pip3 install 'django4'
    ```
    - Make sure to install Django Allauth
    ```
    pip3 install django-allauth==0.41.0
    ```
    Run the project with your chosen method. You can drop index.html into a web browser and it should run fine, open a local port and access it or, if you have python installed, run it on an server via manage.py file with python with a command such as:
    ```
    python3 manage.py runserver
    ```
    - Run and enjoy!

## Github Deployment
### Github Preparation

**Requirements:**
- A free GitHub account.

### Github Instructions
1. Log in to your GitHub account.
navigate to [https://github.com/kevinmcsherry/Kev_Project5](https://github.com/kevinmcsherry/Kev_Project5).
1. You can set up your own repository and copy or clone it, or you fork the repository.
2. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
3. GitHub pages will update from the master branch by default.
4. Go to the **Settings** page of the repository.
5. Scroll down to the **Github Pages** section.
7. Select the Master Branch as the source and **Confirm** the selection.
8. Wait a minute or two and it should be live for viewing.

### Heroku

- In order to deploy my project and make it available to run via a visual program, I needed to synch my GitHub project through Heroku.  I had to sign up for a new account, add credentials, link to the correct repository and add some settings to allow for seemless deployment.  One thing I made sure to do was set to automatic deploys, which meant each time I pushed through gitpod, these changes would then render to the new GUI.
- In order to allow the ability for users to create new products and add images, I had to set my project up with AWS and S3.  I created an account in Amazon and set up the project user groups, accesses and rights to allow users to view and add different images.
- I set up my static and media files on S3 to store all files required for project.
- I added all my product images to the media folder in the S3 account.  I also added my static files for the sites usability. 
- My project is deployed via Heroku.  My live published site - https://git.heroku.com/golfgear.git


<br>

### Credentials

# Golf Gear Super User

- My Admin user Credentials for the Golf Gear app : - **Username** - Kevin  **Password** - AvaandMia1

<br>

# PayPal buyer account

- **Username** - kejesab407@gameszox.com  **Password** - Golfgear123

# Credits

- This was my second venture into using django and bootstrap along with python and javascript... I had a lot of distractions during my last phase of this course, work and personal life has been difficult... this has led to not being able to give it the time required.. I missed some content, and did not have time to go through the full boutique ado project, so I came into this project a little behind and without desired skills.

<br>

- Even with not completing the boutique ado project, it still aided me in many ways, from getting started with set-up of django and framework and also the database set up.  I also used a lot of the template structures to help me with getting basic designs set up. 
The web marketing part was also informative becuase this was completely new to me.

<br> 

- I never rely on just one source for my help.  I did a lot of research online to see about other sources that could help me in the development of this project.  I came across some really helpful content and with a particular person on youtube called Denis Ivanov, thats content really helped.  He has tutorials online and also lots of content online which I could not have got to the stage I'm at without.  I used a lot of his content on his [website](https://www.dennisivy.com/), and a lot of his advice through his video content.

<br>

- For my Page Not Found set up and styling I used a source named [makeuseof](https://www.makeuseof.com/create-custom-404-error-page-django/)

<br>

- For my newsletter I used **mailchimp** integration and services.

<br>

- **Paypal Integration** - I needed help to integrate PayPal into my project.  I wanted to try and use a different payment method than that of any taught projects in the cirriculum.  This proved quite difficult, I used many resources, a key one being 'studygaan.com' and in particular an article in relation to steps to take to set up correctly - [PayPal](https://studygyaan.com/django/django-paypal-payment-gateway-integration-tutorial?utm_content=cmp-true)

<br>

# Project Summary
- Tough!  I felt comfortable with past projects becuase I was comfortable doing a bit of coding.  I felt this took me out of my comfort zone and was a challenge bringing me back to HTML and CSS.  I have always struggled a little with designing and styling my front ends. 
- I had a number of different ideas in which I was going to follow, which I then backtracked becuase of the potential difficulty.  I dedided to go with something that I'm passionate about, Golf!
- My original idea was to have a different page per type of gold gear - Accessories, clothing and clubs.  It became apparent as I tried to build the basket and checkout logic that having seperate pages was going to be difficult...so I had to backtrack once again.
- Ideally for a website, anyone should be able to purchase without signing up, but once again, I found it difficult 
- I really wanted to come up with something much more exciting for this project deliverable, so I'm a little disapointed in the end result.  I need to put more time into learning this framework and especially back into basic web site design.
- As part of the Agile practise, I really was keen to carry out the work in the correct cadence and flow.. what I unfortunately ended up doing was jumping into solutionising and coding first... which meant retro fitting the tasks which should have preceeded.  So not ideal. 
- Overall, I learned a huge amount during this project..I got a real understanding of all the things I did not appreciate about the development cycle and the effort that go into it.  The planning and forward thinking was a challenge, as I just wanted to dive right in.  I also learned a lot about other frameworks and libraries that I was not aware of and surpirsed by the power that they give in relation to work that is already done and not required to be redone!
 
