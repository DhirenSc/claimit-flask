# this is the mysql service used to communicate with the backend
import mysql.connector
from datetime import datetime
from flask import jsonify
import json

# connector method for the spothole db
def connect():
    return mysql.connector.connect(
      host="localhost",
      user="# USERNAME",
      passwd="# PASSWORD",
      database="# DATABASE"
    )

# post new report data
def post_claim_data(data):
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO __claims__ (claim_id, imageURL, severity, userId, status, make, model, vehicle_year, phone_no, created_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (data["claimId"], data["imageUrls"], data["severity"], data["userId"], data["status"], data["make"], data["model"], data["year"], data["phoneNo"], datetime.utcnow())
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " record inserted."

# get reports data for a user
def get_user_claims_data(data):
    data = json.loads(data)
    db = connect()
    cursor = db.cursor()

    sql = "SELECT * FROM __claims__ WHERE userId = %s ORDER BY last_updated DESC"
    userId = (data["userId"], )

    cursor.execute(sql, userId)

    results = cursor.fetchall()

    payload = []
    content = {}
    for result in results:
       content = {'claimId': result[0], 'imageUrl': result[1], 'severity': result[2], 'userId': result[3], 'status': result[4], 'created_date': result[5], 'last_updated': result[6], 'make': result[7], 'model': result[8], 'vehicle_year': result[9], 'phone': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)

# update profile data
def post_user_profile_data(data):
    print(data)
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO __users__ (user_id, email_id, name, photo_url) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE name=%s, photo_url=%s"
    val = (data["userId"], data["emailId"], data["name"], data["photoURL"], data["name"], data["photoURL"])
    cursor.execute(sql, val)
    db.commit()
    return str(cursor.rowcount) + " records affected."