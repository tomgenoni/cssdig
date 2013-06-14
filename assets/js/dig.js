$(document).ready(function(){

    // Show/hide properties from the data list.
    $('input[type=checkbox]').click(function(){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
    });

    // Click into report data to reveal locations in Combined CSS.
    $('.report-entry tr').click(function(){
        if ( $(this).hasClass("active") ) {
            $("#css pre").unhighlight();
            $(this).removeClass("active");
            $(".ruleset").show();
        } else {
            $('.report-entry tr').removeClass("active");
            $(this).addClass("active");
            var target = $(this).find("td").eq(0).text() || (this).find("color-example-wrap").text();
            if ( target.charAt(target.length-1) != ";" && target != "!important") {
                target = target + ":";
            }
            $("#css pre").unhighlight();
            if ( target == "!important" ) {
                $("#css pre").highlight(target, { caseSensitive: true });
            } else {
                $("#css pre").highlight(" " + target, { caseSensitive: true });
            }
            $(".ruleset").hide();
            setTimeout(function(){
                $(".highlight").each(function(){
                    $(this).closest(".ruleset").show();
                })
            },1)
        }
        return false;
    });

    // Wraps each rule in a space so it can be hidden/shown during highlights.
    var css_pure = $("#css pre").html();
    css_pure = css_pure.replace(/\}/g,"}</span><span class='ruleset'>");
    css_pure = css_pure.substring(0, css_pure.length - 7);
    $("#css pre").html("<span class='ruleset'>" + css_pure);

})