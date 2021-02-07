def convert_to_celsius(fahrenheit : float) -> float:
    return(fahrenheit-32.0)*5.0/9.0

def above_freezing(celsius: float ) -> bool:
    return celsius > 0

if __name__ == '__main__':
    fahrenheit=float(input('온도를 화씨로 입력하세요 : '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print('어는점보다 높습니다.')
    else :
        print('어는점보다 낮습니다.')
