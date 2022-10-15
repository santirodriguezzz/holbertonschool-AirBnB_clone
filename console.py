#!/usr/bin/python3
"""Module Console"""
import cmd
import models
from models import storage
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
        """Prints the string representation of an instance"""
        argv = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
        else:
            key = f"{argv[0]}.{argv[1]}"
            try:
                eval(argv[0])
            except:
                print("** class doesn't exist **")
                return
            try:
                print(storage.all()[key])
            except:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
