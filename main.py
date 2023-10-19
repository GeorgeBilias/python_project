import csv


def create_board(col):
    """Δημιουργεί ένα άδειο ταμπλώ παιχνιδιού μεγέθους col που εισάγεται από τον χρήστη."""
    board = [[" " for i in range(col)] for j in range(col)]
    return board


def show_board(board, col):
    """Εμφανίζει το ταμπλώ του παιχνιδιού, με την χρήση του πίνακα board έτσι ώστε να υπάρχει σωστή
        αρίθμηση των γραμμών και των στηλών προς διευκόλυνση των παικτών.

        col_num λειτουργεί ως μετρητής των στηλών προς εμφάνιση των αντίστοιχων αριθμών πάνω από το ταμπλώ (1-10).
        row_let λειτουργεί ως μετρητής των γραμμών προς εμφάνιση των αντίστοιχων γραμμάτων αριστερά του ταμπλώ (Α-J).
    """

    print("    ", end="")
    for col_num in range(1, col + 1):
        print(str(col_num) + "   ", end="")
    print("\n" + ((4 * col) + 3) * "-")
    i = col - 1
    while i >= 0:
        for row_let in range(65, col + 65):
            print(chr(row_let), end="")
            for j in range(col):
                print(" | " + str(board[i][j]), end="")
            print(" | \n")
            i -= 1
    print(((4 * col) + 3) * "-")


def check(check_col):
    """Ελέγχει αν η επιλογή στήλης του εκάστοτε παίκτη είναι μέσα στα πλαίσια του ταμπλώ που έχει οριστεί."""
    while True:
        sel = int(input(""))
        if 1 <= sel <= check_col:
            return sel - 1
        else:
            print("Παρακαλώ δώστε έγκυρη θέση!")
            continue


def valid(valid_board, valid_sel, valid_col):
    """Ελέγχει αν η επιλεγμένη στήλη είναι γεμάτη."""
    return valid_board[valid_col - 1][valid_sel] == " "


def available_row(ar_board, ar_sel, ar_col):
    """Ελέγχει ποιά είναι η επόμενη διαθέσιμη γραμμή στην επιλεγμένη στήλη, προς καταχώρηση της κίνησης του παίκτη."""
    for r in range(ar_col):
        if ar_board[r][ar_sel] == " ":
            return r


def move_register(mr_board, mr_row, mr_sel, mr_move):
    """Καταχωρεί στο ταμπλώ την κίνηση του παίκτη."""
    mr_board[mr_row][mr_sel] = mr_move


def check_win(win_board, win_col, win_move):
    """Ελέγχει την ύπαρξη νικητήριας τετράδας στο ταμπλώ

        Η πρώτη εμφωλευμένη επανάληψη διατρέχει το ταμπλώ οριζόντια ελέγχοντας όλες τις πιθανές θέσεις για την αρχή της
        νικητήριας τετράδας (οι 3 τελευταίες στήλες του πίνακα αποκλείονται καθώς δεν μπορούν να αποτελέσουν
        αρχή τετράδας.

        Η δεύτερη εμφωλευμένη επανάληψη διατρέχει το ταμπλώ κάθετα ελέγχοντας όλες τις πιθανές θέσεις για την αρχή της
        νικητήριας τετράδας (οι 3 τελευταίες γραμμές του πίνακα αποκλείονται καθώς δεν μπορούν να αποτελέσουν
        αρχή τετράδας.

        Η τρίτη εμφωλευμένη επανάληψη διατρέχει όλες τις διαγωνίους του ταμπλώ που έχουν θετική κλίση για την αρχή της
        νικητήριας τετράδας (οι 3 τελευταίες γραμμές και στήλες του πίνακα αποκλείονται καθώς δεν μπορούν να αποτελέσουν
        αρχή τετράδας).

        Η τέταρτη εμφωλευμένη επανάληψη διατρέχει όλες τις διαγωνίους του ταμπλώ που έχουν αρνητική κλίση για την αρχή
        της νικητήριας τετράδας (οι 3 πρώτες γραμμές και οι 3 τελευταίες στήλες του πίνακα αποκλείονται καθώς
        δεν μπορούν να αποτελέσουν αρχή τετράδας).
    """
    for c in range(win_col - 3):
        for r in range(win_col):
            if win_board[r][c] == win_move and win_board[r][c + 1] == win_move and \
                    win_board[r][c + 2] == win_move and win_board[r][c + 3] == win_move:
                return True

    for c in range(win_col):
        for r in range(win_col - 3):
            if win_board[r][c] == win_move and win_board[r + 1][c] == win_move and \
                    win_board[r + 2][c] == win_move and win_board[r + 3][c] == win_move:
                return True

    for c in range(win_col - 3):
        for r in range(win_col - 3):
            if win_board[r][c] == win_move and win_board[r + 1][c + 1] == win_move and \
                    win_board[r + 2][c + 2] == win_move and win_board[r + 3][c + 3] == win_move:
                return True

    for c in range(win_col - 3):
        for r in range(3, win_col):
            if win_board[r][c] == win_move and win_board[r - 1][c + 1] == win_move and \
                    win_board[r - 2][c + 2] == win_move and win_board[r - 3][c + 3] == win_move:
                return True


def save_board(sb, scol):
    """Μετατρέπει τα κελιά του πίνακα σε 0,1,2 ανάλογα με το περιεχόμενο τους και επιστρέφει τον νέο πίνακα προς
        αποθήκευση."""

    for r in range(scol):
        for c in range(scol):
            if sb[r][c] == " ":
                sb[r][c] = 0
            elif sb[r][c] == "X":
                sb[r][c] = 1
            elif sb[r][c] == "O":
                sb[r][c] = 2
    return sb


def load_board(ln):
    """Δέχεται ως όρισμα το όνομα ενός αρχείου στο οποίο έχει αποθηκευτεί ένα ταμπλώ (απο προηγούμενο παιχνίδι) και το
        φορτώνει ώστε να περαστούν τα δεδομένα που έχουν καταγραφεί στο αρχείο σε ένα νεο πίνακα που θα λειτουργήσει
        ως το ταμπλώ του νέου παιχνιδιού.
        Σε αντίθεση με την save_board(), η load_board() μετατρέπει τα 0,1,2 σε " ","Χ","Ο".
    """

    with open(ln, newline="") as load_file:
        data = list(csv.reader(load_file))
    lb = [[" " for i in range(len(data))] for j in range(len(data))]
    for r in range(len(data)):
        for c in range(len(data)):
            if data[r][c] == "0":
                lb[r][c] = " "
            elif data[r][c] == "1":
                lb[r][c] = "X"
            elif data[r][c] == "2":
                lb[r][c] = "O"
    return lb


def start_game(b, col):
    """Δέχεται τον πίνακα που έχει δημιουργηθεί/φορτωθεί απο τον παίκτη (μέσω των συναρτήσεων create_board ή
        load_board() αντίστοιχα) και ξεκινάει την βασική επανάληψη του παιχνιδιού, επιτρέποντας στους 2 παίκτες να
        καταχωρήσουν τις κινήσεις τους (με χρήση των βοηθητικών συναρτήσεων check(), valid(), available_row(),
        move_register()), ελέγχοντας πριν γίνει η εναλλαγή των παικτών για την ύπαρξη νικητήριας τετράδας με χρήση της
        βοηθητικής συνάρτησης check_win().Σε περίπτωση που βρεθεί η νικητήρια τετράδα μετά απο καταχώρηση κίνησης
        κάποιου παίκτη, εκτυπώνεται αντίστοιχο μήνυμα και το πρόγραμμα τερματίζει.

        Αφού και οι 2 παίκτες καταχωρήσουν τις κινήσεις τους, δίνετε η επιλογή να αποθηκεύσουν την τρέχουσα κατάσταση
        του παιχνιδιού μέσω της save_board()
    """
    game_over = False
    turn_counter = 0
    turn = 1
    while (not game_over) and turn_counter < col ** 2:
        if turn == 1:
            print("Παίκτης 1: Επέλεξε στήλη για το πιόνι σου:", end="")
            selection = check(col)
            if valid(b, selection, col):
                row = available_row(b, selection, col)
                move_register(b, row, selection, "X")
                show_board(b, col)
                if check_win(b, col, "X"):
                    print("P1 wins!")
                    game_over = True
                    break
            else:
                print("Η στήλη είναι γεμάτη!")
                continue
            turn = 2
            turn_counter += 1
        else:
            print("Παίκτης 2: Επέλεξε στήλη για το πιόνι σου:", end="")
            selection = check(col)
            if valid(b, selection, col):
                row = available_row(b, selection, col)
                move_register(b, row, selection, "O")
                show_board(b, col)
                if check_win(b, col, "O"):
                    print("P2 wins!")
                    game_over = True
                    break
            else:
                print("Η στήλη είναι γεμάτη!")
                continue
            turn = 1
            turn_counter += 1
        if turn == 1:
            save_game = input("Παρακαλώ πατήστε 'S' για να σταματήσετε προσωρινά και να αποθηκεύσετε το παιχνίδι ή "
                              "οποιοδήποτε άλλο πλήκτρο για να συνεχίσετε:")
            if save_game == "S":
                b = save_board(b, col)
                save_file = open("save_state.txt", "w", newline="")
                with save_file:
                    write = csv.writer(save_file)
                    write.writerows(b)
                    print("Game saved!")
                    save_file.close()
                    break
            else:
                continue
        else:
            continue
    if turn_counter >= col ** 2 and (not game_over):
        print("It's a draw!")
    else:
        print("Exit...")


def main():
    print("Καλωσήλθατε στο παιχνίδι!")
    # [Έλεγχος εγκυρότητας για νέο παιχνίδι ή φόρτωση ήδη υπάρχοντος παιχνιδιού]
    answer = ""
    col = 0
    while True:
        answer = input("Επιθυμείτε νέο παιχνίδι (Ν) ή φόρτωση παιχνιδιού από αρχείο (S);")
        # [Δημιουργία νέου παιχνιδιού]
        if answer == "N":
            # [Έλεγχος εγκυρότητας για αριθμό στηλών νέου παιχνιδιού]
            while True:
                col = int(input("Δώστε αριθμό στηλών παιχνιδιού (5-10):"))
                if 5 <= col <= 10:
                    b = create_board(col)
                    show_board(b, col)
                    start_game(b, col)
                    break
                else:
                    print("Ο αριθμός που δώσατε είναι εκτός ορίων!")
                    continue
            break
        # [Φόρτωση παιχνιδιού απο αρχείο]
        elif answer == "S":
            load_name = input("Παρακαλώ πληκτρολογείστε όνομα αρχείου προς φόρτωση (ή διαδρομή στον δίσκο):")
            print("Loading from .csv file...")
            b = load_board(load_name)
            show_board(b, len(b))
            start_game(b, len(b))
            break
        else:
            print("Μη έγκυρη απάντηση! (N/S)")
            continue
    ex = input("Παρακαλώ πιέστε οποιοδήποτε πλήκτρο για να τερματίσει το παιχνίδι:")


if __name__ == "__main__":
    main()
