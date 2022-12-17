from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, IBMQ

def tic_tac_toe():
    qr = QuantumRegister(9)
    cr = ClassicalRegister(9)
    circuit = QuantumCircuit(qr, cr)

    IBMQ.load_account()
    provider = IBMQ.get_provider('ibm-q')
    qcomp = provider.get_backend('simulator_statevector')


    while True:
        print("Player 1's turn")
        index = int(input("Enter index (0-8): "))

        circuit.x(qr[index])
        circuit.measure(qr, cr)
        result = execute(circuit, backend=qcomp, shots=1).result()
        counts = result.get_counts()

        for k, v in counts.items():
            if v == 1:
                board = list(k)
                board = [int(x) for x in board]
        if check_winner(board, 1):
            print("Player 1 wins!")
            break

        print("Player 2's turn")
        index = int(input("Enter index (0-8): "))

        circuit.z(qr[index])
        circuit.measure(qr, cr)
        result = execute(circuit, backend=qcomp, shots=2).result()
        counts = result.get_counts()

        for k, v in counts.items():
            if v == 2:
                board = list(k)
                board = [int(x) for x in board]
        if check_winner(board, 2):
            print("Player 2 wins!")
            break

def check_winner(board, player):
    for i in range(3):
        if board[i*3] == player and board[i*3+1] == player and board[i*3+2] == player:
            return True

    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True

    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False
tic_tac_toe()

# Player 1's turn
# Enter index (0-8): 0
# Player 2's turn
# Enter index (0-8): 4
# Player 1's turn
# Enter index (0-8): 1
# Player 2's turn
# Enter index (0-8): 5
# Player 1's turn
# Enter index (0-8): 2
# Player 1 wins!