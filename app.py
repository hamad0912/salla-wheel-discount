import requests
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# هنا سيتم إرسال طلب إلى API سلة لإنشاء الكوبون
def create_coupon(discount_percentage, user_email):
    # استبدل بـ API URL الخاص بسلة
    api_url = "https://api.salla.sa/coupons/create"
    headers = {
        "Authorization": "Bearer 7966c5c3c3172e8d88f690368d62b5d6",  # ضع التوكن الخاص بك هنا
        "Content-Type": "application/json"
    }
    data = {
        "discount_type": "percentage",  # نوع الخصم
        "discount_value": discount_percentage,
        "code": f"DISCOUNT-{random.randint(1000, 9999)}",  # كود خصم عشوائي
        "valid_until": "2025-12-31",  # تحديد تاريخ صلاحية الكوبون
        "description": f"خصم {discount_percentage}% على جميع المنتجات",
        "min_value": 0,
        "user_email": user_email,  # البريد الإلكتروني للمستخدم (اختياري)
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()  # إرجاع الكوبون إذا تم إنشاؤه بنجاح
    else:
        return None  # إرجاع None إذا حدث خطأ

@app.route('/spin', methods=['POST'])
def spin_wheel():
    user_email = request.form['email']  # البريد الإلكتروني الذي أرسله المستخدم
    discount = random.choice([10, 20, 50])  # عشوائي لاختيار الخصم من 10%، 20%، 50%
    
    coupon = create_coupon(discount, user_email)

    if coupon:
        return jsonify({
            "message": f"لقد حصلت على خصم {discount}%!",
            "coupon_code": coupon.get('code'),
            "coupon_details": coupon
        })
    else:
        return jsonify({"message": "حدث خطأ أثناء إنشاء الكوبون."}), 500


@app.route('/')
def index():
    return render_template('index.html')  # هنا يتم إظهار صفحة الهبوط

if __name__ == '__main__':
    app.run(debug=True)
