from typing import List


def create_new_endtype(endtype_name: str, endtype_id: int, folder_name: str) -> int:
    """Create a new endtype

    Args:
        endtype_name (str): name
        endtype_id (int): endtype id
        folder_name (str): folder name

    Returns:
        int: [description]
    """
    
def get_endtype_id(name: str) -> int:
    """Gets the endtypeID by endtypename

    Args:
        name (str): endtype name

    Returns:
        int: endtype id
    """
def get_endtype_id_end(element_id: int) -> int:
    """Gets the endtypeID of the end face

    Args:
        arg0 (int): elmement ID

    Returns:
        int: endtype id
    """
def get_endtype_id_facet(element: int, face_number: int) -> int:
    """Gets the endtypeID of the face with a number

    Args:
        element (int): element ID
        face_number (int): face number 

    Returns:
        int: endtype id
    """
def get_endtype_id_start(element: int) -> int:
    """Gets the endtypeID of the start face

    Args:
        element (int): element ID

    Returns:
        int: endtype id
    """
def get_endtype_name(endtype_id: int) -> str:
    """Get endtype name

    Args:
        endtype_id (int): endtype ID

    Returns:
        str: endtype name
    """
def get_endtype_name_end(element: int) -> str:
    """Get endtype name end

    Args:
        endtype_id (int): endtype ID

    Returns:
        str: endtype name
    """
def get_endtype_name_facet(element: int, face_number: int) -> str:
    """Gets the endtypename of the face with a number

    Args:
        element (int): element ID
        face_number (int): face number

    Returns:
        str: endtype name facet
    """
def get_endtype_name_start(element: int) -> str:
    """Gets the endtypename of the start face

    Args:
        element (int): element ID

    Returns:
        str: endtype name start
    """

def set_endtype_id_end(element: int, endtype_id: int) -> None:
    """Sets the endtype to end face by endtypeID

    Args:
        element (int): element ID
        endtype_id (int): endtype ID
    """
def set_endtype_id_facet(element: int, endtype_id: int, face_number: int) -> None:
    """Sets the endtype to a face by endtypeID

    Args:
        element (int): element ID
        endtype_id (int): endtype ID
        face_number (int): face number
    """
    
def set_endtype_id_start(element: int, endtype_id: int) -> None:
    """Sets the endtype to start face by endtypeID

    Args:
        element (int): element ID
        endtype_id (int): endtype ID
    """
def set_endtype_name_end(arg0: int, arg1: str) -> None:
    """[summary]

    Args:
        arg0 (int): [description]
        arg1 (str): [description]
    """
def set_endtype_name_facet(element: int, name: str, face_number: int) -> None:
    """Sets the endtype to a face by endtypename

    Args:
        element (int): element ID
        name (str): name
        face_number (int): face number
    """
def set_endtype_name_start(element: int, face_number: str) -> None:
    """Sets the endtype to start face by endtypename

    Args:
        element (int): element ID
        face_number (str): face number
    """