'''
Tic Tac Toe PyGame 
Milestone Project for Logic and Func implementation
Coded by Shahroz 'Sz' Khan
'''

def clear_disp():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def board_disp(board):
    print('---> Tic Tac Hoe <---\n')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')

def marker_select():
    marker='any'
    right_marker=['X','O','x','o']
    while marker not in right_marker:
        marker=input('\nPlayer Select: X or O: ').upper()
        if marker in right_marker:
            print(f'\nPlayer 1 chose {marker}, Now select where you want place your Mark\n')
        else:
            print('\nInvalid Input: Choose either X or O\n')
    return marker

def marker_switch(umarker):
    switch=True
    while switch:
        if umarker=='X':
            umarker='O'
            switch=False   
        else:
            umarker='X'
            switch=False
    return umarker

def posn_choice(umarker):
    pchoice = 'wrong'
    posn_range=list(range(1,10))
    while pchoice not in posn_range:
        pchoice = int(input(f"\nPick a position to place {umarker}: Choose from 1 to 9 \n"))
        if pchoice not in posn_range:
            print("\nSorry, but you did not choose a valid position\n")
    return pchoice

def replacer(board,umarker,uposn):
    board[uposn]=umarker
    return board

def location_check(board,uposn):
    if board[uposn]==' ':
        return True
    else:
        return False

def check_n_replace(board,umarker,uposn):
    while location_check(board,uposn)==True:
        nvalues=replacer(board,umarker,uposn)
        print(f'\n{umarker} placed at {uposn} Position\n')
        return nvalues

    while location_check(board,uposn)==False:
        print('\nSaid Location is Taken! please choose another location for', umarker)
        uposn=posn_choice(umarker)
        if location_check(board,uposn)==True:
            nvalues=replacer(board,umarker,uposn)
            print(f'\n{umarker} placed at {uposn} Position\n')
            return nvalues

def check_win(board,umarker):
    if (board[1]==board[2]==board[3]==umarker)or(board[4]==board[5]==board[6]==umarker)or(board[7]==board[8]==board[9]==umarker)or(board[1]==board[5]==board[9]==umarker)or(board[7]==board[5]==board[3]==umarker)or(board[7]==board[4]==board[1]==umarker)or(board[8]==board[5]==board[2]==umarker)or(board[9]==board[6]==board[3]==umarker):
        board_disp(board)
        print(f'\n{umarker} has won the game\n')
        return True
    else:
        return False

def game_over(board):
    while ' ' in board:
        return True
    if ' ' not in board:
        return False

def replay():
    lastchoice='anything'
    while lastchoice not in ['y','n','Y','N']:
        lastchoice=input("\nDo You Want Play Again? 'y' or 'n': ",)
        print('\n')
        if lastchoice not in ['y','n','Y','N']:
            clear_disp()
            print('\nINVALID INPUT! Please Choose y or n\n')
    if lastchoice == 'y' or lastchoice=='Y':
        return True
    else:
        return False

game_on=True
while game_on:
    clear_disp()
    main_values=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print("---> Welcome To Sz' Tic-Tac-Toe Game on Python! <---\n")
    print("\nNOTE: To play the game properly play the game on your numpad\nor Imagine your keyboard's numpad as the tic-tac-toe board for\nposition reference.\n\n")
    board_disp(main_values)
    user_marker=marker_select()
    board_disp(main_values)
    user_marker=marker_switch(user_marker)
    while game_over(main_values):
        user_marker=marker_switch(user_marker)
        posn=posn_choice(user_marker)
        main_values=check_n_replace(main_values,user_marker,posn)
        clear_disp()
        board_disp(main_values)
        if check_win(main_values,user_marker):
            clear_disp()
            board_disp(main_values)
            print(f'\n{user_marker} has won the game\n')
            break
        elif game_over(main_values)==False:
            clear_disp()
            board_disp(main_values)
            print('\n---> Game Over! Its a tie <---\n')
            break
    game_on=replay()