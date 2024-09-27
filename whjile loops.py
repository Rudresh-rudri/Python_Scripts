def send_email():
    welcome_email(True,"Rudresh")
    print("send email")


def welcome_email(is_buyer,name):
    print("hi"+" "+name)
    if is_buyer:
        print("welcome to buyer site")
    else:
        print("welcome to seller site")

welcome_email(True,"rudresh")
#
# def multiplay_numbers():
#     return 3*4
#
# print(multiplay_numbers())

# def adding_numbers():
#     #return 3+4
#     #return 5+5
#     print(4+4)
# print(adding_numbers())
