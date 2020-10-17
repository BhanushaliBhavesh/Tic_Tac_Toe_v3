""" Tic_Tac_toe Using Dictionary of Dictionaries """

mark = 'x'

count = 0

board = {

    "0" : {"0":"1", "1":"2", "2":"3"},

    "1" : {"0":"4", "1":"5", "2":"6"},

    "2" : {"0":"7", "1":"8", "2":"9"}

}


def display_board():
    """ displying board """
    print(board['0']['0'], " | ", board['0']['1'], " | ", board['0']['2'])
    print("___ _____ ___")
    print(board['1']['0'], " | ", board['1']['1'], " | ", board['1']['2'])
    print("___ _____ ___")
    print(board['2']['0'], " | ", board['2']['1'], " | ", board['2']['2'])


def winner_checker(mark):
    """here we check winner"""
    #row wise checking
    if board['0']['0'] == mark and board['0']['1'] == mark and board['0']['2'] == mark:
        return True
    elif board['1']['0'] == mark and board['1']['1'] == mark and board['1']['2'] == mark:
        return True
    elif board['2']['0'] == mark and board['2']['1'] == mark and board['2']['2'] == mark:
        return True
    #column wise checking
    elif board['0']['0'] == mark and board['1']['0'] == mark and board['2']['0'] == mark:
        return True
    elif board['0']['1'] == mark and board['1']['1'] == mark and board['2']['1'] == mark:
        return True
    elif board['0']['2'] == mark and board['1']['2'] == mark and board['2']['2'] == mark:
        return True
    #1cross
    elif board['0']['0'] == mark and board['1']['1'] == mark and board['2']['2'] == mark:
        return True
    #2cross
    elif board['0']['2'] == mark and board['1']['1'] == mark and board['2']['0'] == mark:
        return True
    else:
        return False


def box_check(key, column):
    """ for checking box is used or not
    here key and column provide postion """

    return bool(board[key][column] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])


def turn():
    """ swiching plyers"""

    global mark
    global count

    raw1 = ['1', '2', '3']
    raw2 = ['4', '5', '6']
    raw3 = ['7', '8', '9']


    while count <= 9:

        display_board()
        print("Player |{}| Turn".format(mark))
        number = input("Enter The postion 1 to 9 -->")

        if number in raw1: #  if number in ['1','2','3']

            flag = box_check('0', str(raw1.index(number))) # checking mark is prsent on that number

            if flag == True:

                board['0'][str(raw1.index(number))] = mark  # adding mark on given number
                count += 1       #incresing count when mark marked on number

                if count >= 5 and winner_checker(mark) == True:  #checking winner after 5 moves
                    display_board()
                    print("!!! Player |{}| is Winner !!!".format(mark))
                    print("-------Game Over--------")
                    break

                if count >= 9:     #if count >= 9 game will tiee.
                    display_board()
                    print("Game tie")
                    print("-------Game Over--------")
                    break


                if mark == 'x':     #changing mark
                    mark = 'o'
                else:
                    mark = 'x'
            else:
                print("!!! This Task Is Not Valid !!!")
        elif number in raw2:  # if number in ['4','5','6']

            flag = box_check('1', str(raw2.index(number))) # checking mark is prsent on that number

            if flag == True:
                board['1'][str(raw2.index(number))] = mark  # adding mark on given numer
                count += 1       #incresing count when mark marked on number

                if count >= 5 and winner_checker(mark) == True:   #checking winner after 5 moves
                    display_board()
                    print("!!! Plyer |{}| is Winner !!!".format(mark))
                    print("-------Game Over--------")
                    break

                if count >= 9:     #if count >= 9 game will tiee.
                    display_board()
                    print("Game tie")
                    print("-------Game Over--------")
                    break


                if mark == 'x':     #changing mark
                    mark = 'o'
                else:
                    mark = 'x'
            else:
                print("!!! This Task Is Not Valid !!!")

        elif number in raw3:   #if number in ['7', '8', '9']

            flag = box_check('2', str(raw3.index(number))) # checking mark is prsent on that number


            if flag == True:
                board['2'][str(raw3.index(number))] = mark  # adding mark on given numer
                count += 1       #incresing count when mark marked on number

                if count >= 5 and winner_checker(mark) == True:  #checking winne after 5 moves
                    display_board()
                    print("!!! Player |{}| is Winner !!!".format(mark))
                    print("-------Game Over--------")
                    break


                if count >= 9:     #if count >= 9 game will tiee.
                    display_board()
                    print("Game tie")
                    print("-------Game Over--------")
                    break


                if mark == 'x':     #changing mark
                    mark = 'o'
                else:
                    mark = 'x'
            else:
                print("!!! This Task Is Not Valid !!!")
        else:
            print("!!! Enter Valid Number !!!")

turn()
