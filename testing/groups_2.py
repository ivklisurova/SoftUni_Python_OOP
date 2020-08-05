class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name: str, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(self.name + other.name, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, ind):
        return f'Person {ind}: {self.people[ind]}'

    def __str__(self):
        return f'Group {self.name} with members {", ".join(str(x) for x in self.people)}'


import unittest


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('Iv', 'Klisurova')

    def test_custom_add(self):
        person_2 = Person('Second', 'Person')
        person_3 = self.person + person_2
        self.assertEqual(person_3.name, 'Iv')
        self.assertEqual(person_3.surname, 'Person')

    def test_custom_string(self):
        self.assertEqual(self.person.__str__(), 'Iv Klisurova')


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person('Iv', 'Klisurova')
        self.person_2 = Person('Second', 'Person')
        self.group = Group('Group 1', [self.person_1, self.person_2])

    def test_custom_add(self):
        person_3 = Person('Third', 'Person')
        group_2 = Group('Group 2', [person_3])
        group_3 = self.group + group_2
        # self.assertEqual(group_3.name, 'Group 1Group 2')
        self.assertEqual(len(group_3), 3)

    def test_custom_len(self):
        result = len(self.group)
        self.assertEqual(result, 2)

    def test_custom_getitem(self):
        result = self.group[1]
        self.assertIn('Second', result)
        self.assertEqual(result, 'Person 1: Second Person')

    def test_custom_getitem_wrong_index(self):
        with self.assertRaises(IndexError):
            result = self.group[4]

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn('Iv', result)
        self.assertIn('Second', result)
        self.assertIn('Group', result)
        self.assertNotIn('Third', result)
        self.assertEqual(result, 'Group Group 1 with members Iv Klisurova, Second Person')


if __name__ == '__main__':
    unittest.main()
