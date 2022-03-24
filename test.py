bitch = {
                "Start": True,
            "Rules": False,
            "Exit": False
}
if not bitch["Exit"]:
    for i in list(bitch):
        if bitch[i]:
           x = str(list(bitch)[list(bitch).index(i) + 1])
           bitch |= {i:False}
           print(type(x))
           if x == 'Rules':
               print('a')