from axelrod.player import Player
from axelrod.action import Action
from axelrod.strategies import titfortat
C, D = Action.C, Action.D

class Truth(Player):
    name = "Truth"
    classifier = {
        "memory_depth": 3,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, starting_move=C):
        self.starting_move = starting_move
        super().__init__()

    def strategy(self, opponent: Player) -> Action:
        if not opponent.history or len(opponent.history) < 3:
            print("no history or short")
            return C
        else:
            try: 
                last_3_moves = opponent.history[-3:]
                k = 0
                for i in range(len(last_3_moves)):
                    if last_3_moves[i] == D or last_3_moves[i] == "D":
                        k += -i
                    else:
                        k += i
                if k >= 0:
                    #print(str(last_3_moves) + ": C")
                    return C
                else:
                    #print(str(last_3_moves) + ": D")
                    return D
            except Exception as e:
                #print(e)
                return C

