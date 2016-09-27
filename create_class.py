#!/usr/bin/env python

import os, sys

def getSource(className, nameSpace):
    headerSrc = \
'''#ifndef _<NAMESPACE>_<CLASSNAME>_H_
#define _<NAMESPACE>_<CLASSNAME>_H_

namespace <NameSpace> {

class <ClassName>
{
public:
    <ClassName>();

private:
};

} // namespace <NameSpace>

#endif // _<NAMESPACE>_<CLASSNAME>_H_'''

    cppSrc = \
'''#include "<ClassName>.h"

using <NameSpace>::<ClassName>;

<ClassName>::<ClassName>()
{
}'''
    headerSrc = headerSrc.replace('<ClassName>', className)
    headerSrc = headerSrc.replace('<NameSpace>', nameSpace)
    headerSrc = headerSrc.replace('<CLASSNAME>', className.upper())
    headerSrc = headerSrc.replace('<NAMESPACE>', nameSpace.upper())
    cppSrc = cppSrc.replace('<ClassName>', className)
    cppSrc = cppSrc.replace('<NameSpace>', nameSpace)
    return (headerSrc, cppSrc)

def writeFile(filePath, srcStr):
    if os.path.exists(filePath):
        print(filePath + ' already exsits!')
        return
    f = open(filePath, 'w')
    f.write(srcStr)
    f.close()

def main():
    argn = len(sys.argv)

    if argn != 2 and argn != 3:
        print('usage: create.py [ClassName] [NameSpace]')
        return

    nameSpace = 'fei'
    className = sys.argv[1]

    if argn > 2:
        nameSpace = sys.argv[2]

    hPath = os.path.abspath(className + '.h')
    ccPath = os.path.abspath(className + '.cc')

    hSrc, ccSrc = getSource(className, nameSpace)

    writeFile(hPath, hSrc)
    writeFile(ccPath, ccSrc)

if __name__ == '__main__':
    main()
