from ..internal.landmark import Landmark


class Waypoint(Landmark):
    def __init__(self, id: str, name: str, amenity: str, position: list, opening_hours: str, note: str, description: str):
        super().__init__(id, name, amenity, position, opening_hours)
        self.__note = note
        self.__description = description

    # Getters
    def get_note(self) -> str:
        return self.__note

    def get_description(self) -> str:
        return self.__description

    # Setters
    def set_note(self, note: str) -> None:
        self.__note = note

    def set_description(self, description: str) -> None:
        self.__description = description

    def to_dict(self) -> dict:
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'amenity': self.get_amenity(),
            'position': self.get_position(),
            'opening_hours': self.get_opening_hours(),
            'note': self.get_note(),
            'description': self.get_description()
        }