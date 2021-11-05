def is_email_valid(email):
    evaluation_result = None
    if '@' not in email or '.' not in email:
        evaluation_result = False
    else:
        evaluation_result = True
    return evaluation_result

email = input("Enter your email > ")
if is_email_valid(email):
    print ("The email you have entered is valid!")
else:
    print ("The email you have entered is not valid!")