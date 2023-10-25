print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def game_board(board): #рисуем игровое поле
   print("-" * 13) #ограничение полей
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13) #ограничение полей

def check_correct(player): # Функция проверки корректности ввода
   a = False
   while not a:
      player_motion = input("Куда поставим фигуру " + player+"? ") #запрашиваем куда ставим фигуру с обозначением текущей фигуры
      try:
         player_motion = int(player_motion) #проверка корректного ввода
      except:
         print("Некорректный ввод!")
         continue
      if player_motion >= 1 and player_motion <= 9:
         if(str(board[player_motion-1]) not in "XO"):
            board[player_motion-1] = player
            a = True
         else:
            print("Эта клетка занята!")
      else:
        print("Некорректный ввод.")

def check_win(board): #функция проверки победителя
   win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) #возможные варианты победы
   for other in win:
       if board[other[0]] == board[other[1]] == board[other[2]]:
          return board[other[0]]
   return False

def main(board): #основная функция
    counter = 0
    win = False
    while not win:
        game_board(board)
        if counter % 2 == 0:
           check_correct("X")
        else:
           check_correct("O")
        counter += 1
        if counter > 4: #сценарий победы
           b = check_win(board)
           if b:
              print(b, "выиграл!")
              win = True
              break
        if counter == 9: # сценарий ничьи
            print("Ничья!")
            break
    game_board(board)
main(board)















