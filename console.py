#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, ino):
        return True
    def help_quit(self):
        print('Quit command to exit the program')
  
    def help_EOF(self):
        print('EOF command to exit the program')
    do_EOF = do_quit




if __name__ == '__main__':
    HBNBCommand().cmdloop()