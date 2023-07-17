CC := gcc
CFLAGS :=-g -Wall -Wextra -Wconversion -pedantic -std=gnu11
BINS=randomalloc batchalloc leakyalloc

.PHONY: all clean
all: $(BINS)

%alloc: %alloc.o allocator.o
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $^ -o $@

clean:
	rm -rf *.o $(BINS)
