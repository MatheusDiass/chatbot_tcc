def reset_state(states):
    for key in states:
        if key == "gender_movie":
            states[key]["state"] = False
            continue

        if key == "platform_movie":
            states[key]["state"] = False
            continue

        states[key] = 0
