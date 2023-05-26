from myANN import ANN
import axelrod_dojo as dojo
import axelrod as axl



player_ann = ANN
objective = dojo.prepare_objective(name="score", turns=10, repetitions=1)
opponents = [axl.TitForTat(), axl.Alternator(), axl.Defector()]

params_ann = {"num_features":17, "num_hidden": 10}

population = dojo.Population(   player_class=player_ann,
                                params_kwargs=params_ann,
                                size=20,
                                objective=objective,
                                output_filename="training_output.csv",
                                opponents=opponents,

                            )

generations = 50
population.run(generations)



