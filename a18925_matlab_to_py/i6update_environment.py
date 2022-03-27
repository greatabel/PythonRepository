def update_environment(*args, **kwargs):
    varargin = update_environment.varargin
    nargin = update_environment.nargin

    # function that manipulates the global data structure representing
    # environmental information

    global ENV_DATA
    # add 1 timestep to the food's age
    ENV_DATA.food_age = copy(ENV_DATA.food_age + 1)
    # update_environment.m:8
    # make food of age 0 appear randomly in some of the empty cells
    # get cells with no food
    no_food = ENV_DATA.food < 1
    # update_environment.m:12
    # set food age to 0 in empty cells
    # rand_ages = randi(7, ENV_DATA.bm_size, ENV_DATA.bm_size)
    # ENV_DATA.food_age(no_food) = rand_ages(no_food);
    ENV_DATA.food_age[no_food] = 0
    # update_environment.m:17
    # add food to some of the empty cells
    ENV_DATA.food = copy(
        ENV_DATA.food
        + multiply(
            randsrc(ENV_DATA.bm_size, ENV_DATA.bm_size, concat([[0, 5], [0.7, 0.3]])),
            no_food,
        )
    )
    # update_environment.m:20
    return


if __name__ == "__main__":
    pass
