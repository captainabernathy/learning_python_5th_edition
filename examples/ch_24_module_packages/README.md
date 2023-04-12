## Chapter 24 - Module Packages

## Programs

### Package Import Example
* **package_import_example/**
    * **package_import_example.py**
    * **from_vs_import_with_packages.py**
    * **dir1/**
        * **__init__.py**
        * **dir1/dir2/__init__.py**
        * **dir1/dir2/mod.py**

### Package Relative Imports
* **package_relative_imports/**
    * **imports_outside_packages/**
        * **py2x/**
            * **inside_package/**
                * **inside.py**
                * **string.py**
            * **outside_package/**
                * **outside.py**
        * **py3x/**
            * **inside_package/**
                * **inside.py**
                * **string.py**
            * **outside_package/**
                * **outside.py**
    * **imports_within_packages/**
        * **py2x/**
            * **imports_within_packages.py**
            * **pkg/__init__.py**
            * **pkg/eggs.py**
            * **pkg/spam.py**
        * **py3x/**
            * **imports_within_packages.py**
            * **pkg/eggs.py**
    * **imports_are_still_relative_to_cwd/**
        * **py2x/**
            * **imports_are_relative_to_cwd.py**
            * **string.py**
            * **pkg/__init__.py**
            * **pkg/eggs.py**
            * **pkg/spam.py**
        * **py3x/**
            * **imports_are_relative_to_cwd.py**
            * **string.py**
            * **pkg/eggs.py**
            * **pkg/spam.py**
    * **selecting_modules_with_relative_and_absolute_imports/**
        * **py2x/**
            * **absolutely_not/**
                * **absolutely_not.py**
                * **pkg/__init__.py**
                * **pkg/spam.py**
                * **pkg/string.py**
            * **relative/**
                * **relative.py**
                * **pkg/__init_.py**
                * **pkg/spam.py**
                * **pkg/string.py**
        * **py3x/*
            * **absolute/**
                * **absolute.py**
                * **pkg/spam.py**
                * **pkg/string.py**
            * **relative/**
                * **relative.py**
                * **pkg/spam.py**
                * **pkg/string.py**
    * **imports_are_still_relative_to_cwd_again/**
        * **py2x/**
            * **absolutely_not/**
                * **absolutely_not.py**
                * **string.py**
                * **__init__.py**
                * **pkg/__init__.py**
                * **pkg/spam.py**
                * **pkg/string.py**
            * **relative/**
                * **__init__.py**
                * **relative.py**
                * **string.py**
                * **pkg/__init__.py**
                * **pkg/spam.py**
                * **pkg/string.py**
        * **py3x/**
            * **absolute/**
                * **absolute.py**
                * **string.py**
                * **pkg/spam.py**
                * **pkg/string.py**
            * **relative/**
                * **relative.py**
                * **string.py**
                * **pkg/spam.py**
                * **pkg/string.py**

### Pitfalls of Package-Relative Imports: Mixed Use
* **pitfalls_of_package_relative_imports/**
    * **fix_01_package_subdirectories/**
        * **package_subdirectories.py**
        * **pkg/main.py**
        * **pkg/sub/eggs.py**
        * **pkg/sub/spam.py**
    * **fix_02_full_path_absolute_import/**
        * **full_path_absolute_import.py**
        * **pkg/eggs.py**
        * **pkg/main.py**
        * **pkg/spam.py**
    * **application_to_module_self_test_code/**
        * **dualpkg_test.py**
        * **dualpkg/m1.py**
        * **dualpkg/m2.py**

### Namespace Packages in Action
* **namespace_packages_in_action/**
    * **ns1/**
        * **ns1.py**
        * **dir1/sub/mod1.py**
        * **dir2/sub/mod2.py**
    * **ns2/**
        * **ns2.py**
        * **dir1/sub/mod1.py**
        * **dir2/sub/mod2.py**
    * **ns3/**
        * **ns3.py**
        * **dir1/sub/mod1.py**
        * **dir2/sub/mod2.py**

### Namespace Package Nesting
* **namespace_package_nesting/**
    * **ns1/**
        * **ns1.py**
        * **dir1/sub/mod1.py**
        * **dir2/sub/mod2.py**
        * **dir2/sub/lower/mod3.py**
    * **ns2/**
        * **ns2.py**
        * **dir1/sub/mod1.py**
        * **dir1/sub/pkg/__init__.py**
        * **dir2/sub/mod2.py**
        * **dir2/lower/mod3.py**

### Files Still Have Precedence Over Directories
* **files_still_have_precedence_over_directories/**
    * **files_still_have_precedence_over_directories.py**
    * **ns2/**
    * **ns3/**
        * **dir/ns2.py**
    * **ns4/**
        * **dir1/sub/**
        * **dir2/sub/**