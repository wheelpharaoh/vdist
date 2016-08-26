import argparse


def parse_arguments(args=None):
    arg_parser = argparse.ArgumentParser(description="A tool that lets you "
                                                     "create OS packages from "
                                                     "your Python applications "
                                                     "in a clean and self "
                                                     "contained manner.\n",
                                         epilog="Follow vdist development at: "
                                                "<https://github.com/objectified/vdist>")
    subparsers = arg_parser.add_subparsers(help="Available modes")
    automatic_subparser = subparsers.add_parser("batch",
                                                help="Automatic configuration. "
                                                     "Parameters are going to "
                                                     " be read from a"
                                                     "configuration file.")
    automatic_subparser.add_argument("configuration_file",
                                     nargs="?",
                                     default=None,
                                     type=argparse.FileType(),
                                     metavar="CONFIGURATION FILENAME")
    manual_subparser = subparsers.add_parser("manual",
                                             help="Manual configuration. "
                                                  "Parameters are going to be "
                                                  "provided through flags.")
    manual_subparser.add_argument("-a", "--app",
                                  required=True,
                                  help="Name of application to package.",
                                  metavar="APPNAME")
    return args(arg_parser.parse_args(args))