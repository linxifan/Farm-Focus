def handle_level(state, weather):
    level = state["level"]

    if level == 1:
        # 第一关：树长大
        state["day"] += 2 if weather == "rain" else 1
        if state["day"] >= 3:
            state["level"] = 2

    elif level == 2:
        # 第二关：开花
        state["flowers"] += 1
        if state["flowers"] >= 10:
            state["level"] = 3

    elif level == 3:
        # 第三关：结果
        state["fruits"] += 1
        if state["fruits"] >= 10:
            state["level"] = 4

    elif level == 4:
        # 第四关：摘果（消耗体力）
        if state["energy"] > 0:
            state["energy"] -= 1
        if state["energy"] == 0:
            state["level"] = 5

    elif level == 5:
        # 第五关：卖钱（等前端触发）
        pass

    return state