from day2_1 import input_parser, get_df_from_parsed

# input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open('input_day2_1.txt') as fp:
    input = fp.read()

parsed = input_parser(input)
df = get_df_from_parsed(parsed)

min_colors_needed = df.groupby('game_id').max()
power = min_colors_needed['red'] * min_colors_needed['green'] * min_colors_needed['blue']
print(power.sum())