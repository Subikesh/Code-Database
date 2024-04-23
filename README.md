# Code-Database
An application to store the data structures and algorithms questions and track your progress on the road to become an expert programmer.

This application is done using django and a REST API is also created using django-rest-framework and is deployed on [codedatabase.pythonanywhere.com](https://codedatabase.pythonanywhere.com/).

## Run the app

To run the app, follow the below steps
 * Clone the repository
 * Create a virtual environment on that folder, if required
 * Run `pip install -r requirements.txt`
 * Run the server `python manage.py runserver`

## App features

### User Authentication
![loginImage](https://github.com/Subikesh/Code-Database/assets/53510640/c922e1f3-375e-4757-851d-a66e1043c2c3)

This screen allows user to login or register new account to code database. For simplicity you can login to a sample credentials provided in the homepage to quickly view contents.

> Also dont hesitate to check out my [portfolio](subikesh.github.io) website or my [linkedIn](linkedin.com/in/subikeshps) profile in the top right corner of the website 😉.

### Questions page
![questionsHome](https://github.com/Subikesh/Code-Database/assets/53510640/0d469a09-522f-44ea-9d7a-4a96b687ae54)

This screen is the home page which shows the list of private and public questions along with questions search, filters based on difficulty or tag.

Each question can contain informations like description, difficulty, tags/topics and question link and solutions. 

Each solution will contain informations like solution name, notes, code and language and solution/submission link. These questions and solutions can be edited or deleted by the question/solution user at any time.

**Private questions:** These are the questions created by a user along with the solutions and notes for it for private view

**Public questions:** These are the questions which are created just like private questions and shared along with all the users publicly. Other users can view these questions, but cannot store solutions or notes for these. They can take a copy of these questions to store their own solutions for that question.

> Apart from the home page, there are lot more to explore in the website like question/solution details, edit/create forms. Please do check them out 😄.
