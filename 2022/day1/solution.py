import heapq
import sys

def main(input_file, top_n):
    heap = []
    with open(input_file, "r") as file:
        total_per_elf = 0
        for line in file:
            try:
                total_per_elf -= int(line)  # min-heap
            except ValueError:
                heapq.heappush(heap, total_per_elf)
                total_per_elf = 0
    total = 0
    for _ in top_n:
        total += heapq.heappop(heap) * -1  # make positive
    print(total)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
