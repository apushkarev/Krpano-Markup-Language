#Krpano Markup Language (KML)

![Sample Screenshot](/res/syntaxkrpano.png)

Package inclides 
* Syntax definition of [krpano](http://krpano.com) panoramic viewer settings made for [SublimeText 3](http://www.sublimetext.com/3);
* Color theme "May Thunderstorm" for ST optimized to highlight KML code;
* Python Script to remove comments from src.

##Contents

* Installation
* Features
* Code formatting recomendations
* Modifying

## Installation ##

1. Clone or download this repo to some location;
2. Find `dist` folder in package and open it's contents;
3. Open Sublime Text, run Preferences –> Browse Packages...;
4. Navigate to User folder;
5. Copy contents of `dist` folder into opened User folder;
6. Select Preferences - Color Scheme - User and then one of two themes: Monokai Extended or May Thunderstorm.

## Features ##

**I.**	Syntax definition is based on [official krpano documentation](http://krpano.com/docu), [plugin](http://krpano.com/plugins/) docs and is intended to recognize all structural entities(e.g. elements, properties or keywords) of KML.

Current list of recognized entities includes:
* Script perators (`( ) [ ] . , ; == === != !== < > <= >= ! &&(or AND) ||(or 'OR') LT GT LE GE + - / * ^ <<(or LSHT) >>(or RSHT) `). All operators except brackets, dot and comma and semicolon used in code must be separated from operands by spaces;
* Instruction words (see [Programming logic/Flow control](http://krpano.com/docu/actions/#actionsreference) section of krpano docs);
* Basic functions (all other pre-defined functions);
* [Global Variables](http://krpano.com/docu/actions/#globalvarsreference);
* Named constants;
* Pre-defined [elements](http://krpano.com/docu/xml);
* Pre-defined element properties;
* Action arguments;
* Hex numbers prefixed by 0x or #;
* Decimal numbers including % values;
* Single-line string constants;
* Single-line comments(following // until the end of the line**(1)**);
* XML tags.

**1. Single line C-styled comments are not supported niether in actions nor in event handlers. They should be removed from source code before execution.**
You can put XML-styled comments where it's possible by XML rules.

**II.**	KML has a wide amount of entities so it needs custom color theme to display them all. This package includes two themes:

* May Thunderstorm,  based on [Seti Monokai dark color scheme](https://github.com/jesseweed/seti-ui);
* Monokai, based on [Sublime Monokai Extended by Jon Schlinkert](https://github.com/jonschlinkert/sublime-monokai-extended)

Both tmemes support all other languages and are optimized to display Krpano syntax nicely.

**III.**	removeComments.py script removes single-line comments from KML source. This operation is required for correct code exec.

Requires [python environment](https://www.python.org/downloads/windows/)

At one call comments from one file are removed.

Usage:
	`python script_dir/remove_comments.py src_dir src_file output_dir1 output_dir2`

## Code formatting recomendations ##

### String recognition.

It happened that strings in double quotation marks (`""`) in KML are used for two purposes:
* as a string in XML attribute values for numbers, booleans and strings;
* as a code inside a string value.

This syntax highlighting recognizes difference between the two by code formatting. String value should not have next line symbol (`\n`) right after opening quotation mark:

`attribute="value"` would be recognized as string and highlighted as a string entirely;

    attribute="
	    some_code();
    "

would be recognized as a piece of script.

Strings inside single quotation marks are always recognized as string values.

### Code blocks separation.

KML does not have any specific separation symbols which would clearly show nesting of code blocks like curly brackets `{}` in C or JavaScript.

Such complicated cunstructions as `if` condition or loops, or delayedcalls or tweens are just functions that take values and blocks of code as arguments.

So the only way to divide blocks of code are demonstrative indentations which coder put into code.

For example,

    if (condition,
    	actions;
    ,
    	else actions;
    );

would be a nice and correct way to format condition statement.
For loops it might look like

    for (set(i, 0), i LT some_array.count, inc(i),
    	actions;
    );

As one can see comma is playing role of opening curly bracket and closing bracket with semicolon plays role of closing curly bracket.

This is the basic principle of KML code intendation: if you want to put some code into function arguments you write comma and then go to next line with one more tab. If you have finished with block of code, you go to next line. Then you go one tab back to the left and then put `);`  closing the function call.

This simple rule would make your code much easier to read and review. It also is used on screenshot above.

## Modifying ##
 
See [Syntax Definitions](http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html) chapter of ST unofficial manual,
use the same process to modify color scheme.