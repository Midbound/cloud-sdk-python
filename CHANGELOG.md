# Changelog

## 0.5.0 (2026-05-13)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/Midbound/cloud-sdk-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([2791b54](https://github.com/Midbound/cloud-sdk-python/commit/2791b54c0b3e33a31c45002c00cd096e184d66eb))
* **internal/types:** support eagerly validating pydantic iterators ([3d39097](https://github.com/Midbound/cloud-sdk-python/commit/3d390976df9ad4a90b781ec9cf7c1679e90815e8))
* support setting headers via env ([00e752d](https://github.com/Midbound/cloud-sdk-python/commit/00e752d2889ebe5da584b5a7f741050c7780fb5e))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([6790398](https://github.com/Midbound/cloud-sdk-python/commit/6790398c9f84dc06f1830256ed27477c8387a827))
* **client:** preserve hardcoded query params when merging with user params ([e686e91](https://github.com/Midbound/cloud-sdk-python/commit/e686e91cc03da418be0c5af50dff4a54b34ed642))
* ensure file data are only sent as 1 parameter ([a1b8e4c](https://github.com/Midbound/cloud-sdk-python/commit/a1b8e4cab99d8ff9de3c3dda49e4a13182358ff6))
* use correct field name format for multipart file arrays ([1ed5c6b](https://github.com/Midbound/cloud-sdk-python/commit/1ed5c6b71c9559a3bac351164759efdbc7b76dc5))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([444e6ef](https://github.com/Midbound/cloud-sdk-python/commit/444e6efc1f43e14897e60d5aa66383742e215623))


### Chores

* **internal:** more robust bootstrap script ([8d180df](https://github.com/Midbound/cloud-sdk-python/commit/8d180df54b7c59131bf04c834b24a9c03990a584))
* **internal:** reformat pyproject.toml ([3b57078](https://github.com/Midbound/cloud-sdk-python/commit/3b57078a4258b3d00c425c187e43e0bb957a7c3d))

## 0.4.0 (2026-03-27)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/Midbound/cloud-sdk-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([a531c56](https://github.com/Midbound/cloud-sdk-python/commit/a531c569a3ef667397b8cf56f58b38f8e1f981df))
* **internal:** implement indices array format for query and form serialization ([b89ee20](https://github.com/Midbound/cloud-sdk-python/commit/b89ee20a1be3d17df7fa5d015e7ee487d7e91600))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([2c29c75](https://github.com/Midbound/cloud-sdk-python/commit/2c29c75d50a6482dc1f38f45a03b588ecc3c7963))
* **pydantic:** do not pass `by_alias` unless set ([62e9450](https://github.com/Midbound/cloud-sdk-python/commit/62e9450fb66e1ec46100b959d3cb4c5d79b9dbb9))
* sanitize endpoint path params ([e6a153c](https://github.com/Midbound/cloud-sdk-python/commit/e6a153c0fa730aa47647180f043ee6ad15f5617f))


### Chores

* **ci:** bump uv version ([8aac007](https://github.com/Midbound/cloud-sdk-python/commit/8aac0073dfffc62a710cbf47c11a3c406718c3f5))
* **ci:** skip lint on metadata-only changes ([8d69dcd](https://github.com/Midbound/cloud-sdk-python/commit/8d69dcd3adf4bc09c1bbf990dc179a5da7a1f05a))
* **ci:** skip uploading artifacts on stainless-internal branches ([3d7bf8b](https://github.com/Midbound/cloud-sdk-python/commit/3d7bf8b77f2b41239695deab071b663f5bdcad86))
* **dependencies:** require standardwebhooks 1.0.1 ([ae3f965](https://github.com/Midbound/cloud-sdk-python/commit/ae3f9654208386fa89d8265fee12d746b6cb883a))
* **internal:** add request options to SSE classes ([cc60ab9](https://github.com/Midbound/cloud-sdk-python/commit/cc60ab9eda5d42aac93b6590dd90f957dad2114b))
* **internal:** codegen related update ([ac3b1bc](https://github.com/Midbound/cloud-sdk-python/commit/ac3b1bc3356de67786f4d780c354553e6f55fd08))
* **internal:** make `test_proxy_environment_variables` more resilient ([e381350](https://github.com/Midbound/cloud-sdk-python/commit/e381350a5a5285183d35cd712c1e5cf62905a372))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([59a3e58](https://github.com/Midbound/cloud-sdk-python/commit/59a3e58cf7113621a96faec214255b4992ebcece))
* **internal:** refactor authentication internals ([2d8511a](https://github.com/Midbound/cloud-sdk-python/commit/2d8511a1865f35ceb482a88ef60e1b5c769f7536))
* **internal:** tweak CI branches ([b20aacd](https://github.com/Midbound/cloud-sdk-python/commit/b20aacd8faf9ba2fe9192ae840d2e358f1eb90a5))
* **internal:** update gitignore ([35aad80](https://github.com/Midbound/cloud-sdk-python/commit/35aad809646b6c5f72443d0f3d45b10f6340382e))
* **tests:** update webhook tests ([ca2ede7](https://github.com/Midbound/cloud-sdk-python/commit/ca2ede7957e8b7835df238989024de132ad30881))

## 0.3.0 (2026-02-22)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/Midbound/cloud-sdk-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([f8c444e](https://github.com/Midbound/cloud-sdk-python/commit/f8c444e4b82dadec774ee7e71d8d1252d9ea716d))
* **api:** api update ([4ef5a0b](https://github.com/Midbound/cloud-sdk-python/commit/4ef5a0b8c0288672011d972445c2af0ed0f9b92d))


### Chores

* **internal:** remove mock server code ([712f0af](https://github.com/Midbound/cloud-sdk-python/commit/712f0af491e973c3d9558cd554e6358a61a05c93))
* update mock server docs ([a075a5e](https://github.com/Midbound/cloud-sdk-python/commit/a075a5ee2b638b084c2dabb5b528104779e95757))

## 0.2.0 (2026-02-15)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/Midbound/cloud-sdk-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** manual updates ([fe18784](https://github.com/Midbound/cloud-sdk-python/commit/fe18784386c780eeab5912a929c4bbe08a03708d))


### Chores

* update SDK settings ([2e3428c](https://github.com/Midbound/cloud-sdk-python/commit/2e3428c343febda12d97cca3801c377bb94cf20f))
* update SDK settings ([adc60a5](https://github.com/Midbound/cloud-sdk-python/commit/adc60a5a3504130eac1dffb9e475f1dc6be948e7))
* update SDK settings ([c41b5f1](https://github.com/Midbound/cloud-sdk-python/commit/c41b5f1b568c1dd943bc74048519bc089d127604))

## 0.1.0 (2026-02-15)

Full Changelog: [v0.0.4...v0.1.0](https://github.com/Midbound/cloud-sdk-python/compare/v0.0.4...v0.1.0)

### Features

* **api:** manual updates ([08c7382](https://github.com/Midbound/cloud-sdk-python/commit/08c7382932977f9c925946df45152ba55b6bfeea))
* **api:** manual updates ([cef8f12](https://github.com/Midbound/cloud-sdk-python/commit/cef8f121e0ad6103cb2cd4b7baf903aa3d2543fe))
* **api:** manual updates ([48df30a](https://github.com/Midbound/cloud-sdk-python/commit/48df30aff69b296f418c4e36b46e32d78e5ed0b6))
* **api:** manual updates ([74a14b7](https://github.com/Midbound/cloud-sdk-python/commit/74a14b7b43786bb140839a64a0f3916f81a5f8ce))


### Chores

* update SDK settings ([1967eea](https://github.com/Midbound/cloud-sdk-python/commit/1967eea356514c256c6aeb9569bc42a5836b1550))
* update SDK settings ([a7a6e45](https://github.com/Midbound/cloud-sdk-python/commit/a7a6e45451f7097aa2c1bc6698d4707dcf5db589))
* update SDK settings ([5bd28e4](https://github.com/Midbound/cloud-sdk-python/commit/5bd28e47a32eb8178ba14b1e2f4b5abf8fb8fd73))

## 0.0.4 (2026-02-14)

Full Changelog: [v0.0.3...v0.0.4](https://github.com/Midbound/cloud-sdk-python/compare/v0.0.3...v0.0.4)

### Chores

* update SDK settings ([4931289](https://github.com/Midbound/cloud-sdk-python/commit/4931289c071b508236c8ab6a54bfb1889b447048))
* update SDK settings ([fba3263](https://github.com/Midbound/cloud-sdk-python/commit/fba32638fb12acb1ac0daeae83702099c39b5f69))

## 0.0.3 (2026-02-14)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/Midbound/cloud-sdk-python/compare/v0.0.2...v0.0.3)

### Chores

* update SDK settings ([3dd6fc8](https://github.com/Midbound/cloud-sdk-python/commit/3dd6fc81ff75d4f8a042187a63029317c8a926d5))
* update SDK settings ([5a4b563](https://github.com/Midbound/cloud-sdk-python/commit/5a4b563ddda41dc34f09791ff79a7b03ff74b2c9))

## 0.0.2 (2026-02-14)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/Midbound/cloud-sdk-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([803e543](https://github.com/Midbound/cloud-sdk-python/commit/803e543054b282d7d6fd89e14ea03ef34b707bf6))
* update SDK settings ([621e9f4](https://github.com/Midbound/cloud-sdk-python/commit/621e9f44c22f53a5645e77b7ff77ce5d5b33949d))
* update SDK settings ([9039d94](https://github.com/Midbound/cloud-sdk-python/commit/9039d941640eed78ac9e0ed93315d41fdb47bf04))
* update SDK settings ([4e5d545](https://github.com/Midbound/cloud-sdk-python/commit/4e5d54533d50ad0e955a97cff6dd86b22f33f899))
