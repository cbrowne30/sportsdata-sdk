# coding: utf-8

"""
    NBA v3 Scores

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Season(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'season': 'int',
        'start_year': 'int',
        'end_year': 'int',
        'description': 'str',
        'regular_season_start_date': 'str',
        'post_season_start_date': 'str',
        'season_type': 'str',
        'api_season': 'str'
    }

    attribute_map = {
        'season': 'Season',
        'start_year': 'StartYear',
        'end_year': 'EndYear',
        'description': 'Description',
        'regular_season_start_date': 'RegularSeasonStartDate',
        'post_season_start_date': 'PostSeasonStartDate',
        'season_type': 'SeasonType',
        'api_season': 'ApiSeason'
    }

    def __init__(self, season=None, start_year=None, end_year=None, description=None, regular_season_start_date=None, post_season_start_date=None, season_type=None, api_season=None):  # noqa: E501
        """Season - a model defined in Swagger"""  # noqa: E501
        self._season = None
        self._start_year = None
        self._end_year = None
        self._description = None
        self._regular_season_start_date = None
        self._post_season_start_date = None
        self._season_type = None
        self._api_season = None
        self.discriminator = None
        if season is not None:
            self.season = season
        if start_year is not None:
            self.start_year = start_year
        if end_year is not None:
            self.end_year = end_year
        if description is not None:
            self.description = description
        if regular_season_start_date is not None:
            self.regular_season_start_date = regular_season_start_date
        if post_season_start_date is not None:
            self.post_season_start_date = post_season_start_date
        if season_type is not None:
            self.season_type = season_type
        if api_season is not None:
            self.api_season = api_season

    @property
    def season(self):
        """Gets the season of this Season.  # noqa: E501


        :return: The season of this Season.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Season.


        :param season: The season of this Season.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def start_year(self):
        """Gets the start_year of this Season.  # noqa: E501


        :return: The start_year of this Season.  # noqa: E501
        :rtype: int
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """Sets the start_year of this Season.


        :param start_year: The start_year of this Season.  # noqa: E501
        :type: int
        """

        self._start_year = start_year

    @property
    def end_year(self):
        """Gets the end_year of this Season.  # noqa: E501


        :return: The end_year of this Season.  # noqa: E501
        :rtype: int
        """
        return self._end_year

    @end_year.setter
    def end_year(self, end_year):
        """Sets the end_year of this Season.


        :param end_year: The end_year of this Season.  # noqa: E501
        :type: int
        """

        self._end_year = end_year

    @property
    def description(self):
        """Gets the description of this Season.  # noqa: E501


        :return: The description of this Season.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Season.


        :param description: The description of this Season.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def regular_season_start_date(self):
        """Gets the regular_season_start_date of this Season.  # noqa: E501


        :return: The regular_season_start_date of this Season.  # noqa: E501
        :rtype: str
        """
        return self._regular_season_start_date

    @regular_season_start_date.setter
    def regular_season_start_date(self, regular_season_start_date):
        """Sets the regular_season_start_date of this Season.


        :param regular_season_start_date: The regular_season_start_date of this Season.  # noqa: E501
        :type: str
        """

        self._regular_season_start_date = regular_season_start_date

    @property
    def post_season_start_date(self):
        """Gets the post_season_start_date of this Season.  # noqa: E501


        :return: The post_season_start_date of this Season.  # noqa: E501
        :rtype: str
        """
        return self._post_season_start_date

    @post_season_start_date.setter
    def post_season_start_date(self, post_season_start_date):
        """Sets the post_season_start_date of this Season.


        :param post_season_start_date: The post_season_start_date of this Season.  # noqa: E501
        :type: str
        """

        self._post_season_start_date = post_season_start_date

    @property
    def season_type(self):
        """Gets the season_type of this Season.  # noqa: E501


        :return: The season_type of this Season.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Season.


        :param season_type: The season_type of this Season.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def api_season(self):
        """Gets the api_season of this Season.  # noqa: E501


        :return: The api_season of this Season.  # noqa: E501
        :rtype: str
        """
        return self._api_season

    @api_season.setter
    def api_season(self, api_season):
        """Sets the api_season of this Season.


        :param api_season: The api_season of this Season.  # noqa: E501
        :type: str
        """

        self._api_season = api_season

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Season, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Season):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
