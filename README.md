
# Library_Management_App_and_Api-Django

This App/Api manage the complete work of library. It can add books to library, show all available books in library, issue books to students, view issued books, update and delete issued books and library books, and generate fine automatically if submit date is expired. It authenticates and gives access to user by its status, permissions and token.

## Set Up

### Install Pip
	sudo apt-get install python-pip

### Clone library repository
	git clone git@github.com:Neerajsinghtanwar/Library_Management_App_and_Api-Django-

### Install Requirements
	pip install -r requirements.txt

### Set Up MySQL
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install mysql-server
	mysql -u root -p --execute "create database library; grant all on library.* to library@localhost identified by 'Asdf@1234';"

### Run Server
	python manage.py runserver
	open localhost:8000 in your browser
## Authors

- [Neerajsinghtanwar](https://github.com/Neerajsinghtanwar/Library_Management_App_and_Api-Django-.git)

  