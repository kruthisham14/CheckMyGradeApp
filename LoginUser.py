import csv
import sys
import os
import time
from encdyc import TextSecurity

class LoginUser:
    def __init__(self, email_id, password, role, encrypted=False, shift=4):
        self.email_id = email_id.strip()
        self.role = role.strip()
        self.shift = shift
        self.text_security = TextSecurity(self.shift)  # Use TextSecurity for encryption
        #self.password = self.encrypt_password(password)
        if encrypted:
            self.password = password  # Already encrypted password from the file
        else:
            self.password = self.encrypt_password(password)
        

    def login(self, email, password):
        decrypted_password = self.decrypt_password(self.password)
        #print(f"Comparing passwords: {decrypted_password} == {password}") #for debug
        if self.email_id.lower() == email.strip().lower() and decrypted_password == password.strip():
            print("Login successful.")
            return True
        print("Invalid credentials.")
        return False

    def encrypt_password(self, plain_text):
        encrypted_password = self.text_security.encrypt(plain_text)
        #print(f"Encrypting password: {plain_text} -> {encrypted_password}") # for debug
        return encrypted_password

    def decrypt_password(self, encrypted_text):
        decrypted_password = self.text_security.decrypt(encrypted_text)
        #print(f"Decrypting password: {encrypted_text} -> {decrypted_password}") # for debug
        return decrypted_password

    def logout(self):
        print(f"{self.email_id} logged out.")

    def change_password(self, new_password):
        self.password = self.encrypt_password(new_password)
        print("Password changed successfully.")

    def display_user(self):
        print(f"Email: {self.email_id} | Encrypted Password: {self.password} | Role: {self.role}")