import PySimpleGUI as sg

import os
def is_pos_empty(pos):
    if board[pos] != None:
        return False
    return True
def add_to_board(pos,symbolo):
    if is_pos_empty(pos):
        if symbolo =='X':
            if pos == 1:
                line = graph.DrawLine((10*a+(0*a),90*a), (90*a+(0*a), 10*a), width=5*a)
                line = graph.DrawLine((10*a+(0*a),10*a), (90*a+(0*a), 90*a), width=5*a)
            elif pos == 2:
                line = graph.DrawLine((10*a+(100*a),90*a), (90*a+(100*a), 10*a), width=5*a)
                line = graph.DrawLine((10*a+(100*a),10*a), (90*a+(100*a), 90*a), width=5*a)
            elif pos == 3:
                line = graph.DrawLine((10*a+(200*a),90*a), (90*a+(200*a), 10*a), width=5*a)
                line = graph.DrawLine((10*a+(200*a),10*a), (90*a+(200*a), 90*a), width=5*a)
            elif pos == 4:
                line = graph.DrawLine((10*a,90*a+(100*a)), (90*a, 10*a+(100*a)), width=5*a)
                line = graph.DrawLine((10*a,10*a+(100*a)), (90*a, 90*a+(100*a)), width=5*a)
            elif pos == 5:
                line = graph.DrawLine((10*a+(100*a),90*a+(100*a)), (90*a+(100*a), 10*a+(100*a)), width=5*a)
                line = graph.DrawLine((10*a+(100*a),10*a+(100*a)), (90*a+(100*a), 90*a+(100*a)), width=5*a)
            elif pos == 6:
                line = graph.DrawLine((10*a+(200*a),90*a+(100*a)), (90*a+(200*a), 10*a+(100*a)), width=5*a)
                line = graph.DrawLine((10*a+(200*a),10*a+(100*a)), (90*a+(200*a), 90*a+(100*a)), width=5*a)
            elif pos == 7:
                line = graph.DrawLine((10*a,90*a+(200*a)), (90*a, 10*a+(200*a)), width=5*a)
                line = graph.DrawLine((10*a,10*a+(200*a)), (90*a, 90*a+(200*a)), width=5*a)
            elif pos == 8:
                line = graph.DrawLine((10*a+(100*a),90*a+(200*a)), (90*a+(100*a), 10*a+(200*a)), width=5*a)
                line = graph.DrawLine((10*a+(100*a),10*a+(200*a)), (90*a+(100*a), 90*a+(200*a)), width=5*a)
            elif pos == 9:
                line = graph.DrawLine((10*a+(200*a),90*a+(200*a)), (90*a+(200*a), 10*a+(200*a)), width=5*a)
                line = graph.DrawLine((10*a+(200*a),10*a+(200*a)), (90*a+(200*a), 90*a+(200*a)), width=5*a)
            return (line,line)
        elif symbolo == 'O':
            if pos == 1:
               z = graph.DrawCircle((50*a, 50*a), 40*a, line_color='black',line_width=4*a)
            elif pos == 2:
               z = graph.DrawCircle((50*a+(100*a), 50*a), 40*a, line_color='black',line_width=4*a)
            elif pos == 3:
               z = graph.DrawCircle((50*a+(200*a), 50*a), 40*a, line_color='black',line_width=4*a)
            elif pos == 4:
               z = graph.DrawCircle((50*a, 50*a+(100*a)), 40*a, line_color='black',line_width=4*a)
            elif pos == 5:
               z = graph.DrawCircle((50*a+(100*a), 50*a+(100*a)), 40*a, line_color='black',line_width=4*a)
            elif pos == 6:
               z = graph.DrawCircle((50*a+(200*a), 50*a+(100*a)), 40*a, line_color='black',line_width=4*a)
            elif pos == 7:
               z = graph.DrawCircle((50*a, 50*a+(200*a)), 40*a, line_color='black',line_width=4*a)
            elif pos == 8:
               z = graph.DrawCircle((50*a+(100*a), 50*a+(200*a)), 40*a, line_color='black',line_width=4*a)
            elif pos == 9:
               z = graph.DrawCircle((50*a+(200*a), 50*a+(200*a)), 40*a, line_color='black',line_width=4*a)

            return (z)
    else:
        return False

def clicked(cord):
    x = cord[0]
    y = cord[1]
    #print (x,y)
    if x < 100*a:
        if y < 100*a:
            return 1
        elif y < 200*a:
            return 4
        elif y < 300 * a:
            return 7
    elif x < 200*a:
        if y < 100*a:
            return 2
        elif y < 200*a:
            return 5
        elif y < 300 * a:
            return 8
    elif x < 300*a:
        if y < 100*a:
            return 3
        elif y < 200*a:
            return 6
        elif y < 300 * a:
            return 9

def has_anybody_won(theBoard): #Code Credit https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
    if theBoard[7] == theBoard[8] == theBoard[9] != None: # across the top
        return ({'wining_character' : theBoard[7],
                'start_pos' : 7,
                'mid_pos' : 8,
                'end_pos' : 9
                })
            #theBoard[7],7,9)

    elif theBoard[4] == theBoard[5] == theBoard[6] != None: # across the middle
        return ({'wining_character' : theBoard[4],
                'start_pos' : 4,
                'mid_pos' : 5,
                'end_pos' : 6
                })

    elif theBoard[1] == theBoard[2] == theBoard[3] != None: # across the bottom
        return ({'wining_character' : theBoard[1],
                'start_pos' : 1,
                'mid_pos' : 2,
                'end_pos' : 3
                })

    elif theBoard[1] == theBoard[4] == theBoard[7] != None: # down the left side
        return ({'wining_character' : theBoard[1],
                'start_pos' : 1,
                'mid_pos' : 4,
                'end_pos' : 7
                })

    elif theBoard[2] == theBoard[5] == theBoard[8] != None: # down the middle
        return ({'wining_character' : theBoard[2],
                'start_pos' : 2,
                'mid_pos' : 5,
                'end_pos' : 8
                })

    elif theBoard[3] == theBoard[6] == theBoard[9] != None: # down the right side
        return ({'wining_character' : theBoard[3],
                'start_pos' : 3,
                'mid_pos' : 6,
                'end_pos' : 9
                })
                        
    elif theBoard[7] == theBoard[5] == theBoard[3] != None: # diagonal
        return ({'wining_character' : theBoard[7],
                'start_pos' : 7,
                'mid_pos' : 5,
                'end_pos' : 3
                })

    elif theBoard[1] == theBoard[5] == theBoard[9] != None: # diagonal
        return ({'wining_character' : theBoard[1],
                'start_pos' : 1,
                'mid_pos' : 5,
                'end_pos' : 9
                })

    return False

def add_wining_line(start_cord,stop_cord):
    line = graph.DrawLine((start_cord[0]*a,start_cord[1]*a), (stop_cord[0]*a,stop_cord[1]*a), width=10*a,color='Green')

def reset_all():
    board = {7:None,8:None,9:None,
            4:None,5:None,6:None,
            1:None,2:None,3:None}
    


board_cord = {  7:(50,250),8:(150,250),9:(250,250),
                4:(50,150),5:(150,150),6:(250,150),
                1:(50, 50),2:(150,50),3:(250,50)}

board = {7:None,8:None,9:None,
        4:None,5:None,6:None,
        1:None,2:None,3:None}

a = 3 #scale


layout = [
    
            [sg.Graph(canvas_size=(300*a, 300*a), graph_bottom_left=(0, 0), graph_top_right=(300*a, 300*a), key='graph',enable_events=True,background_color ='#cccccc',pad=(0,0),)],
            [sg.T('Current Player:'),
            sg.Button('X',disabled=True, font=('Arial Bold',10*a), key='btn_x',pad=(0,0)),
            sg.Button('O',disabled=True, font=('Arial Bold',10*a), key='btn_o',pad=(0,0))]
        ]

#sg.SetOptions(background_color='#83adb5')
sg.set_options(margins=(0,0))


#sg.ChangeLookAndFeel('Dark2')
window = sg.Window('Tic-Tac-Toe', layout)

window.Finalize()

window['btn_x'].update(button_color=('Black','White'))
window['btn_o'].update(button_color=('Black','Gray'))

graph = window['graph']
#sg.show_debugger_window(location=(100,100))
line = graph.DrawLine((100*a, 0), (100*a, 300*a), width=5*a)  # HORIZONTAL LINE
line = graph.DrawLine((200*a, 0), (200*a, 300*a), width=5*a)  # HORIZONTAL LINE
line = graph.DrawLine((0, 100*a), (300*a, 100*a), width=5*a)  # VERTICAL LINE
graph.DrawLine((0, 200*a), (300*a, 200*a), width=5*a)  # VERTICAL LINE

char ='X'
X_points = 0
O_points = 0
while True:
    event, values = window.read()
    if event == None:
        break
    elif event == 'graph': # Αν υπαρχει ενα event
        pos = clicked(values['graph'])
        returned = add_to_board(pos,char)
        if returned != False: #The move was valid / the player did not clicked on occupied board position
            board[pos] = char
            won = has_anybody_won(board)
            if (won != False ): # Some player has won
                print('Won = ', won['wining_character'])
                add_wining_line(board_cord[won['start_pos']],board_cord[won['end_pos']])
                sg.popup_no_buttons(won['wining_character']+' won',no_titlebar = True,keep_on_top=True,auto_close=True,
                auto_close_duration=3,font=('Arial Bold',11*a),background_color='Black',
                location=(window.get_screen_size()[0]/2,window.get_screen_size()[1]/2))
                
                graph.Erase()
                board = {7:None,8:None,9:None,4:None,5:None,6:None,1:None,2:None,3:None}
                line = graph.DrawLine((100*a, 0), (100*a, 300*a), width=5*a)  # HORIZONTAL LINE
                line = graph.DrawLine((200*a, 0), (200*a, 300*a), width=5*a)  # HORIZONTAL LINE
                line = graph.DrawLine((0, 100*a), (300*a, 100*a), width=5*a)  # VERTICAL LINE
                graph.DrawLine((0, 200*a), (300*a, 200*a), width=5*a)  # VERTICAL LINE

            elif (not any(value == None for value in board.values())):#Isopalia
                sg.popup_no_buttons('Ισοπαλια',no_titlebar = True,keep_on_top=True,auto_close=True,
                auto_close_duration=3,font=('Arial Bold',11*a),background_color='Black',grab_anywhere=True,
                location=(window.get_screen_size()[0]/2,window.get_screen_size()[1]/2))

                graph.Erase() # Clear
                board = {7:None,8:None,9:None,4:None,5:None,6:None,1:None,2:None,3:None}
                line = graph.DrawLine((100*a, 0), (100*a, 300*a), width=5*a)  # HORIZONTAL LINE
                line = graph.DrawLine((200*a, 0), (200*a, 300*a), width=5*a)  # HORIZONTAL LINE
                line = graph.DrawLine((0, 100*a), (300*a, 100*a), width=5*a)  # VERTICAL LINE
                graph.DrawLine((0, 200*a), (300*a, 200*a), width=5*a)  # VERTICAL LINE

            if char == 'X':
                char = 'O'
                window['btn_o'].update(button_color=('Black','White'))
                window['btn_x'].update(button_color=('Black','Gray'))
            else:
                char = 'X'
                window['btn_x'].update(button_color=('Black','White'))
                window['btn_o'].update(button_color=('Black','Gray'))

