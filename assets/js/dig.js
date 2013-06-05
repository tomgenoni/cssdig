$(document).ready(function(){

    function compressArray(original) {

        var compressed = [];
        // make a copy of the input array
        var copy = original.slice(0);

        // first loop goes over every element
        for (var i = 0; i < original.length; i++) {

            var myCount = 0;
            // loop over every element in the copy and see if it's the same
            for (var w = 0; w < copy.length; w++) {
                if (original[i] == copy[w]) {
                    // increase amount of times duplicate is found
                    myCount++;
                    // sets item to undefined
                    delete copy[w];
                }
            }

            if (myCount > 0) {
                var a = new Object();
                a.value = original[i];
                a.count = myCount;
                compressed.push(a);
            }
        }

        return compressed;
    };

    function removeTab(arr) {
        clean_arr = []
        $.each(arr, function(i,d){
            d = d.replace(/\t/g, '');
            clean_arr.push(d)
        })
        return clean_arr;
    }

    function removeColon(arr) {
        clean_arr = []
        $.each(arr, function(i,d){
            d = d.replace(/:/g, '');
            clean_arr.push(d)
        })
        return clean_arr;
    }

    function removeDupes(arr) {
        var unique_arr = [];
        $.each(arr, function(i, el){
            if($.inArray(el, unique_arr) === -1) unique_arr.push(el);
        });
        return unique_arr
    }

    var cssString = " .avatar-change:hover{background-color:#EEE;}.unanswered strong{background:transparent;color:#9A4444!important;}.post-tag.selected{background-color:#c4dae9;}#newsletter-ad-header{font-size:110%;margin-top:70px !important;}.required-tag,.post-text .required-tag,.wmd-preview a.required-tag{border:2px solid #979797;}.example-title-field{width:590px;}.accordion-step{width:100%;}.accordion-header{border-style:solid;border-width:1px;padding:5px;background-color:#EEE;border-color:#E0E0E0;margin-bottom:10px;}.accordion-header h2 span{color:#888;}.question-autocomplete-holder{padding-top:10px;}.auto-complete-question-tile{border-bottom:1px solid #AAA;padding-bottom:20px;padding-top:20px;}#question-autocomplete-holder .auto-complete-question-tile:last-child{border-bottom-style:none;}.take-answer{font-size:120%;font-weight:bold;text-align:center;margin-top:5px;margin-bottom:5px;padding-top:6px;padding-bottom:7px;color:#000;background-color:#c0c0c0;cursor:pointer;width:150px;border:1px solid #999;}.take-answer:hover{background-color:#ff7a00;}.snippet-title{color:black;}.example-tag-container{border-style:solid;border-width:1px;border-color:black;}.auto-complete-question-tile-spacer{border-top:1px dotted #BBB;margin-top:15px;margin-bottom:15px;}#footer.categories #footer-sites th{color:#ccc;}#footer.categories #copyright{color:#ccc!important;}html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,font,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td{margin:0;padding:0;border:0;font-size:100%;vertical-align:baseline;background:transparent;}body{line-height:1;}ol,ul{list-style:none;}blockquote,q{quotes:none;}blockquote:before,blockquote:after,q:before,q:after{content:'';content:none;}ins{text-decoration:none;}del{text-decoration:line-through;}table{border-collapse:collapse;border-spacing:0;}body{background:#FFF;color:#000;font-family:Arial,Liberation Sans,DejaVu Sans,sans-serif;font-size:80%;text-align:center;}code{font-family:Consolas, Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace, serif;background-color:#eeeeee;}textarea{font-family:Consolas, Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace, serif;border:1px solid #999;font-size:90%;}.form-submit input:hover{cursor:pointer;}input,select,button,.button,a.button:link,a.button:visited{border:1px solid #999;font-size:100%;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;}"

    // Convert to json then back to formatted CSS to normalize it.
    var json = CSSJSON.toJSON(cssString);
    var css = CSSJSON.toCSS(json);

    // Regex to find properties (tabs and colon included)
    var prop_regex = new RegExp( "\t[^.}](.*)?:", 'g' );
    var prop_arr = css.match(prop_regex)


    // Clean up properties array, remove duplicates, and sort.
    var prop_arr = removeTab(prop_arr)
    var prop_arr = removeColon(prop_arr)
    var properties = removeDupes(prop_arr);
    var properties = properties.sort();

    // Start search of CSS for matches to properties.
    $.each(properties, function(i,p){

        // Find number of times properites appear, used later only for length.
        var local_prop_regex = new RegExp( "\t" + p +":", 'g' );
        var local_prop_arr = css.match(local_prop_regex)

        // Find full declaration for a given property.
        var dec_regex = new RegExp( "\t" + p +":(.*?);", 'g' );
        var dec_match = css.match(dec_regex);
        var dec_match = removeTab(dec_match)

        // Create json array with declarations and counts.
        var dec_json = compressArray(dec_match);

        console.log("");
        console.log(p + " == " + (local_prop_arr).length);
        console.log("-----");

        // Parse the json array of declaration.
        $.each(dec_json, function(i,p){
            console.log(dec_json[i].value + " : " + dec_json[i].count);
        })

    })

})