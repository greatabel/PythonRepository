WIDGET_WEIGHT = 75
GIZMOS_WEIGHT = 112
widgets = int(input("How many  widgets? "))
gizmos = int(input("How many  gizmos? "))
total = widgets * WIDGET_WEIGHT + gizmos * GIZMOS_WEIGHT

print(" total:$%.2f" % total)
# print("total = {0:.2f}".format(total))