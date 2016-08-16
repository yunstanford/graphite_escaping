# graphite_escaping

Graphite expects everything to be just ASCII to split/processing them, and then make directories based on metric name.
So any special name not allow to appear in directory/file name is not supported by Graphite.

		# pound			< left angle bracket	$ dollar sign			+ plus sign
		% percent		> right angle bracket	! exclamation point		` backtick
		& ampersand		* asterisk				‘ single quotes			| pipe
		{ left bracket	? question mark			“ double quotes			= equal sign
		} right bracket	/ forward slash			: colon	 
		\ back slash	blank spaces			@ at sign


Preferred Naming metrics schema:
```
	<namespace>.<instrumented section>.<target (noun)>.<action (past tense verb)>
```


## Limitation and explaination:

Since we are using IDNA(International Domain Name in Application) rules, there are several limitations we should pay attention to.

The conversions between ASCII and non-ASCII forms of a domain name are accomplished by algorithms called ToASCII and ToUnicode. 
These algorithms are not applied to the domain name as a whole, but rather to individual labels. For example, 
if the domain name is www.example.com, then the labels are www, example, and com. ToASCII or ToUnicode are applied 
to each of these three separately.

The details of these two algorithms are complex, and are specified in RFC 3490. The following gives an overview of their function.

ToASCII leaves unchanged any ASCII label, but will fail if the label is unsuitable for the Domain Name System. 
If given a label containing at least one non-ASCII character, ToASCII will apply the Nameprep algorithm, which converts the 
label to lowercase and performs other normalization, and will then translate the result to ASCII using Punycode[16] before 
prepending the four-character string "xn--".[17] This four-character string is called the ASCII Compatible Encoding (ACE) prefix, 
and is used to distinguish Punycode encoded labels from ordinary ASCII labels. The ToASCII algorithm can fail in several ways; 
for example, the final string could exceed the 63-character limit of a DNS name. A label for which ToASCII fails cannot be used 
in an internationalized domain name.

FAIL CASES:

1. '.fd': starting with 'dot' 
2. 'a..a': continuous 'dot'
3. very long string: exceed the 63-character



## For special characters :

1. 	The dot (.) is a special character because it delineates each metric’s path component, 
	but this is an easy fix; just substitute all dots for underscores or '%2E'. 
	For example, www.zillow.com => www_zillow_com
	
2   For the rest of the special characters(except dot), just URL any metric name with 
	special characters to make it valid for Graphite, and then URL decode it when we need to
	reconstruct the information


## Test

```
python test.py
```


