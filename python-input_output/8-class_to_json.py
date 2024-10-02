#!/usr/bin/python3


def class_to_json(obj):
    cont = obj.__dict__
    dic = {
        clave: valor
        for clave, valor in cont.items()
        if isinstance(valor, (list, dict, str, int, bool))
    }
    return dic
