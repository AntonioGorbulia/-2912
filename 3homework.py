class Relative:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.group = None

    def msg_to_group(self, text: str):
        if self.group:
            self.group.msg(text, self)


class Chat:
    def __init__(self, name: str):
        self.name: str = name
        self.members: list[Relative] = []

    def add(self, relative: Relative):
        self.members.append(relative)
        member.chat = self

    def remove(self, id: int):
        for relative in self.members:
            if member.id == id:
                member.chat = None
                self.members.remove(relative)
                break

    def msg(self, text: str, src: Relative = None):
        if src == None:
            src = self
        for relative in self.members:
            if not member.id == src.id:
                print(f"{src.name} -> {relative.name}: {text}")


Mama = Relative("Mama", 1)
Papa = Relative("Papa", 2)
chat = Chat("B2912")

chat.add(Dima)
chat.add(Anton)

Mama.msg_to_chat("Privet vsem")
