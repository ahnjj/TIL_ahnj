#실제 작업 처리하는 클래스
from pymongo import MongoClient
from BookVO import Book
from datetime import datetime
# import cryptography

class BookDAO:
    # 생성자
    def __init__(self):
        self.conn = None
        self.db = None

    def connect(self):
        # DB연결
        self.conn = MongoClient(host='localhost',port=27017)
        self.db = self.conn.new_db

    
    def disconnect(self):
        # DB접속 종료
        self.conn.close()

    def select(self):
        # 도서조회
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            # 2. 도서정보출력 
            for book in self.db.book.find():
                print(book['bookNo'], book['bookName'], book['bookAuthor'], book['bookPrice'],book['bookDate'].strftime('%Y-%m-%d'),book['bookStock'], book['publisher']['pubNo'], book['publisher']['pubName'])
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 조회 완료')
        except:
            print('도서 조회 실패')


    
    def insert(self, book):
        # 도서등록
        # 1. DB연결 (connect호출)
        try:
            self.connect()
            # 2. Insert
            datetime_format = "%Y-%m-%d"

            book = {
                'bookNo' : book.get_bNo(),
                'bookName' : book.get_bName(),
                'bookAuthor' : book.get_bAuthor(),
                'bookPrice' : book.get_bPrice(),
                'bookDate' :  datetime.strptime(book.get_bDate(), datetime_format),
                'bookStock' : book.get_bStock(),
                'publisher' : {'pubNo':book.get_pNo(), 'pubName' :  book.get_pName()}
            }
            self.db.book.insert_one(book)
            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 입력 완료!')
        except:
            print('도서 입력 실패')

   

    def update(self, book):
        # 도서수정
        # 수정된 데이터 DB에 저장 : update문 수행
        try:
            # 1. DB연결 (connect호출)
            self.connect()

            # 2. UPDATE 문 수행
            datetime_format = "%Y-%m-%d"
            self.db.book.update_one(
                    {'bookNo':book.get_bNo()},
                    {
                        '$set' : {  'bookName' : book.get_bName(),
                                    'bookAuthor' : book.get_bAuthor(),
                                    'bookPrice' : book.get_bPrice(),
                                    'bookDate' :  datetime.strptime(book.get_bDate(), datetime_format),
                                    'bookStock' : book.get_bStock(),
                                    'publisher' : {'pubNo':book.get_pNo(), 'pubName' :  book.get_pName()}

                                  }
                    }
            )

            # 3. DB접속 종료 (disconnect호출)
            self.disconnect()
            print('도서 수정 완료')
        except:
            print('도서 수정 실패')

    
    def delete(self, bookNo):
        # 도서삭제
        try:
            # 1. DB연결 (connect호출)
            self.connect()
            self.db.book.delete_one({'bookNo':bookNo})
            # 2. DB접속 종료
            self.disconnect()
            print('도서 삭제 완료')
        except:
            print('도서 삭제 실패')


    def search(self, bName):
        # 도서 검색하고 결과 출력
         # 1. DB연결
        self.connect()
        # # 2. 검색 결과
        books = self.db.book.find({"bookName":{"$regex":bName}})

        for book in books:
            print(book['bookNo'], book['bookName'], book['bookAuthor'], book['bookPrice'],book['bookDate'].strftime('%Y-%m-%d'),book['bookStock'], book['publisher']['pubNo'], book['publisher']['pubName'])

        # 3. DB접속 종료 (disconnect호출)
        self.disconnect()