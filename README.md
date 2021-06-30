# ClaimIt-Flask
 
## Introduction

ClaimIt-Flask is the flask based API to process user claims for vehicular insurance. The API endpoints help in filing claims and detect vehicle damage images. A final report is genarated as a claim in the database.

## Local Setup

These steps need to followed assuming the local environment is Ubuntu 18.04 with Python 3.6

1. First step is to install Apache2
```
sudo apt update
sudo apt install apache2
```

2. Next step is to go into `/var/www/html` and create a virtual environment, activate it, in the directory you wish to have the API setup.
```
cd /var/www/html
python3 -m venv env
source env/bin/activate
```

3. Then we clone the flask repository in the our apache web server directory
```
git clone https://github.com/DhirenSc/claimit-flask.git
```

4. Next we need to install dependencies for darkflow. Here's the blog I have referred to: https://sites.google.com/view/tensorflow-example-java-api/complete-guide-to-train-yolo/train-yolo-with-darkflow
```
pip install tensorflow==1.15
apt-get update
pip install numpy
pip install opencv-python
pip install cython
```

5. We go into the darkflow repository next and install it globally
```
cd darkflow
python3 setup.py build_ext --inplace
pip install .
```

6. Install MySQL Server next. Here's the blog I referred: https://www.sqlshack.com/how-to-install-mysql-on-ubuntu-18-04/
```
sudo apt update
sudo apt install MySQL-server
sudo systemctl start mysql
sudo mysql_secure_installation
```

7. Once MySQL is setup, we create the database next.
```
CREATE DATABASE claimit;
CREATE TABLE 
    __users__ 
    ( 
        user_id   VARCHAR(50) NOT NULL, 
        email_id  VARCHAR(100) NOT NULL, 
        name      VARCHAR(100) NOT NULL, 
        photo_url VARCHAR(2083), 
        PRIMARY KEY (user_id) 
    ) 
    ENGINE=InnoDB DEFAULT CHARSET=latin1 DEFAULT COLLATE=latin1_swedish_ci;

CREATE TABLE 
    __claims__ 
    ( 
        claim_id     VARCHAR(50) NOT NULL, 
        imageURL     text NOT NULL, 
        severity     INT(2) NOT NULL, 
        userId       VARCHAR(100) NOT NULL, 
        status       VARCHAR(20) NOT NULL, 
        created_date VARCHAR(50) NOT NULL, 
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON 
UPDATE 
    CURRENT_TIMESTAMP, 
    make         VARCHAR(60), 
    model        VARCHAR(60), 
    vehicle_year VARCHAR(4), 
    phone_no     VARCHAR(11), 
    PRIMARY KEY (claim_id), 
    FOREIGN KEY (userId) REFERENCES `__users__` (`user_id`), 
    INDEX userId (userId) 
    ) 
    ENGINE=InnoDB DEFAULT CHARSET=latin1 DEFAULT COLLATE=latin1_swedish_ci;
```

8. Next we setup the database credentials in the mysql_service.py file: https://github.com/DhirenSc/claimit-flask/blob/main/mysql_service.py

9. To load all the car makes and models, we need api tokens and master key for the Back4App database: https://www.back4app.com/database/back4app/car-make-model-dataset. Make sure to create an account and get the appropriate credentials. Fill those credentials in https://github.com/DhirenSc/claimit-flask/blob/main/app.py line 56,57 and 58.

10. The utility.py (https://github.com/DhirenSc/claimit-flask/blob/main/utility.py) needs to be modified appropriately based on user requirements.

11. Once the above steps are done, we can run the flask app locally
```
python app.py
```
