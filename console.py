#!/usr/bin/python3
"""Module Console"""
import cmd
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


def check_class(self, arg):
    """checks if class exisits"""
    argv = arg.split()
    if len(arg) == 0:
        print("** class name missing **")
        return False
    try:
        eval(argv[0])
    except:
        print("** class doesn't exist **")
        return False

def check_id(self, arg):
    """checks if id exisits"""
    argv = arg.split()
    if len(argv) == 1:
        print("** instance id missing **")
        return False
    try:
        key = f"{argv[0]}.{argv[1]}"
        storage.all()[key]
    except:
        print("** no instance found **")
        return False

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
        if check_class(self, arg) == False:
            return
        else:
            try:
                newInstance = eval(arg)()
                newInstance.save()
                print(newInstance.id)
            except:
                print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if check_class(self, arg) == False:
            return
        argv = arg.split()
        if check_id(self, arg) == False:
            return
        else:
            key = f"{argv[0]}.{argv[1]}"
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if check_class(self, arg) == False:
            return
        argv = arg.split()
        if check_id(self, arg) == False:
            return
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

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        argv = arg.split()
        if check_class(self, arg) == False:
            return
        if check_id(self, arg) == False:
            return
        if len(argv) == 2:
            print("** attribute name missing **")
            return
        if len(argv) == 3:
            print("** value missing **") # checked all args are present
            return
        else:
            key = f"{argv[0]}.{argv[1]}"
        for keys, value in storage.all().items():
            if argv[0] == value.__class__.__name__ and argv[1].strip('""') == value.id:
                setattr(value, argv[2], argv[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
