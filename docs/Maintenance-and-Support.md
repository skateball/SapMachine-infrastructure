Maintenance describes the planned and scheduled work which is necessary to keep a product running and secure. Support, on the other hand, is an ad-hoc, on-request effort to fix a specific problem in a product. 

SapMachine updates will be available at no-costs for the full maintenance period. SAP also [offers professional support](https://support.sap.com/en/offerings-programs.html#section_792055716) to all SAP customers who use SapMachine in the context of SAP supported products.

OpenJDK provides a new feature release every six months, and a maintenance/security update based upon each active release every three months. We will follow this schedule for publishing binary releases from SapMachine to ensure you get the latest, most secure builds. 

In addition, every two years one feature release will be designated as Long Term Supported (LTS) release. We will support LTS releases for at least four years. This assurance will allow you to stay on a well-defined code stream, and give you time to migrate to the next, new, stable, LTS release when it becomes available. 

## Supported Releases
The following table lists the lifecycle dates of the current and some upcoming SapMachine releases:

| Release    | General Availability | End of Life |
|------------|--------------------|-------------|
| SapMachine 17 (LTS) | 09/2021 | 09/2026 |
| SapMachine 21 (LTS) | 09/2023 | 09/2028 |
| SapMachine 24 | 03/2025 | 09/2025 |
| SapMachine 25 (LTS) | planned for 09/2025 | 09/2030 |
| ...           | ...     | ...     |

## Supported Platforms
SapMachine supports the following platforms: 
* Linux arm64/aarch64
* Linux ppc64le (little endian)
* Linux x64 (glibc)
* Linux x64 for Alpine/musl (since SapMachine 20 and 17.0.7)
* macOS aarch64 (since SapMachine 17)
* macOS x64 (until SapMachine 24)
* Windows x64
* AIX (since SapMachine 21.0.2)

## Unsupported Releases
This table contains an overview of releases that are out of support:

| Release    | General Availability | End of Life |
|------------|--------------------|-------------|
| SapMachine 11 (LTS) | 09/2018 | 12/2024 ** |
| SapMachine 12 | 03/2019 | 09/2019 |
| SapMachine 13 | 09/2019 | 03/2020 |
| SapMachine 14 | 03/2020 | 09/2020 |
| SapMachine 15 | 09/2020 | 03/2021 |
| SapMachine 16 | 03/2021 | 09/2021 |
| SapMachine 18 | 03/2022 | 09/2022 |
| SapMachine 19 | 09/2022 | 03/2023 |
| SapMachine 20 | 03/2023 | 09/2023 |
| SapMachine 22 | 03/2024 | 09/2024 |
| SapMachine 23 | 09/2024 | 03/2025 |

\** In 2024, we stopped the backporting efforts for all platforms on SapMachine 11. For SAP-internal reasons, additional releases for **_only Linux x64 (glibc)_** will be built for a limited time and may be discontinued without further notice. We strongly recommend migrating to at least **SapMachine&nbsp;21&nbsp;LTS**.

## Unsupported Platforms
SapMachine support for the following platforms ended: 
* Linux ppc64be (big endian); only supported up to SapMachine 15 and SapMachine 11.0.11 (GA 04/2021) 