def extract_local_food(cpos=None, spd=None, *args, **kwargs):
    varargin = extract_local_food.varargin
    nargin = extract_local_food.nargin

    # Extracts array representing distribution of food available in the local
    # area of an agent at position cpos [x,y] and with search radius =spd.
    # This function also makes corrections in the case that the agent is close
    # to the model edge

    global ENV_DATA
    # ENV_DATA is a data structure containing information about the model
    # environment
    #    ENV_DATA.shape - shape of environment - FIXED AS SQUARE
    #    ENV_DATA.units - FIXED AS KM
    #    ENV_DATA.bm_size - length of environment edge in km
    #    ENV_DATA.food is  a bm_size x bm_size array containing distribution
    #    of food

    if cpos(1) > ENV_DATA.bm_size - spd:
        xmax = ENV_DATA.bm_size
    # extract_local_food.m:19
    else:
        xmax = cpos(1) + spd
    # extract_local_food.m:21

    if cpos(1) < spd + 1:
        xmin = 1
    # extract_local_food.m:24
    else:
        xmin = cpos(1) - spd
    # extract_local_food.m:26

    if cpos(2) > ENV_DATA.bm_size - spd:
        ymax = ENV_DATA.bm_size
    # extract_local_food.m:29
    else:
        ymax = cpos(2) + spd
    # extract_local_food.m:31

    if cpos(2) < spd + 1:
        ymin = 1
    # extract_local_food.m:34
    else:
        ymin = cpos(2) - spd
    # extract_local_food.m:36

    loc_food = ENV_DATA.food(arange(xmin, xmax), arange(ymin, ymax))


# extract_local_food.m:39
