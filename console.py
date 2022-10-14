#!/usr/bin/python3
"""Module Console"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the cmd interpreter"""
    prompt = '(hbnb) '
    
    def emptyline(self):
        """when input is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()   

    def do_EOF(self,arg):
        """EOF command to exit the program"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
