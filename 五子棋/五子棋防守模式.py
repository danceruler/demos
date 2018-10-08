import  sys
import  tkinter
import random
import tkinter.messagebox
from tkinter import *

# 判断该位置是否可以下棋
def isCan(x, y, list):
    if list[x - 1][y - 1] == 0:
        return True
    else:
        return False
# 判断该位置下棋后这一行是否已经五连珠
def isEndL(x,y,list):
    cnd = 1
    flag = False
    for i in range(0,14):
        if list[x-1][i] == list[x-1][i+1] and list[x-1][i]!=0:
            cnd+=1
        else:
            cnd = 1
        if cnd == 5:
            flag = True
        if flag == True:
            break
    return flag
# 判断该位置下棋后这一列是否已经五连珠
def isEndH(x,y,list):
    cnd = 1
    flag = False
    for i in range(0,14):
        if list[i][y-1] == list[i+1][y-1] and list[i][y-1]!=0:
            cnd+=1
        else:
            cnd = 1
        if cnd == 5:
            flag = True
        if flag == True:
            break
    return flag
# 判断该位置下棋后从左上往右下的斜线是否五连珠
def isEndUL(x,y,list):
    cnd = 1
    flag = False
    if (x-y)>=0:
        for i in range((x-y),14):
            if list[i][i-(x-y)] == list[i+1][i+1-(x-y)] and list[i][i-(x-y)]!=0:
                cnd+=1
            else:
                cnd = 1
            if cnd == 5:
                flag = True
            if flag == True:
                break
    else:
        for i in range((y-x),14):
            if list[i-(y-x)][i] == list[i+1-(y-x)][i+1] and list[i-(y-x)][i]!=0:
                cnd+=1
            else :
                cnd = 1
            if cnd == 5:
                flag = True
            if flag == True:
                break
    return flag
# 判断该位置下棋后从右上往左下的斜线是否五连珠
def isEndUR(x,y,list):
    cnd = 1
    flag = False
    if (x+y)<=16:
        for i in range(0,(x+y-2)):
            if list[i][x+y-i-2] == list[i+1][x+y-i-3] and list[i][x+y-i-2]!=0:
                cnd+=1
            else:
                cnd = 1
            if cnd == 5:
                flag = True
            if flag == True:
                break
    else:
        for i in range((x+y)-16,14):
            if list[i][x+y-2-i] == list[i+1][x+y-3-i] and list[i][x+y-2-i]!=0:
                cnd+=1
            else:
                cnd = 1
            if cnd == 5:
                flag = True
            if flag == True:
                break
    return flag
# 行中完美四连个数
def HIsExistPFFour():
    global list
    sum = 0
    for i in range(0,15):
        s = ""
        for j in range(0,15):
            s += str(list[j][i])
        if "011110" in s or "022220"in s:
            sum+=1
    return sum
# 列中完美四连个数
def LIsExistPFFour():
    global  list
    sum = 0
    for i in range(0,15):
        s = ""
        for j in range(0,15):
            s += str(list[i][j])
        if "011110" in s or "022220"in s:
            sum+=1
    return sum
# 左上斜列完美四连个数
def ULIsExistPFFour():
    global  list
    sum = 0
    for i in range(-14,15):
        s = ""
        if i >= 0:
            for j in range(i,15):
                s += str(list[j][j-i])
        else:
            for j in range(-i,15):
                s += str(list[j+i][j])
        if "011110" in s or "022220"in s:
            sum+=1
    return sum
# 右上斜列完美四连个数
def RLIsExistPFFour():
    global  list
    sum = 0
    for i in range(0,29):
        s = ""
        if i <= 14:
            for j in range(0,i+1):
                s+=str(list[j][i-j])
        else:
            for j in range(i-14,15):
                s+=str(list[j][i-j])
        if "011110" in s or "022220"in s:
            sum+=1
    return sum
# 完美四连个数
def isPFFour():
    global list
    return HIsExistPFFour()+LIsExistPFFour()+ULIsExistPFFour()+RLIsExistPFFour()
# AI是否有活三
def AIisPFThree():
    global list,player,AI_y,AI_x
    flag = False
    for i in range(0,15):
        for j in range(0,15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 2
                    if isPFFour()>0:
                        AI_x = i+1
                        AI_y = j+1
                        flag = True
                else:
                    list[i][j] = 1
                    if isPFFour() > 0:
                        AI_x = i + 1
                        AI_y = j + 1
                        flag = True
                list[i][j] = 0
            if flag == True:
                break
        if flag == True:
            break
    return  flag
# 判断玩家是否与活三
def PlayerIsPFFour():
    global list, player, AI_y, AI_x
    flag = False
    for i in range(0, 15):
        for j in range(0, 15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 1
                    if isPFFour() > 0:
                        AI_x = i + 1
                        AI_y = j + 1
                        flag = True
                else:
                    list[i][j] = 2
                    if isPFFour() > 0:
                        AI_x = i + 1
                        AI_y = j + 1
                        flag = True
                list[i][j] = 0
            if flag == True:
                break
        if flag == True:
            break
    return flag
# AI下一步是否可以赢，可以的话返回true并将值赋给AIxy
def isAIWin():
    global AI_x,AI_y,player,list
    flag = False
    for i in range(0,15):
        for j in range(0,15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 2
                    x = i+1
                    y = j+1
                    if isEndL(x,y, list) or isEndH(x,y, list) or isEndUL(x,y,
                          list) or isEndUR(x,y, list):
                        AI_x = x
                        AI_y = y
                        flag = True
                else:
                    list[i][j] = 1
                    x = i + 1
                    y = j + 1
                    if isEndL(x, y, list) or isEndH(x, y, list) or isEndUL(x, y,
                                                                           list) or isEndUR(x, y, list):
                        AI_x = x
                        AI_y = y
                        flag = True
                list[i][j] = 0
            if flag == True:
                break
        if flag == True:
            break
    return flag
# 玩家下一步可以赢的话返回True并将坐标值赋给AIxy
def isPlayerWin():
    global AI_x,AI_y,list,player
    flag = False
    for i in range(0,15):
        for j in range(0,15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 1
                    x = i+1
                    y = j+1
                    if  isEndL(x,y, list) or isEndH(x,y, list) or isEndUL(x,y,
                          list) or isEndUR(x,y, list):
                        AI_x = x
                        AI_y = y
                        flag = True
                else:
                    list[i][j] = 2
                    x = i + 1
                    y = j + 1
                    if isEndL(x, y, list) or isEndH(x, y, list) or isEndUL(x, y,
                                                                           list) or isEndUR(x, y, list):
                        AI_x = x
                        AI_y = y
                        flag = True
                list[i][j] = 0
            if flag == True:
                break
        if flag == True:
            break
    return flag
# 后面为得到黑棋或白棋各种情况的数量
#
#
# 黑棋此时棋盘上的眠4数量
def black_mian4num(t):
    global  black_mian4
    num = 0
    #得到横行的眠4
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_mian4:
            num += s.count(j)
    # 得到列的眠4
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_mian4:
            num += s.count(j)
    # 得到左上斜列的眠4
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_mian4:
            num += s.count(j)
    # 获得右斜上列的眠4
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_mian4:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的活3数量
def black_huo3num(t):
    global  black_huo3
    num = 0
    #得到横行的活3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_huo3:
            num += s.count(j)
    # 得到列的活3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_huo3:
            num += s.count(j)
    # 得到左上斜列的活3
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_huo3:
            num += s.count(j)
    # 获得右斜上列的活3
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_huo3:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的眠3数量
def black_mian3num(t):
    global  black_mian3
    num = 0
    #得到横行的眠3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_mian3:
            num += s.count(j)
    # 得到列的眠3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_mian3:
            num += s.count(j)
    # 得到左上斜列的眠3
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_mian3:
            num += s.count(j)
    # 获得右斜上列的眠3
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_mian3:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的活2数量
def black_huo2num(t):
    global  black_huo2
    num = 0
    #得到横行的活2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_huo2:
            num += s.count(j)
    # 得到列的活2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_huo2:
            num += s.count(j)
    # 得到左上斜列的活2
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_huo2:
            num += s.count(j)
    # 获得右斜上列的活2
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_huo2:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的眠2数量
def black_mian2num(t):
    global  black_mian2
    num = 0
    #得到横行的眠2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_mian2:
            num += s.count(j)
    # 得到列的眠2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_mian2:
            num += s.count(j)
    # 得到左上斜列的眠2
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_mian2:
            num += s.count(j)
    # 获得右斜上列的眠2
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_mian2:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的活1数量
def black_huo1num(t):
    global  black_huo1
    num = 0
    #得到横行的活1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_huo1:
            num += s.count(j)
    # 得到列的活1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_huo1:
            num += s.count(j)
    # 得到左上斜列的活1
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_huo1:
            num += s.count(j)
    # 获得右斜上列的活1
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_huo1:
            num += s.count(j)
    return  num
# 黑棋此时棋盘上的眠1数量
def black_mian1num(t):
    global  black_mian1
    num = 0
    #得到横行的眠1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in black_mian1:
            num += s.count(j)
    # 得到列的眠1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in black_mian1:
            num += s.count(j)
    # 得到左上斜列的眠1
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in black_mian1:
            num += s.count(j)
    # 获得右斜上列的眠1
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in black_mian1:
            num += s.count(j)
    return  num

# 白棋此时棋盘上的眠4数量
def white_mian4num(t):
    global  white_mian4
    num = 0
    #得到横行的眠4
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_mian4:
            num += s.count(j)
    # 得到列的眠4
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_mian4:
            num += s.count(j)
    # 得到左上斜列的眠4
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_mian4:
            num += s.count(j)
    # 获得右斜上列的眠4
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_mian4:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的活3数量
def white_huo3num(t):
    global  white_huo3
    num = 0
    #得到横行的活3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_huo3:
            num += s.count(j)
    # 得到列的活3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_huo3:
            num += s.count(j)
    # 得到左上斜列的活3
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_huo3:
            num += s.count(j)
    # 获得右斜上列的活3
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_huo3:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的眠3数量
def white_mian3num(t):
    global  white_mian3
    num = 0
    #得到横行的眠3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_mian3:
            num += s.count(j)
    # 得到列的眠3
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_mian3:
            num += s.count(j)
    # 得到左上斜列的眠3
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_mian3:
            num += s.count(j)
    # 获得右斜上列的眠3
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_mian3:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的活2数量
def white_huo2num(t):
    global  white_huo2
    num = 0
    #得到横行的活2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_huo2:
            num += s.count(j)
    # 得到列的活2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_huo2:
            num += s.count(j)
    # 得到左上斜列的活2
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_huo2:
            num += s.count(j)
    # 获得右斜上列的活2
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_huo2:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的眠2数量
def white_mian2num(t):
    global  white_mian2
    num = 0
    #得到横行的眠2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_mian2:
            num += s.count(j)
    # 得到列的眠2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_mian2:
            num += s.count(j)
    # 得到左上斜列的眠2
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_mian2:
            num += s.count(j)
    # 获得右斜上列的眠2
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_mian2:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的活2数量
def white_huo1num(t):
    global  white_huo1
    num = 0
    #得到横行的活1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_huo1:
            num += s.count(j)
    # 得到列的活1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_huo1:
            num += s.count(j)
    # 得到左上斜列的活1
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_huo1:
            num += s.count(j)
    # 获得右斜上列的活1
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_huo1:
            num += s.count(j)
    return  num
# 白棋此时棋盘上的眠2数量
def white_mian1num(t):
    global  white_mian1
    num = 0
    #得到横行的眠2
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[j][i])
        for j in white_mian1:
            num += s.count(j)
    # 得到列的眠1
    for i in range(0,17):
        s = ""
        for j in range(0,17):
            s += str(t[i][j])
        for j in white_mian1:
            num += s.count(j)
    # 得到左上斜列的眠1
    for i in range(-16,17):
        s = ""
        if i >=0:
            for j in range(i,17):
                s += str(t[j][j-i])
        else:
            for j in range(-i,17):
                s+=str(t[j+i][j])
        for j in white_mian1:
            num += s.count(j)
    # 获得右斜上列的眠1
    for i in range(0,33):
        s = ""
        if i<= 16:
            for j in range(0,i+1):
                s += str(t[j][i-j])
        else:
            for j in range(i-16,17):
                s += str(t[j][i-j])
        for j in white_mian1:
            num += s.count(j)
    return  num

# 目前棋盘AI的得分
def Now_AIScore():
    global list
    t = [[0]*17 for i in range(17)]
    if player == 1:
        for i in range(0,17):
            t[0][i] = 2
            t[16][i] = 2
            t[i][0] = 2
            t[i][16] = 2
        for i in range(1,16):
            for j in range(1,16):
                t[i][j] = list[i-1][j-1]
        return black_mian4num(t)*mian4_num+black_huo3num(t)*huo3_num\
               +black_mian3num(t)*mian3_num+black_huo2num(t)*huo2_num\
               +black_mian2num(t)*mian2_num+black_huo1num(t)*huo1_num+black_mian1num(t)*mian1_num
    else:
        for i in range(0,17):
            t[0][i] = 1
            t[16][i] = 1
            t[i][0] = 1
            t[i][16] = 1
        for i in range(1,16):
            for j in range(1,16):
                t[i][j] = list[i-1][j-1]
        return white_mian4num(t)*mian4_num+white_huo3num(t)*huo3_num\
               +white_mian3num(t)*mian3_num+white_huo2num(t)*huo2_num\
               +white_mian2num(t)*mian2_num+white_huo1num(t)*huo1_num+white_mian1num(t)*mian1_num


# 目前棋盘玩家的得分
def Now_PlayerScore():
    global list
    t = [[0]*17 for i in range(17)]
    if player == 1:
        for i in range(0,17):
            t[0][i] = 1
            t[16][i] = 1
            t[i][0] = 1
            t[i][16] = 1
        for i in range(1,16):
            for j in range(1,16):
                t[i][j] = list[i-1][j-1]
        return white_mian4num(t)*mian4_num+white_huo3num(t)*huo3_num\
               +white_mian3num(t)*mian3_num+white_huo2num(t)*huo2_num\
               +white_mian2num(t)*mian2_num+white_huo1num(t)*huo1_num+white_mian1num(t)*mian1_num
    else:
        for i in range(0,17):
            t[0][i] = 2
            t[16][i] = 2
            t[i][0] = 2
            t[i][16] = 2
        for i in range(1,16):
            for j in range(1,16):
                t[i][j] = list[i-1][j-1]
        return black_mian4num(t)*mian4_num+black_huo3num(t)*huo3_num\
               +black_mian3num(t)*mian3_num+black_huo2num(t)*huo2_num\
               +black_mian2num(t)*mian2_num+black_huo1num(t)*huo1_num+black_mian1num(t)*mian1_num
# 得到AI再走一步后可以得到的最大得分
def findMaxAIScore():
    global AI_x,AI_y,player
    max_score = 0
    min_score = sys.maxsize
    for i in range(0, 15):
        for j in range(0, 15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 2
                else:
                    list[i][j] = 1
                AI_score = Now_AIScore()
                player_score = Now_PlayerScore()
                if AI_score > max_score:
                    AI_x = i + 1
                    AI_y = j + 1
                    max_score = AI_score
                    min_score = player_score
                elif AI_score == max_score:
                    if player_score < min_score:
                        AI_x = i + 1
                        AI_y = j + 1
                        max_score = AI_score
                        min_score = player_score
                list[i][j] = 0
# 得到玩家再走一步后可以得到的最大得分
def findMaxPlayerScore():
    global AI_x,AI_y,player,list
    max_score = 0
    min_score = sys.maxsize
    for i in range(0, 15):
        for j in range(0, 15):
            if list[i][j] == 0:
                if player == 0:
                    list[i][j] = 1
                else:
                    list[i][j] = 2
                AI_score = Now_AIScore()
                player_score = Now_PlayerScore()
                if player_score>max_score:
                    AI_x = i+1
                    AI_y = j+1
                    max_score = player_score
                    min_score = AI_score
                elif player_score == max_score:
                    if AI_score < min_score:
                        AI_x = i + 1
                        AI_y = j + 1
                        max_score = player_score
                        min_score = AI_score
                list[i][j] = 0
# AI根据局势判断下下一步棋
def AIplayed():
    global AI_x,AI_y,isEnd,pos_x,pos_y,player,list,person
    # 如果AI存在一步致胜棋，就走这一步
    if isAIWin():
        ox = -15+30*AI_x
        oy = -15+30*AI_y
        if player == 0:
            list[AI_x-1][AI_y-1] = 2
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
        else:
            list[AI_x - 1][AI_y - 1] = 1
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black")
        tkinter.messagebox.showinfo('提示', 'AI胜')
        button['text'] = "重新开始"
        isEnd = True
        text1['bg'] = 'white'
        text2['bg'] = 'white'
    # 如果玩家下一步存在致胜棋就封堵那一步
    elif isPlayerWin():
        ox = -15 + 30 * AI_x
        oy = -15 + 30 * AI_y
        if player == 0:
            list[AI_x - 1][AI_y - 1] = 2
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
        else:
            list[AI_x - 1][AI_y - 1] = 1
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black")
    # 如果AI存在活三，就形成活四
    elif AIisPFThree():
        ox = -15 + 30 * AI_x
        oy = -15 + 30 * AI_y
        if player == 0:
            list[AI_x - 1][AI_y - 1] = 2
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
        else:
            list[AI_x - 1][AI_y - 1] = 1
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black")
    # 判断玩家是否存在活三，如果有就封堵
    elif PlayerIsPFFour():
        ox = -15 + 30 * AI_x
        oy = -15 + 30 * AI_y
        if player == 0:
            list[AI_x - 1][AI_y - 1] = 2
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
        else:
            list[AI_x - 1][AI_y - 1] = 1
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black")
    else:
        # now_AI = Now_AIScore()
        # now_player = Now_PlayerScore()
        # if now_AI >= now_player:
        # findMaxAIScore()
        # else:
        findMaxPlayerScore()
        ox = -15 + 30 * AI_x
        oy = -15 + 30 * AI_y
        if player == 0:
            list[AI_x - 1][AI_y - 1] = 2
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
        else:
            list[AI_x - 1][AI_y - 1] = 1
            can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black")
    if player == 0:
        ox = AI_x * 30 - 15
        oy = AI_y * 30 - 15
        can.create_oval(ox - 2, oy - 2, ox + 2, oy + 2, fill="black",width = 0)
    else:
        ox = AI_x * 30 - 15
        oy = AI_y * 30 - 15
        can.create_oval(ox - 2, oy - 2, ox + 2, oy + 2, fill="white",width = 0)
    person += 1



#10000000
black_huo4 = ['011110']
white_huo4 = ['022220']
#900
huo3_num = 900
black_huo3 = ['001110', '010110', '011010', '011100']
white_huo3 = ['002220', '020220', '022020', '022200']
#90
huo2_num = 90
black_huo2 = ['000110', '001010', '001100', '010010', '010100', '011000']
white_huo2 = ['000220', '002020', '002200', '020020', '020200', '022000']
#9
huo1_num = 9
black_huo1 = ['000010', '000100', '001000', '010000']
white_huo1 = ['000020', '000200', '002000', '020000']
#1000
mian4_num = 1000
black_mian4 = ['211110','11101','11011','10111','011112']
white_mian4 = ['122220', '22202', '22022', '20222', '022221']
#100
mian3_num = 100
black_mian3 = ['201110', '210110', '211010', '211100', '01101', '10101',
              '11001', '11100', '01011', '10011', '11010', '00111', '10110',
              '001112', '010112', '011012', '011102']
white_mian3 = ['102220', '120220', '122020', '122200', '02202', '20202',
              '22002', '22200', '02022', '20022', '22020', '00222', '20220',
              '002221', '020221', '022021', '022201']
#10
mian2_num = 10
black_mian2 = ['200110', '201010', '201100', '210010', '210100', '211000',
              '00101', '01001', '01100', '10001', '10100', '11000', '00011',
              '01010', '10010', '00110', '000112', '001012', '001102', '010012'
    , '010102', '011002']
white_mian2 = ['100220', '102020', '102200', '120020', '120200', '122000', '00202',
              '02002', '02200', '20002', '20200', '22000', '00022', '02020', '20020',
              '00220', '000221', '002021', '002201', '020021', '020201', '022001']
#1
mian1_num = 1
black_mian1 = ['200010', '200100', '201000', '210000', '00001', '00100', '01000',
              '10000', '00010', '000012', '000102', '001002', '010002']
white_mian1 = ['100020', '100200', '102000', '120000', '00002', '00200', '02000',
              '20000', '00020', '000021', '000201', '002001', '020001']
list = [[0] * 15 for i in range(15)]
pos_x = 9
pos_y = 9
person = 0
isStart = False
isEnd = False
player = 0
AI_x = 8
AI_y = 8
step = 0
# 点击画布后的动作
def play(event):
    global isStart,pos_x,pos_y,person,list,isEnd,list_val,player
    if isStart == False:
        tkinter.messagebox.showinfo('提示', '还未开始')
    else:
        if isEnd == False:
            x = event.x
            y = event.y
            t1 = False
            for i in range(1, 16):
                for j in range(1, 16):
                    if (abs(-15 + 30 * i - x) <= 10 and abs(-15 + 30 * j - y) <= 10):
                        pos_x = i
                        pos_y = j
                        t1 = True
                        break
                if t1 == True:
                    break

            if t1 == True:
                if isCan(pos_x, pos_y, list):
                    if player == 0:
                        if person != 0:
                            ox = AI_x * 30 - 15
                            oy = AI_y * 30 - 15
                            can.create_oval(ox - 2, oy - 2, ox + 2, oy + 2, fill="white",width = 0)
                        ox = -15 + 30 * pos_x
                        oy = -15 + 30 * pos_y
                        list[pos_x - 1][pos_y - 1] = 1
                        can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="black",)

                        if isEndL(pos_x, pos_y, list) or isEndH(pos_x, pos_y, list) or isEndUL(pos_x, pos_y,
                                                                                               list) or isEndUR(
                            pos_x, pos_y, list):
                            tkinter.messagebox.showinfo('提示', '黑棋胜')
                            button['text'] = "重新开始"
                            isEnd = True
                            text1['bg'] = 'white'
                            text2['bg'] = 'white'

                    else:
                        ox = AI_x * 30 - 15
                        oy = AI_y * 30 - 15
                        can.create_oval(ox - 2, oy - 2, ox + 2, oy + 2, fill="black",width = 0)
                        ox = -15 + 30 * pos_x
                        oy = -15 + 30 * pos_y
                        list[pos_x - 1][pos_y - 1] = 2
                        can.create_oval(ox - 12, oy - 12, ox + 12, oy + 12, fill="white")
                        if isEndL(pos_x, pos_y, list) or isEndH(pos_x, pos_y, list) or isEndUL(pos_x, pos_y,
                                                                                               list) or isEndUR(
                            pos_x, pos_y, list):
                            tkinter.messagebox.showinfo('提示', '白棋胜')
                            button['text'] = "重新开始"
                            isEnd = True
                            text1['bg'] = 'white'
                            text2['bg'] = 'white'
                    # for i in range(0, 15):
                    #     for j in range(0, 15):
                    #         if list[i][j] != 0:
                    #             print(i, j)
                    if isEnd == False:
                        AIplayed()






# 开始按钮事件，点击之后刷新界面，清零数组
def start():
    global isStart,isEnd,list,person,player,pos_x,pos_y,AI_x,AI_y
    pos_x = 9
    pos_y = 9
    AI_x = 8
    AI_y = 8
    button['text'] = "重新开始"
    isStart = True
    isEnd = False
    can.delete(ALL)
    person = 0
    player = random.randint(0,1)
    for i in range(0,15):
        for j in range(0,15):
            list[i][j] = 0
    can.create_rectangle(15, 15, 435, 435)
    for i in range(1, 14):
        can.create_line(15 + i * 30, 15, 15 + i * 30, 435)
        can.create_line(15, 15 + i * 30, 435, 15 + 30 * i)
    if player == 1:
        text2['bg'] = 'orange'
        text1['bg'] = 'white'
        AIplayed()
    else:
        text1['bg'] = 'orange'
        text2['bg'] = 'white'

myWindow = Tk()
myWindow.title("五子棋")
myWindow.geometry("450x500+100+100")
can = Canvas(myWindow, width=450, height=450, bg="#D2C0A4")
can.create_rectangle(15,15,435,435)
for i in range(1,14):
    can.create_line(15+i*30,15,15+i*30,435)
    can.create_line(15,15+i*30,435,15+30*i)
can.bind("<Button-1>",play)
can.pack()
text1 = Label(myWindow,text = "黑方",width = 10,height = 5)
text2 = Label(myWindow,text = "白方",width = 10,height = 5)
text1.pack(side = LEFT)
text2.pack(side = RIGHT)
button = tkinter.Button(myWindow,width = 100,height = 50,text = "开始",command = start)
button.pack()
myWindow.mainloop()
