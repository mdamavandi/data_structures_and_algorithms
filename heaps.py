

class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):
        """
        starting at node_index, compares the value at node_index and the parent value
        if the parent value is smaller, the two items swap positions
        the process repeats from the current value's new position
        :param node_index: starting index
        :return: None
        """
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2

            # check for a violation of the max heap property
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                # no violation, so percolate up is done
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                self.heap_array[node_index], self.heap_array[parent_index] = \
                    self.heap_array[parent_index], self.heap_array[node_index]

                # continue the loop from the parent node
                node_index = parent_index

    def percolate_down(self, node_index):
        """
        starting at node_index, compares the value at node_index to the children values
        if either child's value is larger than the current value, swap positions with largest child
        process continues from the current value's new position
        :param node_index: starting index
        :return: None
        """
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # find the max among the node and the node's children
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i += 1

            # check for a violation of the max heap property
            if max_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                self.heap_array[node_index], self.heap_array[max_index] = \
                    self.heap_array[max_index], self.heap_array[node_index]

                # continue loop from the larger child node
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        """
        adds the new value into the MaxHeap and percolates it up to restore MaxHeap order
        :param value: value to be added
        :return: None
        """

        # add the new value to the end of the array
        self.heap_array.append(value)

        # percolate up from the last index to restore heap property
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        """
        removes and returns the max value
        percolates down to restore MaxHeap property
        :return: max value
        """

        # save the max value from the root of the heap
        max_value = self.heap_array[0]

        # move the last item in the array into index 0
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0
            self.heap_array[0] = replace_value

            # percolate down to restore max heap property
            self.percolate_down(0)

        # return the max value
        return max_value