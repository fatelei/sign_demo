function bind_remove_ct_event (url, grid_id) {
    $("#ctRemove").bind("click", function () {
        bind_remove_event(url, grid_id);
    });
}

function bind_edit_ct_event (grid_id) {
    $("#ctEdit").bind("click", function () {

    });
}

function bind_add_ct_event (form_id) {
    $("#addCT").bind("click", function () {
        $(form_id).submit();
    });
    $("#cancelCT").bind("click", function () {
        $(form_id).form("reset");
    });
}

