cmake_minimum_required(
    VERSION 3.13
    FATAL_ERROR
)

add_executable(
    main
    src/main.cpp
    src/main.hpp
    src/bfs.cpp
    src/bfs.hpp
    src/dfs.cpp
    src/dfs.hpp
    src/floyd.cpp
    src/floyd.hpp
    src/kruskal.cpp
    src/kruskal.hpp
    src/prim.cpp
    src/prim.hpp
    src/pruefer.cpp
    src/pruefer.hpp
)

target_link_libraries(
    main
)