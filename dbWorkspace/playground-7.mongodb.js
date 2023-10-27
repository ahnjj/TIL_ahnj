// 결과만 출력
// 1) findOne({"bookNo":"1001"}).bookName
// 2) findOne({"bookNo":"1001"})['bookName']
// 3) js변수로 받아서 변수값 출력

// 방법 1 - 결과창으로
use("new_db")
db.book.findOne({"bookNo":"1001"})['bookName']

// 방법2 - 결과창으로
use("new_db")
db.book.findOne({"bookNo":"1001"}).bookName

// 방법3 - 콘솔로
let book = db.book.findOne({"bookNo":"1001"},{bookName:1})
console.log(book.bookName)


// db.book.find({"bookNo":"1001"}사용해서 도서명 출력하기
// find() : 배열로 반환된 경우
// 방법 1 : Foreach

use("new_db")
books = db.book.find({bookNo:"1001"})
books.forEach(function(book) {
    console.log(book.bookName);
});

// 방법2
use("new_db")
books = db.book.find({"bookNo":"1001"},{bookName:1})
books.forEach(book => {
    console.log(book.bookName);
});

// 도서 전체 내용 출력 (데이터만)
// 도서번호 도서명 저자 가격 출판일 재고 출판사번호 출판사명
use("new_db")
books = db.book.find()

books.forEach(book =>{
    console.log(book.bookNo +' '+ book.bookName +' ' +book.bookAuthor +' '+ book.bookPrice +' '+ book.bookStock+' '+ book.publisher.pubNo +' '+ book.publisher.pubName);
});