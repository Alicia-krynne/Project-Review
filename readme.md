## PROJO

## Author
MACRINE ALICE ADHIAMBO "ALICIA"[https://github.com/Alicia-krynne]

## Description
PROJO is a web app where users can  upload their projects and have them reviewed  by their peers. 

## PROJECT MOCK-UP
FIGMA[https://www.figma.com/file/lMFBNqX8kTDnAcoBJsdMjD/IP-3-PROJO?node-id=0%3A1]

### ACESSING THE  ADMIN PAGE 
1. Create a super user localy using the command (python3 manage.py createsuperuser)
2. Then on the browser access the admin dashboard using the link [http://127.0.0.1:8000/admin]
3. add the  images using these site to  vies them on the browser

To access the admin page on heroku,navigate to the more section and choose runcosole as shown below and follow the steps above

### Heroku run console ![HEROKU](./static/pics/heroku.png)

## SCREENSHOTS  OF THE PAGE 
### 1.TESTS RUN ![Test ](https://user-images.githubusercontent.com/78471467/120720981-ad546700-c4d5-11eb-9aad-111711ec336a.png)

### 2.  SIGNING IN ![signin](https://user-images.githubusercontent.com/78471467/120721075-cfe68000-c4d5-11eb-87ca-9461a137ccc1.png)

### 3. HOMEPAGE ![welcome](./static/pics/welcome.png)

### 4. PROFILE PAGE ![profilepage](./static/pics/profile.png)

### 5.PROJECT PAGE  ![projectpage](./static/pics/projects.png)

### 6. ADDING A PROJECT![newproject](./static/pics/newproject.png)

### 7.RESPONSIVE PAGE  ![Responsive](./static/pics/responsive.png)



## CLONNG THE  REPOSITORY:
copy the  link :https://github.com/Alicia-krynne/project-review.

1. On the terminal create an empty directory and  type ' git clone' and paste the link to the repo.
2. Upon sucessfull  cloning, crate a new branch using 'git branch <name of thr branch>' and then switch to the branch using 'git checkout <name of the branch>'.
3. create a new virtual environmet and install the necessary dependencies using  the command 'pip install -r requirements.txt'.
4. To Run the application : 'python3 manage.py runserver'.
5. To Test the application: 'python3 manage.py test'.
6. To run the admin page:'python3 createsuperuser and  create new  admin  credentials.  access the  admin page using [http://127.0.0.1:8000/admin].

## TECHNOLOGIES
1. Python :This is the main language in this project to create the methods and funtions needed. 
2. HTML: for creating the pages that are in the web app. also using HTML to manipulate the display. 
3. css : this is the styling language used for this app. Bootsrap is also added to make styling more efficient. 
4. shell&powershell : used to combine the flexibility of scripting, command-line speed, and the power of a GUI-based admin tool, in this case for our app.
5. Heroku :  for deploying the  app .

### Current Bugs:
Displaying the  ratings is  till under process.

## Contact Information
If you have any question or contributions, please email me at [alicakryne@outlook.com]

## License
MIT License:
Copyright (c) 2021 Macrine Alice Adhiambo
