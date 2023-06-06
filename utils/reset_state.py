def reset_state(states):
    for key in states:
        if key == "gender_movie":
            states[key]["state"] = 0
            continue

        states[key] = 0
