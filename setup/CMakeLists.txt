cmake_minimum_required(VERSION 3.16)
project(SetupCheck LANGUAGES CXX)

add_executable(setup-check main.cpp)
target_compile_features(setup-check PRIVATE cxx_std_17)
