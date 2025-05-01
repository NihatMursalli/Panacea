import pandas as pd
import json
import csv

# Every database action for drugs

def read(path:str):
    df = pd.read_csv(path)
    return df.to_json()

def update(path:str, id, col, new_val):
    with open(path, mode="r") as file:
        csvFile = list(csv.reader(file))
        cols = csvFile[0]
        index = cols.index(col)

        for line in csvFile:
            if line[0]==id:
                line[index]=new_val

        csvWriter = csv.writer(file)

    with open(path, mode="w") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(csvFile)
        print(csvFile)

def create_data(path:str, obj):
    with open(path, 'r') as file:
        reader = list(csv.reader(file))
        attrs = reader[0]
        last_id = reader[-1][0]
    
    with open(path, 'a') as file:
        writer = csv.writer(file)
        new_row = []

        for attr in attrs:
            new_row.append(getattr(obj, attr))
        
        new_row[0] = int(last_id)+1
        writer.writerow(new_row)

def remove_data(path:str, id):
    with open(path, "r") as file:
        reader = list(csv.reader(file))
        for i in range(1,len(reader)-1):
            if int(reader[i][0]) == id:
                reader.pop(i)
                break
        print(reader[0])
    for i in range(len(reader)):
        file =  open(path, "w")
        csvWriter = csv.writer(file)
        csvWriter.writerow(reader[i])
        file.close()

class User:
    def __init__(self, user_id, user_name, user_surname, password, email, number, user_age):
        self.user_id = user_id
        self.user_name = user_name
        self.user_surname = user_surname
        self.password = password
        self.email = email
        self.number = number
        self.user_age = user_age

# drug_id,generic_name,brand_name,dosage_form,strength,
# package_size,manufacturer,price_usd,category,is_otc,atc_code,
# image_url,stock_qty,reorder_level,weight_g,length_cm,width_cm,
# height_cm,expiry_date,avg_rating,num_reviews

class Medication:
    def __init__(self, drug_id, generic_name, brand_name, dosage_form,
                 strenght, package_size, manufacturer, price_usd, category,
                 is_otc, atc_code, image_url, stock_qty, reorder_lvl, weight_g,
                 lenght_cm, width_cm, height_cm, expiry_date, avg_rating, num_reviews):
        self.drug_id = drug_id
        self.generic_name = generic_name
        self.brand_name = brand_name
        self.dosage_form = dosage_form
        self.strenght = strenght
        self.package_size = package_size
        self.manufacturer = manufacturer
        self.price_usd = price_usd
        self.category = category
        self.is_otc = is_otc
        self.atc_code = atc_code
        self.image_url = image_url
        self.stock_qty = stock_qty
        self.reorder_lvl = reorder_lvl
        self.weight_g = weight_g
        self.lenght_cm = lenght_cm
        self.width_cm = width_cm
        self.height_cm = height_cm
        self.expiry_date = expiry_date
        self.avg_rating = avg_rating
        self.num_reviews = num_reviews

# drug_name,drug_amount,price,user_id

class Checkout:
    def __init__(self, drug_name, drug_amount, price, user_id):
        self.drug_name = drug_name
        self.drug_amount = drug_amount
        self.price = price
        self.user_id = user_id

test_obj = User(11, "nihat", "mursalli", "password123", "nihatmursalli30@gmail.com", 994-50-703-1003, 16)
# create_data('./data/user.csv', test_obj)
remove_data('./data/user.csv', 8)

# update('./data/user.csv', 'nina', 'user_age', 10)

