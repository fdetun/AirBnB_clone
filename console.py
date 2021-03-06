#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

Cls = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """
    Subclass of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Method to exit the program.
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        print("{}".format(self))
        return True

    def emptyline(self):
        """
        emptyline
        """
        pass

    def counter(self, clas):
        """counter class"""
        j = 0
        all_objs = storage.all()
        for i in all_objs.values():
            if i.__class__.__name__ == clas:
                j = j + 1
        return j

    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        saves it (to the JSON file) and prints the id.
        """
        if line is '':
            print("** class name missing **")
        elif line in Cls.keys():
            a = Cls[line]()
            print("{}".format(a.id))
            a.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id
        """
        all_objs = storage.all()
        Args_l = line.split()
        if len(Args_l) == 0:
            print("** class name missing **")
        elif Args_l[0] not in Cls.keys():
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join((Args_l[0], Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        else:
            print(all_objs['.'.join((Args_l[0], Args_l[1]))])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        all_objs = storage.all()
        Args_l = line.split()
        if len(Args_l) == 0:
            print("** class name missing **")
        elif Args_l[0] not in Cls.keys():
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join((Args_l[0], Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs['.'.join((Args_l[0], Args_l[1]))]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        Args_l = line.split()
        if len(Args_l) == 1:
            if Args_l[0] not in Cls.keys():
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                print([str(obj)
                       for Key, obj in all_objs.items() if Args_l[0] in Key])
        else:
            all_objs = storage.all()
            print([str(obj) for Key, obj in all_objs.items()])

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        """
        all_objs = storage.all()
        Args_l = line.split()
        if len(Args_l) == 0:
            print("** class name missing **")
        elif Args_l[0] not in Cls.keys():
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join((Args_l[0], Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        elif len(Args_l) == 2:
            print("** attribute name missing **")
        elif len(Args_l) == 3:
            print("** value missing **")
        else:
            id = '.'.join((Args_l[0], Args_l[1]))
            Dict = all_objs[id].to_dict()
            Dict[Args_l[2]] = Args_l[3].strip('"\'')
            tmpBase = Cls[Args_l[0]](**Dict)
            all_objs[id] = tmpBase
            storage.save()

    def do_User(self, arg):
        """User.all()"""
        if arg == ".all()":
            self.do_all("User")
        elif arg == ".count()":
            a = self.counter("User")
            print(a)

    def do_BaseModel(self, arg):
        """BaseModel.all()"""
        if arg == ".all()":
            self.do_all("BaseModel")
        elif arg == ".count()":
            a = self.counter("BaseModel")
            print(a)

    def do_City(self, arg):
        """City.all()"""
        if arg == ".all()":
            self.do_all("City")
        elif arg == ".count()":
            a = self.counter("City")
            print(a)

    def do_State(self, arg):
        """State.all()"""
        if arg == ".all()":
            self.do_all("State")
        elif arg == ".count()":
            a = self.counter("State")
            print(a)

    def do_Place(self, arg):
        """Place.all()"""
        if arg == ".all()":
            self.do_all("Place")
        elif arg == ".count()":
            a = self.counter("Place")
            print(a)

    def do_Review(self, arg):
        """Review.all()"""
        if arg == ".all()":
            self.do_all("Review")
        elif arg == ".count()":
            a = self.counter("Review")
            print(a)

    def do_Amenity(self, arg):
        """Amenity.all()"""
        if arg == ".all()":
            self.do_all("Amenity")
        elif arg == ".count()":
            a = self.counter("Amenity")
            print(a)


if __name__ == "__main__":
    """
    code executed when not imported
    """
    HBNBCommand().cmdloop()
