class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        self._transactions = transactions

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self.transactions.append(amount)
            return
        raise ValueError('please use int for amount')

    @property
    def balance(self):
        return int(self.amount + sum(self.transactions))

    @staticmethod
    def validate_transaction(accout, amount_to_add):
        if not accout.balance + amount_to_add >= 0:
            raise ValueError('sorry cannot go in debt!')
        accout.add_transaction(amount_to_add)
        return f'New balance: {accout.balance}'

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __reversed__(self):
        return reversed(self.transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance==other.balance

    def __ne__(self, other):
        return self.balance!=other.balance

    def __add__(self, other):
        acc_u = Account(owner=f'{self.owner}&{other.owner}', amount=self.amount + other.amount)
        acc_u._transactions.extend(self.transactions + other.transactions)
        return acc_u
        # self.owner += '&' + other.owner
        # self.amount += other.amount
        # self._transactions += other.transactions


import unittest


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account('First Person', 100)

    def test_if_add_transaction_not_valid(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction('test')

    def test_if_add_transaction_valid(self):
        self.assertEqual(len(self.account), 0)
        self.account.add_transaction(20)
        self.assertEqual(len(self.account), 1)

    def test_balance_property(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_validate_static_validate_transaction_valid_transaction(self):
        result = Account.validate_transaction(self.account, 100)
        self.assertEqual(result, f'New balance: 200')

    def test_validate_static_validate_transaction_invalid_transaction(self):
        with self.assertRaises(ValueError):
            result = Account.validate_transaction(self.account, -102)

    def test_validate_transaction_static_method(self):
        import types
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_custom_string(self):
        result = str(self.account)
        self.assertEqual(result, 'Account of First Person with starting amount: 100')

    def test_custom_repr(self):
        result = repr(self.account)
        self.assertEqual(result, 'Account(First Person, 100)')

    def test_custom_len(self):
        self.account.add_transaction(50)
        result = len(self.account)
        self.assertEqual(result, 1)

    def test_getitem_valid_index(self):
        self.account.add_transaction(20)
        result = self.account[0]
        self.assertEqual(result, 20)

    def test_getitem_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.account[1]

    def test_custom_reversed(self):
        self.account.add_transaction(20)
        self.account.add_transaction(30)
        result = list(reversed(self.account))
        self.assertEqual(result, [30, 20])

    def test_custom_grater_than(self):
        account2 = Account('Second person', 50)
        self.assertGreater(self.account, account2)
        self.assertTrue(self.account.balance > account2.balance)

    def test_custom_grater_or_equal(self):
        account2 = Account('Second person', 100)
        self.assertGreaterEqual(self.account, account2)
        self.assertTrue(self.account.balance >= account2.balance)

    def test_less_than(self):
        account2 = Account('Second person', 200)
        self.assertLess(self.account, account2)
        self.assertTrue(self.account.balance < account2.balance)

    def test_less_or_equal(self):
        account2 = Account('Second person', 100)
        self.assertLessEqual(self.account, account2)
        self.assertTrue(self.account.balance <= account2.balance)

    def test_accounts_are_equal(self):
        account2 = Account('Second person', 100)
        self.assertEqual(self.account, account2)
        self.assertTrue(self.account.balance == account2.balance)

    def test_not_equal(self):
        account2 = Account('Second person', 500)
        self.assertNotEqual(self.account, account2)
        self.assertTrue(self.account.balance != account2.balance)

    def test_custom_add_method(self):
        account2 = Account('Second person', 500)
        account_3 = self.account + account2
        self.assertEqual(repr(account_3), 'Account(First Person&Second person, 600)')
        self.assertEqual(account_3.balance, 600)
        self.assertEqual(account_3.owner, 'First Person&Second person')


if __name__ == '__main__':
    unittest.main()
