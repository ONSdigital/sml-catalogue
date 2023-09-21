The Statistical Methods Library (SML) and the associated methods are versioned using semantic versioning comprised of a major, minor and patch release version separated by full stops (e.g 3.5.4). 

There are separate releases of the libraries based on the method implementation, python/pandas or python/pySpark, and each library uses semantic versioning.

The major version is incremented (and minor and patch releases reset to zero) when backward incompatible changes are made (e.g renaming a pre-existing method function name).

The minor version is incremented (and the patch version reset to zero) when new features are added without breaking backward compatibility (e.g addition of a new statistical method)

The patch release version is incremented when backward compatible bugfixes are implemented.

Consult the [SML python/pySpark release history in Github](https://github.com/ONSdigital/statistical-methods-library/releases) for the current and past releases for the python/pySpark methods and the [associated python/pySpark release notes](https://github.com/ONSdigital/statistical-methods-library/tree/main/docs/release-notes) to understand the changes between releases.

Consult the [SML python/pandas release history in Github](https://github.com/ONSdigital/sml-python-small/releases) for the current and past releases for the python/pandas methods and the [associated python/pandas release notes](https://github.com/ONSdigital/sml-python-small/tree/main/docs/release-notes) to understand the changes between releases.

For further information about semantic versioning read the recommended [semantic versioning guidance](https://semver.org).