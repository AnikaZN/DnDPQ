# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

@app.callback(Output("prediction-content", "children"),
             [Input("one", "value"),
              Input("two", "value"),
              Input("three", "value"),
              Input("four", "value"),
              Input("five", "value"),
              Input("six", "value"),
              Input("seven", "value"),
              Input("eight", "value"),
              Input("nine", "value"),
              Input("ten", "value"),
              Input("eleven", "value"),
              Input("twelve", "value"),
              Input("thirteen", "value"),
              Input("fourteen", "value"),
              Input("fifteen", "value"),
              Input("sixteen", "value"),
              Input("seventeen", "value"),
              Input("eighteen", "value"),
              Input("nineteen", "value"),
              Input("twenty", "value"),
              Input("twentyone", "value"),
              Input("twentytwo", "value"),
              Input("twentythree", "value"),
              Input("twentyfour", "value"),
              Input("twentyfive", "value"),
              Input("twentysix", "value"),
              Input("twentyseven", "value"),
              Input("twentyeight", "value"),
              Input("twentynine", "value"),
              Input("thirty", "value"),
              Input("thirtyone", "value"),
              Input("thirtytwo", "value"),
              Input("thirtythree", "value"),
              Input("thirtyfour", "value"),
              Input("thirtyfive", "value"),
              Input("thirtysix", "value"),
              Input("thirtyseven", "value"),
              Input("thirtyeight", "value"),
              Input("thirtynine", "value"),
              Input("forty", "value"),
              Input("fortyone", "value"),
              Input("fortytwo", "value"),
              Input("fortythree", "value"),
              Input("fortyfour", "value"),
              Input("fortyfive", "value"),
              Input("fortysix", "value"),
              Input("fortyseven", "value"),
              Input("fortyeight", "value"),
              Input("fortynine", "value"),
              Input("fifty", "value"),
              Input("fiftyone", "value"),
              Input("fiftytwo", "value"),
              Input("fiftythree", "value"),
              Input("fiftyfour", "value"),
              Input("fiftyfive", "value"),
              Input("fiftysix", "value"),
              Input("fiftyseven", "value"),
              Input("fiftyeight", "value"),
              Input("fiftynine", "value"),
              Input("sixty", "value"),
                 ])
def predict(one, two, three, four, five, six, seven, eight, nine, ten, eleven,
            twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen,
            nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour,
            twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty,
            thirtyone, thirtytwo, thirtythree, thirtyfour, thirtyfive, thirtysix,
            thirtyseven, thirtyeight, thirtynine, forty, fortyone, fortytwo,
            fortythree, fortyfour, fortyfive, fortysix, fortyseven, fortyeight,
            fortynine, fifty, fiftyone, fiftytwo, fiftythree, fiftyfour, fiftyfive,
            fiftysix, fiftyseven, fiftyeight, fiftynine, sixty):
    values = [one, two, three, four, five, six, seven, eight, nine, ten, eleven,
              twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen,
              nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour,
              twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty,
              thirtyone, thirtytwo, thirtythree, thirtyfour, thirtyfive, thirtysix,
              thirtyseven, thirtyeight, thirtynine, forty, fortyone, fortytwo,
              fortythree, fortyfour, fortyfive, fortysix, fortyseven, fortyeight,
              fortynine, fifty, fiftyone, fiftytwo, fiftythree, fiftyfour, fiftyfive,
              fiftysix, fiftyseven, fiftyeight, fiftynine, sixty]
    actor = sum([value == 'acting' for value in values])
    explorer = sum([value == 'exploring' for value in values])
    instigator = sum([value == 'instigating' for value in values])
    fighter = sum([value == 'fighting' for value in values])
    optimizer = sum([value == 'optimizing' for value in values])
    solver = sum([value == 'problem solving' for value in values])
    storyteller = sum([value == 'storytelling' for value in values])
    ranks = {'Actor': actor, 'Explorer': explorer, 'Instigator': instigator,
             'Fighter': fighter, 'Optimizer': optimizer, 'Problem-Solver': solver,
             'Storyteller': storyteller}
    result = max(ranks, key=ranks.get)
    return f"Your type is: {result}! Here is the breakdown of all the possible types: {ranks}"

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Personality Test

            Answer the questions below to find out your RPG Player Personality! (Won't be accurate unless all questions are answered according to your preference.)

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown("## Questions", className="mb-5"),
        dcc.Markdown("#### Question 1: I prefer..."),
        dcc.RadioItems(
            id="one",
            options=[
                {"label": "Opportunities to develop my character's personality and background.", "value": "acting"},
                {"label": "Having steady access to new abilities and spells.", "value": "optimizing"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 2: I prefer..."),
        dcc.RadioItems(
            id="two",
            options=[
                {"label": "Unexpected combat encounters.", "value": "fighting"},
                {"label": "When my character's background helps shape the story of the campaign.", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 3: I prefer..."),
        dcc.RadioItems(
            id="three",
            options=[
                {"label": "Vivid descriptions of the havoc my character is wreaking in combat.", "value": "fighting"},
                {"label": "When magic items I want are rewards for adventuring.", "value": "optimizing"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 4: I prefer..."),
        dcc.RadioItems(
            id="four",
            options=[
                {"label": "Encounters that let my character shine.", "value": "optimizing"},
                {"label": "Encounters that advance the story in some way.", "value": "storytelling"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 5: I prefer..."),
        dcc.RadioItems(
            id="five",
            options=[
                {"label": "Combat encounters with large numbers of weak monsters.", "value": "fighting"},
                {"label": "Encounters that emphasize problem-solving.", "value": "problem solving"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 6: I prefer..."),
        dcc.RadioItems(
            id="six",
            options=[
                {"label": "When I receive quantifiable rewards, like experience points, for noncombat encounters.", "value": "optimizing"},
                {"label": "When I get in-game benefits for planning and strategy.", "value": "problem solving"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 7: I prefer..."),
        dcc.RadioItems(
            id="seven",
            options=[
                {"label": "Encounters with NPCs who are as feisty and unpredictable as my character is.", "value": "instigating"},
                {"label": "Skipping the talking and diving straight into combat.", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 8: I prefer..."),
        dcc.RadioItems(
            id="eight",
            options=[
                {"label": "Interacting regularly with NPCs.", "value": "acting"},
                {"label": "Hints and clues about things yet to come.", "value": "exploring"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 9: I prefer..."),
        dcc.RadioItems(
            id="nine",
            options=[
                {"label": "Combat encounters that include roleplay elements.", "value": "acting"},
                {"label": "Creating characters who are the best at what they do.", "value": "optimizing"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 10: I prefer..."),
        dcc.RadioItems(
            id="ten",
            options=[
                {"label": "When there are lots of opportunities to pick fights with NPCs.", "value": "instigating"},
                {"label": "When social interaction and exploration is interrupted with combat.", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 11: I prefer..."),
        dcc.RadioItems(
            id="eleven",
            options=[
                {"label": "When my actions affect my surroundings.", "value": "instigating"},
                {"label": "Lots of opportunities to put my broad range of abilities to use.", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 12: I prefer..."),
        dcc.RadioItems(
            id="twelve",
            options=[
                {"label": "When my actions gets me into a sticky situation.", "value": "instigating"},
                {"label": "When a smart plan sometimes gets me an easy win.", "value": "problem solving"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 13: I prefer..."),
        dcc.RadioItems(
            id="thirteen",
            options=[
                {"label": "Exploring an area and finding things.", "value": "exploring"},
                {"label": "When my character's actions help steer future events.", "value": "storytelling"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 14: I prefer..."),
        dcc.RadioItems(
            id="fourteen",
            options=[
                {"label": "Unexpected combat encounters.", "value": "fighting"},
                {"label": "Interacting with NPCs with complex motives.", "value": "problem solving"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 15: I prefer..."),
        dcc.RadioItems(
            id="fifteen",
            options=[
                {"label": "Rich descriptions of exciting environments with interesting maps and props.", "value": "exploring"},
                {"label": "Exercising my power every opportunity I have - it's not often you get to use a sword or magic!", "value": "fighting"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 16: I prefer..."),
        dcc.RadioItems(
            id="sixteen",
            options=[
                {"label": "When elements from my character's background make an appearance in the campaign.", "value": "acting"},
                {"label": "Monsters that have secrets to uncover or cultural details to learn.", "value": "exploring"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 17: I prefer..."),
        dcc.RadioItems(
            id="seventeen",
            options=[
                {"label": "Big, intense, combat-focused sessions against a final boss.", "value": "fighting"},
                {"label": "When NPCs have ideals, bonds, and flaws that I can exploit.", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 18: I prefer..."),
        dcc.RadioItems(
            id="eighteen",
            options=[
                {"label": "Encounters that emphasize problem-solving.", "value": "problem solving"},
                {"label": "When my character has clearly had an impact on the world.", "value": "storytelling"},
            ],
            value="problem solving"
        ),
        dcc.Markdown("#### Question 19: I prefer..."),
        dcc.RadioItems(
            id="nineteen",
            options=[
                {"label": "When I can get really deeply into character.", "value": "acting"},
                {"label": "Causing trouble everywhere I go.", "value": "instigating"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 20: I prefer..."),
        dcc.RadioItems(
            id="twenty",
            options=[
                {"label": "Spending lots of time learning about the areas I visit.", "value": "exploring"},
                {"label": "Narrative moments in combat where die rolls don't really matter.", "value": "storytelling"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 21: I prefer..."),
        dcc.RadioItems(
            id="twentyone",
            options=[
                {"label": "Making my mark in the world - good or bad.", "value": "instigating"},
                {"label": "When items seem to be made for my character, not just random.", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 22: I prefer..."),
        dcc.RadioItems(
            id="twentytwo",
            options=[
                {"label": "Causing trouble everywhere I go.", "value": "instigating"},
                {"label": "Navigating tricky social situations successfully.", "value": "problem solving"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 23: I prefer..."),
        dcc.RadioItems(
            id="twentythree",
            options=[
                {"label": "A world that rewards my character's adventurousness rather than punishing it.", "value": "instigating"},
                {"label": "Combat that suits my playstyle.", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 24: I prefer..."),
        dcc.RadioItems(
            id="twentyfour",
            options=[
                {"label": "Fair consequences for my actions.", "value": "instigating"},
                {"label": "When I'm rewarded for progressing or completing a story arc.", "value": "storytelling"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 25: I prefer..."),
        dcc.RadioItems(
            id="twentyfive",
            options=[
                {"label": "Vivid descriptions of the havoc my character is wreaking in combat.", "value": "fighting"},
                {"label": "When adventures always connect to a core plot.", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 26: I prefer..."),
        dcc.RadioItems(
            id="twentysix",
            options=[
                {"label": "Encounters that push or challenge my character's morals and ethics.", "value": "acting"},
                {"label": "In-game puzzles that test my real-life skills.", "value": "problem solving"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 27: I prefer..."),
        dcc.RadioItems(
            id="twentyseven",
            options=[
                {"label": "Fostering relationships with other characters.", "value": "acting"},
                {"label": "When my character's background helps shape the story of the campaign.", "value": "storytelling"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 28: I prefer..."),
        dcc.RadioItems(
            id="twentyeight",
            options=[
                {"label": "Revisiting familiar places and familiar NPCs.", "value": "exploring"},
                {"label": "A steady flow of new and fresh challenges.", "value": "optimizing"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 29: I prefer..."),
        dcc.RadioItems(
            id="twentynine",
            options=[
                {"label": "When my actions affect my surroundings.", "value": "instigating"},
                {"label": "Having steady access to new abilities and spells.", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 30: I prefer..."),
        dcc.RadioItems(
            id="thirty",
            options=[
                {"label": "Small-scale adventures that help me learn more about the minutiae of the world.", "value": "exploring"},
                {"label": "Combat encounters with large numbers of weak monsters.", "value": "fighting"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 31: I prefer..."),
        dcc.RadioItems(
            id="thirtyone",
            options=[
                {"label": "When there are lots of opportunities to pick fights with NPCs.", "value": "instigating"},
                {"label": "Encounters that advance the story in some way.", "value": "storytelling"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 32: I prefer..."),
        dcc.RadioItems(
            id="thirtytwo",
            options=[
                {"label": "When social interaction and exploration is interrupted with combat.", "value": "fighting"},
                {"label": "When magic items I want are rewards for adventuring.", "value": "optimizing"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 33: I prefer..."),
        dcc.RadioItems(
            id="thirtythree",
            options=[
                {"label": "Getting information like flyers and pamphlets in real life as I explore the in-game world.", "value": "exploring"},
                {"label": "Unexpected combat encounters.", "value": "fighting"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 34: I prefer..."),
        dcc.RadioItems(
            id="thirtyfour",
            options=[
                {"label": "Hints and clues about things yet to come.", "value": "exploring"},
                {"label": "When my actions get me into a sticky situation.", "value": "instigating"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 35: I prefer..."),
        dcc.RadioItems(
            id="thirtyfive",
            options=[
                {"label": "When my roleplaying has an impact on the world.", "value": "acting"},
                {"label": "Skipping the talking and diving straight into combat.", "value": "fighting"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 36: I prefer..."),
        dcc.RadioItems(
            id="thirtysix",
            options=[
                {"label": "Opportunities to develop my character's personality and background.", "value": "acting"},
                {"label": "Exercising my power every opportunity I have - it's not often you get to use a sword or magic!", "value": "fighting"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 37: I prefer..."),
        dcc.RadioItems(
            id="thirtyseven",
            options=[
                {"label": "Big, intense, combat-focused sessions against a final boss.", "value": "fighting"},
                {"label": "Encounters that let my character shine.", "value": "optimizing"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 38: I prefer..."),
        dcc.RadioItems(
            id="thirtyeight",
            options=[
                {"label": "Exploring an area and finding things.", "value": "exploring"},
                {"label": "Encounters with NPCs who are as feisty and unpredictable as my character is.", "value": "instigating"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 39: I prefer..."),
        dcc.RadioItems(
            id="thirtynine",
            options=[
                {"label": "Rich descriptions of exciting environments with interesting maps and props.", "value": "exploring"},
                {"label": "Pulling off a sneaky maneuver that gets me out of combat.", "value": "problem solving"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 40: I prefer..."),
        dcc.RadioItems(
            id="forty",
            options=[
                {"label": "Interacting regularly with NPCs.", "value": "acting"},
                {"label": "Making my mark in the world - good or bad.", "value": "instigating"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 41: I prefer..."),
        dcc.RadioItems(
            id="fortyone",
            options=[
                {"label": "A world that rewards my character's adventurousness rather than punishing it.", "value": "instigating"},
                {"label": "When my character's actions help steer future events.", "value": "storytelling"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 42: I prefer..."),
        dcc.RadioItems(
            id="fortytwo",
            options=[
                {"label": "When I receive quantifiable rewards, like experience points, for noncombat encounters.", "value": "optimizing"},
                {"label": "When NPCs have ideals, bonds, and flaws that I can exploit.", "value": "storytelling"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 43: I prefer..."),
        dcc.RadioItems(
            id="fortythree",
            options=[
                {"label": "Combat encounters that include roleplay elements.", "value": "acting"},
                {"label": "When my character has clearly had an impact on the world.", "value": "storytelling"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 44: I prefer..."),
        dcc.RadioItems(
            id="fortyfour",
            options=[
                {"label": "Creating characters who are the best at what they do.", "value": "optimizing"},
                {"label": "Obstacles that have multiple possible solutions.", "value": "problem solving"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 45: I prefer..."),
        dcc.RadioItems(
            id="fortyfive",
            options=[
                {"label": "Monsters that have secrets to uncover or cultural details to learn.", "value": "exploring"},
                {"label": "Fair consequences for my actions.", "value": "instigating"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 46: I prefer..."),
        dcc.RadioItems(
            id="fortysix",
            options=[
                {"label": "When elements from my character's background make an appearance in the campaign.", "value": "acting"},
                {"label": "When my actions affect my surroundings.", "value": "instigating"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 47: I prefer..."),
        dcc.RadioItems(
            id="fortyseven",
            options=[
                {"label": "Spending lots of time learning about the areas I visit.", "value": "exploring"},
                {"label": "Lots of opportunities to put my broad range of abilities to use.", "value": "optimizing"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 48: I prefer..."),
        dcc.RadioItems(
            id="fortyeight",
            options=[
                {"label": "When I get in-game benefits for planning and strategy.", "value": "problem solving"},
                {"label": "Narrative moments in combat where die rolls don't really matter.", "value": "storytelling"},
            ],
            value="problem solving"
        ),
        dcc.Markdown("#### Question 49: I prefer..."),
        dcc.RadioItems(
            id="fortynine",
            options=[
                {"label": "When there are lots of opportunities to pick fights with NPCs.", "value": "instigating"},
                {"label": "When a smart plan sometimes gets me an easy win.", "value": "problem solving"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 50: I prefer..."),
        dcc.RadioItems(
            id="fifty",
            options=[
                {"label": "Revisiting familiar places and familiar NPCs.", "value": "exploring"},
                {"label": "When items seem to be made for my character, not just random.", "value": "optimizing"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 51: I prefer..."),
        dcc.RadioItems(
            id="fiftyone",
            options=[
                {"label": "When I can get really deeply into character.", "value": "acting"},
                {"label": "A steady flow of new and fresh challenges.", "value": "optimizing"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 52: I prefer..."),
        dcc.RadioItems(
            id="fiftytwo",
            options=[
                {"label": "Interacting with NPCs with complex motives.", "value": "problem solving"},
                {"label": "When I'm rewarded for progressing or completing a story arc.", "value": "storytelling"},
            ],
            value="problem solving"
        ),
        dcc.Markdown("#### Question 53: I prefer..."),
        dcc.RadioItems(
            id="fiftythree",
            options=[
                {"label": "Encounters that push or challenge my character's morals and ethics.", "value": "acting"},
                {"label": "Encounters that emphasize problem-solving.", "value": "problem solving"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 54: I prefer..."),
        dcc.RadioItems(
            id="fiftyfour",
            options=[
                {"label": "Small-scale adventures that help me learn more about the minutiae of the world.", "value": "exploring"},
                {"label": "In-game puzzles that test my real-life skills.", "value": "problem solving"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 55: I prefer..."),
        dcc.RadioItems(
            id="fiftyfive",
            options=[
                {"label": "Fostering relationships with other characters.", "value": "acting"},
                {"label": "When adventures always connect to a core plot.", "value": "storytelling"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 56: I prefer..."),
        dcc.RadioItems(
            id="fiftysix",
            options=[
                {"label": "When my roleplaying has an impact on the world.", "value": "acting"},
                {"label": "Pulling off a sneaky maneuver that gets me out of combat.", "value": "problem solving"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 57: I prefer..."),
        dcc.RadioItems(
            id="fiftyseven",
            options=[
                {"label": "Opportunities to develop my character's personality and background.", "value": "acting"},
                {"label": "Getting information like flyers and pamphlets in real life as I explore the in-game world.", "value": "exploring"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 58: I prefer..."),
        dcc.RadioItems(
            id="fiftyeight",
            options=[
                {"label": "Having steady access to new abilities and spells.", "value": "optimizing"},
                {"label": "When my character's background helps shape the story of the campaign.", "value": "storytelling"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 59: I prefer..."),
        dcc.RadioItems(
            id="fiftynine",
            options=[
                {"label": "When magic items I want are rewards for adventuring.", "value": "optimizing"},
                {"label": "Navigating tricky social situations successfully.", "value": "problem solving"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 60: I prefer..."),
        dcc.RadioItems(
            id="sixty",
            options=[
                {"label": "Hints and clues about things yet to come.", "value": "exploring"},
                {"label": "Obstacles that have multiple possible solutions.", "value": "problem solving"},
            ],
            value="exploring"
        ),
        html.H2("RPG Player Personality", className="mb-5"),
        html.Div(id="prediction-content", className="lead")
    ],
)

layout = dbc.Row([column1, column2])
