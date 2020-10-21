# remote access must be granted to ip address in Cpanel before executing
import mysql.connector
from mysql.connector import Error


# fetch credentials
import json
host = json.load(open('config.json'))['db_host']
database = json.load(open('config.json'))['db_database']
user = json.load(open('config.json'))['db_user']
password = json.load(open('config.json'))['db_password']

try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password)

    # ****************************** --- SQL --- ******************************
    # --- create table ---
    # sql_Query = "CREATE TABLE eatdrinkSF (col1 int, name longtext, address text, category text, website text, photo text, photo_credit mediumtext, google_maps_link_ text, google_maps_link text, lat text, lng text, price_range text, price_range_grey text, yelp_rating text, yelp_stars text, yelp_review_count text, google_rating text, google_stars text, google_stars_grey text, google_review_count text, PRIMARY KEY (col1));"
    # sql_Query = "CREATE TABLE breweriesPDX (col1 int, name longtext, address text, zipcode text, category text, website text, photo text, photo_credit mediumtext, google_maps_link_ text, google_maps_link text, lat text, lng text, price_range text, price_range_grey text, yelp_rating text, yelp_stars text, yelp_review_count text, google_rating text, google_stars text, google_stars_grey text, google_review_count text, PRIMARY KEY (col1));"
    # sql_Query = "CREATE TABLE page_list (col1 int, color1 text, page_title text, page_description text, page_keywords text, page_name text, page_author text, page_image text, twitter_link text, table_name text, last_update text, PRIMARY KEY (col1));"
    # sql_Query = "CREATE TABLE breweriesPDX_list (col1 int, place text, place_description text, photo text, PRIMARY KEY (col1));"
    # sql_Query = "CREATE TABLE eatSF_list (id int NOT NULL AUTO_INCREMENT, place text, place_description text, photo text, PRIMARY KEY (id));"
    sql = "CREATE TABLE test_list (id int NOT NULL AUTO_INCREMENT, place text, place_description text, photo text, PRIMARY KEY (id));"
    
    # --- alter table ---
    # sql = "ALTER TABLE test_list ADD id INT PRIMARY KEY AUTO_INCREMENT;"
    
    # --- drop (Delete) table ---
    # sql = "DROP TABLE test_list;"

    # --- insert data ---
    # sql = "INSERT INTO wineriesSF (col1,name,address) VALUES ('1','Schramsberg Vineyards','test');"

    # --- truncate data ---
    # sql = "Truncate TABLE breweriesPDX_list;"

    # --- Delete row ---  
    # sql = "DELETE FROM eatSF_list where id = (select id from (select id from eatSF_list order by id limit 3,1) as n)";

    # ---  ---  

    # ---  ---  

    # --- show all tables in database ---  
    # sql = "SHOW TABLES;";
    
    # ***************************************************************************

    cursor = connection.cursor()
    cursor.execute(sql)

    # uncomment next two lines if retrieving data
    # result = cursor.fetchall()
    # print(result)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")