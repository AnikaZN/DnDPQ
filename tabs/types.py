from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
## More Info on the Types

#### Actor:

Players who enjoy acting like getting into character and speaking in their
characters' voices. Roleplayers at heart, they enjoy social interactions with
NPCs, monsters, and their fellow party members.

#### Explorer:

Players who desire exploration want to experience the wonders that a fantasy
world has to offer. They want to know what's around the next corner or hill.
They also like to find hidden clues and treasure.

#### Instigator:

Players who like to instigate action are eager to make things happen, even if
that means taking perilous risks. They would rather rush headlong into danger
and face the consequences than face boredom.

#### Fighter:

Players who enjoy fantasy combat like kicking the tar out of villains and
monsters. They look for any excuse to start a fight, favoring bold action over
careful deliberation.

#### Optimizer:

Players who enjoy optimizing their characters' capabilities like to fine-tune
their characters for peak combat performance by gaining levels, new features,
and magic items. They welcome any opportunity to demonstrate their character's
superiority.

#### Problem-Solver:

Players who want to solve problems like to scrutinize NPC motivations, untangle
a villain's machinations, solve puzzles, and come up with plans.

#### Storyteller:

Players who love storytelling want to contribute to a narrative. They like it
when their characters are heavily invested in an unfolding story, and they
enjoy encounters that are tied to and expand an overarching plot.

""")]
