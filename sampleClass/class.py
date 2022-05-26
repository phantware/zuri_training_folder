from unicodedata import name


class User:
 pass
 def __init__(self, full_name,birthday):
  self.name = full_name
  self.birthday = birthday #yyyymmdd

  #Extract first and last names
  name_pieces = full_name.split(" ")
  self.first_name = name_pieces[0]
  self.last_name = name_pieces[-1]

  
user = User("Jamiu Talabi",19700623)


print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
# user1 = User()
# user1.first_name = "Lala"
# user1.last_name = "Brown"

# print(user1.first_name)

# first_name = "Egbon"
# last_name = "Adugbo"

# print(first_name,last_name)


# user2 = User()
# user2.first_name = "Fola"
# user2.last_name = "Smith"

# print(user2.first_name, user2.last_name)