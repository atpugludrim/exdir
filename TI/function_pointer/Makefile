CC = gcc
OFLAGS = -c
caller: caller.o something.o
	$(CC) -o $@ $^

%.o: %.c
	$(CC) $(OFLAGS) $?

.PHONY: clean
clean:
	rm *.o caller
.PHONY: rmobj
rmobj:
	rm *.o
