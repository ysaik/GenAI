'''
This module provides functions to list callable objects
(functions, classes, methods)
'''
import inspect


def list_module_contents(module):
    """
    Lists functions and classes defined directly within a module.

    Args:
        module: The module object to inspect.

    Returns:
        A dictionary with 'functions' and 'classes' as keys,
        each holding a list of names.
    """
    results = {'functions': [], 'classes': []}
    for name in dir(module):
        try:
            attribute = getattr(module, name)
            # Check if it's defined in *this* module to avoid listing imports
            if inspect.getmodule(attribute) == module:
                if inspect.isfunction(attribute):
                    results['functions'].append(name)
                elif inspect.isclass(attribute):
                    results['classes'].append(name)
        except (AttributeError, TypeError):
            # Some attributes might not be gettable or inspectable
            continue
    return results


def list_class_methods(cls):
    """
    Lists methods (instance, class, static) of a class.

    Args:
        cls: The class object to inspect.

    Returns:
        A list of method names.
    """
    methods = []
    for name in dir(cls):
        try:
            attribute = getattr(cls, name)

            if inspect.isfunction(attribute) or \
               inspect.ismethod(attribute) or \
               inspect.isbuiltin(attribute) or \
               isinstance(attribute, (classmethod, staticmethod)):

                if callable(attribute):
                    methods.append(name)
        except AttributeError:
            continue
    # Using set to remove potential duplicates from dir() inspection
    return sorted(list(set(methods)))
