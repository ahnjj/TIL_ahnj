from Controller import Controller


class Main:
    def __init__(self):
        self.controller = Controller()

    def start(self):
        # 메뉴 출력
        # 1. 도서조회 2. 도서등록 3. 도서수정 4. 도서삭제 5. 검색 6. 종료
        # 선택한 번호에 따라 controller 클래스의 메소드 호출
        

        while True:
            num = input("\n\n1. 도서조회 2. 도서등록 3. 도서수정 4. 도서삭제 5. 검색 6. 종료 : ")

            if num == '1':
                # 컨트롤러 클래스의 select() 호출
                self.controller.select()
            elif num == '2':
                self.controller.insert()
            elif num == '3':
                self.controller.update()
            elif num == '4':
                self.controller.delete()
            elif num == '5':
                self.controller.search()
            elif num == '6':
                print('종료합니다.')
                break
            else:
                print('잘못 입력하였습니다.')

# 현재 모듈이 시작모듈
if __name__ == "__main__":
    # start 메소드 실행하면서 시작
    m = Main()  # 객체 만들고
    m.start()
