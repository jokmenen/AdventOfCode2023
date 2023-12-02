input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open('input_day2_1.txt') as fp:
    input = fp.read()

possible = {
    'red' : 12,
    'green' : 13,
    'blue' :14
}

#input has games, game has turns, turn has colours
def input_parser(input_string):
    ' returns dict containing { id : [turn1, turn2, ...]}'
    game_dict = {}
    i = 0
    for line in input_string.split('\n'):
        if ':' not in line:
            print("Warning: No : found in line", line)
            print('Skipping....')
            continue

        game_nr, game_info = line.split(':')
        game_id = int(game_nr.split(' ')[1])
        turns = game_info.split(';')
        turn_dict = {}

        for i, turn in enumerate(turns):
            color_split = turn.split(',')
            color_set_dict = {}

            for color_set in color_split:
                # print(color_set)
                value, color = color_set.lstrip().split(' ')
                color_set_dict[color] = int(value)

            turn_dict[i] = color_set_dict

        game_dict[game_id] = turn_dict        
    

    return game_dict

parsed = input_parser(input)

# Without pandas
# impossible_dict = {}
# for game_id, game_info in parsed.items():
#     # check if this game has any turns that are impossible
#     for turn_id, turn_info in game_info.items():
#         impossible_color_found = False

#         for color, value in turn_info.items():
#             # print(color,value)
#             if possible[color] < value:
#                 impossible_color_found = True
#                 break

#         if impossible_color_found == True:
#             print(f'impossible color found in game {game_id}, turn {turn_id}: {turn_info}')
#             impossible_dict[game_id] = True
#             break #make sure it breaks to prevent it from being set to true first
#         else:
#             if game_id in impossible_dict:
#                 assert impossible_dict[game_id] != True
#             impossible_dict[game_id] = False


# print(impossible_dict)

# print(sum([id for id, impossible in impossible_dict.items() if impossible == False]))


#with pandas:
import pandas as pd

df_list = []
for game_id, game_info in parsed.items():
    for turn_id, turn_info in game_info.items():
        print(turn_info)
        red = turn_info.get('red',0)
        green = turn_info.get('green',0)
        blue = turn_info.get('blue',0)
        df_list += [[game_id, turn_id, red, green, blue]]

        


print(df_list)

df = pd.DataFrame(df_list, columns = ['game_id', 'turn_id','red','green', 'blue'])

max_colors_per_game = df.groupby('game_id').max()


possible_games = max_colors_per_game[((max_colors_per_game['red'] <= possible['red']) &\
                                       (max_colors_per_game['green'] <= possible['green']) &\
                                          (max_colors_per_game['blue'] <= possible['blue']))]

print(sum(possible_games.index.tolist()))
