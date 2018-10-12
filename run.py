# coding:utf-8
import sys
import signal
from os.path import dirname, abspath
import argparse
import importlib
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

project_root_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, project_root_path)
settings = importlib.import_module('settings')
parser = argparse.ArgumentParser(
    description='aioip --  SDK of dynamic IP proxy pool based on python3.6 ')

sub_parsers = parser.add_subparsers(dest='sub_cmd_name')
api = sub_parsers.add_parser('api')
spiders = sub_parsers.add_parser('spiders')

args, unknown_args = parser.parse_known_args()

if args.sub_cmd_name is None:
    parser.print_help()
    sys.exit()

subcmd_package_name_map = {
    "api": "api",
    "spiders": "spiders",
    "score": "score",
    "processing": "processing"
}

subcmd_connector_map = {
    "api": [],
    "spiders": [],
    "score": [],
    "processing": [],
}
# 按需链接第三方服务，保证权限需求最小
connector_init = importlib.import_module('connections.instances')
connector_init.init_connections(subcmd_connector_map[args.sub_cmd_name])
module_name = subcmd_package_name_map[args.sub_cmd_name]
module = importlib.import_module(module_name + '.entry')
module.main(args, unknown_args)
