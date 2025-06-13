from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from CRUD.data_manip import *


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data/':
            response = {"message": "This is a GET response"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_GET(self):
        print('PATH',self.path)
        if self.path == "/":
            endpoints = ['create-user/', 'create_drug/', "create_checkout/"]
            with open("index.html") as html:
                html_red = html.read()
                data = ''
                for endpoint in endpoints:
                  data+=f'<li><a href="http://localhost:8001/{endpoint}">{endpoint[:-1]}</a></li>\n'
                
                html_red = html_red.replace("{{list}}",data)

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html_red.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_POST(self):

        # Create user

        if self.path == '/create-user/':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                user_data = json.loads(post_data.decode('utf-8'))
                user = User(user_data.get("user_name"), user_data.get("user_surname"),
                            user_data.get("password"), user_data.get("email"),
                            user_data.get("number"), user_data.get("user_age"))
                user.save()
                response = {"status": "received", "data": user_data}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")

        # create drug

        elif self.path == "create_drug/":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                drug_data = json.loads(post_data.decode('utf-8'))
                drug = Medication(drug_data.get("generic_name"), drug_data.get("brand_name"),
                                  drug_data.get("dosage_form"), drug_data.get(
                                      "strenght"),
                                  drug_data.get("package_size"), drug_data.get(
                                      "manufacturer"),
                                  drug_data.get("price_usd"), drug_data.get(
                                      "category"),
                                  drug_data.get("is_otc"), drug_data.get(
                                      "atc_code"), drug_data.get("image_url"),
                                  drug_data.get("stock qty"), drug_data.get(
                                      "reorder_level"), drug_data.get("weight_g"),
                                  drug_data.get("lenght_cm"), drug_data.get(
                                      "width_cm"), drug_data.get("height_cm"),
                                  drug_data.get("expiry_date"), drug_data.get("avg_rating"), drug_data.get("num_reviews"))
                drug.save()
                response = {"status": "received", "data": drug_data}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")

        # create checkout

        elif self.path == "create_checkout/":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                checkout_data = json.loads(post_data.decode("utf-8"))
                checkout = Checkout(checkout_data.get("drug_name"), checkout_data.get("drug_amount"),
                                    checkout_data.get("price"))
                checkout.save()
                response = {"status": "received", "data": checkout_data}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


def run(port=8001):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server running at http://localhost:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
