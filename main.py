def insert_data(idx, pokemon):
    """
    선형 리스트의 idx위치에 원소 삽입
    :param idx: int
    :param pokemon: str
    :return: void
    """
    if idx < 0 or idx > len(pokemons):  # 범위 지정
        print("Out of range!")
        return

    pokemons.append(None)  # .append() poketmons 끝에 빈칸을 추가합니다.

    for i in range(len(pokemons) - 1, idx, -1):  # len(pokemons) - 1은 마지막 인덱스를 뜻합니다. 배열 전체 길이는 0부터 세지 않기 때문에 -1을 빼주는 겁니다.
                                                # 삽입할 위치 idx까지 인덱스 1씩 감소시키면서 다음 for문을 반복합니다.
        pokemons[i] = pokemons[i - 1]           # 마지막 자리에 그 앞에 있는 데이터를 할당합니다.
        pokemons[i - 1] = None                  # 그러면 같은 데이터가 중복이 되는데 마지막 인덱스에는 데이터를 남기고 그 전 인덱스에 빈칸을 두고 계속 이런식으로 빈칸의 위치를 옮깁니다.

    pokemons[idx] = pokemon     # idx 위치에 pokemon 값을 할당합니다.


# self study 3-1 입력한 위치 이후가 모두 삭제
def delete_data(idx):
    """
    선형 리스트 idx 위치의 원소 삭제
    :param idx: int
    :return: void
    """
    if idx < 0 or idx > len(pokemons):  # 범위 지정
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 삭제할 위치의 데이터를 삭제합니다.


    #1 for문 이용해서 이렇게 옮겨줘서 값 없애주기
    for i in range(idx + 1, len_pokemons):  # 삭제할 인덱스의 다음 인덱스에서부터 마지막 인덱스까지 None으로 비워줄 겁니다.
        # del (pokemons[i])
        # 길이는 줄어드는데 i가 계속 증가하니까 에러 발생
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    #2 .pop()으로 간단하게 나타냄. pop은 인덱스 값을 주지 않으면 맨 뒤 거를 삭제함.
    for i in range(len_pokemons - idx): # 맨 뒤 거부터 idx 뒤까지 삭제해준다는 말임.
        pokemons.pop()

# add_data를 만듦.
def add_data(pokemon):
    """
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon: str
    :return: void
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    delete_data(3)
    print(pokemons)
    delete_data(1)
    print(pokemons)
    add_data('터검니')
    print(pokemons)