from disk import Disk
from day9_input import day9_input, day9_example


def main():
    data = list("12345")
    data = day9_input
    disk = Disk()
    file_id = 0
    disk_sector = 0
    for i, block_length in enumerate(data):
        if i % 2 == 0:
            disk.store_file(file_id, disk_sector, block_length)
            file_id += 1
        disk_sector += int(block_length)

    # disk.compact()
    # ans = disk.calc_checksum()
    # print(f"Day 9 Part 1: {ans}")

    disk = Disk()
    file_id = 0
    disk_sector = 0
    for i, block_length in enumerate(data):
        if i % 2 == 0:
            disk.store_file(file_id, disk_sector, block_length)
            file_id += 1
        disk_sector += int(block_length)

    disk.compact_no_frag()
    ans = disk.calc_checksum()
    print(f"Day 9 Part 2: {ans}")


if __name__ == "__main__":
    main()
