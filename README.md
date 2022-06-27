## Managing-Address-Information
Simple Address Manager of parent and children using Rest-API (GET/POST/PUT/DELETE/PATCH) Development and Testing 

## For Running the APP

To run this application Python (above 3.6) and some additional module needed to be installed. A text file (requirements.txt) is been added, where all the required module is listed. 
In order to install it, run a command-prompt where directory of ‘manage.py’ file stands (..\viewsetapi).
Then enter the following command ‘pip install –r requirements.txt’. All the necessary module would be installing one by one.
To run this project following command needs to written “python manage.py runserver”.
Following 5 links is added. 
1.	http://127.0.0.1:8000/admin/  //username = rukia,  password = asdf
2.	http://127.0.0.1:8000/parent/ [name='parent']  
3.	http://127.0.0.1:8000/parent/<int:pk>/ [name='parent-detail']
4.	http://127.0.0.1:8000/children/ [name='children']
5.	http://127.0.0.1:8000/children/<int:pk>/


## For Testing the APP

‘python manage.py test address’ this command will automatically run the test cases, which have been written in (..\viewsetapi\address\tests.py)
