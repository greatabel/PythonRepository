def create_agents(nr=None, ng=None, *args, **kwargs):
    varargin = create_agents.varargin
    nargin = create_agents.nargin

    # creates the objects representing each agent

    # agent - cell array containing list of objects representing agents
    # nr - number of red squirrels
    # ng - number of grey squirrels

    # global parameters
    # ENV_DATA - data structure representing the environment (initialised in
    # create_environment.m)
    # MESSAGES is a data structure containing information that agents need to
    # broadcast to each other
    # PARAM - structure containing values of all parameters governing agent
    # behaviour for the current simulation

    global ENV_DATA, MESSAGES, PARAM

    bm_size = ENV_DATA.bm_size
    # create_agents.m:19
    rloc = dot((bm_size - 1), rand(nr, 2)) + 1
    # create_agents.m:20

    gloc = dot((bm_size - 1), rand(ng, 2)) + 1
    # create_agents.m:21

    MESSAGES.pos = copy(concat([[rloc], [gloc]]))
    # create_agents.m:23
    # generate all red squirrel agents and record their positions in ENV_MAT_R
    for r in arange(1, nr).reshape(-1):
        pos = rloc(r, arange())
        # create_agents.m:27
        # food level 20
        age = ceil(dot(rand, 10))
        # create_agents.m:30
        food = 20
        # create_agents.m:32
        lbreed = round(dot(rand, PARAM.R_BRDFQ))
        # create_agents.m:33
        agent[r] = red_squirrel(age, food, pos, PARAM.S_SPD, lbreed)
    # create_agents.m:34

    # generate all grey squirrel agents and record their positions in ENV_MAT_F
    for f in arange(nr + 1, nr + ng).reshape(-1):
        pos = gloc(f - nr, arange())
        # create_agents.m:39
        # food level 30
        age = ceil(dot(rand, 10))
        # create_agents.m:42
        food = 30
        # create_agents.m:44
        lbreed = round(dot(rand, PARAM.G_BRDFQ))
        # create_agents.m:45
        agent[f] = grey_squirrel(age, food, pos, PARAM.S_SPD, lbreed)


# create_agents.m:46
