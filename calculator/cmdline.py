import sys
from optparse import OptionParser
from calculator.logger import logger
from calculator.functions import mshard_calculator

logger.info(f'''

████████╗███╗   ███╗███████╗ ██████╗ █████╗ ██╗     
╚══██╔══╝████╗ ████║██╔════╝██╔════╝██╔══██╗██║     
   ██║   ██╔████╔██║███████╗██║     ███████║██║     
   ██║   ██║╚██╔╝██║╚════██║██║     ██╔══██║██║     
   ██║   ██║ ╚═╝ ██║███████║╚██████╗██║  ██║███████╗
   ╚═╝   ╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝
''')


def main():
    parser = OptionParser()

    parser.add_option('--level', '-l', dest='level', type='int', action='store',
                          help='Level of your character. Default is 1')
    parser.add_option('--shards', '-s', dest='shards', type='int', action='store',
                          help='Shards Quantity to calculate how many levels you will get')


    args, _ = parser.parse_args(sys.argv[1:])
    
    if args.level and args.shards:
        res = mshard_calculator(args.level, args.shards)
        
    elif args.level and not args.shards:
        logger.error("Please, insert --shards option")
        sys.exit(1)

    elif not args.level and args.shards:
        logger.warning("No level input. Using default (level 1)...\n")
        res = mshard_calculator(1, args.shards)

    elif not args.level and not args.shards:
        logger.error("Please, insert --level and --shards as option")
        sys.exit(1)

    logger.info(f"\n       You'll be able to level up {res} times.")
    logger.info(f"___________________________________________________")
    sys.exit(0)
