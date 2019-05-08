def game_manager(info_list):
    dictionary = {}
    for piece_info in info_list:
        piece_info = piece_info.split('||')
        piece_info[2] = int(piece_info[2])
        if piece_info[2] not in dictionary:
            dictionary[piece_info[2]] = {(piece_info[1],piece_info[0])}
        dictionary[piece_info[2]].add((piece_info[1],piece_info[0]))
    print(dictionary)


info = ['Final Fantasy VII||SCEA||1997','Mirror’s Edge||Electronic Arts||2008','GTA 4||Rockstar Games||2008','Grandia||SCEA||1997', \
'Half Life 2||Valve||2004']

game_manager(info)
