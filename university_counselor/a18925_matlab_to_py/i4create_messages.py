def create_messages(nr=None, ng=None, agent=None, *args, **kwargs):
    varargin = create_messages.varargin
    nargin = create_messages.nargin

    # function that populates the global data structure representing
    # message information

    # MESSAGES is a data structure containing information that agents need to
    # broadcast to each other
    #    MESSAGES.atype - n x 1 array listing the type of each agent in the model
    #    (1=red squirrel, 2-grey squirrel, 3=dead agent)
    #    MESSAGES.pos - list of every agent position in [x y]
    #    MESSAGE.dead - n x1 array containing ones for agents that have died
    #    in the current iteration

    global MESSAGES

    for an in arange(1, length(agent)).reshape(-1):
        if isa(agent[an], "red_squirrel"):
            MESSAGES.atype[an] = 1
            # create_messages.m:18
            MESSAGES.pos[an, arange()] = get(agent[an], "pos")
        # create_messages.m:19
        else:
            if isa(agent[an], "grey_squirrel"):
                MESSAGES.atype[an] = 2
                # create_messages.m:21
                MESSAGES.pos[an, arange()] = get(agent[an], "pos")
            # create_messages.m:22
            else:
                MESSAGES.atype[an] = 0
                # create_messages.m:24
                MESSAGES.pos[an, arange()] = concat([-1, -1])
        # create_messages.m:25
        MESSAGES.dead[an] = 0


# create_messages.m:27
