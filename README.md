# Krpano Markup Language (KML)

Latest update: krpano 1.19-pr16

![Sample Screenshot](/res/syntaxkrpano.png)

Package inclides 
* Syntax definition of [krpano](http://krpano.com) panoramic viewer settings made for [SublimeText 3](http://www.sublimetext.com/3);
* Color theme "May Thunderstorm" for ST optimized to highlight KML code;
* Python Script to remove comments from src.

## Contents

* Installation
* Features
* Code formatting recomendations
* Modifying

## Installation ##

1. Clone or download this repo to some location;
2. Find `dist` folder in package and open it's contents;
3. Open Sublime Text, run Preferences –> Browse Packages... on Windows or Sublime Text -> Preferences -> Browse Packages on Mac;
4. Navigate to User folder;
5. Copy contents of `dist` folder into opened User folder;
6. Select Preferences - Color Scheme - User and then one of two themes: Monokai Extended or May Thunderstorm.

## Features ##

**I.**  Syntax definition is based on [official krpano documentation](http://krpano.com/docu), [plugin](http://krpano.com/plugins/) docs and is intended to recognize all structural entities(e.g. elements, properties or keywords) of KML.

Current list of recognized entities includes:
* Script perators (`( ) [ ] . , ; == === != !== < > <= >= ! &&(or AND) ||(or 'OR') BAND BOR XOR LT GT LE GE + - / * ^ <<(or LSHT) >>(or RSHT) `). All operators except brackets, dot and comma and semicolon used in code must be separated from operands by spaces;
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

**II.** KML has a wide amount of entities so it needs custom color theme to display them all. This package includes two themes:

* May Thunderstorm,  based on [Seti Monokai dark color scheme](https://github.com/jesseweed/seti-ui);
* Monokai, based on [Sublime Monokai Extended by Jon Schlinkert](https://github.com/jonschlinkert/sublime-monokai-extended)

Both tmemes support all other languages and are optimized to display Krpano syntax nicely.

**III.**    removeComments.py script removes single-line comments from KML source. This operation is required for correct code exec.

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

# Krpano snippets and completions (incomplete)

There is a set of shortcuts to cover majority of writing code cases. Please feel free to troubleshoot;

### Snippets (tags mixed with actions code)
* action – creates action;
* actjs – creates JS action with CDATA wrap;
* asynccall – creates asynchronous call (mode in krpano devlib ;)
* asyncfor;
* asyncloop;
* callwhen;
* cl – console.log() action (more in krpano devlib);
* data – data tag with CDATA wrap;
* delayedcall;
* events;
* for;
* hs – for hotspot tag;
* hsi – visibility controlled hotspot (more in krpano devlib);
* hsikt – same with keep set to true;
* if;
* ife – if-else operator;
* ifce – if with conditional else;
* ifnot;
* layer;
* lsi – visibility controlled layer (more in krpano devlib);
* lsikt – same with keep set to true;
* krpano;
* loop;
* plugin;
* setinterval;
* style;
* tag – for random tag;
* this – create this alias;
### Script autocompletions with alises
* fs – fullscreen;
* stw – stagewidth;
* sth – stageheight;
* sts – stagescale;
* bgc – bgcolor;
* devd – device.desktop;
* dtab – device.tablet;
* dmob – device.mobile;
* dhand – device.handheld;
* dcss – device.css3d;
* dwebgl – device.webgl;
* dtouch – device.touch;
* dios – device.ios;
* diphone – device.iphone;
* dipod – device.ipod;
* dipad – device.ipad;
* dandroid – device.android;
* dchrome – device.chrome;
* dchromob – device.chromemobile;
* dfirefox – device.firefox;
* die – device.ie;
* dedge – device.edge;
* dsafari – device.safari;
* dopera – device.opera;
* dwin – device.windows;
* dmac – device.mac;
* dlnx – device.linux;
* pi – Math.PI;
* mx – mouse.x;
* my – mouse.y;
* msx – mouse.stagex;
* msy – mouse.stagey;
* mdx – mouse.downx;
* mdy – mouse.downy;
* mcx – mouse.clickx;
* mcy – mouse.clicky;
* cp – copy($1, $2);
* cht – copy(this, hotspot[$2]);
* clt – copy(this, layer[$2]);
* ct – copy(this, $2);
* cc – copy($1, calc($2));
* abs – Math.abs($1);
* acos – Math.acos($1);
* asin – Math.asin($1);
* atan – Math.atan($1);
* atan2 – Math.atan2($1);
* ceil – Math.ceil($1);
* cos – Math.cos($1);
* exp – Math.exp($1);
* floor – Math.floor($1);
* log – Math.log($1);
* max – Math.max($1);
* min – Math.min($1);
* pow – Math.pow($1);
* round – Math.round($1);
* sin – Math.sin($1);
* sqrt – Math.sqrt($1);
* tan – Math.tan($1);
* cwh – callwith(hotspot[$1], $2);
* cwl – callwith(layer[$1], $2);
* cw – callwith($1, $2);
* ++ – ' + $1 + ' (for string operations in JS);
### XML autocompletions with alises
* ef – enabled="false";
* et – enabled="true";
* vf – visible="false";
* vt – visible="true";
* tt – type="text";
* tc – type="container";
* hct – handcursor="true";
* hcf – handcursor="false";
* ac – align="center";
* at – align="top";
* atr – align="righttop";
* art – align="righttop";
* ar – align="right";
* arb – align="rightbottom";
* abr – align="rightbottom";
* ab – align="bottom";
* alb – align="leftbottom";
* abl – align="leftbottom";
* al – align="left";
* alt – align="lefttop";
* atl – align="lefttop";
* et – edge="top";
* etr – edge="righttop";
* ert – edge="righttop";
* ec – edge="center";
* er – edge="right";
* erb – edge="rightbottom";
* ebr – edge="rightbottom";
* eb – edge="bottom";
* elb – edge="leftbottom";
* ebl – edge="leftbottom";
* el – edge="left";
* elt – edge="lefttop";
* etl – edge="lefttop";
* kt – keep="true";
* kf – keep="false";
* w100 – width="100%";
* h100 – height="100%";
* bgc – bgcolor="0x$1";
* bga – bgalpha="$1";
* bgb – bgborder="$1";
* bgf – bg="false";
* bgr – bgroundedge="$1";
* bgs – bgshadow="$1";
* txs – textshadow="$1";
* bgc – bgcapture="$1";
* ov – onover="\n\t$1\n";
* od – ondown="\n\t$1\n";
* oh – onhover="\n\t$1\n";
* oo – onout="\n\t$1\n";
* oc – onclick="\n\t$1\n";
* ou – onup="\n\t$1\n";
* ol – onloaded="\n\t$1\n";
* oa – onautosized="\n\t$1\n";
* ovr – onvideoready="\n\t$1\n";
* ovpl – onvideoplay="\n\t$1\n";
* ovpa – onvideopaused="\n\t$1\n";
* ovc – onvideocomplete="\n\t$1\n";
* ont – onneedtouch="\n\t$1\n";
* ong – ongottouch="\n\t$1\n";
* oe – onerror="\n\t$1\n";
* os – onscroll="\n\t$1\n";
* oexfs – onexitfullscreen="\n\t$1\n";
* oxc – onxmlcomplete="\n\t$1\n";
* opc – onpreviewcomplete="\n\t$1\n";
* olc – onloadcomplete="\n\t$1\n";
* onp – onnewpano="\n\t$1\n";
* orp – onremovepano="\n\t$1\n";
* ons – onnewscene="\n\t$1\n";
* oxe – onxmlerror="\n\t$1\n";
* ole – onloaderror="\n\t$1\n";
* okd – onkeydown="\n\t$1\n";
* oku – onkeyup="\n\t$1\n";
* osc – onsingleclick="\n\t$1\n";
* odc – ondoubleclick="\n\t$1\n";
* omd – onmousedown="\n\t$1\n";
* omu – onmouseup="\n\t$1\n";
* omw – onmousewheel="\n\t$1\n";
* ocm – oncontextmenu="\n\t$1\n";
* oi – onidle="\n\t$1\n";
* ovch – onviewchange="\n\t$1\n";
* ovchd – onviewchanged="\n\t$1\n";
* or – onresize="\n\t$1\n";
* oarsa – onautorotatestart="\n\t$1\n";
* oarso – onautorotatestop="\n\t$1\n";
* oaror – onautorotateoneround="\n\t$1\n";
* oarch – onautorotatechange="\n\t$1\n";
* oga – gyro_onavailable="\n\t$1\n";
* ogu – gyro_onunavailable="\n\t$1\n";
* oge – gyro_onenable="\n\t$1\n";
* ogd – gyro_ondisable="\n\t$1\n";
* owva – webvr_onavailable="\n\t$1\n";
* owvu – webvr_onunavailable="\n\t$1\n";
* owvud – webvr_onunknowndevice="\n\t$1\n";
* owven – webvr_onentervr="\n\t$1\n";
* owvex – webvr_onexitvr="\n\t$1\n";
* css1 – css="\n\tmargin: 0;\n";
* ovs – oversampling="2";
* crop – crop="$1|$2|$3|$4";
* oocrop – onovercrop="$1|$2|$3|$4";
* odcrop – ondowncrop="$1|$2|$3|$4";
* sic – style="invisible_content";
* sicv – style="invisible_content|visible";
* ic – invisible_content;
* xy – x="$1" y="$2";
* oxy – ox="$1" oy="$2";
* wh – width="$1" height="$2";
* w – width="$1";
* h – height="$1";
* pw – pixelwidth="$1";
* ph – pixelheight="$1";
* mct – maskchildren="true";
* hc – hotspot.count;
* lc - layer.count;
* arri – $1[get(i)].$2;
* kc – krpano.call('$1');
* ks – krpano.set('$1');
* kg – krpano.get('$1');
* cl – console.log($1);
* cd – console.divider();


Majority of other krpano words is also here.
