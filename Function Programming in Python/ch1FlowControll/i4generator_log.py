import random 


def complex_condition(line):
    return random.choice([True, False])

# --------------------------------
huge_log_file = 'logfile.txt'


fh = open(huge_log_file, 'rt')
log_lines = (line for line in fh.readlines()
                  if complex_condition(line))


for logline in log_lines:
    print(logline)

fh.close()