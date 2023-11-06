class Account:
    __instance = None
    __init = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __init__(self):
        cls = type(self)
        if not cls.__init:
            self.__balance = 100000
            self.__sales_volume = 0 # 매출
            self.__expenses = 0 # 지출
            cls.__init = True
        return None
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            return cls()
        
        return cls.__instance
    
    def regist_expenses(self, expenses):
        if self.__balance > expenses:
            self.__deduct_balance(expenses)
            self.__add_expenses(expenses)
            return True
        return False
    
    # 따로 기능 단위로 뺀다.
    def regist_sales(self, price):
        self.__add_balance(price)
        self.__add_sales_volume(price)

    def __add_sales_volume(self, price):
        self.__sales_volume += price

    def __add_balance(self, price):
        self.__balance += price

    def __add_expenses(self, expenses):
        self.__expenses += expenses

    def __deduct_balance(self, expenses):
        self.__balance -= expenses
        
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_sales_volumn(self):
        return self.__sales_volume

    def set_sales_volumn(self, sales_volume):
        self.__sales_volumn = sales_volume

    def get_expenses(self):
        return self.__expenses

    def set_expenses(self, expenses):
        self.__expenses = expenses
