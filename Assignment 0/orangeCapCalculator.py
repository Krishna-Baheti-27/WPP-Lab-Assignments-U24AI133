def orange_cap(scores):
    total_scores = {}
    
    for test, players in scores.items():
        for player, runs in players.items():
            total_scores[player] = total_scores.get(player, 0) + runs

    max_scorer = max(total_scores, key=total_scores.get)
    return max_scorer, total_scores[max_scorer]

scores = {
    'test1': {'Dhoni': 74, 'kohil': 150},
    'test2': {'Dhoni': 29, 'Sachin': 143}
}

winner, max_runs = orange_cap(scores)
print(f"The Orange Cap winner is {winner} with {max_runs} runs.")
