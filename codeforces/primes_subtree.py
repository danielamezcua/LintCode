#Twitter: Primes in a subtree

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeQuery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY first
#  3. INTEGER_ARRAY second
#  4. INTEGER_ARRAY values
#  5. INTEGER_ARRAY queries
#
class Node:
	def __init__(self, label=None, data=None, prime=None):
		self.__label = label
		self.__data = data
		self.__children = []
		self.__prime = prime

	def addChild(self, node=None):
		if node != None:
			self.__children.append(node)

	def label(self):
		return self.__label

	def children(self):
		return self.__children

	def value(self):
		return self.__data

	def prime(self):
		return self.__prime

	def __str__(self):
		return str(self.__data)

def its_prime(number):
	if number == 1:
		return False
	if number == 2:
		return True
	if number%2 == 0:
		return False
	k = math.ceil(number**0.5)
	for i in range(3,k,2):
		if number%i == 0:
			return False
	return True

def count_primes_subtree(head,nodes_visited):
	result = 0
	if head.prime():
		result+=1
	nodes_to_search = head.children()
	nodes_visited.add(head.label())
	while True:
		if not nodes_to_search:
			break
		aux_nodes_to_search = []
		for node in nodes_to_search:
			if node.label() not in nodes_visited:
				if node.prime():
					result += 1
				aux_nodes_to_search+=node.children()
				nodes_visited.add(node.label())
		nodes_to_search = aux_nodes_to_search

	return result

def search_node(node_number, head):
	nodes_visited = set()
	if head.label() == node_number:
		return count_primes_subtree(head,nodes_visited)
	else:
		nodes_visited.add(head.label())
		nodes_to_search = head.children()
		while True:
			if not nodes_to_search:
				break
			aux_nodes_to_search = []
			for node in nodes_to_search:
				if node.label() not in nodes_visited:
					if node.label() == node_number:
						return count_primes_subtree(node,nodes_visited)
					aux_nodes_to_search += node.children()
					nodes_visited.add(node.label())
			nodes_to_search = aux_nodes_to_search
		return 0

		
def primeQuery(n, first, second, values, queries):
	#Construct the nodes
	list_nodes = []
	list_connections = []
	#Create nodes
	for i in range(0,n):
		prime = its_prime(values[i])
		list_nodes.append(Node(label=i+1, data=values[i], prime=prime))
		list_connections.append([])

	number_of_pairs = len(first)

	#Create tree
	for i in range(0,number_of_pairs):
		fst = first[i]-1
		snd = second[i]-1
		list_nodes[fst].addChild(list_nodes[snd])
		list_nodes[snd].addChild(list_nodes[fst])

	head = list_nodes[0]
	result = []

	#Do the queries
	for query in queries:
		result += [search_node(query, head)]
	return result


if __name__ == '__main__':

    n = int(input().strip())

    first_count = int(input().strip())

    first = []

    for _ in range(first_count):
        first_item = int(input().strip())
        first.append(first_item)

    second_count = int(input().strip())

    second = []

    for _ in range(second_count):
        second_item = int(input().strip())
        second.append(second_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = primeQuery(n, first, second, values, queries)

    print(result)
