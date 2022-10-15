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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        argv = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
        else:
            key = f"{argv[0]}.{argv[1]}"
            try:
                del storage.all()[key]
            except:
                print("** no instance found **")
            storage.save()
            try:
                eval(argv[0])
            except:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all str repr of all instances not based on class name"""
        argv = arg.split()
        if len(argv) >= 1:
            try:
                eval(arg)()
                print(storage.all())
            except:
                print('** class doesn\'t exist **')
        else:
            print(storage.all())

    # all errors (e.g.: instance not found) could be all added to 1 method which does all
    # + return argv as a dictonary, then eval will be easier.
    # 'tis done like this because functionality before optimization.


if __name__ == '__main__':
    HBNBCommand().cmdloop()
