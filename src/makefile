CC = gcc
CFLAGS = -shared -fPIC
INCLUDES = -I.

OBJ_DIR = ../obj
DLL_DIR = ../dll
HEADER_DIR = ./headers

OBJS_GRAFO = $(OBJ_DIR)/grafo.o
OBJS_ASTAR = $(OBJ_DIR)/astar.o $(OBJS_GRAFO)
OBJS_DIJKSTRA = $(OBJ_DIR)/dijkstra.o $(OBJS_GRAFO)

all: $(DLL_DIR)/grafo.dll $(DLL_DIR)/astar.dll $(DLL_DIR)/dijkstra.dll

$(DLL_DIR)/grafo.dll: $(OBJS_GRAFO) | $(DLL_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(DLL_DIR)/astar.dll: $(OBJS_ASTAR) | $(DLL_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(DLL_DIR)/dijkstra.dll: $(OBJS_DIJKSTRA) | $(DLL_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: %.c $(HEADER_DIR)/grafo.h | $(OBJ_DIR)
	$(CC) -fPIC -c $(INCLUDES) -o $@ $<

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(DLL_DIR):
	mkdir -p $(DLL_DIR)

reset:
	rm -f $(OBJ_DIR)/*.o $(DLL_DIR)/*.dll
