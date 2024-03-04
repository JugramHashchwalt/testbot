#  # NAMED TUPLE
# employees = [
#     (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
#     (2, "Sobir", "Sobirov", 30, "sobir@gmail.com")
# ]
#
# for employee in employees:
#     employee.name
#     # print(employee[1], employee[1], employee[4])
#

# class Employee:
#       def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
#
# employees = [
#         (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
#         (2, "Sobir", "Sobirov", 30, "sobir@gmail.com")
#     ]
#
# for employee in employees:
#         em = Employee(*employee)
#         print(em.id, em.name)
#

# from collections import namedtuple
# Employee = namedtuple("Employee", "id name lastname age email")
#
#
# employees = [
#     (1, "Toxir", "Toxirov", 27, "toxir@gmail.com"),
#     (2, "Sobir", "Sobirov", 30, "sobir@gmail.com")
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)


# class Car:
#     def __init__(self, id, model, color, speed, price):
#         self.id = id
#         self.model = model
#         self.color = color
#         self.speed = speed
#         self.price = price
#
# cars = [
#     (1, "Skyline", "Blue", 235, 15000),
#     (2, "Malibu",  "Black", 220, 10000),
#     (3, "Supra", "Orange", 225, 14000)
# ]
# for car in cars:
#     cr = Car(*car)
#     print(cr.id,cr.model,cr.color, cr.speed, cr.price)




# from collections import namedtuple
#
#
# Car = namedtuple("Car", "id model color speed price")
#
# cars = [
#     (1, "Skyline", "Blue", 235, 15000),
#     (2, "Malibu",  "Black", 220, 10000),
#     (3, "Supra", "Orange", 225, 14000)
# ]
# for car in cars:
#     cr = Car(*car)
#     print(cr.id, cr.model, cr.color, cr.speed, cr.price)



