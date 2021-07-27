from bowler import Bowler


def test_bowler():
    annie = Bowler("Annie", 190, 210)
    benny = Bowler("Benny", 190, 195)
    chance = Bowler("Chance", 185, 225)
    delia = Bowler("Delia", 165, 170)

    assert annie == benny
    assert benny >= chance
    assert benny >= annie
    assert delia < chance
