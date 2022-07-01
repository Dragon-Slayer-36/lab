class Television:
    """
    A class representing details for a television object via the using multiple functions below.   
    """
    
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.   
        """
        
        self.__channel = 0          #Default TV channel
        self.__volume = 0           #Default TV volume
        self.__status = 'False'     #Default TV power

    def power(self) -> str:
        """
        Method to determine and modify a television's power status.
        :return: Television's power status.
        """
        
        if self.__status == 'False':
            self.__status = 'True'
            return self.__status
        if self.__status == 'True':
            self.__status = 'False'
            return self.__status

    def channel_up(self) -> int:
        """
        Method to determine and/or modify a television's channel up by one with a maximum channel limit of 3.
        :return: Television's channel number.
        """
        
        if self.__status == 'True':
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

            elif self.__channel >= Television.MIN_CHANNEL:
                self.__channel += 1
        else:
            return self.__channel

    def channel_down(self) -> int:
        """
        Method to determine and/or modify television's channel down by one with a minimum channel limit of 3.
        :return: Television's channel number.        
        """
        
        if self.__status == 'True':
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

            elif self.__channel <= Television.MAX_CHANNEL:
                self.__channel -= 1
        else:
            return self.__channel

    def volume_up(self) -> int:
        """
        Method to determine and/or modify a television's volume up by one with a maximum channel limit of 2.
        :return: Television's volume number.
        """
        
        if self.__status == 'True':
            if self.__volume == Television.MAX_VOLUME:
                return self.__volume

            elif self.__volume >= Television.MIN_VOLUME:
                self.__volume += 1
        else:
            return self.__volume

    def volume_down(self) -> int:
        """
        Method to determine and/or modify a television's volume up by one with a minimum channel limit of 0.
        :return: Television's volume number.
        """
        
        if self.__status == 'True':
            if self.__volume == Television.MIN_VOLUME:
                return self.__volume

            elif self.__volume <= Television.MAX_VOLUME:
                self.__volume -= 1
        else:
            return self.__volume


    def __str__(self) -> str:
        """
        Constructor to display details of a television object as string. 
        :return: Print all details of a television object in a formatted string.
        """
        
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
