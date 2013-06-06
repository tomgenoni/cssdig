$(document).ready(function(){

    prop_on_arr = [
        "background",
        "border",
        "color",
        "content",
        "display",
        "font",
        "font-family",
        "font-size",
        "font-style",
        "font-weight",
        "height",
        "line-height",
        "width",
        "z-index"
    ];

    $("#form-dig button").click(function(){
        $(this).addClass("disabled");
        var url = $("#url").val();
        $("#css, #prop-checkboxes").html("");
        $("#report").html("loading...")
        $.ajax({
            url: "/application/",
            type: 'post',
            data: url,
            success: function(data, status){
                $("#form-dig button").removeClass("disabled");
                cssString = data['css_combined'];
                dig(cssString);
            }
        });
        return false;
    })

    $('body').on('click', 'input[type=checkbox]', function (){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
    });

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
            d = d.replace(/: /g, '');
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


    function dig(cssStrig) {

        // Convert to json then back to formatted CSS to normalize it.
        var json = CSSJSON.toJSON(cssString);
        var css = CSSJSON.toCSS(json);

        // Regex to find properties (tabs and colon included)
        var prop_regex = new RegExp( "\t[^.}](.*?):\\s", 'g' );
        var prop_arr = css.match(prop_regex);

        // Clean up properties array, remove duplicates, and sort.
        var prop_arr = removeTab(prop_arr)
        var prop_arr = removeColon(prop_arr)
        var properties = removeDupes(prop_arr);
        var properties = properties.sort();

        prop_checkboxes = "";
        report_html = "<h2>Dig Report</h2>";

        // Start search of CSS for matches to properties.
        $.each(properties, function(i,p){

            // Find number of times properites appear, used later only for length.
            var local_prop_regex = new RegExp( "\t" + p + ":", 'g' );
            var local_prop_arr = css.match(local_prop_regex)

            // Find full declaration for a given property.
            var dec_regex = new RegExp( "\t" + p + ":(.*?);", 'g' );
            var dec_match = css.match(dec_regex);
            var dec_match = removeTab(dec_match)

            // Create json array with declarations and counts.
            var dec_json = compressArray(dec_match);

            prop_checked = ""
            table_style_default = "style='display:none'"

            if ( $.inArray(p, prop_on_arr) > -1 ) {
                prop_checked = "checked='checked'"
                table_style_default = "";
            }

            prop_checkboxes += "<li><input type='checkbox' " + prop_checked + " id='checkbox-"+p+"' name='checkbox-"+p+"'><label for='checkbox-"+p+"'>" + p + "</label></li>"

            report_html += "<table class='report-entry' id='table-" + p + "' "+ table_style_default +">";
            report_html += "<thead>";
            report_html += "<tr>";
            report_html += "<td>" + p + "</td>";
            report_html += "<td>" + (local_prop_arr).length + "</td>";
            report_html += "</tr>";
            report_html += "</thead>";
            report_html += "<tbody>";

            // Parse the json array of declaration.
            $.each(dec_json, function(i,v){
                report_html += "<tr>";
                if ( p == "color") {
                    report_html += "<td><div class='color-example-wrap'><span class='color-example' style='background-"+dec_json[i].value +"'></span>" + dec_json[i].value + "</div></td>";
                } else {
                    report_html += "<td>" + dec_json[i].value + "</td>";
                }
                report_html += "<td>" + dec_json[i].count + "</td>";
                report_html += "</tr>";
            })

            report_html +="</tbody>";
            report_html +="</table>";
        })

        $("#prop-checkboxes").html(prop_checkboxes);
        $("#report").html(report_html);
        $("#css").html("<h2>Combined CSS</h2><pre>" + css + "</pre>");

    }


})