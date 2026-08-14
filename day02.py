for x in range(5):
    for y in range(5):
       if x in [0,4] and y in [0,4]: pydle(x, y, "", "blue")
       if x in [0,4] and y in [1,2,3]:pydle(x, y, "", "orange")
       if x in [1,2,3] and y in [0,4]:pydle(x, y, "", "orange")
       if x in [1,3] and y in [1,3]:pydle(x, y, "", "yellow")
