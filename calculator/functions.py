from calculator.logger import logger


def level_exp_calculator(level):
    level=level-1
    return (50*level**3-150*level**2+400*level)/3


def midnight_shard_calculator(level):
    shard_mult = 300
    return shard_mult*level if level < 200 else shard_mult*200


def mshard_calculator(level, shards_qty):
    shards_total, loops = 0, 0
    while True:
        level+=1
        shard_exp = midnight_shard_calculator(level)
        level_exp = level_exp_calculator(level)    
        shards_total+=level_exp/shard_exp
        if shards_total > shards_qty:
            break
        loops+=1    
        logger.info(f'{str(int(shards_total)).rjust(16)} shards for level {level}')
        
    return loops