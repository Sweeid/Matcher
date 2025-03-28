import json


def parse_matches(input_data):
    # Split the input into lines
    lines = input_data.strip().split('\n')

    # Extract headers
    headers = [h.strip() for h in lines[0].split('\t')]
    mat_headers = headers[2:]  # Matta 1, Matta 2, etc.

    # Initialize the result dictionary
    result = {}

    # Process each match
    for line in lines[1:]:
        parts = [p.strip() for p in line.split('\t')]
        match_num = int(parts[0])
        time = parts[1]

        # Process each mat
        for i, match in enumerate(parts[2:]):
            mat = mat_headers[i]
            if ' vs ' in match:
                player1, player2 = match.split(' vs ')

                # Add entry for player1
                if player1 not in result:
                    result[player1] = []
                result[player1].append({
                    'match': match_num,
                    'time': time,
                    'opponent': player2,
                    'mat': mat
                })

                # Add entry for player2
                if player2 not in result:
                    result[player2] = []
                result[player2].append({
                    'match': match_num,
                    'time': time,
                    'opponent': player1,
                    'mat': mat
                })

    return result


# Example input data (you would load this from a file in practice)
input_data = """Match #	Tid	Matta 1	Matta 2	Matta 3	Matta 4	Matta 5
1	12:00	Anna vs Björn	Emil vs Frida	Jonas vs Karin	Peter vs Quinna	Xander vs Ylva
2	12:04	Clara vs David	Gustav vs Helena	Ludvig vs Maja	Rasmus vs Simon	Zacharias vs Alice
3	12:08	Anna vs Clara	Frida vs Isak	Jonas vs Ludvig	Peter vs Rasmus	Bella vs Ylva
4	12:12	Björn vs David	Emil vs Gustav	Karin vs Maja	Quinna vs Simon	Xander vs Alice
5	12:16	Anna vs David	Frida vs Helena	Ludvig vs Noah	Peter vs Viktor	Zacharias vs Bella
6	12:20	Clara vs Björn	Gustav vs Isak	Maja vs Olivia	Rasmus vs Ulla	Alice vs Zacharias
7	12:24	Anna vs Clara	Emil vs Frida	Jonas vs Maja	Peter vs Viktor	Ylva vs Xander
8	12:28	Björn vs David	Gustav vs Helena	Ludvig vs Noah	Quinna vs Simon	Bella vs Alice
9	12:32	Anna vs Björn	Frida vs Isak	Karin vs Olivia	Peter vs Rasmus	Zacharias vs Ylva
10	12:36	Clara vs David	Gustav vs Helena	Maja vs Jonas	Viktor vs Ulla	Xander vs Bella
11	12:40	Anna vs Clara	Emil vs Frida	Ludvig vs Olivia	Rasmus vs Simon	Alice vs Ylva
12	12:44	Björn vs David	Gustav vs Isak	Karin vs Maja	Peter vs Viktor	Zacharias vs Bella
13	12:48	Anna vs Björn	Frida vs Helena	Jonas vs Ludvig	Quinna vs Ulla	Alice vs Zacharias
14	12:52	Clara vs David	Emil vs Gustav	Maja vs Noah	Peter vs Rasmus	Xander vs Ylva
15	12:56	Anna vs Clara	Frida vs Isak	Ludvig vs Maja	Viktor vs Simon	Bella vs Alice
16	13:00	Björn vs David	Gustav vs Helena	Karin vs Olivia	Peter vs Quinna	Zacharias vs Ylva
17	13:04	Anna vs Björn	Frida vs Isak	Jonas vs Maja	Rasmus vs Simon	Xander vs Bella
18	13:08	Clara vs David	Gustav vs Helena	Ludvig vs Noah	Peter vs Viktor	Alice vs Zacharias
19	13:12	Anna vs Clara	Frida vs Isak	Karin vs Maja	Quinna vs Ulla	Ylva vs Zacharias
20	13:16	Björn vs David	Gustav vs Isak	Maja vs Olivia	Peter vs Simon	Alice vs Bella
21	13:20	Anna vs Björn	Emil vs Frida	Ludvig vs Maja	Rasmus vs Viktor	Xander vs Zacharias
22	13:24	Clara vs David	Gustav vs Helena	Karin vs Noah	Quinna vs Ulla	Bella vs Alice
23	13:28	Anna vs Clara	Frida vs Isak	Jonas vs Ludvig	Peter vs Rasmus	Ylva vs Zacharias
24	13:32	Björn vs David	Gustav vs Helena	Maja vs Olivia	Rasmus vs Simon	Xander vs Bella
25	13:36	Anna vs Björn	Emil vs Frida	Ludvig vs Maja	Peter vs Viktor	Alice vs Ylva
26	13:40	Clara vs David	Gustav vs Isak	Jonas vs Olivia	Quinna vs Ulla	Zacharias vs Bella
27	13:44	Anna vs Clara	Frida vs Isak	Karin vs Maja	Peter vs Simon	Alice vs Ylva
28	13:48	Björn vs David	Gustav vs Helena	Ludvig vs Noah	Rasmus vs Ulla	Zacharias vs Xander
29	13:52	Anna vs Björn	Frida vs Isak	Maja vs Olivia	Peter vs Viktor	Alice vs Bella
30	13:56	Clara vs David	Gustav vs Helena	Jonas vs Ludvig	Quinna vs Rasmus	Bella vs Ylva"""

# Parse the matches
result = parse_matches(input_data)

# Convert to JSON and print with pretty formatting
json_output = json.dumps(result, indent=4, ensure_ascii=False)
print(json_output)

# If you want to save to a file:
# with open('matches.json', 'w', encoding='utf-8') as f:
#     f.write(json_output)