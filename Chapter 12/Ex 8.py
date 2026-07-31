# update_board_state literally redoes the check that place_one_step does, but I'm not sure how to consolidate it to be once and done.
# making a precise coordinate system is terrible
from graphics import *
from button import *
from math import ceil
class model():
    def __init__(self, interface):
        self.interface = interface
        self.p1_concede = False
        self.p2_concede = False
        # key is the coordinates, values are the colours "w", "b", ""
        self.board_state = {
            (x, y): "" for x in range(1, 9) for y in range(1, 9)
        }
        # starting 4 pieces
        self.board_state[(4, 4)] = "w"
        self.board_state[(5, 5)] = "w"
        self.board_state[(4, 5)] = "b"
        self.board_state[(5, 4)] = "b"

    def run(self):
        current_turn = 1
        while self.p1_concede == False and self.p2_concede == False:
            if not self.has_legal_move(current_turn):
                if current_turn == 1:
                    current_turn = 2
                else:
                    current_turn = 1
                pass
            self.place_one_piece(current_turn)
            p1_count, p2_count = self.recountpieces()
            self.interface.update_piece_count(p1_count, p2_count)
            if current_turn == 1:
                current_turn = 2
            else:
                current_turn = 1
        if self.p1_concede:
            self.interface.winner("p2")
        else:
            self.interface.winner("p1")

    def place_one_piece(self, current_turn):
        self.interface.display_turn(current_turn)
        # input received is the coordinates, e.g. (4, 4)
        coordinates = self.interface.get_input()
        # if "Pass" or "Quit" is received, nothing happens
        if coordinates == "Pass":
            return
        if coordinates == "Quit":
            if current_turn == 1:
                self.p1_concede = True
            else:
                self.p2_concede = True
            return

        outcome, affected_directions = self.input_validation(coordinates, current_turn)
        while outcome == False:
            self.interface.input_failed()
            coordinates = self.interface.get_input()
            if coordinates == "Pass":
                return
            if coordinates == "Quit":
                if current_turn == 1:
                    self.p1_concede = True
                else:
                    self.p2_concede = True
                return
            outcome, affected_directions = self.input_validation(coordinates, current_turn)
        self.update_board_state(coordinates, affected_directions, current_turn) #
        self.interface.update_piece(self.board_state)

    def recountpieces(self):
        p1_sum = 0
        p2_sum = 0
        for (x, y), piece in self.board_state.items():
            if piece == "b":
                p1_sum += 1
            elif piece == "w":
                p2_sum += 1
        return p1_sum, p2_sum
    
    def has_legal_move(self,current_turn):
        for (x,y),value in self.board_state.items():
            if value == "":
                is_valid, a = self.placement_validation(x,y,current_turn)
                if is_valid:
                    return True
        return False
                
    def input_validation(self, coordinates, current_turn):
        #only houses basic validation, placement_validation checks the effect of the placement if any
        if not isinstance(coordinates, (list)) or len(coordinates) != 2:
            return False, []

        try:
            x = int(coordinates[0])
            y = int(coordinates[1])
        except (TypeError, ValueError):
            return False, []

        if not (1 <= x <= 8 and 1 <= y <= 8):
            return False, []

        if self.board_state[(x, y)] != "": #occupied tile
            return False, []

        is_valid, affected_directions = self.placement_validation(x,y,current_turn)
        return is_valid, affected_directions
                
    def placement_validation(self,x,y,current_turn):
        direction_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        affected_directions = []

        for dx, dy in direction_list:
            mult = 1
            while True: #n for new
                nx = x + dx * mult
                ny = y + dy * mult

                if not (1 <= nx <= 8 and 1 <= ny <= 8): #if out of bounds
                    break

                piece = self.board_state[(nx, ny)]
                if current_turn == 1:  # b
                    if piece == "w":
                        mult += 1
                        continue
                    elif piece == "":
                        break
                    else:  # b found
                        if mult == 1:
                            break
                        affected_directions.append((dx, dy))
                        break
                elif current_turn == 2:  # w
                    if piece == "b":
                        mult += 1
                        continue
                    elif piece == "":
                        break
                    else:  # w found
                        if mult == 1:
                            break
                        affected_directions.append((dx, dy))
                        break

        if not affected_directions:
            return False, []
        return True, affected_directions

    def update_board_state(self, coordinates, directions, current_turn):
        if current_turn == 1:
            colour = "b"
        else:
            colour = "w"

        x, y = int(coordinates[0]), int(coordinates[1])
        self.board_state[(x, y)] = colour

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 1 <= nx <= 8 and 1 <= ny <= 8:
                piece = self.board_state[(nx, ny)]
                if piece == "": #stop when blank
                    break 
                if piece == colour: #stop when same colour
                    break
                self.board_state[(nx, ny)] = colour
                nx += dx
                ny += dy

class view():

    def __init__(self):
        self.win = GraphWin("Reversi", 768, 930)
        self.win.setBackground("darkgreen")
        # board looks better at the bottom and plotting coords with
        # the y-values not identical to x-values is deeply irritating
        self.win.setCoords(0,0,768,930) 
        self.status = Text(Point(384, 900), "Welcome to Reversi!")
        self.status.setSize(20)
        self.status.setTextColor("white")
        self.status.draw(self.win)
        close = Button(self.win,Point(256,450),50,40,"Exit")
        open_prompt = Button(self.win,Point(512,450),80,40,"Let's Play!")
        self.buttons = [close,open_prompt]
        self.closewin = False
        while True:
            b = self.choose(["Exit","Let's Play!"])
            if b == "Exit":
                self.win.close()
                self.closewin = True
                return
            elif b == "Let's Play!":
                self.set_up()
                return

    def set_up(self):
        self.board_info = {} #for tracking pieces of the board
        self.board_pieces = {} #for tracking the objects representing the pieces of the board
        board = Image(Point(384,384),"Ex 8/board.png")
        board.draw(self.win)
        self.quit_button = Button(self.win,Point(256, 830),50,40, "Quit")
        self.pass_button = Button(self.win,Point(512, 830), 50, 40, "Pass")
        self.quit_button.activate()
        self.pass_button.activate()
        #starting pieces
        self.draw_piece((4,4),"w")
        self.draw_piece((5,5),"w")
        self.draw_piece((4,5),"b")
        self.draw_piece((5,4),"b")
        self.p1_count = Text(Point(256, 790), "Black: 2")
        self.p1_count.setTextColor("White")
        self.p2_count = Text(Point(512, 790), "White: 2")
        self.p2_count.setTextColor("White")
        self.p1_count.setSize(18)
        self.p2_count.setSize(18)
        self.p1_count.draw(self.win)
        self.p2_count.draw(self.win)
        board_width = 768
        self.cell_size = board_width/8

    def display_turn(self,current):
        if current == 1:
            self.status.setText("It is black's turn" + "\n Place a piece.")
        elif current == 2:
            self.status.setText("It is white's turn" + "\n Place a piece.")

    def get_input(self):
        click = self.win.getMouse()
        if self.quit_button.clicked(click):
            return "Quit"
        elif self.pass_button.clicked(click):
            return "Pass"
        x, y = click.getX(), click.getY()
        row = ceil(x/self.cell_size)
        column = ceil(y/self.cell_size)
        return [row,column]
    
    def input_failed(self):
        self.status.setText("Input failed. Try again.")

    def update_piece_count(self,p1_count, p2_count):
        self.p1_count.setText(f"Black: {p1_count}")
        self.p2_count.setText(f"White: {p2_count}")

    def winner(self,player):
        if player == "p1":
            self.status.setText("Black wins!")
        elif player == "p2":
            self.status.setText("White wins!")

    def update_piece(self,board_state):
        for key, value in board_state.items():
            if value == "":
                pass
            elif key not in self.board_info:
                self.draw_piece(key,value)
            elif value != self.board_info[key]: #was updated
                self.undraw_piece(key)
                self.draw_piece(key,value)

    def draw_piece(self,coord,colour):
        self.board_info.update({coord : colour})
        x,y = coord
        x = (x - 0.5) * 96 #width and height of cell
        y = (y - 0.5) * 96
        if colour == "w":
            piece = Image(Point(x,y),"Ex 8/white_piece.png")
        elif colour == "b":
            piece = Image(Point(x,y),"Ex 8/black_piece.png")
        piece.draw(self.win)
        self.board_pieces.update({coord: piece})

    def undraw_piece(self,coord):
        self.board_info.update({coord : ""})
        piece = self.board_pieces[coord]
        self.board_pieces.update({coord: ""})
        piece.undraw()

    def choose(self, choices):
        buttons = self.buttons
        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.


        

graph = view()
if not graph.closewin:
    reversi = model(graph)
    reversi.run()
