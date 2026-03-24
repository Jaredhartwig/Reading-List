# Reading List
Reading list project for Pega interview
The following is a terminal program that allows users to create and update a reading list.

# Project Overview
Below is the requirements and specifications of this project.

<img width="763" height="222" alt="Project Overview" src="https://github.com/user-attachments/assets/da0e14b1-b788-4b0a-8d2d-6396f5699081" />

Tech Used: Python
For this project, I used a mixture of Python for the backend and HMTL for the frontend. For the UI framwework, I used Flask as it is super lighteeight which is ideal given the size of this project. 
Persisting Data: JSON File
I chose to store the data in a JSON as it integreated the easiest with my framework and made sense with the scale of the project. 


# How to Run Reading List
There are 2 versions of the project included in this repository. The first, version 1, is a simple terminal project that saves user information to a text file to persist data. The files for this project are:

- readingListLogic.py
- readingList.py

Version 2, the main version of this project, utilizes the Flask framework to create a web application. The files for this project are:

- app.py
- reading_list.html

TO start running reading list, make sure that you have Flask installed.

- pip3 install flask
  
Make sure the html file is included in a file named templates inside the "Reading List" directory.
Run project with:

- python3 app.py

Copy the output URL (example: http://127.0.0.1:5000)
The output should be a reading list web application.

# Sources
All resources I used to complete this project.
- https://stackoverflow.com/questions/415192/best-way-to-create-a-simple-python-web-service
- I used Copilot for a portion of the HTML file to integreate Flask properly and to create app.py for quick prototyping ofnthe project once I had completed version 1.
