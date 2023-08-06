## Chapter 24 - Module Packages

### Source Code Directory

### Package Import Example
* package\_import\_example
    * package\_import\_example.py
    * from\_vs\_import\_with\_packages.py
    * dir1
        * \_\_init\_\_.py
        * dir1/dir2/\_\_init\_\_.py
        * dir1/dir2/mod.py

### Package Relative Imports
* package\_relative\_imports
    * imports\_outside\_packages
        * py2x
            * inside\_package
                * inside.py
                * string.py
            * outside\_package
                * outside.py
        * py3x
            * inside\_package
                * inside.py
                * string.py
            * outside\_package
                * outside.py
    * imports\_within\_packages
        * py2x
            * imports\_within\_packages.py
            * pkg/\_\_init\_\_.py
            * pkg/eggs.py
            * pkg/spam.py
        * py3x
            * imports\_within\_packages.py
            * pkg/eggs.py
    * imports\_are\_still\_relative\_to\_cwd
        * py2x
            * imports\_are\_relative\_to\_cwd.py
            * string.py
            * pkg/\_\_init\_\_.py
            * pkg/eggs.py
            * pkg/spam.py
        * py3x
            * imports\_are\_relative\_to\_cwd.py
            * string.py
            * pkg/eggs.py
            * pkg/spam.py
    * selecting\_modules\_with\_relative\_and\_absolute\_imports
        * py2x
            * absolutely\_not
                * absolutely\_not.py
                * pkg/\_\_init\_\_.py
                * pkg/spam.py
                * pkg/string.py
            * relative
                * relative.py
                * pkg/\_\_init\_.py
                * pkg/spam.py
                * pkg/string.py
        * py3x
            * absolute
                * absolute.py
                * pkg/spam.py
                * pkg/string.py
            * relative
                * relative.py
                * pkg/spam.py
                * pkg/string.py
    * imports\_are\_still\_relative\_to\_cwd\_again
        * py2x
            * absolutely\_not
                * absolutely\_not.py
                * string.py
                * \_\_init\_\_.py
                * pkg/\_\_init\_\_.py
                * pkg/spam.py
                * pkg/string.py
            * relative
                * \_\_init\_\_.py
                * relative.py
                * string.py
                * pkg/\_\_init\_\_.py
                * pkg/spam.py
                * pkg/string.py
        * py3x
            * absolute
                * absolute.py
                * string.py
                * pkg/spam.py
                * pkg/string.py
            * relative
                * relative.py
                * string.py
                * pkg/spam.py
                * pkg/string.py

### Pitfalls of Package-Relative Imports: Mixed Use
* pitfalls\_of\_package\_relative\_imports
    * fix\_01\_package\_subdirectories
        * package\_subdirectories.py
        * pkg/main.py
        * pkg/sub/eggs.py
        * pkg/sub/spam.py
    * fix\_02\_full\_path\_absolute\_import
        * full\_path\_absolute\_import.py
        * pkg/eggs.py
        * pkg/main.py
        * pkg/spam.py
    * application\_to\_module\_self\_test\_code
        * dualpkg\_test.py
        * dualpkg/m1.py
        * dualpkg/m2.py

### Namespace Packages in Action
* namespace\_packages\_in\_action
    * ns1
        * ns1.py
        * dir1/sub/mod1.py
        * dir2/sub/mod2.py
    * ns2
        * ns2.py
        * dir1/sub/mod1.py
        * dir2/sub/mod2.py
    * ns3
        * ns3.py
        * dir1/sub/mod1.py
        * dir2/sub/mod2.py

### Namespace Package Nesting
* namespace\_package\_nesting
    * ns1
        * ns1.py
        * dir1/sub/mod1.py
        * dir2/sub/mod2.py
        * dir2/sub/lower/mod3.py
    * ns2
        * ns2.py
        * dir1/sub/mod1.py
        * dir1/sub/pkg/\_\_init\_\_.py
        * dir2/sub/mod2.py
        * dir2/lower/mod3.py

### Files Still Have Precedence Over Directories
* files\_still\_have\_precedence\_over\_directories
    * files\_still\_have\_precedence\_over\_directories.py
    * ns2
    * ns3
        * dir/ns2.py
    * ns4
        * dir1/sub
        * dir2/sub
