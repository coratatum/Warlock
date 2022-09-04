import random
import re
from config.settings import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

InvalidInput = "Invalid Format"

async def parse_xdy(xdy):
    is_valid = re.fullmatch(r'\d+d\d+', xdy)
    if is_valid != None:
        split_str = re.split(r'd', xdy)
        split_ints = list(map(int, split_str))
        if all(num > 0 for num in split_ints):
            return split_ints
    
    logger.warning("Parse encountered incorrect format: " + xdy)
    return InvalidInput

async def roll_parsed(x, y):
    results = []
    for i in range(x):
        results.append(random.randint(1,y))
    return results

async def roll_xdy(xdy):
    parsed = await parse_xdy(xdy)
    return await roll_parsed(parsed[0], parsed[1])
