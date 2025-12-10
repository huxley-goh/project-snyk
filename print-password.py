import os

def insecure_function(password):
    print("Received password: " + password)

user_input = "sensitivePassword"
insecure_function(user_input)
