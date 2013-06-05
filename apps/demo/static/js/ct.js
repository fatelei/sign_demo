function bind_remove_ct_event (url, grid_id) {
    $("#ctRemove").bind("click", function () {
        bind_remove_event(url, grid_id);
    });
}

function bind_edit_ct_event (grid_id) {
    $("#ctEdit").bind("click", function () {
        var row = $(grid_id).datagrid("getSelected");
        if (row) {
            if (!row.is_delete) {
                url = update_url + row.id;
                $.ajax({
                    url: update_url + row.id,
                    type: "GET",
                    dataType: "json",
                    error: function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus);
                    }
                }).done(function (data) {
                    if ("id" in data) {
                        $("#editCtDlg").dialog("open").dialog("setTitle", "编辑合同模板");
                        $("#ctEditFrom").form("load", {
                            user_id: data.user_id,
                            tpl_name: data.tpl_name,
                            tpl_instruction: data.tpl_instruction
                        });
                    } else {
                        $.messager.alert("错误", "合同模板以删除不能修改");
                    }
                });
            } else {
                $.messager.alert("错误", "合同模板以删除不能修改");
            }
        }
    });
    $("#saveCT").bind("click", function () {
        $("#ctEditFrom").form("submit", {
            url: url,
            onSubmit: function () {
                return $(this).form("validate");
            },
            success: function (data) {
                data = $.evalJSON(data);
                if ("errmsg" in data) {
                    $.messager.alert("错误", data.errmsg);
                } else {
                    $.messager.alert("成功", data.msg);
                    $("#editCtDlg").dialog("close");
                    $(grid_id).datagrid("reload");
                }
            }
        });
    });
    $("#cancelCT").bind("click", function () {
        $("#editCtDlg").dialog("close");
    });
}

function bind_add_ct_event () {
    $("#addCTForm").submit();
}


function bind_remove_ct_event (url, grid_id) {
    $("#ctRemove").bind("click", function () {
        bind_remove_event(url, grid_id);
    });
}


function bind_sign_contract_event () {
    $("#ctSign").bind("click", function () {
        var row = $("#ctList").datagrid("getSelected");
        console.log(row.is_delete);
        if (row) {
            $.ajax({
                url: sign_url + row.id,
                type: "GET",
                dataType: "json",
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus);
                }
            }).done(function (data) {
                console.log(data);
                if (data.info) {
                    var rst = $(data.info);
                    $("#dpl").append(rst);
                    $("#signWin").dialog("open");
                }
            });
        }
    });
}