CC = gcc
CXX = g++
CPPFLAGS = -Wall -g -O2

EXE = hello
SRC_FILES = hello.cpp ../utils.cpp

all: $(EXE)

$(EXE): $(SRC_FILES)
	$(CXX) $(CPPFLAGS) -o $@ $^

clean:
	rm -f $(EXE)
