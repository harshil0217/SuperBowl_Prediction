def HA_helper(x, stat_col, status_col):
    if (x[status_col] == "away"):
        if "_away" in x[stat_col]:
            return True
    else:
        if "_home" in x[stat_col]:
            return True
    return False


def filter_home_away_stats(data):
    include = data.apply(lambda x: HA_helper(x, "stat", "status"), axis = 1)
    data = data[include]
    return data


def ignore_helper(x, stat_col):
    name = x[stat_col]
    if "_away" in name:
        name = name[:name.index("_away")]
    else:
        name = name[:name.index("_home")]
    x[stat_col] = name
    return x


def ignore_home_away(data):
    data = data.apply(lambda x: ignore_helper(x, "stat"), axis = 1)
    return data


