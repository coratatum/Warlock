import pytest
import utils.dice_roller as dice_roller
from utils.exceptions import InvalidInputException

@pytest.mark.asyncio
async def test_parse_xdy_valid():
    xdy = "3d6"
    retval = await dice_roller.parse_xdy(xdy)
    assert retval[0] == 3
    assert retval[1] == 6

@pytest.mark.asyncio
async def test_parse_xdy_negative_x():
    xdy = "-1d5"
    has_ex = False
    try:
        retval = await dice_roller.parse_xdy(xdy)
    except Exception as retval:
        assert isinstance(retval, InvalidInputException)
        has_ex = True
    assert has_ex

@pytest.mark.asyncio
async def test_parse_xdy_negative_y():
    xdy = "1d-5"
    has_ex = False
    try:
        retval = await dice_roller.parse_xdy(xdy)
    except Exception as retval:
        assert isinstance(retval, InvalidInputException)
        has_ex = True
    assert has_ex

@pytest.mark.asyncio
async def test_parse_xdy_incorrect_format():
    xdy = "asdfsasdf"
    has_ex = False
    try:
        retval = await dice_roller.parse_xdy(xdy)
    except Exception as retval:
        assert isinstance(retval, InvalidInputException)
        has_ex = True
    assert has_ex

@pytest.mark.asyncio
async def test_roll_parsed():
    x = 5
    y = 6
    retval = await dice_roller.roll_parsed(x, y)
    assert len(retval) == x
    for val in retval:
        assert 1 <= val <= y

@pytest.mark.asyncio
async def test_roll_xdy_valid():
    xdy = "4d6"
    retval = await dice_roller.roll_xdy(xdy)
    assert len(retval) == 4
    for val in retval:
        assert 1 <= val <= 6


@pytest.mark.asyncio
async def test_roll_xdy_error():
    xdy = "asdf"
    retval = await dice_roller.roll_xdy(xdy)
    assert retval == "Error Occurred: Invalid format for roll command"


