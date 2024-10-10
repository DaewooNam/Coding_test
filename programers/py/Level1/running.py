def solution(players, callings):

    

    # 아래 방법에 대해서는 너무 복잡한데, 따른 방법은 어떻게 할까? 


    # 특정 인물이 불렸을 때, 그 사이에 값을 넣어 줄 수 있을까? 

    # 특정 값이 있을 때 , 서로 교환 하는게 가장 나이스 
    
    # 특정 인물이 불린 인덱스와, 그 앞에 인덱스를 서로 교환 


    
    # # 아래 코드는 시간 초과가 뜨는데.. 이걸 어떻게 해결 하지?
    # for c in callings: 
    #     for idx, p in enumerate(players):
    #         if c == p:     
    #             players[idx-1], players[idx] = players[idx], players[idx-1]

    # print(players)



    # 딕셔너리 형태로 만들어 주면 된다는데?
    # 플레이어 숫자를 딕셔너리 형태로 

    p_dict =  {p : i for i, p in enumerate(players)}


    for c in callings:
        idx = p_dict[c]

        p_dict[c] -= 1
        p_dict[players[idx-1]] += 1 

        players[idx - 1], players[idx] = players[idx], players[idx-1]

    answer = players

    print(answer)



   



    







    # # 아래 코드는 시간 초과가 뜨는데.. 이걸 어떻게 해결 하지?
    # for c in callings: 
    #     for idx, p in enumerate(players):
    #         if c == p:     
    #             players[idx-1], players[idx] = players[idx], players[idx-1]

                

    # answer = 0
    




    





    return answer
    


if __name__ == "__main__":

    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    res = ["mumu", "kai", "mine", "soe", "poe"]


    solution(players,callings)