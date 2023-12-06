CC = gcc
CXX = g++
CPPFLAGS = -Wall -g -O2

EXE = day3
SRC_FILES = day3.cpp ../utils.cpp

all: $(EXE)

$(EXE): $(SRC_FILES)
	$(CXX) $(CPPFLAGS) -o $@ $^

clean:
	rm -f $(EXE)
