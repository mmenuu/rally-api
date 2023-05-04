import uuid

class Magazine:
    def __init__(self, title, description):
        self.__id = str(uuid.uuid4())
        self.__title = title
        self.__description = description

    # Getters
    def get_title(self) -> str:
        return self.__title

    def get_description(self) -> str:
        return self.__description

    def get_id(self) -> str:
        return self.__id

    # Setters
    def set_title(self, title: str) -> None:
        self.__title = title

    def set_description(self, text: str) -> None:
        self.__description = text

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'title': self.get_title(),
            'description': self.get_description()
        }