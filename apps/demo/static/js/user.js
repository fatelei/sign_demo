function bind_modify_event(form_id) {
    $("#upProfile").bind("click", function () {
        $("#"+form_id).submit();
    });
    $("#clProfile").bind("click", function () {
        $("#"+form_id).form("reset");
    });
}

function bind_pwdchange_event(form_id) {
    $("#pwdChange").bind("click", function () {
        $("#"+form_id).submit();
    });
}

function bind_user_remove_event(url, grid_id) {
    $("#userRemove").bind("click", function () {
        bind_remove_event(url, grid_id);
    });
}

function bind_add_user_event(form_id) {
    $("#addUser").bind("click", function () {
        $(form_id).submit();
    });
    $("#cancelUser").bind("click", function () {
        $(form_id).form("reset");
    });
}