// 展示全部类型，收起排序
$(function () {

    // 展示：全部类型，并收起：综合排序
    the_slideDown("#all_types", "#all_cer", "#sort_rule", "#sort_cer");
    // 收起：全部类型
    the_slideUp("#all_types", "#all_cer",);

    // 展示：综合排序，并收起：全部类型
    the_slideDown("#sort_rule", "#sort_cer", "#all_types", "#all_cer");
    // 收起：综合排序
    the_slideUp("#sort_rule", "#sort_cer",);

})


// the_text:当前点击的文字  the_shade:当前阴影
// 展示
function the_slideDown(the_text, the_shade, other_text, other_shade) {
    $(the_text).click(function () {
        // 点击文字，显示阴影
        var $the_shade = $(the_shade);
        $the_shade.slideDown();
        the_chevron(the_text, "glyphicon-chevron-down", "glyphicon-chevron-up");
        var $other_shade = $(other_shade);
        $other_shade.slideUp();
        the_chevron(other_text, "glyphicon-chevron-up", "glyphicon-chevron-down");
    })
}

// 收起
function the_slideUp(the_text, the_shade) {
    $(the_shade).click(function () {
        // 点击阴影，收回阴影
        var $the_shade = $(the_shade);
        $the_shade.slideUp();
        the_chevron(the_text, "glyphicon-chevron-up", "glyphicon-chevron-down");
    })
}


// 改变V形符号，向上向下
function the_chevron(the_text, the_rem, the_add) {
    var $the_text = $(the_text);
    var $span = $the_text.find("span").find("span");
    $span.removeClass(the_rem).addClass(the_add);
}