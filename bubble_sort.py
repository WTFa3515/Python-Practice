#氣泡排序法
#bubble sort
def buble_sorted(ite):
    new_list=list(ite)              #將輸入值list(串列)化
    for i in range(len(new_list)):  #從i到整體長度
        for j in range(len(new_list)-1,i,-1):#從倒數第二到最前面
            if new_list[j]< new_list[j-1]:  #當發現後面比前面大時
                new_list[j],new_list[j-1]= new_list[j-1],new_list[j] #左右對調
                """
                print('sort:',new_list) #check過程
            else:
                print(new_list,i)       #check過程
                """
    return new_list #回傳
    
print("bouble sorted:", buble_sorted([4,1,3,2]))