class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        strout = "Name " + self.name + "\n"
        strout = strout + "Id " + str(self.id) + "\n"
        strout = strout + "Value " + str(self.value) + "\n"
        return strout


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
          @origin: int(id) or str(name) of the first account
          @dest:
         int(id) or str(name) of the destination account
          @amount: float(amount) amount to transfer
          @return
          True if success, False if an error occured
        """
        try:
            amount = int(amount)
        except ValueError:
            print("Amount have to be a number")
            return
        # Get account and check if exist :
        ao = None
        ad = None
        for account in self.account:
            if type(origin) is int and account.id == origin:
                ao = account
            elif type(origin) is str and account.name == origin:
                ao = account
            elif type(dest) is int and account.id == dest:
                ad = account
            elif type(dest) is str and account.name == dest:
                ad = account
        if ao is None:
            print("Account", ao, "do not exist")
            return -1
        if ad is None:
            print("Account", ad, "do not exist")
            return -1

        # Check if accounts are corrupted :
        if hasattr(ao, 'value') is False
        or hasattr(ao, 'id') is False or hasattr(ao, 'name') is False:
            print("The account ORIGIN of this transaction\
            is corrupted,\nplease fix it.")
            return -1

        if hasattr(ad, 'value') is False
        or hasattr(ad, 'id') is False or hasattr(ad, 'name') is False:
            print("The account DEST of this transaction\
            is corrupted,\nplease fix it.")
            return -1

        cor = 0
        for key in ao.__dict__:
            if key[0] == 'b':
                print("The account ORIGIN of this transaction\
                is corrupted,\nplease fix it.")
                return -1
            if cor == 0 and (key.find('zip') == 0 or key.find('addr') == 0):
                cor = 1
        if cor == 0 or len(ao.__dict__) % 2 == 0:
            print("The account ORIGIN of this transaction\
            is corrupted,\nplease fix it.")
            return -1

        cor = 0
        for key in ad.__dict__:
            if key[0] == 'b':
                print("The account DEST of this transaction\
                is corrupted,\nplease fix it.")
                return -1
            if cor == 0 and (key.find('zip') == 0 or key.find('addr') == 0):
                cor = 1
        if cor == 0 or len(ao.__dict__) % 2 == 0:
            print("The account DEST of this transaction\
            is corrupted,\nplease fix it.")
            return -1

        if ao.value < amount:
            print("This man don't have money, too bad")
            return

        ao.transfer(-amount)
        print("An error have occured")
        return
        ad.transfer(amount)

    def fix_account(self, account):
        """
          fix the corrupted account
          @account: int(id) or str(name) of the account
          @return
          True if success, False if an error occured
        """
        ao = None
        for elem in self.account:
            if type(account) is int and elem.id == account:
                ao = elem
            if type(account) is str and elem.name == account:
                ao = elem
        if ao is None:
            print("Error, this account does not exist")
            return
        save = None
        cor = 0
        for key in ao.__dict__:
            if key[0] == 'b':
                print("This attribute is fucking insane :", key)
                save = key
            if cor == 0 and (key.find('zip') == 0 or key.find('addr') == 0):
                cor = 1
        if cor == 0:
            print("This attribute is fucking insane :", key)
            save = key
        if save is not None:
            ao.__dict__.pop(save)
        if type(account) is int:
            ao.id = account
        if type(account) is str:
            ao.name = account

        if hasattr(ao, 'value') is False:
            ao.value = 0
        if hasattr(ao, 'name') is False:
            print("Enter name :", end='')
            ao.name = input()
        if hasattr(ao, 'id') is False:
            print("Enter id :", end='')
            ao.id = input()

        corrupted = 0
        if len(ao.__dict__) % 2 == 0:
            while hasattr(ao, str(corrupted)) is True:
                corrupted = corrupted + 2
            ao.__dict__[str(corrupted)] = corrupted + 1
