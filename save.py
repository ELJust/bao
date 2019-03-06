# -*- coding: utf-8 -*-
"""
Save the Winner and turns taken into a file.
"""


def result_to_file(filename, data):
    
    filehandler = open(filename, "a")
    filehandler.write(str(data['Winner'])+ ','+ str(data['turn count']) + '\n')
        
    filehandler.close()


