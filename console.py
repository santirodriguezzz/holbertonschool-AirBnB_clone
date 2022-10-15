#!/usr/bin/python3
"""Module Console"""
import cmd
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the cmd interpreter"""
    prompt = '(hbnb) '
    
    def emptyline(self):
        """when input is an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()   

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        exit()

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                newInstance = eval(arg)()
                newInstance.save()
                print(newInstance.id)
            except:
                print('** class doesn\'t exist **')

    
    def do_show(self, arg):
        """ """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
