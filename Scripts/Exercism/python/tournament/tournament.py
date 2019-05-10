def tally(tournament_results=None):
    # Input and split
    # Separation of each score

    if tournament_results:
        tournament_results = tournament_results.split("\n")
        result_list = []
        team_names = set()

        for score in tournament_results:
            score_as_a_list = score.split(";")
            for item in score_as_a_list[0:2]:
                # To obtain names of all teams without duplicates
                team_names.add(item)
            # List of scores [home team, away team, result]
            result_list.append(score.split(";"))

        # results keep as a dictionary, creation of the empty dictionary
        result_dict = {}
        for team in team_names:
            result_dict[str(team)] = {"win": 0,
                                      "loss": 0,
                                      "draw": 0,
                                      "matches": 0,
                                      "points": 0}
        # Processing the results

        for score in result_list:
            if score[2] == "win":
                result_dict[score[0]]["win"] += 1
                result_dict[score[1]]["loss"] += 1
            elif score[2] == "loss":
                result_dict[score[0]]["loss"] += 1
                result_dict[score[1]]["win"] += 1
            elif score[2] == "draw":
                result_dict[score[0]]["draw"] += 1
                result_dict[score[1]]["draw"] += 1

        for team in result_dict:
            result_dict[team]["matches"] = result_dict[team]["win"] + result_dict[team]["loss"]\
                                           + result_dict[team]["draw"]
            result_dict[team]["points"] = result_dict[team]["win"] * 3 + result_dict[team]["draw"]

        # Creation of "sorting_list" to sort teams by the result and name
        team_names = sorted(team_names)
        sorting_list = []
        for team in team_names:
            sorting_list.append([team, result_dict[team]["points"]])

        sorting_list.sort(key=lambda elem: elem[1], reverse=True)
        # Form of header of the table
        result = str('Team                           | MP |  W |  D |  L |  P\n')
        i = 0
        for team, _ in sorting_list:
            result += "{:31s}| {:3s}| {:3s}| {:3s}| {:3s}| {:2s}".format(team,
                                                                str(result_dict[team]["matches"]).center(3),
                                                                str(result_dict[team]["win"]).center(3),
                                                                str(result_dict[team]["draw"]).center(3),
                                                                str(result_dict[team]["loss"]).center(3),
                                                                str(result_dict[team]["points"]).rjust(2))
            i += 1
            if i < len(sorting_list):
                result += "\n"

        return result
    else:
        result = str('Team                           | MP |  W |  D |  L |  P')
        return result
