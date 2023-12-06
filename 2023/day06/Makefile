CC = gcc
CXX = g++
CPPFLAGS = -Wall -g -O2

EXE = day6
SRC_FILES =day6.cpp ../utils.cpp

all: $(EXE)

$(EXE): $(SRC_FILES)
	$(CXX) $(CPPFLAGS) -o $@ $^
	./$(EXE)

clean:
	rm -f $(EXE)
