class Heap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    def add(self, element):
        self.heap.append(element)
        self.size += 1
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            else:
                break
            i = parent

    def add_list(self, elements):
        for element in elements:
            self.add(element)

    def repair(self):
        i = 0
        while True:
            l_child = 2 * i + 1
            r_child = 2 * i + 2
            if r_child < self.size:
                if self.heap[r_child] > self.heap[i]:
                    if self.heap[l_child] < self.heap[r_child]:
                        self.heap[r_child], self.heap[i] = self.heap[i], self.heap[r_child]
                        i = r_child
                        continue
                    else:
                        self.heap[l_child], self.heap[i] = self.heap[i], self.heap[l_child]
                        i = l_child
                        continue
            if l_child < self.size:
                if self.heap[l_child] > self.heap[i]:
                    if r_child < self.size:
                        if self.heap[r_child] > self.heap[l_child]:
                            self.heap[r_child], self.heap[i] = self.heap[i], self.heap[r_child]
                            i = r_child
                            continue
                        else:
                            self.heap[l_child], self.heap[i] = self.heap[i], self.heap[l_child]
                            i = l_child
                            continue
                    else:
                        self.heap[l_child], self.heap[i] = self.heap[i], self.heap[l_child]
                        i = l_child
                        continue
            break

    def take_max(self):
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        del self.heap[self.size - 1]
        # print(self.size)
        self.size -= 1
        self.repair()
        return max_value

    def __str__(self):
        line_size = 1
        remain_heap_elements = self.size
        string = ""
        idx = 0
        while remain_heap_elements > 0:
            elements_amount = min(line_size, remain_heap_elements)
            for i in range(elements_amount):
                string += str(self.heap[idx]) + " "
                idx += 1
                if idx % 2 == 1:
                    string += "     "
            remain_heap_elements -= elements_amount
            string += "\n"
            line_size *= 2
        return string
