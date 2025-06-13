import requests

base_url = "http://localhost:8001/"
create_user_url = 'create-user/'
create_user_endpoint = f"{base_url}{create_user_url}"
user_obj = {
    "user_name": "Nurlan",
    "user_surname": "Mursalli",
    "password": "wordpass456",
    "email":"ilovemyborther@gmail.com",
    "number": "555-4545",
    "user_age": "14"
}

user_post_request = requests.post(url = create_user_endpoint, json=user_obj)
print(user_post_request.text)

create_drug_url = 'create_drug/'
create_drug_endpoint = f'{base_url}{create_drug_url}'
drug_obj = {
    "drug_id": "D001",
    "generic_name": "Paracetamol",
    "brand_name": "Tylenol",
    "dosage_form": "Tablet",
    "strength": "500mg",
    "package_size": "20 tablets",
    "manufacturer": "Johnson & Johnson",
    "price_usd": 4.99,
    "category": "Analgesic",
    "is_otc": True,
    "atc_code": "N02BE01",
    "image_url": "https://example.com/images/tylenol.jpg",
    "stock_qty": 150,
    "reorder_level": 50,
    "weight_g": 75,
    "length_cm": 10.0,
    "width_cm": 6.0,
    "height_cm": 3.0,
    "expiry_date": "2026-05-01",
    "avg_rating": 4.5,
    "num_reviews": 87
}

drug_post_request = requests.post(url = create_drug_endpoint, json = drug_obj)

# user_id,drug_name,drug_amount,price,
create_checkout_url = "create_checkout/"
create_checkout_endpoint = f"{base_url}{create_checkout_url}"
checkout_obj = {
    "drug_name": "Paracetamol",
    "drug_amount": 2,
    "price": 4.99
}

checkout_post_request = requests.post(url = create_checkout_endpoint, json = checkout_obj)

print("sending")


