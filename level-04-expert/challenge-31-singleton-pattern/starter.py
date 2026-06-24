class Singleton:
    """
    A base class that implements the Singleton pattern.
    """

    _instance = None

    def __new__(cls):
        # Create object only if it doesn't exist
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        # Return the same object every time
        return cls._instance


class AppConfig(Singleton):
    """
    Singleton class for storing application configuration.
    """

    def __init__(self):
        # Initialize only once
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self._config = {}

    def set(self, key, value):
        """
        Store value under key
        """
        self._config[key] = value

    def get(self, key, default=None):
        """
        Get value or default
        """
        return self._config.get(key, default)


class Logger(Singleton):
    """
    Singleton logger that stores messages.
    """

    def __init__(self):
        # Initialize only once
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self._messages = []

    def log(self, message):
        """
        Add message to log
        """
        self._messages.append(message)

    def get_logs(self):
        """
        Return all logs
        """
        return self._messages

    def clear(self):
        """
        Clear logs
        """
        self._messages = []
