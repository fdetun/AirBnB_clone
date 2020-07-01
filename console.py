#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        saves it (to the JSON file) and prints the id.
        """
        if line is '':
            print("** class name missing **")
        elif line == "BaseModel":
            a = BaseModel()
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
        elif Args_l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join(("BaseModel", Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        else:
            print(all_objs['.'.join(("BaseModel", Args_l[1]))])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        all_objs = storage.all()
        Args_l = line.split()
        if len(Args_l) == 0:
            print("** class name missing **")
        elif Args_l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join(("BaseModel", Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs['.'.join(("BaseModel", Args_l[1]))]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        Args_l = line.split()
        if len(Args_l) == 1 and Args_l[0] != "BaseModel":
            print("** class doesn't exist **")
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
        elif Args_l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(Args_l) == 1:
            print("** instance id missing **")
        elif '.'.join(("BaseModel", Args_l[1])) not in all_objs.keys():
            print("** no instance found **")
        elif len(Args_l) == 2:
            print("** attribute name missing **")
        elif len(Args_l) == 3:
            print("** value missing **")
        else:
            id = '.'.join(("BaseModel", Args_l[1]))
            Dict = all_objs[id].to_dict()
            print("-->{}".format(type(Args_l[3])))
            Dict[Args_l[2]] = Args_l[3].strip('"\'')
            tmpBase = BaseModel(**Dict)
            all_objs[id] = tmpBase
            storage.save()


if __name__ == "__main__":
    """
    code executed when not imported
    """
    HBNBCommand().cmdloop()
