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
                
        if not self.history:
            return C
        else:
            try: 
                last_3_moves = self._history.cooperations[-3:]
                k = 0
                for i in len(last_3_moves):
                    if last_3_moves[i] == D:
                        k += -i
                    else:
                        k += i
                print(last_3_moves)
                if k >= 0:
                    return C
                else:
                    return D
            except Exception as e:
                print(self.history)
                return C

