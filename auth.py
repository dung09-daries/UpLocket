import os
import requests
import uuid

class Auth:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None

    def create_token(self):
        # Lấy AppCheck từ Vercel Env, nếu không có sẽ dùng mã mặc định
        app_check = os.getenv("APP_CHECK_TOKEN", "dán_mã_ey_của_bạn_vào_đây")

        request_data = {
            "email": self.email,
            "password": self.password,
            "clientType": "CLIENT_TYPE_IOS",
            "returnSecureToken": True
        }

        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
        
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "X-Firebase-AppCheck": app_check,
            "X-Firebase-GMPID": "1:641029076083:ios:cc8eb46290d69b234fa606",
            "X-Ios-Bundle-Identifier": "com.locket.Locket",
            "User-Agent": "FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.82.0 iPhone/18.0"
        }

        response = requests.post(url, headers=headers, json=request_data)

        if response.ok:
            self.token = response.json().get('idToken')
            return self.token
        else:
            raise Exception(f"Failed to login: {response.text}")

    def get_token(self):
        if not self.token:
            self.create_token()
        return self.token
