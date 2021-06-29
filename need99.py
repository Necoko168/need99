import random

def root_win(peoplenum:int, times:int):
    ''' 
    通常のロットシミュレーション
    peoplenum: ロットに参加する人数
    times: ロットぶん回す回数
    '''

    winners = []
    win_number = []

    for i in range(times):
        rootbox = [n+1 for n in range(99)]  # 1から99まで書かれたカードの束を用意する(この時点では1,2,3,4...と順番に並んでる)
        random.shuffle(rootbox) # カードの束をシャッフルする(ここでバラバラになる)

        deals = rootbox[:peoplenum] # シャッフルしたカードをひとりめから順番に配っていく
        
        # 結果を確認する
        #winners.append(p for p in range(peoplenum) if deals[p] == max(deals) )  # 何番目に配られた人が勝ったかを記録
        for p in range(peoplenum):
            if deals[p] == max(deals):
                winners.append(p)

        win_number.append(max(deals))   # 勝ったときの数値を記録

    print(str(peoplenum) + " 人で通常ロットを " + str(times) + " 回やり倒した結果")
    for i in range(peoplenum):
        print(str(i+1) + "人目：" + str(winners.count(i)))

    print("勝ったときのロット数値の平均：" + str(sum(win_number)/len(win_number)))
    print("勝ったときのロット数値の最低値：" + str(min(win_number)))

def root_need99(peoplenum:int, times:int):
    ''' 
    NEED99が1枚とそれ以外が(人数-1)枚入っている条件でのロット勝負
    peoplenum: ロットに参加する人数
    times: ロットぶん回す回数
    '''

    winners = []
    win_number = []

    for i in range(times):
        rootbox = [n+1 for n in range(peoplenum-1)] # 勝てない人の分のカードをセット
        rootbox.append(99)                     # 99のカードを混入する。ここでカード枚数とロット人数は一緒になる
        random.shuffle(rootbox) # カードの束をシャッフルする(ここでバラバラになる)

        deals = rootbox[:peoplenum] # シャッフルしたカードをひとりめから順番に配っていく
        
        # 結果を確認する
        winners.append(p for p in range(peoplenum) if deals[p] == max(deals) )  # 何番目に配られた人が勝ったかを記録
        for p in range(peoplenum):
            if deals[p] == max(deals):
                winners.append(p)

        win_number.append(max(deals))   # 勝ったときの数値を記録

    print(str(peoplenum) + " 人でNEED99ロットを " + str(times) + " 回やり倒した結果")
    for i in range(peoplenum):
        print(str(i+1) + "人目が99を引いた回数：" + str(winners.count(i)))

    print("勝ったときのロット数値の平均：" + str(sum(win_number)/len(win_number)))
    print("勝ったときのロット数値の最低値：" + str(min(win_number)))

def main():
    root_need99(4,10000)     # 4人ロット(LightParty) でロット100万回
    root_need99(8,10000)     # 8人ロット(FullParty) でロット100万回
    root_need99(24,10000)    # 24人ロット(Alliance) でロット100万回
    root_win(4,10000)     # 4人ロット(LightParty) で99ロット100万回
    root_win(8,10000)     # 8人ロット(FullParty) で99ロット100万回
    root_win(24,10000)    # 24人ロット(Alliance) で99ロット100万回

if __name__ == '__main__':
    main()



