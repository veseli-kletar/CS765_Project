import axelrod as axl
import axelrod_dojo as dojo

# Initialize an EvolvableANN player

player_evolvable = axl.EvolvableANN
player_ann = axl.ANN

opponents = [axl.TitForTat(), axl.Alternator(), axl.Defector()]
objective = dojo.prepare_objective(name="score", turns=10, repetitions=1)

params_kwargs = {"seed":11, "num_features": 17, "num_hidden": 1, "mutation_probability": 0.1, "mutation_distance": 5}

params_ann5 = {"num_features":17, "num_hidden": 5}

params_ann = {"num_features":17, "num_hidden": 10}

population = dojo.Population(   player_class=player_evolvable,
                                params_kwargs=params_ann,
                                size=20,
                                objective=objective,
                                output_filename="training_output.csv",
                                opponents=opponents,

                            )

generations = 50
population.run(generations)