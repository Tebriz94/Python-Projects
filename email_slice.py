#Collect email from user
#split the email using @


def split_email():

    print("Welcome to the email slicer ")
    print("--------------")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")


    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension:", extension)


split_email()