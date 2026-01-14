def sell_fruits(state):
    state["money"] += state["fruits"]
    state["fruits"] = 0
    return state