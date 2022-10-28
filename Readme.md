# Quantifying NPM Dependency Size

Counts the number of files and lines of JS/TS in every module in a node_modules folder.

## Details

This doesn't count JSON or other data files. Note that some of the included JavaScript files are redundant, due to the dependencies including multiple kinds of old module types or non-executable TypeScript definitions. If the number of semi-colons in a file is greater than the number of actual lines, the semi-colon count is used instead (to handle minified files fairly.) Scoped modules like @types/node are (correctly IMO) considered separate modules and not just part of some huge module called e.g. @types.

## Output

This program yields two CSVs - one with raw data and one containing the data for a histogram with buckets' intervals sized on a log scale - and one Markdown file with a table like the one below.

### Sample output

Sample smallest and largest dependencies for [https://github.com/toBeOfUse/SingleHandedTypist](SingleHandedTypist) (as of 10/28/2022):

| module name                                      | lines   | files |
| ------------------------------------------------ | ------- | ----- |
| css-color-names                                  | 0       | 0     |
| cssdb                                            | 0       | 0     |
| node-releases                                    | 0       | 0     |
| vendors                                          | 0       | 0     |
| globals                                          | 2       | 1     |
| svg-tags                                         | 2       | 1     |
| caller-path                                      | 4       | 1     |
| html-tags                                        | 4       | 2     |
| @vue/babel-preset-jsx                            | 5       | 1     |
| at-least-node                                    | 5       | 1     |
| import-cwd                                       | 5       | 1     |
| strict-uri-encode                                | 6       | 1     |
| is-plain-obj                                     | 7       | 1     |
| boolbase                                         | 8       | 1     |
| is-absolute-url                                  | 8       | 1     |
| @types/parse-json                                | 9       | 1     |
| @vue/babel-sugar-composition-api-inject-h        | 10      | 1     |
| is-arrayish                                      | 10      | 1     |
| mississippi                                      | 10      | 1     |
| only                                             | 10      | 1     |
| pkg-dir                                          | 10      | 1     |
| escape-string-regexp                             | 11      | 1     |
| minimalistic-assert                              | 11      | 1     |
| p-defer                                          | 11      | 1     |
| queue-microtask                                  | 11      | 2     |
| tty-browserify                                   | 11      | 1     |
| @vue/babel-sugar-composition-api-render-instance | 12      | 1     |
| @vue/babel-sugar-functional-vue                  | 12      | 1     |
| @vue/babel-sugar-inject-h                        | 12      | 1     |
| import-from                                      | 12      | 1     |
| mime-db                                          | 12      | 1     |
| @vue/babel-helper-vue-jsx-merge-props            | 13      | 1     |
| is-extendable                                    | 13      | 1     |
| lodash.\_reinterpolate                           | 13      | 1     |
| prepend-http                                     | 14      | 1     |
| unquote                                          | 14      | 1     |
| cache-content-type                               | 15      | 1     |
| has                                              | 15      | 2     |
| param-case                                       | 15      | 2     |
| for-in                                           | 16      | 1     |
| has-value                                        | 16      | 1     |
| is-resolvable                                    | 16      | 1     |
| strip-final-newline                              | 16      | 1     |
| unicode-match-property-ecmascript                | 16      | 1     |
| cssnano-util-get-arguments                       | 17      | 1     |
| isobject                                         | 17      | 2     |
| path-exists                                      | 17      | 1     |
| remove-trailing-separator                        | 17      | 1     |
| binary-extensions                                | 18      | 3     |
| constants-browserify                             | 18      | 1     |
| cssnano-util-get-match                           | 18      | 1     |
| cssnano-util-same-parent                         | 19      | 1     |
| mdn-data                                         | 19      | 4     |
| shebang-command                                  | 19      | 1     |
| is-extglob                                       | 20      | 1     |
| path-is-absolute                                 | 20      | 1     |
| ...                                              | ...     | ...   |
| yaml                                             | 15795   | 54    |
| svgo                                             | 15962   | 111   |
| bluebird                                         | 16684   | 41    |
| vue-template-es2015-compiler                     | 16883   | 2     |
| prosemirror-view                                 | 17896   | 15    |
| tippy.js                                         | 17953   | 11    |
| @vue/compiler-sfc                                | 18344   | 2     |
| postcss-preset-env                               | 19339   | 116   |
| csstype                                          | 20256   | 1     |
| vue-router                                       | 20574   | 46    |
| pako                                             | 22232   | 22    |
| css-tree                                         | 23041   | 119   |
| @tiptap/core                                     | 23674   | 304   |
| uglify-js                                        | 24774   | 14    |
| vue-server-renderer                              | 27123   | 25    |
| core-js                                          | 27206   | 3097  |
| csso                                             | 31902   | 164   |
| lodash                                           | 44947   | 1048  |
| @nuxt/babel-preset-app                           | 45886   | 1481  |
| es-abstract                                      | 46625   | 1370  |
| webpack                                          | 58795   | 368   |
| rxjs                                             | 77210   | 2474  |
| @types/node                                      | 77790   | 108   |
| @nuxt/webpack                                    | 80909   | 127   |
| tailwindcss                                      | 103610  | 188   |
| vue                                              | 125733  | 214   |
| prettier                                         | 185248  | 31    |
| @babel                                           | 257693  | 659   |
| TOTAL                                            | 2860264 | 21746 |
