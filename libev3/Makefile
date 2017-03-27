## Copyright (c) 2015 Ahmad Fatoum
#override PREFIX = /home/selles/ev3/test/arm-2009q1/bin/
override PREFIX = /usr/bin/
#CC = $(PREFIX)arm-none-linux-gnueabi-gcc
CC = $(PREFIX)arm-linux-gnueabi-gcc-6
#AR = $(PREFIX)arm-none-linux-gnueabi-ar
AR = $(PREFIX)arm-linux-gnueabi-ar
SRCS = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SRCS))

.DEFAULT: libev3api.a
libev3api.a: $(OBJS)
	$(AR) rcs $@ $^
	
%.o: %.c
	$(CC) -Os -isystem. -c $<

#ifeq ($(OS),Windows_NT)
#RM = del /Q
#endif

.PHONY: clean
clean:
	$(RM) *.o *.a *.d
