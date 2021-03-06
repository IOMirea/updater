"""
IOMirea-updater - An updater for IOMirea messenger
Copyright (C) 2019  Eugene Ershov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse

from pathlib import Path


argparser = argparse.ArgumentParser(description="IOMirea server updater")
argparser.add_argument(
    "-H",
    "--host",
    default="127.0.0.1",
    help="Host to run API on. Defaults to 127.0.0.1",
)

argparser.add_argument(
    "-P", "--port", default="8081", help="Port to run API on. Defaults to 8081"
)

argparser.add_argument(
    "-C",
    "--config-file",
    type=Path,
    default=Path("/config/config.yaml"),
    help="Path to the config file. Defaults to /config/config.yaml",
)

args = argparser.parse_args()
