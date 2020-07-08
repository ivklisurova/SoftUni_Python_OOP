class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def rent_dvd(self, customer_id, dvd_id):
        d = [d for d in self.dvds if dvd_id == d.id]
        c = [c for c in self.customers if customer_id == c.id]
        if d[0].is_rented:
            if d[0] not in c[0].rented_dvds:
                return f'DVD is already rented'
            return f'{c[0].name} has already rented {d[0].name}'
        if c[0].age < d[0].age_restriction:
            return f'{c[0].name} should be at least {d[0].age_restriction} to rent this movie'
        c[0].rented_dvds.append(d[0])
        d[0].is_rented = True
        return f'{c[0].name} has successfully rented {d[0].name}'

    def return_dvd(self, customer_id, dvd_id):
        d = [d for d in self.dvds if dvd_id == d.id]
        c = [c for c in self.customers if customer_id == c.id]
        if d[0] not in c[0].rented_dvds:
            return f'{c[0].name} does not have that DVD'
        c[0].rented_dvds.remove(d[0])
        d[0].is_rented = False
        return f'{c[0].name} has successfully returned {d[0].name}'

    def __repr__(self):
        cust = [c for c in self.customers]
        dvd = [d for d in self.dvds]
        result = ''
        for j in cust:
            result += f'{j.__repr__()}\n'
        for i in dvd:
            result += f'{i.__repr__()}\n'
        return result

    def add_customer(self, customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

# from atributes_and_methods.movie_world.project.customer import Customer
# from atributes_and_methods.movie_world.project.dvd import DVD
#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
# print(movie_world.return_dvd(1, 2))
# print(movie_world.rent_dvd(2, 2))
#
#
# print(movie_world)
