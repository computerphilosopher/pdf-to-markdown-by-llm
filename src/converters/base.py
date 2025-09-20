"""
Defines the abstract base class for all converters.
"""
from abc import ABC, abstractmethod
from pathlib import Path


class BaseConverter(ABC):
    """
    Abstract base class for a converter.

    Any concrete converter implementation must inherit from this class
    and implement the `convert` method.
    """

    @abstractmethod
    def convert(self, source_path: Path) -> str:
        """
        Converts a source file to a Markdown string.

        Args:
            source_path: The path to the source file to be converted.

        Returns:
            A string containing the raw Markdown content.
        
        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        raise NotImplementedError
