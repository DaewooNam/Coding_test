


def solution(mats, park):
    
    # 시작 인덱스에서 

    # [0+mat_size,0 + mat_size]
    # 이때 mat_size를 순차적으로 증가 시킨 

    # [0,0]을 증가 시켜야 되네 
    # park의 사이즈를 확인 
    mats = sorted(mats)

    x_len = len(park) # row
    y_len = len(park[0]) # col
    max_size = 0

    for mat in mats:
        for x in range(x_len):
            for y in range(y_len):
                if (serach_matsize(park, x, y, x_len, y_len, mat)):
                    max_size = mat
    
    return max_size


def serach_matsize(park, x, y, x_len, y_len, mat):

    x_pos = x + mat #여기서 
    y_pos = y + mat

    if x_pos >= x_len or y_pos >= y_len:
        return False
    

    for dx in range(mat):
        for dy in range(mat):
            if park[x+dx][y+dy] != "-1":
                return False


    return True




    







if __name__ == "__main__":


    mats = [5,3,2]	
    park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], 
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
         ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], 
         ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], 
         ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], 
         ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]	


    res = solution(mats, park)

    print(res)

    