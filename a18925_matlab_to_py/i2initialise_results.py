def initialise_results(nr=None, ng=None, nsteps=None, *args, **kwargs):
    varargin = initialise_results.varargin
    nargin = initialise_results.nargin

    global IT_STATS, ENV_DATA

    # set up data structure to record statistics for each model iteration
    # IT_STATS  -  is data structure containing statistics on model at each
    # iteration (number of agents etc)
    # ENV_DATA - data structure representing the environment

    IT_STATS = struct(
        "div_red",
        concat([zeros(1, nsteps + 1)]),
        "div_grey",
        concat([zeros(1, nsteps + 1)]),
        "died_red",
        concat([zeros(1, nsteps + 1)]),
        "died_grey",
        concat([zeros(1, nsteps + 1)]),
        "eaten",
        concat([zeros(1, nsteps + 1)]),
        "mig",
        concat([zeros(1, nsteps + 1)]),
        "tot",
        concat([zeros(1, nsteps + 1)]),
        "tot_red",
        concat([zeros(1, nsteps + 1)]),
        "tot_grey",
        concat([zeros(1, nsteps + 1)]),
        "tfood",
        concat([zeros(1, nsteps + 1)]),
    )
    # initialise_results.m:10

    tf = sum(sum(ENV_DATA.food))
    # initialise_results.m:22

    IT_STATS.tot[1] = nr + ng
    # initialise_results.m:23
    IT_STATS.tot_red[1] = nr
    # initialise_results.m:24
    IT_STATS.tot_grey[1] = ng
    # initialise_results.m:25
    IT_STATS.tfood[1] = tf


# initialise_results.m:26
