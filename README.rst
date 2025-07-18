~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Basler Kantonalbank plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plugin to read ISO-20022 formatted statements with specific adaptation to BKB.

This project is derived from Andrey Lebedev's (andrey@lebedev.lt) ofstatement-iso20022 (https://github.com/nausicaea/ofxstatement-bkb) project.

Plugin supports the following configuration options:

* ``currency``: Account currency. In case currency is not specified in ISO20022 
  statement, you can specify it with this setting. Only statement lines with account 
  currency will be included in OFX files.
* ``iban``: Account IBAN. In case the IBAN is not specified in the ISO20022 statement, you need to specify this option.

Currently implementation is very trivial and naive. If it doesn't work for
you, feel free to improve it or file a bug on github with sample (anonymized)
state file.
