function bind_remove_ct_event (url, grid_id) {
    $("#ctRemove").bind("click", function () {
        bind_remove_event(url, grid_id);
    });
}

function bind_edit_ct_event (grid_id) {
    $("#ctEdit").bind("click", function () {

    });
}

function bind_add_ct_event () {
    $("#addCTForm").submit();
}

function bind_edit_cttpl_event () {
    $("#inputBtn").bind("click", function () {
        func_input();
    });
    $("#textBtn").bind("click", function () {
        func_textarea();
    });
}

function add_draggable_input (target_id) {
    var num = 1;
    function real_func () {
        var html = '<div id="tpl_input_' + num + '">';
        html += '<table><tr><td>';
        html += '<input type="text"/>:</td>';
        html += '<td><span><input type="text" disabled/></span></td></tr></div>';
        $(target_id).append(html);
        $("#tpl_input_" + num).draggable({handle: "span"});
        num++;
    }
    return real_func;
}

function add_draggable_textarea (target_id) {
    var num = 1;
    function real_func () {
        var html = '<div id="tpl_textarea_' + num + '">';
        html += '<table><tr><td>';
        html += '<input type="text"/>:</td>';
        html += '<td><span><textarea style="width:300px;height:200px;" disabled></textarea></span></td></tr></div>';
        $(target_id).append(html);
        $("#tpl_textarea_" + num).draggable({handle: "span"});
        num++;
    }
    return real_func;
}
