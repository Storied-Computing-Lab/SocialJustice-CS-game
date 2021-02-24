"""
This file is needed because getting the path in a .rpy file will 
just result in the renpy download path.
"""
import os
student_notebook_path = os.path.dirname(os.path.realpath(__file__)) + '/studentNotebook.txt'