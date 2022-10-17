/* ethash: C/C++ implementation of Ethash, the Ethereum Proof of Work algorithm.
 * Copyright 2018 Pawel Bylica.
 * Licensed under the Apache License, Version 2.0. See the LICENSE file.
 */

#pragma once

#include <ethash/hash_types.h>

#include <stddef.h>

#ifdef __cplusplus
#define NOEXCEPT noexcept
#else
#define NOEXCEPT
#endif

#ifdef __cplusplus
extern "C" {
#endif

union ethash_hash512 ethash_blake2b512(const uint8_t* data, size_t size) NOEXCEPT;
union ethash_hash512 ethash_blake2b512_64(const uint8_t data[64]) NOEXCEPT;

#ifdef __cplusplus
}
#endif
