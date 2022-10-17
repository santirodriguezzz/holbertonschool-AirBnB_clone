# Python - AirBnB Clone

![](https://i.imgur.com/EKbgvKF.png)

## Description

This is the first step towards creating our own clone of the AirBnB webpage. For this first fiew packages we are developing the console part of the whole project. The console is fully functional in various areas, such as creating new models, showing information, and is also able to update information. All of this is information is saved by serializing the information from a dictionary format into json format. Last, this serialized information can be deserialized so it can be accessed as well as updated.

## The how to:

1) First you should type ``./console.py`` into the command interpret.
2) Now that you are in the fully functional console, you have several features to choose from to use:

> **Create** - with this feature you can create a new ``BaseModel`` and once you push enter it will show you the id of the new created ``BaseModel``.
>
> **Show** - this feature shows you the information of a specific ``BaseModel`` + id given.
>
> **Destroy** - as the name states, it destroys a ``BaseModel`` by also specifying the id.
>
> **All** - shows all the saved information, or you can also specify "all BaseModel" and shows all BaseModels
>
> **Update** - by specifying ``update`` + ``class name`` ``id`` ``attribute name`` ``attribute value``, you can update the chosen attribute.

### Here we are using ``create``:

![](https://i.imgur.com/0r6pa16.jpg)

### Here we are ``create`` a new BaseModel, then we ``show`` it and last we ``destroy`` it:

~![](https://i.imgur.com/J7LMw6N.jpg)

### Here we are using the feature ``all``:

![](https://i.imgur.com/QFdx6Ji.jpg)

### Last but not least, here we use the ``update`` feature:

![](https://i.imgur.com/aolvu6D.jpg)

---

### Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all files start with ``#!/usr/bin/python3``
- Code uses the ``pycodestyle`` (version 2.7.x)
- All files will be executables
- Length of files will be tested using ``wc``

---
### Python Test Cases - ``Unittest``

- All files are under the ``/tests`` folder
- All tests files are python files - extension ``.py``
- All test were executed using: ``python3 -m unittest discover tests``

---

### File Description

Model files ``(/models)``:
>**amenity.py** - contains class ``Amenity``.
>
>**base_model.py** - contains class ``BaseModel``.
>
>**city.py** - contains class ``City``.
>
> **place.py** - contains class ``Place``.
>
> **review.py** - contains class ``Review``.
>
> **state.py** - contains class ``State``.
>
> **user.py** - contains class ``User``
>
> **__init__.py** - package initializer.

Storage setion **/models/engine**:

>**__init__.py** - engine package initializer.
>
> **file_storage.py** - contains methods which save and reload data.

Test files with ``/tests``:
>**__init__.py** - tests package initializer.
>
>**test_console.py** - contains the test corresponding to the console.

Model testing files with ``/tests/test_models``:
>**__init__.py** - models test package initializer.
>
>**test_amenity.py** - test corresponding to the ``Amenity`` class.
>
>**test_base_model.py** - test corresponding to the ``BaseModel`` class.
>
>**test_city.py** - test corresponding to the ``City`` class.
>
>**test_place.py** - test corresponding to the ``Place`` class.
>
>**test_review.py** - test corresponding to the ``Review`` class.
>
>**test_state.py** - test corresponding to the ``State`` class.
>
>**test_user.py** - test corresponding to the ``User`` class.

Engine testing files with ``/tests/test_models/test_engine``:
>**__init__.py** - tests engine package initializer.
>
>**test_file_storage.py** - tests if files are being stored correctly.

>**console.py** - contains the entry point of the command interpreter.
---

## Authors

Written by [Denisse Landau](https://www.linkedin.com/in/denisselandau/ "Denisse Landau") and [Santiago Rodriguez](https://www.linkedin.com/in/santiago-rodriguez-a1901b246 "Santiago Rodriguez")
