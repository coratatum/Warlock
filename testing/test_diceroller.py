import pytest
import utils.DiceRoller as dice_roller



@pytest.mark.asyncio
async def test_parse_xdy_valid():
    xdy = "3d6"
    retval = await dice_roller.parse_xdy(xdy)
    assert retval[0] == 3
    assert retval[1] == 6

@pytest.mark.asyncio
async def test_parse_xdy_negative_x():
    xdy = "-1d5"
    retval = await dice_roller.parse_xdy(xdy)
    assert retval == dice_roller.InvalidInput

@pytest.mark.asyncio
async def test_parse_xdy_negative_y():
    xdy = "1d-5"
    retval = await dice_roller.parse_xdy(xdy)
    assert retval == dice_roller.InvalidInput

@pytest.mark.asyncio
async def test_parse_xdy_incorrect_format():
    xdy = "asdfsasdf"
    retval = await dice_roller.parse_xdy(xdy)
    assert retval == dice_roller.InvalidInput