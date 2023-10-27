# controller 클래스
# 메뉴에서 선택한 항목에 따라 메소드 수행

from BookDAO import BookDAO
from BookVO import Book

class Controller:
    def __init__(self):
        self.dao = BookDAO()

    def select(self):
        # 도서조회
        # DAO 클래스의 select()호출(DAO : 도서정보출력)
        self.dao.select()
    
    def insert(self):
        # 도서등록
        # 데이터 입력 받기
        bookNo = input('도서번호 입력 : ')
        bookName = input('도서명 입력 : ')
        bookAuthor = input('저자 입력 : ')
        bookPrice = input('가격 입력 : ')
        bookDate = input('출판일 입력 : ')
        bookStock = input('재고 입력 : ')
        pubNo = input('출판사번호 입력 : ')
        pubName = input('출판사명 입력 : ')

        book = Book(bookNo,bookName,bookAuthor,bookPrice, bookDate, bookStock, pubNo,pubName) # 객체에 넣어서
        # DAO 클래스의 insert()호출하면서 book객체 전달
        self.dao.insert(book) # 객체를 넘겨준다.


    def update(self):
        # 도서수정
        # 수정할 데이터 입력 받기
        bookNo = input('수정할 도서번호 입력 : ')
        bookName = input('도서명 입력 : ')
        bookAuthor = input('저자 입력 : ')
        bookPrice = input('가격 입력 : ')
        bookDate = input('출판일 입력 : ')
        bookStock = input('재고 입력 : ')
        pubNo = input('출판사번호 입력 : ')
        pubName = input('출판사명 입력 : ')

        # 객체에 넣어서
        book = Book(bookNo,bookName,bookAuthor,bookPrice, bookDate, bookStock, pubNo, pubName)
        # DAO 클래스 update()호출하면서 book객체 전달
        self.dao.update(book)
    
    def delete(self):
        # 도서삭제
        # 삭제할 도서번호 입력 받기
        bookNo = input('삭제할 도서번호 : ')
        # DAO 클래스의 delete()호출하면서 도서번호 전달(DAO : DB에서 도서번호에 해당되는 데이터 삭제)
        self.dao.delete(bookNo)
    
    def search(self):
        # 도서 검색하고 결과 출력
        # 검색할 도서명 입력
        bName = input('도서명 입력 :')
        # DAO 클래스의 Search()호출하면서 도서명 전달(DAO : DB에서 도서번호에 해당되는 데이터 검색)
        self.dao.search(bName)