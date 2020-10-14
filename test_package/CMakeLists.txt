project(example CXX)
cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 17)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories("GistTest/test-signals")

add_executable(
    example main.cpp
    GistTest/test-signals/Test_Signals.cpp
    GistTest/Test_CoreFrequencyDomainFeatures.cpp
    GistTest/Test_CoreTimeDomainFeatures.cpp    
    GistTest/Test_Gist.cpp
    GistTest/Test_MFCC.cpp 
    GistTest/Test_OnsetDetectionFunction.cpp 
    GistTest/Test_Pitch.cpp
)

target_link_libraries(example stdc++fs ${CONAN_LIBS})






