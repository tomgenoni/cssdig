$(document).ready(function(){

    $('input[type=checkbox]').click(function(){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
    });

    $('#prop-checkboxes .show-prop').click(function(){
        var target = $(this).attr("data-target");
        trigger_top = $(this).offset().top;
        target_top = $("#"+target).offset().top;
        report_top = $("#report").scrollTop();
        $('#report').animate({
             scrollTop: target_top + report_top - trigger_top + 4
        }, 500);
        return false;
    });

    $('.report-entry tr').click(function(){
        if ( $(this).hasClass("active") ) {
            $("#css pre").unhighlight();
            $(this).removeClass("active");
            $(".ruleset").show();
        } else {
            $('.report-entry tr').removeClass("active")
            $(this).addClass("active");
            var target = $(this).find("td").eq(0).text() || (this).find("color-example-wrap").text()
            if ( target.charAt(target.length-1) != ";") {
                target = target + ":";
            }
            $("#css pre").unhighlight();
            $("#css pre").highlight(target);
            $(".ruleset").hide();
            setTimeout(function(){
                $(".highlight").each(function(){
                    $(this).closest(".ruleset").show()
                })
            },1)
        }
        return false;
    });

    $("#button-reset-css").click(function(){
        $("#css pre").unhighlight();
        $(".ruleset").show();
        $(this).hide();
        return false;
    });

    var css_pure = $("#css pre").html()
    css_pure = css_pure.replace(/\}/g,"}</span><span class='ruleset'>")
    css_pure = css_pure.substring(0, css_pure.length - 7);
    $("#css pre").html("<span class='ruleset'>" + css_pure)

})