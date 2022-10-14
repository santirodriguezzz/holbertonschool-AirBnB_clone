#!/usr/bin/python3
"""Module Console"""
import cmd
from models import BaseModel, FileStorage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the cmd interpreter"""
    prompt = '(hbnb)'

cmd.PROMPT

if __name__ == '__main__':
    HBNBCommand().cmdloop()
