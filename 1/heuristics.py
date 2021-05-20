import chess

##evaluation function  ##if piece.color =True, piece is white, otherwise black
##piece_type: pawn:1, knight:2, bishop:3, rook:4,queen:5,king:6
def get_piece_value(piece):
    if piece.color:
        color_factor = 1;
    else:
        color_factor = -1;
    if piece.piece_type == 1:
        return 1.0 * color_factor
    elif piece.piece_type == 2:
        return 3.0 * color_factor
    elif piece.piece_type == 3:
        return 3.0 * color_factor
    elif piece.piece_type == 4:
        return 5.0 * color_factor
    elif piece.piece_type == 5:
        return 9.0 * color_factor
    elif piece.piece_type == 6:
        return 0 * color_factor

def materials(board,weight):
        scores = 0.0
        for i in range(8):
            for j in range(8):
                if board.piece_at(chess.square(i,j)):
                    piece = board.piece_at(chess.square(i,j))
                    scores += get_piece_value(piece)
        return scores*weight

def get_square_at_position(position):
    """
    Square position sanitizer for when either a string
    or chess.Square can be entered as a position
    Args:
        position( Union[str, chess.Square])
    Returns:
        (chess.Square)
    """
    # Convert from string to chess.square via characters in string
    if isinstance(position, str):
        file, rank = ord(position[0].lower()) - 97, int(position[1]) - 1
        square = chess.square(file, rank)
    elif isinstance(position, chess.Square):
        square = position

    return square

def get_piece_at(
    board: chess.Board, position):
    """
    Gets chess symbol of piece at position on board
    Args:
        board (chess.Board): current board state in python-chess object
        position (str/chess.Square): position of square i.e chess.A1 or "A1"
    Returns:
        (str): symbol of piece at square if any
    """
    # Convert position to chess.Square
    square = get_square_at_position(position)
    piece = board.piece_at(square)

    if piece:
        return piece.symbol()
    return ""

def piece_moves(board, weight):
    scores = 0
    square_values = {"e4": 1, "e5": 1, "d4": 1, "d5": 1, "c6": 0.5, "d6": 0.5, "e6": 0.5, "f6": 0.5,
                    "c3": 0.5, "d3": 0.5, "e3": 0.5, "f3": 0.5, "c4": 0.5, "c5": 0.5, "f4": 0.5, "f5": 0.5}
    possible_moves =board.legal_moves
    for move in possible_moves:
        if board.turn:
            if str(move)[2:4] in square_values:
                scores += square_values[str(move)[2:4]] #“a1a2”
        else:
            if str(move)[2:4] in square_values:
                scores -= square_values[str(move)[2:4]]
    return scores * weight

def in_check(board, weight):
    scores = 0 
    # Turn should be 'w' or 'b'
    # Check or Checkmate situations
    if board.turn:
        if board.is_checkmate():
            scores -= 9999.0
        elif  board.is_check():
            scores -= weight
    else:
        if board.is_checkmate():
            scores += 9999.0
        elif board.is_check():
            scores += weight
    return scores

#pawn:1, knight:2, bishop:3, rook:4,queen:5,king:6

pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]
knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]
bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]
rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]
queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]
kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]
def piece_score(board,weight):
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KING, chess.BLACK)])
    score = pawnsq + knightsq + bishopsq + rooksq + queensq +kingsq
    return score*weight

def MVV_LVA(board):
    piece_values = {"P":1,"N":3,"B":3,"R":5,"Q":9,"K":25}
    available_captures = {}#: Dict[int,List[chess.Move]]
    move_list = list(board.legal_moves)
    # For each move, evaluate if any captures. If so, rank captures based
    # off value gained
    for move in move_list:
        if board.is_capture(move):
            aggressor_piece = get_piece_at(board, str(move)[:2]).upper()
            victim_piece = get_piece_at(board, str(move)[2:]).upper()
            if aggressor_piece and victim_piece:
                value_diff = (
                    piece_value[victim_piece].value
                    - piece_value[aggressor_piece].value
                )
                available_captures[value_diff] = move

    # If any available captures, sort captures by value_diff of captures
    # and return list of sorted captures
    if available_captures:
        move_list_sorted = []
        for val_diff in sorted(available_captures, reverse=True):
            move_list_sorted.append(available_captures[val_diff])
        return move_list_sorted

    # If no captures, return shuffled list of all legal moves
    random.shuffle(move_list)
    return move_list