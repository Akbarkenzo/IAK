from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal untuk toko HP (contoh 10 data)
phones = [
    {"id": "1", "name": "iPhone 14", "brand": "Apple", "price": 12000000, "stock": 10},
    {"id": "2", "name": "Samsung Galaxy S23", "brand": "Samsung", "price": 10000000, "stock": 15},
    {"id": "3", "name": "Xiaomi 13", "brand": "Xiaomi", "price": 8000000, "stock": 20},
    {"id": "4", "name": "OnePlus 11", "brand": "OnePlus", "price": 9000000, "stock": 8},
    {"id": "5", "name": "Google Pixel 7", "brand": "Google", "price": 9500000, "stock": 12},
    {"id": "6", "name": "Huawei P50", "brand": "Huawei", "price": 7000000, "stock": 10},
    {"id": "7", "name": "OPPO Reno 8", "brand": "OPPO", "price": 6000000, "stock": 18},
    {"id": "8", "name": "Vivo X90", "brand": "Vivo", "price": 7500000, "stock": 20},
    {"id": "9", "name": "Sony Xperia 5", "brand": "Sony", "price": 8500000, "stock": 5},
    {"id": "10", "name": "Realme GT 2", "brand": "Realme", "price": 5000000, "stock": 25}
]

class PhoneList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(phones),
            "phones": phones
        }

class PhoneDetail(Resource):
    def get(self, phone_id):
        phone = next((p for p in phones if p["id"] == phone_id), None)
        if phone:
            return {"error": False, "message": "success", "phone": phone}
        return {"error": True, "message": "Phone not found"}, 404

class AddPhone(Resource):
    def post(self):
        data = request.get_json()
        new_phone = {
            "id": str(len(phones) + 1),
            "name": data["name"],
            "brand": data["brand"],
            "price": data["price"],
            "stock": data["stock"]
        }
        phones.append(new_phone)
        return {"error": False, "message": "Phone added successfully", "phone": new_phone}, 201

class UpdatePhone(Resource):
    def put(self, phone_id):
        phone = next((p for p in phones if p["id"] == phone_id), None)
        if not phone:
            return {"error": True, "message": "Phone not found"}, 404
        data = request.get_json()
        phone.update({
            "name": data.get("name", phone["name"]),
            "brand": data.get("brand", phone["brand"]),
            "price": data.get("price", phone["price"]),
            "stock": data.get("stock", phone["stock"])
        })
        return {"error": False, "message": "Phone updated successfully", "phone": phone}

class DeletePhone(Resource):
    def delete(self, phone_id):
        global phones
        phones = [p for p in phones if p["id"] != phone_id]
        return {"error": False, "message": "Phone deleted successfully"}

# Adding resources to the API
api.add_resource(PhoneList, '/phones')
api.add_resource(PhoneDetail, '/phones/<string:phone_id>')
api.add_resource(AddPhone, '/phones/add')
api.add_resource(UpdatePhone, '/phones/update/<string:phone_id>')
api.add_resource(DeletePhone, '/phones/delete/<string:phone_id>')

if __name__ == '__main__':
    app.run(debug=True)
