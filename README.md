TravelWise — Priority-Based Travel Recommendation System
Project Description
TravelWise is a web application developed using Django and SQLite. It recommends tourist destinations based on the user's travel type and highest travel priority.
Features
User registration, login and logout
•	Selection of travel type: Solo, Friends or Family
•	Selection of highest priority: Food, Nature, Adventure, Heritage, Budget or Comfort
•	Recommendations from 13 predefined tourist packages
•	SQLite database integration
•	Package management through Django Admin
Technologies Used
•	Python
•	Django
•	SQLite
•	HTML and CSS
Installation
1.	Install the required packages:
python -m pip install -r requirements.txt
2.	Create the database tables:
python manage.py migrate
3.	Insert sample packages:
python add_packages.py
4.	Create an administrator:
python manage.py createsuperuser
5.	Start the server:
python manage.py runserver
6.	Open http://127.0.0.1:8000/
Limitations
The application is currently recommending the packages based on the 13 locations provided by the admin. It is not real travel booking application. It also does not have real time reviews for priorities provided by user. It recommends based on the information that was provided by admin.
Future Scop
 In future Real-time travel package integration, Budget filtering, Multiple weighted preferences and Booking functionality can be integrated.

Author
Ira Bhogayata
