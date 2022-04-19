def update_messages(agent=None, prev_n=None, temp_n=None, *args, **kwargs):
    varargin = update_messages.varargin
    nargin = update_messages.nargin

    # copy all surviving and new agents in to a new agent list - dead agents
    # will be empty structures

    # agent - list of existing agents, including those that have died in the
    # current iteration
    # prev_n - previous number of agents at the start of this iteration
    # temp_n - number of existing agents, including those that have died in the
    # current iteration
    # nagent - list of surviving agents and empty structures
    # nn - number of surviving agents

    # global variables
    # N_IT current iteration no
    # IT_STATS data structure for saving model statistics
    # MESSAGES is a data structure containing information that agents need to
    # broadcast to each other
    #    MESSAGES.atype - n x 1 array listing the type of each agent in the model
    #    (1=red squirrel, 2-grey squirrel, 3=dead agent)
    #    MESSAGES.pos - list of every agent position in [x y]
    #    MESSAGE.dead - n x1 array containing ones for agents that have died
    #    in the current iteration
    # ENV_DATA - is a data structure containing information about the model
    # environment

    global MESSAGES, IT_STATS, N_IT, ENV_DATA
    nagent = cell(1, temp_n)
    # update_messages.m:29

    nn = 0
    # update_messages.m:30

    for cn in arange(1, temp_n).reshape(-1):
        if isempty(agent[cn]):
            dead = 1
        # update_messages.m:33
        else:
            if cn <= prev_n:
                dead = MESSAGES.dead(cn)
            # update_messages.m:35
            else:
                dead = 0
        # update_messages.m:37
        if dead == 0:
            nagent[cn] = agent[cn]
            # update_messages.m:40
            pos = get(agent[cn], "pos")
            # update_messages.m:41
            MESSAGES.pos[cn, arange()] = pos
            # update_messages.m:42
            if isa(agent[cn], "red_squirrel"):
                MESSAGES.atype[cn] = 1
                # update_messages.m:44
                IT_STATS.tot_red[N_IT + 1] = IT_STATS.tot_red(N_IT + 1) + 1
            # update_messages.m:45
            else:
                if isa(agent[cn], "grey_squirrel"):
                    MESSAGES.atype[cn] = 2
                    # update_messages.m:47
                    IT_STATS.tot_grey[N_IT + 1] = IT_STATS.tot_grey(N_IT + 1) + 1
            # update_messages.m:48
            MESSAGES.dead[cn] = 0
            # update_messages.m:50
            nn = nn + 1
        # update_messages.m:51
        else:
            MESSAGES.pos[cn, arange()] = concat([-1, -1])
            # update_messages.m:53
            MESSAGES.atype[cn] = 0
            # update_messages.m:54
            MESSAGES.dead[cn] = 0
    # update_messages.m:55

    IT_STATS.tot[N_IT + 1] = nn
    # update_messages.m:58

    IT_STATS.tfood[N_IT + 1] = sum(sum(ENV_DATA.food))


# update_messages.m:59
