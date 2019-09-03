#!/bin/env python

from __future__ import print_function
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import os
import sys

def flatten_file(file):
   result = [] 
   for key in file.GetListOfKeys():
      try:
        traverse_till_end(key.ReadObj(), '', result)
      except:
        pass
   
   return result

def traverse_till_end(node, dirs_list, result):
   new_dir_list = dirs_list + '/' + get_node_name(node)
   if hasattr(node, 'GetListOfKeys'): 
        for key in node.GetListOfKeys():
            traverse_till_end(key.ReadObj(), new_dir_list, result)
   else:
        path = new_dir_list
        result.append(path)

def get_node_name(node):
    if node.InheritsFrom('TObjString'):
        # Strip out just the name from a tag (<name>value</name>)
        name = node.GetName().split('>')[0][1:]
        return name + get_string_suffix()
    else:
        return node.GetName()

def get_string_suffix():
    return '_string_monitor_element'

def compare(path1, path2):
    file1 = ROOT.TFile(path1, 'read')
    file2 = ROOT.TFile(path2, 'read')

    file1_set = set(flatten_file(file1))
    file2_set = set(flatten_file(file2))
    
    mes_not_in_file_1 = file2_set - file1_set
    mes_not_in_file_2 = file1_set - file2_set

    print('Monitor elements that are in first file but are not in the second one:')
    for item in mes_not_in_file_2:
        print(item[1:])

    print('')

    print('Monitor elements that are in second file but are not in the first one:')
    for item in mes_not_in_file_1:
        print(item[1:])

    file1.Close()
    file2.Close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print('This tool prints paths to monitor elements that exist in one file but not in the other.')
            print('Usage: ' + os.path.basename(__file__) + ' file1.root file2.root')
            exit()
    if len(sys.argv) != 3:
        print('Please provide two root files')
        exit()
    
    path1 = sys.argv[1]
    path2 = sys.argv[2]

    compare(path1, path2)
