from dataclasses import dataclass
from dlinkedlist import DLinkedList


@dataclass
class FileBlock:
    start_location: int
    file_id: int
    length: int


class Disk:
    def __init__(self):
        self.disk = DLinkedList()
        self.read_ptr = None
        self.write_ptr = None

    def store_file(self, file_id, disk_sector, block_length):
        self.disk.append(FileBlock(disk_sector, file_id, int(block_length)))

    def seek_free_space(self):
        """Return first location of free space"""
        self.write_ptr = self.disk.head
        block_location = self.write_ptr.value.start_location
        while self.write_ptr:
            if self.write_ptr.value.start_location > block_location:
                self.write_ptr = self.write_ptr.previous
                return block_location
            block_location += self.write_ptr.value.length
            self.write_ptr = self.write_ptr.next
        return -1

    def reverse_seek_used_space(self):
        """Return last location of used space"""
        self.read_ptr = self.disk.tail
        return self.disk.tail.value.start_location + self.disk.tail.value.length

    def compact(self):
        while (
            self.seek_free_space() >= 0
            and self.reverse_seek_used_space() > self.seek_free_space()
        ):
            self.disk.tail.value.length -= 1
            if self.write_ptr.value.file_id == self.read_ptr.value.file_id:
                # Extend existing Block
                self.write_ptr.value.length += 1
            else:
                # Write new file block
                block_sector = (
                    self.write_ptr.value.start_location + self.write_ptr.value.length
                )
                self.disk.insert_after(
                    FileBlock(block_sector, self.read_ptr.value.file_id, 1),
                    self.write_ptr,
                )
            if self.disk.tail.value.length == 0:
                self.disk.tail = self.disk.tail.previous
                del self.disk.tail.next
                self.disk.tail.next = None

    def compact_no_frag(self):
        """Move all files into free space but do not fragment them"""
        file_handle = self.disk.tail
        for index in range(file_handle.value.file_id, -1, -1):
            file_handle = self.disk.tail
            while file_handle.value.file_id != index:
                file_handle = file_handle.previous
                if file_handle is None:
                    raise ValueError
            file_size = file_handle.value.length
            previous_file = self.find_space(file_size)
            if previous_file is None:
                continue
            if file_handle.value.start_location > previous_file.value.start_location:
                self.disk.move(file_handle, previous_file)
        pass

    def find_space(self, length):
        """Return location of first contiguous place of length"""
        pointer = self.disk.head
        size = 0
        while size < length:
            if pointer is self.disk.tail:
                return None
            size = (
                pointer.next.value.start_location
                - pointer.value.start_location
                - pointer.value.length
            )
            pointer = pointer.next
        return pointer.previous

    def calc_checksum(self):
        pointer = self.disk.head
        checksum = 0
        while pointer is not None:
            file = pointer.value
            checksum += sum(
                index * file.file_id
                for index in range(
                    file.start_location, file.start_location + file.length
                )
            )
            pointer = pointer.next

        return checksum
