import pandas as pd
import json
import csv

# Every database action for drugs


def read(path: str):
    df = pd.read_csv(path)
    return df.to_json()


def update(path: str, id, col, new_val):
    with open(path, mode="r") as file:
        csvFile = list(csv.reader(file))

        for line in csvFile:
            if line[0] == id:
                for row in csvFile:
                    if col in row:
                        index = row.index(col)
                        print("ok")
                        break

                line[index] = new_val

        print(csvFile)
        csvWriter = csv.writer(file)

    with open(path, mode="w") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(csvFile)

def create_data(path: str, obj):
    with open(path, 'r') as file:
        reader = list(csv.reader(file))
        attrs = reader[0]
        last_id = reader[-1][0]

    with open(path, 'a') as file:
        writer = csv.writer(file)
        new_row = []

        for attr in attrs:
            print(attr)
            new_row.append(getattr(obj, attr))

        new_row[0] = int(last_id)+1
        writer.writerow(new_row)


def remove_data(path: str, id):
    with open(path, "r") as file:
        reader = list(csv.reader(file))
        for i in range(1, len(reader)):
            if int(reader[i][0]) == int(id):
                reader.pop(i)
                break
    file = open(path, "w")
    for i in range(len(reader)):
        csvWriter = csv.writer(file)
        csvWriter.writerow(reader[i])
    file.close()


class User:
    path = "C:\\Users\\User\\Panacea\\backend\\data\\user.csv"

    def __init__(self, user_name, user_surname, password, email, number, user_age):
        self.user_name = user_name
        self.user_surname = user_surname
        self.password = password
        self.email = email
        self.number = number
        self.user_age = user_age

    def save(self):
        create_data(User.path, self)

    def update_user(self, target_value, new_value):
        update(User.path, target_value, new_value)
    
    def delete(self):
        remove_data(User.path)

# drug_id,generic_name,brand_name,dosage_form,strength,
# package_size,manufacturer,price_usd,category,is_otc,atc_code,
# image_url,stock_qty,reorder_level,weight_g,length_cm,width_cm,
# height_cm,expiry_date,avg_rating,num_reviews


class Medication:
    path = "data/medication.csv"

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

    def save(self):
        create_data(Medication.path, self)

    def update_drug(self, target_value, new_value):
        update(Medication.path, self.drug_id, target_value, new_value)
    
    def delete(self):
        remove_data(Medication.path, self.drug_id)

# drug_name,drug_amount,price,user_id


class Checkout:
    path = "data/checkout.csv"

    def __init__(self, drug_name, drug_amount, price, user_id):
        self.drug_name = drug_name
        self.drug_amount = drug_amount
        self.price = price
        self.user_id = user_id

    def save(self):
        create_data(Checkout.path, self)

    def update_drug(self, target_value, new_value):
        update(Checkout.path, self.user_id, target_value, new_value)
    
    def delete(self):
        remove_data(Checkout.path, self.user_id)


# test_obj = User("13", "nihat", "mursalli", "password123",
#                 "nihatmursalli30@gmail.com", 994-50-703-1003, 16)

# test_checkout = Checkout("Edqiy", 1, 167.59, 11)
# test_checkout.save()


# create_data('./data/user.csv', test_obj)
# remove_data('data/user.csv', 8)

# test_obj.save()
# test_obj.update_user(test_obj.password, "wordpass123")
# test_obj.delete()
# update('./data/user.csv', 'nina', 'user_age', 10)