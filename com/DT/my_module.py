class MyClass:
    def run(self):
        print("run!!",__name__)
#모듈 작성자 현재 내용을 테스트 하기 위해서
if __name__=='__main__':
    m=MyClass()
    
    m.run()
