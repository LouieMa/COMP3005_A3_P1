# COMP3005 A3 – Student Database CRUD Application

1. Install and start PostgreSQL
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo service postgresql start

2. Set database password and create the database
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres createdb students_db

3. Create the table and load the initial data
PGPASSWORD=postgres psql -U postgres -h localhost -d students_db -f database_setup.sql

4. Set up Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

5. Compile and run application
python student_manager.py

Video Link For Demo
https://youtu.be/6A_sW17fTys