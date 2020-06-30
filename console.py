#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd


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
        return True

    def emptyline(self):
        """
        emptyline
        """
        pass


if __name__ == "__main__":
    """
    code executed when not imported
    """
    HBNBCommand().cmdloop()
