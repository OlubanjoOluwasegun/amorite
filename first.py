import datetime

filename=datetime.datetime.str(2023-5-3)

#create empty file
def create_file():
    """this function creates an empty file"""
    with open(filename.strftime("%y-%m-%d-%h"),"w") as file:
        file.write("")

create_file()