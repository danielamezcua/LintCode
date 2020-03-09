class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        n = len(s)
        #the number of rotations must be between 0 and n-1. n rotations would derive on the same string
        offset = offset % n 
        n_movements = n

        start_index = 0

        source_index = start_index
        target_index = offset

        source = s[source_index]
        while n_movements > 0:
            aux = s[target_index]
            s[target_index] = source
            source = aux

            source_index = target_index

            if source_index == start_index:
                #we reach a cycle
                source_index = (source_index + 1)%n
                source = s[source_index]
                start_index = source_index

            target_index = (source_index + offset)%n
            n_movements = n_movements - 1



