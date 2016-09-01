import contextlib
import copy
import os.path
import tempfile

# TODO: Something has to be wrong with my way os doing imports. If pytest is run
# with python 3 all goes fine, but if I use python 2 all tests folder's tests
# fail because ImportErrors (except test_sources.py).
import vdist.builder as builder
import vdist.console_parser as console_parser
import vdist.configuration as configuration
import vdist.source as source
import vdist.vdist as vdist

DUMMY_CONFIGURATION_TEXT = """[DEFAULT]
app = geolocate
version = 1.3.0
source_git = https://github.com/dante-signal31/${app}, master
fpm_args = --maintainer dante.signal31@gmail.com -a native --url
    https://github.com/dante-signal31/${app} --description
    "This program accepts any text and searchs inside every IP
    address. With each of those IP addresses,
    ${app} queries
    Maxmind GeoIP database to look for the city and
    country where
    IP address or URL is located. Geolocate is designed to be
    used in console with pipes and redirections along with
    applications like traceroute, nslookup, etc."
    --license BSD-3 --category net
requirements_path = /REQUIREMENTS.txt
runtime_deps = libssl1.0.0, dummy1.0.0
compile_python = True
python_version = 3.4.4
output_folder = ./vdist

[Ubuntu-package]
profile = ubuntu-trusty

[Centos6-package]
profile = centos6

[Centos7-package]
profile = centos
"""

DUMMY_OUTPUT_FOLDER = "/tmp/vdist"

UBUNTU_ARGPARSED_ARGUMENTS = {
        "app": 'geolocate',
        "version": '1.3.0',
        "source": "https://github.com/dante-signal31/geolocate, master",
        "profile": 'ubuntu-trusty',
        "compile_python": "True",
        "python_version": '3.4.4',
        "fpm_args": '--maintainer dante.signal31@gmail.com -a native --url '
                    'https://github.com/dante-signal31/geolocate --description '
                    '"This program accepts any text and searchs inside every IP'
                    ' address. With each of those IP addresses, '
                    'geolocate queries '
                    'Maxmind GeoIP database to look for the city and '
                    'country where'
                    ' IP address or URL is located. Geolocate is designed to be'
                    ' used in console with pipes and redirections along with '
                    'applications like traceroute, nslookup, etc."'
                    ' --license BSD-3 --category net',
        "requirements_path": '/REQUIREMENTS.txt',
        "runtime_deps": "libssl1.0.0, dummy1.0.0",
        "output_folder": DUMMY_OUTPUT_FOLDER
}

CORRECT_UBUNTU_PARAMETERS = {
        "app": 'geolocate',
        "version": '1.3.0',
        "source": source.git(
            uri='https://github.com/dante-signal31/geolocate',
            branch='master'
        ),
        "profile": 'ubuntu-trusty',
        "compile_python": True,
        "python_version": '3.4.4',
        "fpm_args": '--maintainer dante.signal31@gmail.com -a native --url '
                    'https://github.com/dante-signal31/geolocate --description '
                    '"This program accepts any text and searchs inside every IP'
                    ' address. With each of those IP addresses, '
                    'geolocate queries '
                    'Maxmind GeoIP database to look for the city and '
                    'country where'
                    ' IP address or URL is located. Geolocate is designed to be'
                    ' used in console with pipes and redirections along with '
                    'applications like traceroute, nslookup, etc."'
                    ' --license BSD-3 --category net',
        "requirements_path": '/REQUIREMENTS.txt',
        "runtime_deps": ["libssl1.0.0", "dummy1.0.0"]
    }

DUMMY_PACKAGE_NAME = "geolocate-1.3.0-ubuntu-trusty"
DUMMY_PACKAGE_EXTENSION = ".deb"
DUMMY_CONFIGURATION_ARGUMENTS = copy.deepcopy(CORRECT_UBUNTU_PARAMETERS)
DUMMY_CONFIGURATION_ARGUMENTS["output_folder"] = DUMMY_OUTPUT_FOLDER
DUMMY_CONFIGURATION = configuration.Configuration(UBUNTU_ARGPARSED_ARGUMENTS)
CORRECT_OUTPUT_FOLDER = "./vdist"
DUMMY_CONFIGURATION_FILE_ARGUMENTS = ["vdist", "batch", "config.cfg"]
DUMMY_MANUAL_ARGUMENTS = ["vdist", "manual",
                          "--app", "geolocate",
                          "--version", "1.3.0",
                          "--source-git", "https://github.com/dante-signal31/geolocate,master",
                          "--profile", "ubuntu-trusty",
                          "--compile_python",
                          "--python_version", "3.4.4",
                          "--fpm_args", '--maintainer dante.signal31@gmail.com -a native --url '
                                        'https://github.com/dante-signal31/geolocate --description '
                                        '"This program accepts any text and searchs inside every IP'
                                        ' address. With each of those IP addresses, '
                                        'geolocate queries '
                                        'Maxmind GeoIP database to look for the city and '
                                        'country where'
                                        ' IP address or URL is located. Geolocate is designed to be'
                                        ' used in console with pipes and redirections along with '
                                        'applications like traceroute, nslookup, etc."'
                                        ' --license BSD-3 --category net',
                          "--requirements_path", "/REQUIREMENTS.txt",
                          "--runtime_deps", "libssl1.0.0, dummy1.0.0",
                          "--output_folder", DUMMY_OUTPUT_FOLDER]


@contextlib.contextmanager
def _create_dummy_configuration_file(configuration_text):
    with tempfile.NamedTemporaryFile(mode="wb") as temporary_file:
        temporary_file.write(configuration_text.encode("UTF-8"))
        temporary_file.flush()
        yield temporary_file


def test_configuration_file_read():
    with _create_dummy_configuration_file(DUMMY_CONFIGURATION_TEXT) as config_file:
        configurations = configuration.read(config_file.name)
        ubuntu_configuration = configuration.Configuration(configurations["Ubuntu-package"])
        assert ubuntu_configuration.builder_parameters == CORRECT_UBUNTU_PARAMETERS
        assert ubuntu_configuration.output_folder == CORRECT_OUTPUT_FOLDER
        assert "Centos7-package" in configurations


def test_parse_arguments_configuration_file():
    parsed_arguments = console_parser.parse_arguments(DUMMY_CONFIGURATION_FILE_ARGUMENTS)
    assert parsed_arguments["configuration_file"] == "config.cfg"


def test_move_package_to_output_folder():
    with tempfile.TemporaryDirectory() as tempdir:
        with tempfile.NamedTemporaryFile(prefix=DUMMY_PACKAGE_NAME,
                                         suffix=DUMMY_PACKAGE_EXTENSION,
                                         dir=tempdir) as dummy_package:
            dummy_source_folder, dummy_package_name = os.path.split(dummy_package.name)
            builder._move_package_to_output_folder(DUMMY_CONFIGURATION,
                                                   source_folder=dummy_source_folder)
            correct_package = os.path.join(DUMMY_OUTPUT_FOLDER,
                                           dummy_package_name)
            assert os.path.isfile(correct_package)


def test_build_package_batch():
    with _create_dummy_configuration_file(DUMMY_CONFIGURATION_TEXT) as config_file:
        configurations = configuration.read(config_file)
        builder.build_package(configurations[0])
        correct_output_package = os.path.join(configurations[0].output_folder,
                                              ".".join(DUMMY_PACKAGE_NAME, "deb"))
        assert os.path.isfile(correct_output_package)


def test_build_package_manual():
    console_arguments = console_parser.parse_arguments(DUMMY_MANUAL_ARGUMENTS)
    configurations = vdist._get_build_configurations(console_arguments)
    for _configuration in configurations:
        builder.build_package(configurations[_configuration])
    correct_output_package = os.path.join(configurations[0].output_folder,
                                          ".".join(DUMMY_PACKAGE_NAME, "deb"))
    assert os.path.isfile(correct_output_package)