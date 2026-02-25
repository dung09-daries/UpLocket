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
        app_check = os.getenv("APP_CHECK_TOKEN", " eyJhbGciOiJSUzI1NiIsImtpZCI6IjJjMjdhZmY1YzlkNGU1MzVkNWRjMmMwNWM1YTE2N2FlMmY1NjgxYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVOG6pW4gRMWpbmdnKFDDtCkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9maXJlYmFzZXN0b3JhZ2UuZ29vZ2xlYXBpcy5jb206NDQzL3YwL2IvbG9ja2V0LWltZy9vL3VzZXJzJTJGMDFvcW15NTA3Y2JBYUNWNGplSFhGTVYya3FNMiUyRnB1YmxpYyUyRnByb2ZpbGVfcGljLndlYnA_YWx0PW1lZGlhJnRva2VuPWVhM2IwODJjLWExNzUtNDg1My05MGMxLTFiYmVhNTZiNzI2YiIsInJldmVudWVDYXRFbnRpdGxlbWVudHMiOltdLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbG9ja2V0LTQyNTJhIiwiYXVkIjoibG9ja2V0LTQyNTJhIiwiYXV0aF90aW1lIjoxNzcyMDE3NjU2LCJ1c2VyX2lkIjoiMDFvcW15NTA3Y2JBYUNWNGplSFhGTVYya3FNMiIsInN1YiI6IjAxb3FteTUwN2NiQWFDVjRqZUhYRk1WMmtxTTIiLCJpYXQiOjE3NzIwMTc2NTYsImV4cCI6MTc3MjAyMTI1NiwiZW1haWwiOiJkdGFuOTg2MUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkdGFuOTg2MUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.jKfiOCmFd1rfr1AFrwR3ULYQdOpTjdSBmYA7bXn4UH2FDANNARMK_P1Yw0dFuVgPCbhV_6PVbU6aCt9bxHnkqzy7_yIOvbAfC8Vu1_oMTYE9j4cWHB_hbADRpeQyJWUxDAxhv371lZIppnUOyjOPX7NT2BbClF7TXzoyrkcYA3PwLtOi4g0v5fOTukQ8YDgGPC6qCW6d-uEuWLncobDiZfBjL7T2J2PKXvzDNnD9S0MpD2_PtxZU7qIfo68kN4ZUcm0fRPDsBT-WxyPmcq9lBS7LNxjoEzz3HzVHFsND2UPPUKTE_KU3dvstojfIoppYWLrWNDkgqcMcMMu9P-reeQ")

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
