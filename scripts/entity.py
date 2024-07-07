class Entity:
    """
    A class to represent any entity.

        Attributes
        ----------
        
        valid_kwargs : dict
            Dictionary with the valid key word arguments

        Methods
        -------

        validate_kwargs(self, kwargs: dict, valid_kwargs: dict) -> None:
            Validate the key word arguments.
    """

    def validate_kwargs(self, kwargs: dict, valid_kwargs: dict) -> None:
        """
        Validate the key word arguments.

            Parameters
                kwargs (dict): Dictionary with the key word arguments
                valid_kwargs (dict) : Dictionary with the allowed key word arguments
    
            Returns
                return None
        """

        for key in kwargs:
            # Validate key & value
            if valid_kwargs.get(key, None):
                if isinstance(kwargs[key], valid_kwargs[key]):
                    setattr(self, key, kwargs[key])
                else:
                    raise Exception(f"The attributes values ({kwargs[key]}) are invalid.")
            else:
                raise Exception(f"The key ({key}) ins't a valid keyword argument.")
