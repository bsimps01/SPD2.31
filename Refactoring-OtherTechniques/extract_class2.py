# by Kami Bigdely
# Extract class
class Person:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)


elizabeth = Person(
    'elizabeth',
    'debicki',
    1990,
    ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
    'deb@makeschool.com'
)

jim = Person(
    'Jim',
    'Carrey',
    1962,
    ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'],
    'jim@makeschool.com'
)

people = [elizabeth, jim]

for person in people:
    if person.birth_year > 1985:
        print(person.first_name, person.last_name)
        print('Movies Played: ', end='')
        for m in person.movies:
            print(m, end=', ')
        print()
        person.send_hiring_email()