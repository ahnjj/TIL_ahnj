# 데이터 클래스
class Book:
    def __init__(self, bookNo, bookName, bookAuthor, bookPrice, bookDate, bookStock, pubNo,pubName): 
        # 객체 생성하면서 초기화
        self.__bookNo = bookNo
        self.__bookName = bookName
        self.__bookAuthor = bookAuthor
        self.__bookPrice = bookPrice
        self.__bookDate = bookDate
        self.__bookStock = bookStock
        self.__pubNo = pubNo
        self.__pubName = pubName

    def get_bNo(self):
        return self.__bookNo
    
    def get_bName(self):
        return self.__bookName
    
    def get_bAuthor(self):
        return self.__bookAuthor
    
    def get_bPrice(self):
        return self.__bookPrice
    
    def get_bDate(self):
        return self.__bookDate
    
    def get_bStock(self):
        return self.__bookStock
    
    def get_pNo(self):
        return self.__pubNo
    
    def get_pName(self):
        return self.__pubName