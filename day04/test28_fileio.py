# file: text28_fileio.py
# desc: 텍스트 파일 입출력

# mode : a(append:내용 추가) r(reed:파일 읽기) w(write:파일 쓰기)
# endocing : cp949(euc-kr : 한글), utf-8(만국공통어)
#.\day04\ 현재 위치 폴더에 생성
f = open('sample.txt', mode='w', encoding='utf-8')
# .wrtie()에서 엔터를 추가하려면 마지막에 \n 추가
f.write('안녕하세요. 우리는 IoT개발자 과정입니다.\n') # mode = a or w
f.write('반갑습니다\n')

f.close() # 파일은 무조건 마지막에 닫아야한다
print('파일이 생성되었습니다')

