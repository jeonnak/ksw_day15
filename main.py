## 함수 선언 부분 ##
# 다항식 형식을 출력해보겠습니다.
# 매개변수 px는 다항식 계수 배열
def print_poly(px):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 문자열
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수를 추출합니다.

        if i > 0 and coef > 0:  #  첫번째 항이니까 얘를 스킵하기 위함. 그리고 계수가 0보다 커야함.
            poly_str = poly_str + "+"
        elif coef == 0:  # 계수가 0이라면 차수하나 감소해서 문자열로 만들어주는 겁니다.
            term = term - 1  # 항의 차수를 1 감소합니다.
            continue

        poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1

    return poly_str  # 생성된 다항식 문자열 반환합니다.


def calc_poly(x_val, p_x):
    """
    다항식의 산술연산을 계산하는 함수
    :param x_val: x값 integer
    :param p_x: 계수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 integer
    """
    return_val = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        return_val = return_val + coef * x_val ** term
        term -= 1

    return return_val


## 전역 변수 선언 부분 ##
px = [3, -4, 0, 6]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_poly(px))

    x_value = int(input("X 값 : "))
    print(calc_poly(x_value, px))

