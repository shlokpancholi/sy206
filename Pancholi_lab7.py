#!/usr/bin/python3

#*****************************************************
# Name: Shlok Pancholi
# Date: 1 March 2024
# Course: SY206
# Section: 1122
# Assignment: Lab 6 - Binary Search Trees
#*****************************************************

class Node:
    def __init__(self, n_code, description):
        self.n_code = n_code
        self.description = description
        self.left = None
        self.right = None

    def __str__(self):
        return f"N Code: {self.n_code}, Description: {self.description}"
#node class with modified string method to display the N code and the job description when printed

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        n_code, description = data.split(': ')
        if self.root is None:
            self.root = Node(n_code, description)
        else:
            self._insert_recursive_helper(self.root, n_code, description)
    def _insert_recursive_helper(self, current_node, n_code, description):
        if n_code < current_node.n_code:
            if current_node.left is None:
                current_node.left = Node(n_code, description)
            else:
                self._insert_recursive_helper(current_node.left, n_code, description)
        elif n_code > current_node.n_code:
            if current_node.right is None:
                current_node.right = Node(n_code, description)
            else:
                self._insert_recursive_helper(current_node.right, n_code, description)
#recursive insert function and helper for inserting the N codes into the binary search tree

    def print_tree(self):
        self._print_tree_recursive(self.root)
    def _print_tree_recursive(self, current_node):
        if current_node:
            self._print_tree_recursive(current_node.left)
            print(current_node)
            self._print_tree_recursive(current_node.right)
#recursive print tree method and helper for printing out the tree and the associated N codes and job descriptions

def main():
    opnav_tree = Bst()
    opnav_tree.insert("CNO: Chief of Naval Operations")
    opnav_tree.insert("VCNO: Vice Chief of Naval Operations")
    opnav_tree.insert("DNS: Director of Navy Staff")
    opnav_tree.insert("N1: DCNO Manpower, Personnel, Training & Education")
    opnav_tree.insert("N2/N6: DCNO Information Warfare/Director of Naval Intelligence")
    opnav_tree.insert("N3/N5: DCNO Operations, Plans, & Strategy")
    opnav_tree.insert("N4: DCNO Installations & Logistics")
    opnav_tree.insert("N8: DCNO Integration of Capabilities & Resources")
    opnav_tree.insert("N7: DCNO of Warfighting Development")
    opnav_tree.insert("N9: DCNO of Warfare Systems")
    opnav_tree.insert("N00D: MCPON")
    opnav_tree.insert("N00N: Director of Naval Nuclear Propulsion Program")
    opnav_tree.insert("N091: Director for Test and Evaluation for Tech")
    opnav_tree.insert("N093: Surgeon General of the Navy")
    opnav_tree.insert("N095: Chief of the Navy Reserve")
    opnav_tree.insert("N097: Chief of Chaplains")
    opnav_tree.print_tree()

if __name__ == "__main__":
    main()
