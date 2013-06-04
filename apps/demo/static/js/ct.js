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

