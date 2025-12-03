filee = input('텍스트 파일 이름을 입력하세요: ')
try:

    infile =  open(filee, 'r')
    reading = infile.read()
    print(reading)

except FileNotFoundError:
    print('이것은 예제파일입니다.')
