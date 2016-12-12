PKG_NAME := jdk-htmlunit-core-js
URL := https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-2.17.tar.gz
ARCHIVES := https://github.com/HtmlUnit/htmlunit-rhino-fork/archive/ef0faa3e34ef6c3b42c1be4474d0252d96eb4535/htmlunit-rhino-fork-ef0faa3e34ef6c3b42c1be4474d0252d96eb4535.tar.gz %{buildroot}

include ../common/Makefile.common
