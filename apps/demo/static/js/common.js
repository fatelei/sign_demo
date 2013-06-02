function bind_event_to_form(form_id, target_url, redirect_url) {
    $(form_id).form({
        url: target_url,
        onSubmit: function () {
            var isValid = $(this).form("validate");
            return isValid;
        },
        success: function (data) {
            data = $.evalJSON(data);
            if (tools.show_message(data)) {
                if (redirect_url != undefined) {
                    document.location = redirect_url;
                }
            }
        }
    });
}

function bind_remove_event(url, grid_id) {
    var row = $(grid_id).datagrid("getSelected");
    if (row) {
        $.messager.confirm("你确定吗？", "是否要删除所选？", function (r) {
            if (r) {
                var _xsrf = document.getElementsByName("_xsrf")[0].value;
                $.ajax({
                    url: url,
                    dataType: 'json',
                    type: "POST",
                    data: {"id": row.id, "_xsrf": _xsrf},
                    error: function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus);
                    }
                }).done(function (data) {
                    if (tools.show_message(data)) {
                        $(grid_id).datagrid("reload");
                    }
                });
            }
        });
    }
}

function bind_edit_event(url, grid_id, dialog_id) {
    var row = $(grid_id).datagrid("getSelected");
    if (row) {
        $.ajax({
            url: url,
            dataType: "json",
            type: "GET",
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus);
            }
        }).done(function (data) {

        });
    }
}