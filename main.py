"""Simple MVC using the pattern Observer."""


class ModelCocoTheParrot:
    """A Parrot : repeats everything he hears."""

    def __init__(self):
        """Init the sentences."""
        self.base_sentence = "Coco say hello to you !"
        self.last_sentence_heard = ""
        self.coco_say = "Coco say : "

    def talk(self):
        """Talk to you !"""
        if not self.last_sentence_heard:
            return f"{self.coco_say}{self.base_sentence}"

        return self.coco_say + f"{self.last_sentence_heard}! " * 2


class ControllerObserver:
    """Controller class.

    Implements the Observer pattern. This is the Observer.
    """

    def __init__(self, view):
        """Init the view and running."""
        self.running = True

        self.model = ModelCocoTheParrot()

        self.view = view
        self.view.attach(self)

    def run(self):
        """Run the application."""
        while self.running:
            self.view.display(self.model)

    def update(self, choice: str):
        """Update the application."""
        self.model.last_sentence_heard = choice


class ViewSubject:
    """View class.

    Implements the observer pattern. This is the Subject.
    """

    def __init__(self):
        """Init an observer to None."""
        self.observer = None

    def attach(self, observer):
        """Attach an observer."""
        self.observer = observer

    def notify(self, choice):
        """Notify an observer."""
        self.observer.update(choice)

    def display(self, model):
        """Display the view."""
        print()
        print(model.talk())
        self.display_input()

    def display_input(self):
        """Display an input and notify the observer of the result."""
        choice = input("Say something : ")
        self.notify(choice)


if __name__ == "__main__":
    view = ViewSubject()
    controller = ControllerObserver(view)
    controller.run()
