# Game of Greed 3

For _Game of Greed 3_ we'll be handing cheaters and losers. In other words, people who entered dice they didn't actually roll and people who gambled and lost.

#### Describe and Define

- Validating user input
- Edge cases in game rules
- Assess game improvements

#### Execute

- Block invalid dice
- Continue rolling when all dice scored in current turn
- End turn when there's a _zilch_

## Today's Outline

- Challenge Review
- Challenge Preview
- Lab Review
- Lab Preview
- Guided Research
- Demo

## Notes 

# What is a regression?
When new code changes breaks an existing feature. We can detect this by running all of our existing test cases and checking if our new code causes our existing tests to fail. This only works if you have existing tests and your tests are up to date with your feature requirements.

## User Story e.g.

As a player I would like a input validator so that when I enter invalid input I get a chance to correct it.

Format:
As a <type of user> I would like <feature> so that <benefit>


## Acceptance Criteria
If the user can input invalid input and have the chance to correct it.

### Gherkin Format

GIVEN <some initial state / condition is met>
WHEN <some action is taken>
THEN <some outcome / state change is achieved>

GIVEN the user is prompted to enter which dice to keep
WHEN then user enters a valid list of dice to keep
THEN the user sees their unbanked points and the game continues

GIVEN the user is prompted with a roll of *** 5 2 3 5 4 2 *** and asked to enter which dice to keep
WHEN then user enters 55
THEN the user sees their unbanked points and the game continues

GIVEN the user is prompted with a roll of *** 5 2 3 5 4 2 *** and asked to enter which dice to keep
WHEN then user enters 555
THEN the user sees 
"Cheater!!! Or possibly made a typo...
*** 5 2 3 5 4 2 ***
Enter dice to keep, or (q)uit:"
as is given the opportunity to correct it.

## Non-Functional Requirements
Every feature should be tested.