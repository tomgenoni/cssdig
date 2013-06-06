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
        $("#button-reset-css").show();
        $('.report-entry tr').removeClass("active")
        $(this).addClass("active");
        // var target = $(this).attr("data-target");
        // $("#css pre").unhighlight();
        // $("#css pre").highlight(target);
        // $(".ruleset").hide();
        // setTimeout(function(){
        //     $(".highlight").each(function(){
        //         $(this).closest(".ruleset").show()
        //     })
        // },1)
        return false;
    });

    $("#button-reset-css").click(function(){
        $("#css pre").unhighlight();
        $(".ruleset").show();
        $(this).hide();
        return false;
    });

    var css_dirty = $("#css pre").html()
    var css_json = CSSJSON.toJSON(css_dirty);
    var css_clean = CSSJSON.toCSS(css_json);
    css_clean = css_clean.replace(/\}/g,"}</span><span class='ruleset'>")
    css_clean = css_clean.substring(0, css_clean.length - 7);
    $("#css pre").html("<span class='ruleset'>" + css_clean)

})