#---------------------------------------------------------------------------------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or 
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
#---------------------------------------------------------------------------------------------------------------------------------------------
"""Flask configuration."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, ".env"))

class Config:
    #
    API_HOST_ADDRESS=environ.get('API_HOST_ADDRESS')
    API_PORT_NUMBER=environ.get('API_PORT_NUMBER')
    CLIENT_HOST_ADDRESS=environ.get('CLIENT_HOST_ADDRESS')
    CLIENT_PORT_NUMBER=environ.get('CLIENT_PORT_NUMBER')