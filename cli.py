import argparse
import os
from . import data

def main():
    args = parse_args()
    args.funct(args)

def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")
    commands.required = True
    init_parser = commands.add_parser("init")
    init_parser.set_defaults(funct=init)
    return parser.parse_args()

def init(args):
    data.init()
    print(f"Initialized empty git repository in {os.getcwd()}/{data.GET_DIR}")
