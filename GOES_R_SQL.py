import sqlite3
import os

def main():
    #create_calfire_table()
    #create_goes_r_fire_table()
    #create_goes_r_image_table()
    #create_user_table()
    #create_user_alert_table()
    create_downloaded_files_table()

def create_calfire_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cal_fire("
            "incident_id TEXT PRIMARY KEY,"
            "id INTEGER,"
            "incident_name TEXT,"
            "incident_is_final INTEGER,"
            "incident_date_last_update DATETIME,"
            "incident_date_created DATETIME,"
            "incident_administrative_unit TEXT,"
            "incident_administrative_unit_url TEXT,"
            "incident_county TEXT,"
            "incident_location TEXT,"
            "incident_acres_burned INTEGER,"
            "incident_containment INTEGER,"
            "incident_control TEXT,"
            "incident_cooperating_agencies TEXT,"
            "incident_longitude FLOAT,"
            "incident_latitude FLOAT,"
            "incident_type TEXT,"
            "incident_url TEXT,"
            "incident_date_extinguished DATETIME,"
            "incident_dateonly_extinguished DATETIME,"
            "incident_dateonly_created DATETIME,"
            "is_active INTEGER)")




def create_goes_r_fire_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS goes_r_fire("
              "id INTEGER,"
              "cal_fire_incident_id TEXT,"
              "lat FLOAT,"
              "lng FLOAT,"
              "scan_dt DATETIME,"
              "s3_filename TEXT,"
              "fire_id INTEGER, "
              "UNIQUE(lat, lng, scan_dt) ON CONFLICT REPLACE, "
              "FOREIGN KEY (cal_fire_incident_id) REFERENCES cal_fire(incident_id),"
              "FOREIGN KEY (scan_dt) REFERENCES goes_r_images(scan_dt))")

def create_goes_r_image_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS goes_r_images("
              "id INTEGER,"
              "scan_dt DATETIME,"
              "fire_temp_image BLOB,"
              "fire_temp_gif BLOB, "
              "s3_filename TEXT,"
              "fire_id TEXT,"
              "FOREIGN KEY (scan_dt) REFERENCES create_user_table(scan_dt))")


def create_user_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users("
              "id INTEGER,"
              "user_id TEXT,"
              "first_name TEXT,"
              "last_name TEXT,"
              "email TEXT, "
              "alert_time_start DATETIME, "
              "alert_time_end DATETIME, "
              "user_lat FLOAT,"
              "user_lng FLOAT,"
              "fav_lat FLOAT,"
              "fav_lng FLOAT,"
              "last_alert DATETIME,"
              "alerted_calfire_id TEXT,"
              "UNIQUE(user_id, email) ON CONFLICT REPLACE)")

def create_user_alert_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_alert_log("
              "id INTEGER,"
              "user_id TEXT,"
              "alerted_cal_fire_incident_id TEXT,"
              "alerted_incident_id TEXT,"
              "alert_time DATETIME,"
              "need_to_alert INTEGER,"
              "dist_to_fire FLOAT,"
              "fire_lat FLOAT,"
              "fire_lng FLOAT,"
              "FOREIGN KEY (user_id) REFERENCES users(user_id))")

def create_downloaded_files_table():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS fdfc_files_downloaded("
              "id INTEGER," 
              "s3_filename_fdfc TEXT,"
              "s3_filename_multiband TEXT,"
              "new_fires INTEGER,"
              " DATETIME)")


if __name__ == "__main__":
    main()