#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from reporter.reporter import Reporter
from collector.collector import Collector
from config.config import Config
import asyncio


__author__ = "Garry Lachman"
__copyright__ = "Copyright 2021, Garry Lachman"
__credits__ = [""]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Garry Lachman"
__email__ = "garry@lachman.co"
__status__ = "Development"

import argparse
from logzero import logger


def log(function):
    """Handy logging decorator."""
    def inner(*args, **kwargs):
        """Innter method."""
        logger.debug(function)
        function(*args, **kwargs)
    return inner


def main(args: argparse.Namespace):
    loop = asyncio.get_event_loop()
    
    config = Config(args.config)
    collector = Collector(config)
    collector.start()
    reporter = Reporter(config, collector.result_queue)
    reporter.start()
      
    loop.run_forever()


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("-c", "--config", type=argparse.FileType('r'))


    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    PARSER.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    PARSER.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    MYARGS = PARSER.parse_args()
    main(MYARGS)
