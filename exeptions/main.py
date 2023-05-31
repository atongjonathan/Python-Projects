# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["sdfsdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"{error_message} non existent")
# else:
#     print(file.read())
# finally:
#     # raise KeyError("The message is key")
#
#
height = int(input("Height: "))
weight = float(input("Weight: "))
if height > 3:
    raise ValueError("Height can never be more than 3")
bmi = weight / height ** 2
