# ethash: C/C++ implementation of Ethash, the Ethereum Proof of Work algorithm.
# Copyright 2019 Pawel Bylica. Edit by 2022 Andrei Kondakov
# SPDX-License-Identifier: Apache-2.0

include(GNUInstallDirs)

add_library(blake2b)
add_library(ethash::blake2b ALIAS blake2b)
target_compile_features(blake2b PUBLIC c_std_99)
set_target_properties(blake2b PROPERTIES C_EXTENSIONS OFF)
target_include_directories(blake2b PUBLIC $<BUILD_INTERFACE:${include_dir}>$<INSTALL_INTERFACE:include>)
target_sources(blake2b PRIVATE
    ${include_dir}/ethash/blake2b.h
    ${include_dir}/ethash/blake2b.hpp
    blake2b.c
)

install(
    TARGETS blake2b
    EXPORT ethashTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
