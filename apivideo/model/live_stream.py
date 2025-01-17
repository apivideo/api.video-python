"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""


import re  # noqa: F401
import sys  # noqa: F401

from apivideo.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from apivideo.model.live_stream_assets import LiveStreamAssets
    from apivideo.model.restreams_response_object import RestreamsResponseObject
    globals()['LiveStreamAssets'] = LiveStreamAssets
    globals()['RestreamsResponseObject'] = RestreamsResponseObject


class LiveStream(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'live_stream_id': (str,),  # noqa: E501
            'restreams': ([RestreamsResponseObject],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'stream_key': (str,),  # noqa: E501
            'public': (bool,),  # noqa: E501
            'assets': (LiveStreamAssets,),  # noqa: E501
            'player_id': (str,),  # noqa: E501
            'broadcasting': (bool,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'live_stream_id': 'liveStreamId',  # noqa: E501
        'restreams': 'restreams',  # noqa: E501
        'name': 'name',  # noqa: E501
        'stream_key': 'streamKey',  # noqa: E501
        'public': 'public',  # noqa: E501
        'assets': 'assets',  # noqa: E501
        'player_id': 'playerId',  # noqa: E501
        'broadcasting': 'broadcasting',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, live_stream_id, restreams, *args, **kwargs):  # noqa: E501
        """LiveStream - a model defined in OpenAPI

        Args:
            live_stream_id (str): The unique identifier for the live stream. Live stream IDs begin with \"li.\"
            restreams ([RestreamsResponseObject]): Returns the list of restream destinations.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): The name of your live stream.. [optional]  # noqa: E501
            stream_key (str): The unique, private stream key that you use to begin streaming.. [optional]  # noqa: E501
            public (bool): Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/delivery/video-privacy-access-management).. [optional]  # noqa: E501
            assets (LiveStreamAssets): [optional]  # noqa: E501
            player_id (str): The unique identifier for the player.. [optional]  # noqa: E501
            broadcasting (bool): Whether or not you are broadcasting the live video you recorded for others to see. True means you are broadcasting to viewers, false means you are not.. [optional]  # noqa: E501
            created_at (datetime): When the player was created, presented in ATOM UTC format.. [optional]  # noqa: E501
            updated_at (datetime): When the player was last updated, presented in ATOM UTC format.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.live_stream_id = live_stream_id
        self.restreams = restreams
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
