#!/bin/sh

VERSION=`cat VERSION`

# Creating git tag
echo "Creating tag version ${VERSION}:"
git tag -a ${VERSION} -m 'Bump version ${VERSION}'

echo "Consider doing: git push origin ${VERSION}"
