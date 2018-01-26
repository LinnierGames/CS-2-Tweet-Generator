#!python


class Node(object):

	def __init__(self, data):
		"""Initialize this node with the given data."""
		self.data = data
		self.next = None

	def __repr__(self):
		"""Return a string representation of this node."""
		return 'Node({!r})'.format(self.data)


class LinkedList(object):

	def __init__(self, items=None):
		"""Initialize this linked list and append the given items, if any."""
		self.head = None  # First node
		self.tail = None  # Last node
		# Append given items
		if items is not None:
			for item in items:
				self.append(item)

	def __str__(self):
		"""Return a formatted string representation of this linked list."""
		items = ['({!r})'.format(item) for item in self.items()]
		return '[{}]'.format(' -> '.join(items))

	def __repr__(self):
		"""Return a string representation of this linked list."""
		return 'LinkedList({!r})'.format(self.items())

	def items(self):
		"""Return a list (dynamic array) of all items in this linked list.
		Best and worst case running time: O(n) for n items in the list (length)
		because we always need to loop through all n nodes to get each item."""
		items = []  # O(1) time to create empty list
		# Start at head node
		node = self.head  # O(1) time to assign new variable
		# Loop until node is None, which is one node too far past tail
		while node is not None:  # Always n iterations because no early return
			items.append(node.data)  # O(1) time (on average) to append to list
			# Skip to next node to advance forward in linked list
			node = node.next  # O(1) time to reassign variable
		# Now list contains items from all nodes
		return items  # O(1) time to return list

	def is_empty(self):
		"""Return a boolean indicating whether this linked list is empty."""
		return self.head is None

	def length(self):
		"""Return the length of this linked list by traversing its nodes"""
		length = 0
		iterator = self.head
		while iterator is not None:
			length += 1
			iterator = iterator.next

		return length

	def append(self, item):
		"""Insert the given item at the tail of this linked list."""
		node = Node(item)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def prepend(self, item):
		"""Insert the given item at the head of this linked list."""
		node = Node(item)
		node.next = self.head
		self.head = node
		if self.tail is None:
			self.tail = node

	def find(self, quality):
		"""Return an item from this linked list satisfying the given quality."""
		iterator = self.head
		is_found = False

		while iterator is not None and is_found is False:
			if quality(iterator.data):
				is_found = True
			else:
				iterator = iterator.next

		return iterator.data if is_found else None

	def delete(self, item):
		"""Delete the given item from this linked list, or raise ValueError.
        ll = LinkedList(['A', 'B', 'C', 'D', 'E'])
		TODO: Best case running time: O(???) Why and under what conditions?
		TODO: Worst case running time: O(???) Why and under what conditions?"""

		prev_pointer = None
		current_pointer = self.head

		while current_pointer is not None:
			if current_pointer.data is item:
				if current_pointer is self.head:
					if self.head is self.tail:
						self.tail = None
					self.head = current_pointer.next
				elif current_pointer is self.tail:
					self.tail = prev_pointer
					prev_pointer.next = None
				else:
					prev_pointer.next = current_pointer.next
				current_pointer.next = None

				return True
			else:
				prev_pointer = current_pointer
				current_pointer = current_pointer.next

		raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
	ll = LinkedList()
	print('list: {}'.format(ll))

	print('\nTesting append:')
	for item in ['A', 'B', 'C']:
		print('append({!r})'.format(item))
		ll.append(item)
		print('list: {}'.format(ll))

	print('head: {}'.format(ll.head))
	print('tail: {}'.format(ll.tail))
	print('length: {}'.format(ll.length()))

	# Enable this after implementing delete method
	delete_implemented = False
	if delete_implemented:
		print('\nTesting delete:')
		for item in ['B', 'C', 'A']:
			print('delete({!r})'.format(item))
			ll.delete(item)
			print('list: {}'.format(ll))

		print('head: {}'.format(ll.head))
		print('tail: {}'.format(ll.tail))
		print('length: {}'.format(ll.length()))


if __name__ == '__main__':
	test_linked_list()
