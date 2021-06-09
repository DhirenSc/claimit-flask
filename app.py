from flask import Flask, request
from json import dumps
from parent_service import multiple_image_detection_results
import os
import random
import utility
import uuid
import json
import requests
from mysql_service import post_user_profile_data, post_claim_data, get_user_claims_data

app = Flask(__name__)


# route for validating multiple images
# accepts the claim id for resource placed on the server
# to detect damages on the image. connects with the dark-flow service
# at the backend.
@app.route('/api/detect/multiple', methods=['POST'])
def detect_damage_in_multiple_image():
    data = json.loads(request.get_json(silent=True))
    claim_id = data['claimId']
    return multiple_image_detection_results(claim_id)

# upload files using this route.
# renames the file and passes the url back for the uploaded file
@app.route('/api/upload', methods=['POST'])
def upload_files():
    session_id = uuid.uuid4()
    session_path = utility.IMG_UPLOADS_DIRECTORY+'/'+str(session_id)+'/'
    if not os.path.exists(session_path):
        os.makedirs(session_path)
    file_names = []
    for key in request.files:
        file = request.files[key]
        fn = str(random.getrandbits(128)) + utility.DEFAULT_FILE_TYPE
        file_names.append(fn)
        try:
            file.save(os.path.join(session_path, fn))
        except:
            print('save fail: ' + os.path.join(session_path, fn))
    
    final_url = utility.IMG_UPLOADS_DISPLAY_URL+str(session_id)+'/'
    return dumps({
        'claimId': str(session_id),
        'filename': [final_url + f for f in file_names]}
    )

# route to get car models and makes from 
# dataset present at back4app
@app.route('/api/car/data', methods=['GET'])
def get_all_car_data():
    model_url = 'https://parseapi.back4app.com/aggregate/Carmodels_Car_Model_List?distinct=Model'
    make_url = 'https://parseapi.back4app.com/aggregate/Carmodels_Car_Model_List?distinct=Make'
    headers = {
        'X-Parse-Application-Id': '', # This is your app's application id
        'X-Parse-REST-API-Key': '', # This is your app's REST API key
        'X-Parse-Master-Key': '' # app's Master Key
    }
    model_data = json.loads(requests.get(model_url, headers=headers).content.decode('utf-8'))["results"]
    make_data = json.loads(requests.get(make_url, headers=headers).content.decode('utf-8'))["results"]
    return dumps({
        'makes': make_data,
        'models': model_data
    })

# update user profile data
@app.route('/api/profile/update', methods=['POST'])
def post_user_profile():
    data = json.loads(request.get_json(silent=True))
    return post_user_profile_data(data)

# submit a new claim
@app.route('/api/submit/claim', methods=['POST'])
def submit_claim():
    data = json.loads(request.get_json(silent=True))
    return post_claim_data(data)

# get user claims
@app.route('/api/claims', methods=['POST'])
def get_user_claims():
    print(request.get_json())
    data = request.get_json(silent=True)
    return get_user_claims_data(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
