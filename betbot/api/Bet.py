"""LICENSE
Copyright 2020 Hermann Krumrey <hermann@krumreyh.com>

This file is part of betbot.

betbot is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

betbot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with betbot.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from typing import Dict
from dataclasses import dataclass


@dataclass
class Bet:
    """
    Class that encapsulates Bet information
    """
    match_id: int
    """
    The ID of the associated match
    """

    home_score: int
    """
    The score bet on the home team
    """

    away_score: int
    """
    The score bet on the away team
    """

    def to_dict(self) -> Dict[str, int]:
        """
        :return: A dictionary that canbe used to place the bet using the API
        """
        return {
            f"{self.match_id}-home": self.home_score,
            f"{self.match_id}-away": self.away_score
        }
