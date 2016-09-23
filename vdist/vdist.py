#!/usr/bin/env python
import sys

import console_parser
import configuration
import builder


def _get_build_configurations(arguments):
    try:
        if arguments["configuration_file"] is None:
            configurations = {"Default project": arguments, }
        else:
            configurations = configuration.read(arguments["configuration_file"])
    except KeyError:
        configurations = {"Default project": arguments, }
    return configurations


def main(args=sys.argv[1:]):
    console_arguments = console_parser.parse_arguments(args)
    configurations = _get_build_configurations(console_arguments)
    for _configuration in configurations:
        builder.build_package(configurations[_configuration])


if __name__ == "__main__":
    main()
